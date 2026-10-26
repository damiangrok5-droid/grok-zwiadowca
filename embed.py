import json
d=json.load(open('data.json'))
open('index.html','w').write(open('template.html').read().replace('__DATA__', json.dumps(d,ensure_ascii=False).replace('</','<\\/')))
