"""High-resolution real attraction photographs with bilingual captions."""
import json,re,posixpath
from pathlib import Path
from html import escape
from rockies import t

def enhance(root,dist):
 manifest=json.loads((dist/'assets/park-scenes/manifest.json').read_text())
 byslug={m['slug']:m for m in manifest}
 def figure(m,prefix='../../',extra=''):
  t(m['alt_zh'],m['alt_en']);t(m['title_zh'],m['title_en'])
  label=t('點開高解析照片','Open the high-resolution photo')
  return f'<figure class="hires-photo"><a class="photo-full" href="{prefix}{m["file"]}" target="_blank" rel="noopener" aria-label="{label}"><img src="{prefix}{m["file"]}" alt="{escape(m["alt_zh"])}" width="{m["width"]}" height="{m["height"]}" loading="lazy" decoding="async"></a><figcaption><span>{m["title_zh"]}</span><a href="{escape(m["source"])}">{escape(m["credit"])}</a><a href="{prefix}{m["file"]}" target="_blank" rel="noopener">{label} ↗</a></figcaption>{extra}</figure>'
 # Large source photographs also replace the park cover in cards and route pages.
 heroes={'grand':'mather-point','death':'zabriskie','kenai':'kenai-cover','denali':'denali-cover','katmai':'katmai-cover','wrangell':'wrangell-cover'}
 replacement={'wrangell-center':'wrangell-center','culture':'ahtna-center','dogs':'denali-dogs','savage':'savage-river','brooks-river':'katmai-river','brooks-falls':'katmai-falls'}
 for p in dist.rglob('*.html'):
  if 'en' in p.relative_to(dist).parts:continue
  s=p.read_text();prefix=posixpath.relpath('.',str(p.parent.relative_to(dist)))+'/'
  if prefix=='./':prefix=''
  # Replace complete older spot figures so credits cannot become stale.
  def spot(match):
   block=match.group(0)
   for key,slug in replacement.items():
    if f'assets/spots/{key}.jpg' in block and slug in byslug:return figure(byslug[slug],prefix)
   return block
  s=re.sub(r'<figure\b[^>]*>.*?</figure>',spot,s,flags=re.S)
  for old,slug in heroes.items():
   if slug not in byslug:continue
   m=byslug[slug];t(m['alt_zh'],m['alt_en'])
   pattern=r'<img\b[^>]*src="[^"]*assets/'+old+r'\.jpg"[^>]*>'
   img=f'<img src="{prefix}{m["file"]}" alt="{escape(m["alt_zh"])}" width="{m["width"]}" height="{m["height"]}" loading="lazy">'
   s=re.sub(pattern,lambda _:img,s)
  p.write_text(s)
 for park in ['grand-canyon','death-valley','kenai-fjords','denali','katmai','wrangell-st-elias']:
  p=dist/'parks'/park/'index.html';s=p.read_text();items=[m for m in manifest if m['park']==park and m.get('display',True)]
  gallery='<section id="landscape-photos" class="landscape-gallery"><p class="eyebrow">LANDSCAPES IN DETAIL</p><h2>'+t('主要景點・大幅實景照片','Major sights · full-size landscape photographs')+'</h2><p>'+t('點開照片可看高解析版本。照片呈現景點風貌；季節、天候與實際停留依各頁行程說明。','Open a photo for its high-resolution version. Images illustrate the scenery; seasons, conditions and actual stops follow the itinerary descriptions.')+'</p>'
  for m in items:
   extra=''
   if m['slug'] in ['exit-glacier','kennecott','root-glacier','desert-view']:
    extra='<p class="fine">'+t('延伸景點：需另留時間，不代表已包含在本頁實際行程或所訂團體行程。','Optional extension: allow additional time. This does not imply inclusion in the recorded itinerary or booked tour.')+'</p>'
   gallery+='<article><h3>'+t(m['title_zh'],m['title_en'])+'</h3>'+figure(m,extra=extra)+'</article>'
  gallery+='</section>'
  # Place imagery before the descriptive notes, with a direct jump for repeat readers.
  s=s.replace('<section id="park-notes">',gallery+'<section id="park-notes">',1)
  p.write_text(s)
