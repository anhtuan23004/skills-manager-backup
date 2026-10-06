#!/usr/bin/env python3
"""Read BTC resource limits; opt in to one tiny DeepSeek Flash request. Stdlib only."""
import argparse
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import socket
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import HTTPRedirectHandler, Request, build_opener


BASE_URL = 'https://api.thucchien.ai'
MODEL = 'deepseek-flash'
ENV_PATH = Path(__file__).resolve().parents[3] / '.env'


def read_api_key(env_path=ENV_PATH):
    """Environment takes precedence; read only AITC_API_KEY from the repo root .env.

    Supports KEY=value and single/double quoted values. No shell evaluation,
    interpolation, multiline values, or inline comments.
    """
    if 'AITC_API_KEY' in os.environ:
        return os.environ['AITC_API_KEY'].strip()
    try:
        lines = env_path.read_text(encoding='utf-8').splitlines()
    except FileNotFoundError:
        return ''
    value = ''
    for line in lines:
        name, separator, candidate = line.partition('=')
        if separator and name.strip() == 'AITC_API_KEY':
            value = candidate.strip()
            if len(value) >= 2 and value[0] in "\"'" and value[-1] == value[0]:
                value = value[1:-1].strip()
    return value


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None  # Never forward credentials or repeat a paid request.


def number(value):
    return value if (isinstance(value, (int, float)) and
                     not isinstance(value, bool) and math.isfinite(value)) else None


def limits(info):
    if not isinstance(info, dict):
        info = {}
    result = {field: number(info.get(field)) for field in
              ('spend', 'max_budget', 'rpm_limit', 'tpm_limit', 'max_parallel_requests')}
    spend, budget = result['spend'], result['max_budget']
    result['remaining'] = max(0, budget - spend) if spend is not None and budget is not None else None
    result['status'] = 'KNOWN' if result['remaining'] is not None else 'UNVERIFIED'
    metadata = info.get('metadata')
    if isinstance(metadata, dict):
        result['model_limits'] = {
            key: {model: number(value) for model, value in values.items()}
            for key, values in metadata.items()
            if key.startswith('model_') and key.endswith('_limit') and isinstance(values, dict)
        }
    return result


def request_api(key, timeout):
    opener = build_opener(NoRedirect())

    def call(path, payload=None):
        request = Request(BASE_URL + path,
                          data=json.dumps(payload).encode() if payload is not None else None,
                          headers={'Authorization': 'Bearer ' + key,
                                   'Content-Type': 'application/json'})
        started = time.monotonic()
        try:
            with opener.open(request, timeout=timeout) as response:
                data = json.load(response)
                if not isinstance(data, dict):
                    return {'status': 'ERROR', 'reason': 'INVALID_JSON_SHAPE'}
                headers = {k.lower(): v for k, v in response.headers.items()
                           if k.lower().startswith('x-ratelimit-') or
                           k.lower() in ('retry-after', 'x-litellm-response-cost')}
                return {'status': 'OK', 'data': data, 'headers': headers,
                        'latency_ms': round((time.monotonic() - started) * 1000)}
        except HTTPError as exc:
            # Do not emit response bodies: key/info and errors may contain credentials.
            reasons = {401: 'AUTH_FAILED', 403: 'FORBIDDEN', 404: 'ENDPOINT_UNAVAILABLE',
                       429: 'RATE_OR_BUDGET_LIMIT_CHECK_DASHBOARD'}
            return {'status': 'ERROR', 'http_status': exc.code,
                    'reason': reasons.get(exc.code, 'HTTP_ERROR'),
                    'retry_after': exc.headers.get('Retry-After')}
        except (URLError, TimeoutError, socket.timeout, OSError):
            return {'status': 'ERROR', 'reason': 'NETWORK_OR_TIMEOUT_NO_RETRY'}
        except (ValueError, UnicodeError):
            return {'status': 'ERROR', 'reason': 'INVALID_JSON'}

    return call


def inspect_resources(call, smoke=False):
    report = {'checked_at': datetime.now(timezone.utc).isoformat(),
              'gateway': BASE_URL, 'checks': {},
              'note': 'null = UNVERIFIED; model listed does not prove inference availability. '
                      'Rate limits are configured caps, not remaining tokens. '
                      'Key and team budgets overlap; do not add them.'}

    def get(path, name):
        result = call(path)
        report['checks'][name] = {k: v for k, v in result.items() if k != 'data'}
        return result.get('data', {}) if result.get('status') == 'OK' else {}

    key_data = get('/key/info', 'key').get('info', {})
    if not isinstance(key_data, dict):
        key_data = {}
    report['key'] = limits(key_data)
    team_id = key_data.get('team_id')
    team_data = {}
    if isinstance(team_id, str) and team_id:
        team_data = get('/team/info?' + urlencode({'team_id': team_id}), 'team').get('team_info', {})
    else:
        report['checks']['team'] = {'status': 'UNVERIFIED', 'reason': 'NO_TEAM_ID'}
    report['team'] = limits(team_data)
    rows = get('/v1/models', 'models').get('data')
    valid_models = isinstance(rows, list) and all(
        isinstance(row, dict) and isinstance(row.get('id'), str) for row in rows)
    report['models'] = sorted(set(row['id'] for row in rows)) if valid_models else []
    if not valid_models and report['checks']['models']['status'] == 'OK':
        report['checks']['models'] = {'status': 'UNVERIFIED', 'reason': 'INVALID_MODEL_LIST'}
    report['smoke'] = {'status': 'NOT_REQUESTED'}
    if not smoke:
        return report

    remaining = [report[scope]['remaining'] for scope in ('key', 'team')]
    reason = None
    if MODEL not in report['models']:
        reason = 'DEEPSEEK_FLASH_NOT_LISTED_NO_FALLBACK'
    elif any(value is not None and value <= 0 for value in remaining):
        reason = 'BUDGET_EXHAUSTED'
    elif report['checks']['key']['status'] != 'OK' or report['team']['remaining'] is None:
        reason = 'TEAM_BUDGET_UNVERIFIED_CHECK_BTC_DASHBOARD'
    if reason:
        report['smoke'] = {'status': 'SKIPPED', 'reason': reason}
        return report

    result = call('/v1/chat/completions', {
        'model': MODEL, 'messages': [{'role': 'user', 'content': 'Reply with only OK.'}],
        'thinking': {'type': 'disabled'}, 'max_tokens': 16, 'stream': False,
    })
    report['smoke'] = {k: v for k, v in result.items() if k != 'data'}
    report['smoke']['model'] = MODEL
    if result.get('status') == 'OK':
        data = result.get('data', {})
        choices = data.get('choices')
        choice = choices[0] if isinstance(choices, list) and choices and isinstance(choices[0], dict) else {}
        message = choice.get('message')
        content = message.get('content') if isinstance(message, dict) else None
        report['smoke']['status'] = 'OK' if isinstance(content, str) and content.strip() == 'OK' else 'UNVERIFIED'
        report['smoke']['received_ok'] = report['smoke']['status'] == 'OK'
        usage = data.get('usage')
        report['smoke']['usage'] = {k: number(usage.get(k)) for k in
                                   ('prompt_tokens', 'completion_tokens', 'total_tokens')} if isinstance(usage, dict) else None
    # Read-only refresh even after a failed POST: timeout does not prove no charge.
    if isinstance(team_id, str) and team_id:
        report['team_after_smoke'] = limits(get(
            '/team/info?' + urlencode({'team_id': team_id}), 'team_after_smoke').get('team_info', {}))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--smoke', action='store_true', help='One paid deepseek-flash request, max 16 output tokens, no retry')
    parser.add_argument('--timeout', type=float, default=15, help='Timeout per request in seconds (1–60)')
    args = parser.parse_args()
    if not math.isfinite(args.timeout) or not 1 <= args.timeout <= 60:
        parser.error('--timeout must be between 1 and 60 seconds')
    try:
        key = read_api_key()
    except (OSError, UnicodeError):
        parser.exit(2, 'Cannot read repo root .env; check file permissions and UTF-8 encoding.\n')
    if not key or any(char.isspace() for char in key):
        parser.exit(2, 'Set AITC_API_KEY in repo root .env or environment; never pass it on the command line.\n')
    report = inspect_resources(request_api(key, args.timeout), smoke=args.smoke)
    output = json.dumps(report, ensure_ascii=False, indent=2)
    print(output.replace(key, '[REDACTED]'))
    complete = (all(check['status'] == 'OK' for check in report['checks'].values())
                and report['team']['remaining'] is not None
                and (not args.smoke or report['smoke']['status'] == 'OK'))
    return 0 if complete else 1


if __name__ == '__main__':
    raise SystemExit(main())
