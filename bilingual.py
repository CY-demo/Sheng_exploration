"""Build static English counterparts; language switching never requires a network service."""
from html.parser import HTMLParser
from html import escape
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
import json, re, posixpath
CJK=re.compile('[\u4e00-\u9fff]')

def render_bilingual(root,dist):
 catalog=json.loads((root/'english.json').read_text())
 from rockies import T
 catalog.update(T)
 from themes import brand
 catalog={brand(k):brand(v) for k,v in catalog.items()}
 pages=sorted(p for p in dist.rglob('*.html') if 'en' not in p.relative_to(dist).parts)
 missing=set()
 def translate(s):
  if not CJK.search(s):return s
  if s not in catalog:
   core=s.strip()
   if core in catalog:return s.replace(core,catalog[core])
   if core.endswith(' ↗') and core[:-2] in catalog:return s.replace(core,catalog[core[:-2]]+' ↗')
   missing.add(s);return s
  return catalog[s]
 class English(HTMLParser):
  def __init__(self,path):super().__init__(convert_charrefs=True);self.path=path;self.out=[];self.raw=False
  def url(self,value):
   u=urlsplit(value)
   if u.scheme or u.netloc or not u.path:return value
   target=posixpath.normpath(posixpath.join(str(self.path.parent),u.path))
   targetpath=dist/target
   ispage=targetpath.suffix=='.html' or targetpath.is_dir() and (targetpath/'index.html').exists()
   target=('en/'+target) if ispage else target
   rel=posixpath.relpath(target,'en/'+str(self.path.parent))
   if u.path.endswith('/') and not rel.endswith('/'):rel+='/'
   return urlunsplit(('', '',rel,u.query,u.fragment))
  def handle_decl(self,d):self.out.append('<!'+d+'>')
  def handle_comment(self,d):self.out.append('<!--'+d+'-->')
  def handle_starttag(self,tag,attrs):
   aa=[]
   for key,val in attrs:
    key={'viewbox':'viewBox','preserveaspectratio':'preserveAspectRatio'}.get(key,key)
    if tag=='html' and key=='lang':val='en'
    elif key in ('href','src'):val=self.url(val)
    elif val and (key in ('alt','title','aria-label') or tag=='meta' and key=='content'):val=translate(val)
    aa.append(' '+key if val is None else ' '+key+'="'+escape(val,quote=True)+'"')
   self.out.append('<'+tag+''.join(aa)+'>')
   if tag in ('script','style'):self.raw=True
  def handle_startendtag(self,t,a):self.handle_starttag(t,a)
  def handle_endtag(self,t):
   self.out.append('</'+t+'>')
   if t in ('script','style'):self.raw=False
  def handle_data(self,s):self.out.append(s if self.raw else escape(translate(s),quote=False))
 def controls(s,current,other,english):
  # These are real links, so both languages also work with JavaScript disabled.
  zh=other if english else current;en=current if english else other
  links=f'<nav class="language-switch" aria-label="Language"><a href="{zh}" lang="zh-Hant" hreflang="zh-Hant" '+('' if english else 'aria-current="page" ')+'>中文</a><a href="'+en+'" lang="en" hreflang="en" '+('aria-current="page" ' if english else '')+'>English</a></nav>'
  s=s.replace('<div class="actions">',links+'<div class="actions">',1)
  alternates=f'<link rel="alternate" hreflang="zh-Hant" href="{zh}"><link rel="alternate" hreflang="en" href="{en}">'
  return s.replace('</head>',alternates+'</head>')
 for p in pages:
  rel=p.relative_to(dist);s=p.read_text();parser=English(rel);parser.feed(s);en=''.join(parser.out)
  enpath=dist/'en'/rel;enpath.parent.mkdir(parents=True,exist_ok=True)
  entozh=posixpath.relpath(str(rel),'en/'+str(rel.parent))
  zhtoen=posixpath.relpath('en/'+str(rel),str(rel.parent))
  enpath.write_text(controls(en,'index.html',entozh,True))
  p.write_text(controls(s,'index.html',zhtoen,False))
 if missing:raise ValueError('Missing English translations: '+json.dumps(sorted(missing),ensure_ascii=False))
 # Include every language, directory URL and asset in the download bundle.
 sw=dist/'sw.js';s=sw.read_text();a=s.index('const FILES=');b=s.index(';',a)
 files=['./']+['./'+str(p.relative_to(dist)) for p in sorted(dist.rglob('*')) if p.is_file() and p.name!='sw.js']+['./'+str(p.parent.relative_to(dist))+'/' for p in sorted(dist.rglob('index.html')) if p.parent!=dist]
 s=s[:a]+'const FILES='+json.dumps(files)+s[b:]
 sw.write_text(s)
