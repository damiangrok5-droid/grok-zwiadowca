# Odświeża gwiazdki/daty w raw_github.json z GitHub API (gh api).
import json, subprocess
r=json.load(open('raw_github.json'))
for k,v in r.items():
    p=subprocess.run(['gh','api','repos/'+v['full_name']],capture_output=True,text=True)
    if p.returncode: print('pominięto',k); continue
    d=json.loads(p.stdout); lic=(d.get('license') or {}).get('spdx_id')
    v.update(stars=d['stargazers_count'],pushed_at=d['pushed_at'],license=lic,archived=d['archived'],desc=d['description'])
json.dump(r,open('raw_github.json','w'),ensure_ascii=False,indent=1)
print('ok',len(r))
