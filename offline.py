import json,re,hashlib
from urllib.parse import urljoin,urlsplit

def render(dist):
 files=['./']+['./'+str(p.relative_to(dist)) for p in sorted(dist.rglob('*')) if p.is_file() and p.name!='sw.js' and not p.name.startswith('.')]+['./'+str(p.parent.relative_to(dist))+'/' for p in sorted(dist.rglob('index.html')) if p.parent!=dist]
 selected={'./','./index.html','./en/index.html','./app.js','./style.css','./hub.js','./theme-home.js','./parks.json'}
 for lang in ('','en/'):
  for page in ('routes/southwest','parks/grand-canyon','parks/death-valley','nearby/page','themes/us-national-parks'):
   path=lang+page+'/index.html';selected.add('./'+path)
   html=(dist/path).read_text()
   for ref in re.findall(r'(?:src|href)="([^"]+)"',html):
    resolved=urljoin(path,ref).split('#')[0]
    if not urlsplit(resolved).scheme and (dist/resolved).is_file():selected.add('./'+resolved)
 for path in ('index.html','en/index.html'):
  for ref in re.findall(r'(?:src|href)="([^"]+)"',(dist/path).read_text()):
   resolved=urljoin(path,ref).split('#')[0]
   if resolved.startswith('assets/') and (dist/resolved).is_file():selected.add('./'+resolved)
 version=hashlib.sha256(''.join(hashlib.sha256((dist/f[2:]).read_bytes()).hexdigest() for f in files if (dist/f[2:]).is_file()).encode()).hexdigest()[:12]
 template=(dist.parent/'offline-worker.js').read_text()
 (dist/'sw.js').write_text("'use strict';\nconst CACHE='parks-offline-"+version+":'+self.registration.scope;\nconst FILES="+json.dumps(files)+";\nconst SOUTHWEST="+json.dumps(sorted(selected))+";\n"+template)
