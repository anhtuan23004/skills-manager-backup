import unittest
import io
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError

from check_resources import ENV_PATH, NoRedirect, inspect_resources, limits, read_api_key, request_api


class EnvTests(unittest.TestCase):
    def test_default_env_is_at_repository_root(self):
        self.assertEqual(ENV_PATH, Path(__file__).resolve().parents[3] / '.env')
        self.assertTrue((ENV_PATH.parent / '.env.example').is_file())

    @patch.dict('os.environ', {}, clear=True)
    def test_env_file_supports_quotes_and_ignores_other_keys(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / '.env'
            self.assertEqual(read_api_key(path), '')
            for value in ['fake-key', "'fake-key'", '"fake-key"']:
                path.write_text('# comment\nAI_LOG_API_KEY=other\nAITC_API_KEY=' + value + '\n')
                self.assertEqual(read_api_key(path), 'fake-key')

    @patch.dict('os.environ', {'AITC_API_KEY': 'from-environment'}, clear=True)
    def test_environment_wins_without_reading_file(self):
        with patch.object(Path, 'read_text', side_effect=AssertionError('must not read')):
            self.assertEqual(read_api_key(), 'from-environment')


class FakeAPI:
    def __init__(self, remaining=9, models=None, smoke_error=False):
        self.calls = []
        self.remaining = remaining
        self.models = ['deepseek-flash'] if models is None else models
        self.smoke_error = smoke_error

    def __call__(self, path, payload=None):
        self.calls.append((path, payload))
        if path == '/key/info':
            data = {'info': {'team_id': 'team /1', 'max_budget': None, 'spend': 1}}
        elif path.startswith('/team/info?'):
            data = {'team_info': {'max_budget': 10, 'spend': 10 - self.remaining}}
        elif path == '/v1/models':
            data = {'data': [{'id': model} for model in self.models]}
        elif self.smoke_error:
            return {'status': 'ERROR', 'http_status': 429}
        else:
            data = {'choices': [{'message': {'content': 'OK'}, 'finish_reason': 'stop'}],
                    'usage': {'prompt_tokens': 8, 'completion_tokens': 1}}
        return {'status': 'OK', 'data': data, 'headers': {}, 'latency_ms': 1}


class ResourceTests(unittest.TestCase):
    def test_default_is_read_only_and_null_is_unknown(self):
        api = FakeAPI()
        report = inspect_resources(api)
        self.assertTrue(all(body is None for _, body in api.calls))
        self.assertIsNone(report['key']['remaining'])
        self.assertEqual(report['team']['remaining'], 9)
        self.assertIn('/team/info?team_id=team+%2F1', [p for p, _ in api.calls])

    def test_smoke_is_one_bounded_nonthinking_request(self):
        api = FakeAPI()
        report = inspect_resources(api, smoke=True)
        posts = [body for _, body in api.calls if body is not None]
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['model'], 'deepseek-flash')
        self.assertEqual(posts[0]['thinking'], {'type': 'disabled'})
        self.assertEqual(posts[0]['max_tokens'], 16)
        self.assertEqual(report['smoke']['status'], 'OK')

    def test_no_post_when_exhausted_or_model_absent(self):
        for api in [FakeAPI(remaining=0), FakeAPI(models=['expensive-pro'])]:
            report = inspect_resources(api, smoke=True)
            self.assertEqual(report['smoke']['status'], 'SKIPPED')
            self.assertTrue(all(body is None for _, body in api.calls))

    def test_no_retry_on_429(self):
        api = FakeAPI(smoke_error=True)
        report = inspect_resources(api, smoke=True)
        self.assertEqual(report['smoke']['http_status'], 429)
        self.assertEqual(sum(body is not None for _, body in api.calls), 1)

    def test_missing_budget_blocks_smoke(self):
        calls = []
        def api(path, payload=None):
            calls.append((path, payload))
            data = {'data': [{'id': 'deepseek-flash'}]} if path == '/v1/models' else {}
            return {'status': 'OK', 'data': data}
        report = inspect_resources(api, smoke=True)
        self.assertEqual(report['smoke']['status'], 'SKIPPED')
        self.assertTrue(all(body is None for _, body in calls))

    def test_malformed_limits_do_not_become_money(self):
        for value in [None, True, '100', float('nan'), float('inf')]:
            self.assertIsNone(limits({'max_budget': value, 'spend': 0})['remaining'])

    def test_empty_response_is_not_success(self):
        api = FakeAPI()
        def empty_smoke(path, payload=None):
            return {'status': 'OK', 'data': {}} if payload else api(path)
        self.assertEqual(inspect_resources(empty_smoke, smoke=True)['smoke']['status'], 'UNVERIFIED')

    def test_malformed_models_block_smoke(self):
        api = FakeAPI()
        def malformed(path, payload=None):
            return {'status': 'OK', 'data': {'data': [None]}} if path == '/v1/models' else api(path, payload)
        report = inspect_resources(malformed, smoke=True)
        self.assertEqual(report['checks']['models']['status'], 'UNVERIFIED')
        self.assertEqual(report['smoke']['status'], 'SKIPPED')


class TransportTests(unittest.TestCase):
    @patch('check_resources.build_opener')
    def test_errors_do_not_leak_body_or_retry(self, build):
        for error in [TimeoutError('secret-key'),
                      HTTPError('url', 429, 'secret-key', {}, io.BytesIO(b'secret-key'))]:
            opener = MagicMock()
            build.return_value = opener
            opener.open.side_effect = error
            result = request_api('secret-key', 2)('/v1/chat/completions', {'model': 'deepseek-flash'})
            self.assertEqual(result['status'], 'ERROR')
            self.assertNotIn('secret-key', str(result))
            self.assertEqual(opener.open.call_count, 1)

    @patch('check_resources.build_opener')
    def test_invalid_json_is_reported(self, build):
        response = MagicMock()
        response.read.return_value = b'not json'
        build.return_value.open.return_value.__enter__.return_value = response
        self.assertEqual(request_api('fake', 2)('/key/info')['reason'], 'INVALID_JSON')

    def test_redirects_are_not_followed(self):
        self.assertIsNone(NoRedirect().redirect_request(None, None, 302, '', {}, 'https://other.example'))


if __name__ == '__main__':
    unittest.main()
