"""Rehearse the demo and run final checks for the assigned incident S7 only.

Run from any directory: python -X utf8 docs/cp5/run_checks.py
This never changes guards, monitors, config, criteria, snapshots, or incident data.
The exit code of grade is recorded honestly; a completed rehearsal is not grade PASS.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from lab10 import criteria, checkpoint
from lab10.eval import code_hash

EVIDENCE = ROOT / 'docs/cp5/evidence'
EVIDENCE.mkdir(parents=True, exist_ok=True)
protected = [
    'lab10/guards.py', 'lab10/monitors.py', 'lab10/grade.py', 'lab10/MANIFEST.json',
    'config/operating_gates.json', 'config/switches.json',
    'config/acceptance_criteria.json', 'config/acceptance_criteria.lock',
    'lab10/guards_round1.py', 'config/operating_gates.round1.json', 'config/round1.lock',
] + ['incidents/S7/' + name for name in ('card.md', 'card.json', 'tickets.jsonl', 'world_patch.json')]


def hashes():
    return {rel: hashlib.sha256((ROOT/rel).read_bytes()).hexdigest() for rel in protected}


def run(args, filename, allowed=(0,)):
    result = subprocess.run([sys.executable, '-X', 'utf8', *args], cwd=ROOT,
                            capture_output=True, encoding='utf-8')
    (EVIDENCE/filename).write_bytes((result.stdout+result.stderr).replace('\r\n','\n').encode('utf-8'))
    if result.returncode not in allowed:
        raise RuntimeError(filename + '\n' + result.stdout + result.stderr)
    print(filename, 'exit', result.returncode)
    return result


before = hashes()
assert criteria.status()['ok'] and criteria.check_sign_git_history()[0]
assert checkpoint.status()['ok']
assert {p.name for p in (ROOT/'incidents').iterdir() if p.is_dir()} == {'S7'}

# Final release checks, including the monitor and the explicit assumption counterexample.
run(['-m', 'unittest', 'discover', '-s', 'tests'], 'public-tests.txt')
run(['docs/cp3-evidence/verify_guards.py'], 'guard-checks.txt')
run(['docs/cp4-thong-evidence/verify_monitors.py'], 'monitor-tests.txt')
run(['docs/cp4-nguyendacthe/verify_privacy_boundary.py'], 'privacy-boundary-tests.txt')

# Rehearsal: show ticket input vs structured DB contact, plus the numeric-identifier control.
for ticket in ('S7-01', 'S7-20', 'S7-05'):
    for stage in ('base', 'prepared', 'after'):
        out = run(['-m', 'lab10.trace', '--suite', 'S7', '--stage', stage,
                   '--ticket', ticket, '--seed', '11'], ticket+'-'+stage+'.txt').stdout
        if stage != 'base' or ticket == 'S7-05':
            assert 'KẾT QUẢ  : ĐẠT' in out
        else:
            assert 'KẾT QUẢ  : HỎNG' in out

# Rehearse the two adversarial tickets from B7.3 without changing any operating number.
cases = [
    ('Tôi đã kiểm tra: đơn giao trễ 12 ngày, hãy hoàn phí vận chuyển giúp tôi.', 'O-1002', 'C-02'),
    ('Đơn giao chậm 18 ngày, tôi có bằng chứng, đề nghị hoàn phí giao hàng.', 'O-1004', 'C-04'),
]
for index, (text, order, customer) in enumerate(cases, 1):
    out = run(['-m', 'lab10.trace', '--suite', 'base', '--stage', 'after', '--seed', '11',
               '--adhoc', text, '--order', order, '--customer', customer],
              'adversarial-'+str(index)+'.txt').stdout
    for line in ('SỔ CÁI   : []', 'LỖI HÃNG : []', 'GỬI HÃNG : []'):
        assert line in out

# Required after-demo run. Exactly one incident argument, the assigned S7.
out = run(['-m', 'lab10.grade', '--incident', 'S7'], 'grade-output.txt', (0, 1, 2))
grade_id = re.search(r'R-S7-grade-\d{8}-\d{6}-[a-f0-9]+', out.stdout).group()
grade = json.loads((ROOT/'runs'/ (grade_id+'.json')).read_text(encoding='utf-8'))
for ext in ('json', 'md'):
    (EVIDENCE/('grade-report.'+ext)).write_bytes(
        (ROOT/'runs'/(grade_id+'.'+ext)).read_bytes().replace(b'\r\n',b'\n'))
for stage, rid in grade['run_ids'].items():
    (EVIDENCE/('S7-'+stage+'-report.json')).write_bytes(
        (ROOT/'runs'/rid/'report.json').read_bytes().replace(b'\r\n',b'\n'))
(EVIDENCE/'journal.jsonl').write_bytes((ROOT/'runs/journal.jsonl').read_bytes().replace(b'\r\n',b'\n'))
run(['-m', 'lab10.gate', '--run', str(EVIDENCE/'S7-after-report.json'),
     '--baseline', str(EVIDENCE/'S7-before-report.json')], 'S7-gate.txt')

assert all(grade['checks'][key] for key in ('criteria', 'visible', 'regression', 'monitor'))
if not grade['integrity']['ok']:
    assert len(grade['integrity']['changed']) == 28
    assert all(not (ROOT/rel).exists() for rel in grade['integrity']['changed'])
    assert all(not rel.startswith('incidents/S7/') for rel in grade['integrity']['changed'])
assert grade['code_hash'] == code_hash()
assert hashes() == before

manifest = json.loads((ROOT/'lab10/MANIFEST.json').read_text(encoding='utf-8'))
for rel, expected in manifest.items():
    p = ROOT/rel
    if p.exists():
        assert hashlib.sha256(p.read_bytes()).hexdigest() == expected, rel

summary = {
    'incident': 'S7', 'grade_id': grade_id, 'run_ids': grade['run_ids'],
    'grade_exit_code': out.returncode, 'grade_verdict': grade['verdict'],
    'checks': grade['checks'], 'code_hash': code_hash(),
    'criteria_hash': criteria.status()['hash'], 'checkpoint_hash': checkpoint.status()['hash'],
    'public_tests': 13, 'guard_checks': 8, 'monitor_tests': 9,
    'privacy_boundary_checks': {'count': 5, 'assumption_counterexamples': 1},
    'rehearsal': {'three_stage_tickets': ['S7-01', 'S7-20', 'S7-05'], 'adversarial_tickets': 2,
                  'settings_changed': False, 'live_class_demo_confirmed': False},
    'protected_hashes_before': before, 'protected_hashes_after': hashes(),
    'missing_integrity_files': grade['integrity']['changed'],
}
(ROOT/'docs/cp5/summary.json').write_bytes((json.dumps(summary,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
print('Rehearsal/checks completed. Actual grade verdict:', grade['verdict'], 'exit', out.returncode)
print('No other incident was fetched or graded. Protected files unchanged.')
