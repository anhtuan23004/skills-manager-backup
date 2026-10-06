"""Local workspace helpers. These checks are not an operating-system sandbox."""
from __future__ import annotations
import hashlib, json, os, re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROTECTED = {'.git', '.ai-log', '.agents', '.claude', '.codex', '.cursor', '.gemini', '.github', '.env', 'scripts', 'hooks'}
class ToolkitError(Exception):
    """Expected input, permission, or operational error."""

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def root_path(root: str | Path) -> Path:
    p = Path(root).expanduser().resolve()
    if not p.is_dir():
        raise ToolkitError('Workspace root must already exist. Use a dedicated working subfolder.')
    return p

def safe_path(root: str | Path, value: str | Path, *, exists: bool = True) -> Path:
    r = root_path(root)
    s = str(value)
    if not s or '\x00' in s or '\\' in s or re.match(r'^[A-Za-z]:', s):
        raise ToolkitError('Use a nonempty relative path with forward slashes.')
    q = Path(s)
    if q.is_absolute() or '..' in q.parts:
        raise ToolkitError('Absolute paths and traversal are not allowed.')
    if any(part.startswith('.') or part.lower() in PROTECTED for part in q.parts):
        raise ToolkitError('Hidden, credential, hook, and BTC control paths are protected.')
    current = r
    for part in q.parts:
        current = current / part
        if current.is_symlink():
            raise ToolkitError('Symlinks are not allowed in tool paths.')
    p = (r/q).resolve()
    if not p.is_relative_to(r):
        raise ToolkitError('Path escapes workspace.')
    if exists and not p.exists():
        raise ToolkitError(f'File or directory does not exist: {q.as_posix()}')
    return p

def write_new(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as f:
        f.write(data)

def json_bytes(obj: Any) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, indent=2, allow_nan=False)+'\n').encode('utf-8')

def hash_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

def snapshot(root: str | Path, directory: str = 'final', *, max_files: int = 500) -> dict:
    r = root_path(root); d = safe_path(r, directory)
    if not d.is_dir():
        raise ToolkitError('Manifest target must be a directory.')
    if d == r:
        raise ToolkitError('Use a specific artifact folder, not the whole workspace.')
    files = []
    for p in sorted(d.rglob('*')):
        rel = p.relative_to(r).as_posix()
        safe_path(r, rel)
        if p.is_file():
            files.append({'path': rel, 'bytes': p.stat().st_size, 'sha256': hash_file(p)})
            if len(files) > max_files:
                raise ToolkitError('Too many files; select the final artifact folder only.')
    if not files:
        raise ToolkitError('No files in artifact folder.')
    return {'created_at': utc_now(), 'directory': directory, 'files': files,
            'total_bytes': sum(f['bytes'] for f in files),
            'note': 'Local hashes identify versions; not a trusted timestamp or content-quality approval.'}

def verify_snapshot(root: str | Path, manifest_path: str) -> dict:
    p = safe_path(root, manifest_path)
    if p.stat().st_size > 2_000_000:
        raise ToolkitError('Manifest is unexpectedly large.')
    prior = json.loads(p.read_text('utf-8'))
    current = snapshot(root, prior['directory'])
    old = {f['path']: (f['bytes'],f['sha256']) for f in prior['files']}
    new = {f['path']: (f['bytes'],f['sha256']) for f in current['files']}
    return {'unchanged': old == new, 'added': sorted(new.keys()-old.keys()),
            'removed': sorted(old.keys()-new.keys()),
            'modified': sorted(k for k in old.keys() & new.keys() if old[k] != new[k])}

def assert_not_frozen(root: str | Path) -> None:
    if (root_path(root)/'ops'/'freeze.json').exists():
        raise ToolkitError('Workspace is frozen. Do not generate or alter competition artifacts.')

def validate_live_permission(root: str | Path) -> dict:
    r = root_path(root); assert_not_frozen(r)
    p = safe_path(r, 'ops/permission.json')
    v = json.loads(p.read_text('utf-8'))
    required = ['toolkit_scope_approved','official_logging_verified','agent_routes_only_btc']
    if any(v.get(k) is not True for k in required):
        raise ToolkitError('Human readiness checks are incomplete in ops/permission.json.')
    if v.get('mode') not in {'practice','competition'}:
        raise ToolkitError('Set mode to practice or competition.')
    if v['mode'] == 'competition':
        end = v.get('end_at')
        if not end:
            raise ToolkitError('Competition mode requires end_at with time-zone offset.')
        try:
            dt = datetime.fromisoformat(end)
        except (TypeError, ValueError) as e:
            raise ToolkitError('Invalid end_at.') from e
        if dt.tzinfo is None:
            raise ToolkitError('end_at requires a time-zone offset.')
        if datetime.now(timezone.utc) >= dt:
            raise ToolkitError('Competition working time has ended; no generation calls allowed.')
    return v
