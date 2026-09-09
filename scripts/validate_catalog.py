import json
import sys
from pathlib import Path

p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('data/350_visual_templates.jsonl')
rows = [json.loads(line) for line in p.read_text(encoding='utf-8').splitlines() if line.strip()]
ids = [r.get('id') for r in rows]
required = {'id','path','visual_title','english_title','layout','alignment','color','reuse_rule','scene'}
errors=[]
if len(rows) != 350: errors.append(f'expected 350 rows, got {len(rows)}')
if len(set(ids)) != len(ids): errors.append('duplicate ids')
for r in rows:
    missing=required-set(r)
    if missing: errors.append(f"{r.get('id')}: missing {sorted(missing)}")
if errors:
    print('\n'.join(errors)); raise SystemExit(1)
print(f'OK: {len(rows)} template records; IDs unique; required fields present')
