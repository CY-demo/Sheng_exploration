from pathlib import Path
from urllib.parse import urlsplit,unquote
from html.parser import HTMLParser
import json
class Doc(HTMLParser):
 def __init__(self,s):
  super().__init__();self.elements=[];self.feed(s)
 def handle_starttag(self,tag,attrs):self.elements.append((tag,dict(attrs)))
 def ids(self):return [a['id'] for t,a in self.elements if 'id' in a]
root=Path(__file__).parent/'dist'
pages=list(root.rglob('*.html'));assert len(pages)==32
for p in pages:
 s=p.read_text();doc=Doc(s)
 assert any(t=='meta' and a.get('name')=='viewport' for t,a in doc.elements)
 assert any(t=='h1' for t,a in doc.elements)
 assert len(doc.ids())==len(set(doc.ids()))
 for tag,a in doc.elements:
  if tag=='img':assert a.get('alt') and a.get('width') and a.get('height')
  for attr in ['href','src']:
   if attr not in a:continue
   link=a[attr];u=urlsplit(link)
   if u.scheme or u.netloc:continue
   target=(p.parent/unquote(u.path)).resolve() if u.path else p
   if target.is_dir():target=target/'index.html'
   assert target.is_relative_to(root.resolve()),(p,link)
   assert target.exists(),(p,link)
   if u.fragment and target.suffix=='.html':assert u.fragment in Doc(target.read_text()).ids(),(p,link)
 assert 'app.notion.com' not in s
 assert not any(x in s for x in ['原筆記','原始筆記','筆記提到','原路線'])
 assert not __import__('re').search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',s)

for p in (root/'assets').glob('*.jpg'):assert p.read_bytes().startswith(b'\xff\xd8')
assert len(json.loads((root/'parks.json').read_text()))==8
print('PASS: 32 bilingual pages, local assets and anchors, 8 park entries, mobile viewport, and private itinerary markers.')
from itinerary import DAYS
assert len(DAYS)==9
kenai=(root/'parks/kenai-fjords/index.html').read_text()
denali=(root/'parks/denali/index.html').read_text()
assert '12:00–17:30' in kenai
assert '提前報名' in denali and '48 小時' in denali
for d in DAYS:
 s=(root/d['page']/'index.html').read_text()
 assert f'id="day-{d["n"]}"' in s
manifest=json.loads((root/'assets/spots/manifest.json').read_text())
assert len(manifest)>=12
for entry in manifest.values():
 assert (root/'assets/spots'/entry['file']).exists()
sw=(root/'sw.js').read_text()
assert './days/anchorage/' in sw
for entry in manifest.values():assert './assets/spots/'+entry['file'] in sw
print('PASS: nine complete day routes, selected noon sailing, Denali advance-booking instructions, spot photos, offline assets.')
# Every public page has a complete, navigable English counterpart.
zhpages=[p for p in pages if 'en' not in p.relative_to(root).parts]
assert len(zhpages)==16
for p in zhpages:
 ep=root/'en'/p.relative_to(root)
 en=ep.read_text();zh=p.read_text()
 assert '<html lang="en">' in en
 assert not __import__('re').search('[\u4e00-\u9fff]',en.replace('中文','')),(ep,'untranslated content')
 assert set(Doc(zh).ids())==set(Doc(en).ids())
 assert 'class="language-switch"' in zh and 'class="language-switch"' in en
 assert './en/'+str(p.relative_to(root)) in sw
 for tag,a in Doc(en).elements:
  if tag=='a' and a.get('href') and not a.get('hreflang'):
   u=urlsplit(a['href'])
   if not u.scheme and not u.netloc and u.path:
    target=(ep.parent/u.path).resolve()
    if target.suffix=='.html' or target.is_dir():assert target.is_relative_to((root/'en').resolve()),(ep,a['href'])
for p in pages:
 assert not any(x in p.read_text() for x in ['日期已移除','移除私人出發日期','下方九日表是較寬鬆','補上了','原筆記'])
assert 'id="day-7"' in (root/'parks/katmai/index.html').read_text()
assert 'Copper Center' in (root/'en/parks/katmai/index.html').read_text()
print('PASS: all 16 English counterparts, full translation coverage, matching anchors, language-contained navigation and bilingual offline bundle.')

# New guides, geographic links and offline photographs.
from park_map import PARKS
assert len(PARKS)==8
home=Doc((root/'index.html').read_text())
markers=[a for tag,a in home.elements if tag=='a' and a.get('class')=='map-park']
assert len(markers)==8
assert len({a['href'] for a in markers})==8
for slug,lat,lon,*rest in PARKS:assert -180<=lon<=180 and 18<=lat<=72
photos=json.loads((root/'assets/yellowstone/manifest.json').read_text())
assert len(photos)==16
for item in photos.values():
 assert (root/item['file']).read_bytes().startswith(b'\xff\xd8')
 assert './'+item['file'] in sw
route=(root/'routes/yellowstone-grand-teton/index.html').read_text()
assert '我們實際在同一天' in route and 'Jenny Lake' in route and 'Mormon Row' in route
assert '第五天' in route
print('PASS: 8 geographic markers, 16 real attraction photos, actual compact route and separate extended option.')
