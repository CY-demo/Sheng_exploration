"""Themed expedition homepage and consistent public branding."""
import re
from pathlib import Path
from rockies import t,T
BRAND='生生不息探險隊'
ENBRAND='Sheng Sheng Expeditions'

def brand(s):
 return s.replace('公園隨行',BRAND).replace('NATIONAL PARK FIELD GUIDE','SHENG SHENG EXPEDITIONS').replace('National Park Field Guide',ENBRAND)

def render_themes(ROOT,D,head):
 for zh,en in [(' / 交通與旅行準備',' / Getting There & Travel Essentials'),(' / 美國國家公園',' / U.S. National Parks'),(' / 自然景觀與戶外',' / Nature & Outdoors'),('AI-assisted build · 旅行紀錄與規劃參考','AI-assisted build · Travel journals and planning guidance'),('從一座公園開始。','Begin with one park.'),('讓好奇心繼續旅行。','Let curiosity keep traveling.'),('走進風景，','Step into the landscape.')]:t(zh,en)
 def photo(file,alt,english,prefix=''):
  return '<img src="'+prefix+'assets/'+file+'" alt="'+t(alt,english)+'" width="1200" height="750" loading="lazy">'
 def footer(prefix=''):
  return '</main><footer><strong>'+BRAND+'</strong><p>'+t('把走過的路，變成下一趟旅行的靈感。','Let the places we have explored inspire your next journey.')+'</p><a href="'+prefix+'index.html">'+t('返回主題首頁','Back to the theme homepage')+'</a><p class="fine">AI-assisted build · '+t('旅行紀錄與規劃參考','Travel journals and planning guidance')+'</p><p id="offline-status" role="status" aria-live="polite"></p></footer></body></html>'
 # Move the former park-only homepage into its own theme without changing park URLs.
 portal=(D/'index.html').read_text()
 def relocate(m):
  a,u=m.groups()
  if u.startswith(('#','http','mailto:','data:')):return m.group(0)
  return a+'="../../'+u+'"'
 portal=re.sub(r'(href|src)="([^"]+)"',relocate,portal)
 portal=portal.replace('<title>國家公園總覽｜','<title>美國國家公園｜').replace('<p class="eyebrow">NATIONAL PARKS / PERSONAL JOURNEYS</p>','<p class="eyebrow">THEME 01 / U.S. NATIONAL PARKS</p>').replace('從一座公園，<br>展開一趟旅行。','美國國家公園<br>從一座公園開始。')
 portal=portal.replace('<nav class="tabs">','<nav class="breadcrumbs"><a href="../../index.html">'+t('主題首頁','Theme homepage')+'</a> / '+t('美國國家公園','U.S. National Parks')+'</nav><nav class="tabs">',1)
 p=D/'themes/us-national-parks';p.mkdir(parents=True,exist_ok=True);(p/'index.html').write_text(portal)
 # Meaningful themes reuse existing public guides; no invented destinations.
 cards=[
 ('us-national-parks','01',t('美國國家公園','U.S. National Parks'),'us-illustrated-map.webp',t('八座公園，三條區域路線。從地圖選目的地，閱讀地景形成、短步道、遊客中心與逐日行程。','Eight parks and three regional routes. Choose a destination on the map, then explore landscapes, short walks, visitor centers and day-by-day journeys.'),t('8 座公園 · 中英文 · 地區分類','8 parks · bilingual · regional browsing')),
 ('nature-outdoors','02',t('自然景觀與戶外','Nature & Outdoors'),'page.jpg',t('走到國家公園之外，看羚羊谷的光影、馬蹄灣的河曲，以及 Matanuska 冰川與周邊步道。','Go beyond national park boundaries to Antelope Canyon’s light, Horseshoe Bend’s river curve, and Matanuska Glacier and nearby trails.'),t('峽谷 · 河流 · 冰川','Canyons · rivers · glaciers')),
 ('travel-practical','03',t('交通與旅行準備','Getting There & Travel Essentials'),'spots/anchorage-center.jpg',t('把旅程接起來：Anchorage 城市安排、火車與船班銜接，以及 SJC、LAS 機場貴賓室。','Connect the journey: Anchorage city plans, train and boat connections, and airport lounges at SJC and LAS.'),t('交通銜接 · 城市補給 · 機場','Connections · city stops · airports'))]
 # Choose a verified existing photo for the transport theme.
 for i,c in enumerate(cards):
  if not (D/'assets'/c[3]).exists():cards[i]=(*c[:3],'kenai.jpg',*c[4:])
 s=head(BRAND)+'<nav class="tabs"><a href="#themes">'+t('主題導覽','Explore by theme')+'</a><a href="themes/us-national-parks/#map">'+t('公園地圖','Park map')+'</a><a href="themes/us-national-parks/#routes">'+t('完整旅行路線','Complete journeys')+'</a></nav>'
 s+='<section class="expedition-hero"><div class="expedition-copy"><p class="eyebrow">SHENG SHENG EXPEDITIONS</p><h1>'+BRAND+'</h1><p class="expedition-tagline">'+t('走進風景，<br>讓好奇心繼續旅行。','Step into the landscape.<br>Let curiosity keep traveling.')+'</p><p>'+t('從親身走過的路出發，分享景點故事、交通銜接與可照著安排的旅程。選一個主題，開始下一段探索。','Starting with journeys we have taken, we share place stories, practical connections and itineraries you can follow. Choose a theme and begin your next exploration.')+'</p><a class="cta primary" href="#themes">'+t('選擇旅行主題 ↓','Choose a travel theme ↓')+'</a></div><a class="expedition-art" href="themes/us-national-parks/#map" aria-label="'+t('探索美國國家公園地圖','Explore the U.S. national parks map')+'">'+photo('us-illustrated-map.webp','美國地景與阿拉斯加、夏威夷的手繪風格旅行插畫','Illustrated U.S. landscapes with Alaska and Hawaii insets')+'<span>'+t('第一個主題 · 美國國家公園 ↗','Featured theme · U.S. National Parks ↗')+'</span></a></section>'
 s+='<section id="themes"><div class="section-title"><p class="eyebrow">CHOOSE YOUR NEXT CHAPTER</p><h2>'+t('依主題，展開旅程','Start your journey by theme')+'</h2><p>'+t('國家公園是探險的一個起點；自然景觀與旅行配套，也各有自己的入口。','National parks are one starting point. Natural landscapes and practical travel guides have their own entrances too.')+'</p></div><div class="theme-grid">'
 for slug,no,title,img,desc,meta in cards:
  s+='<article class="theme-card"><a class="theme-image" href="themes/'+slug+'/">'+photo(img,title+'主題照片',T[title]+' theme image')+'</a><div><p class="eyebrow">THEME '+no+'</p><h3><a href="themes/'+slug+'/">'+title+'</a></h3><p>'+desc+'</p><p class="fine">'+meta+'</p><a class="cta" href="themes/'+slug+'/">'+t('進入主題導覽 →','Explore this theme →')+'</a></div></article>'
 s+='</div></section><script src="theme-home.js" defer></script>'+footer();(D/'index.html').write_text(s)
 groups=[('nature-outdoors',cards[1],[
  ('nearby/page/',t('羚羊谷、馬蹄灣與 Page 周邊','Antelope Canyon, Horseshoe Bend & Page'),'page.jpg',t('砂岩裂縫、科羅拉多河、包威爾湖與水壩；搭配大峽谷行程串遊。','Sandstone slots, the Colorado River, Lake Powell and the dam; combine them with a Grand Canyon journey.')),
  ('nearby/matanuska/',t('Matanuska：觀景與冰川健行','Matanuska: viewpoints & glacier hiking'),'spots/matanuska.jpg',t('比較州立休憩區的簡單步行，以及由導遊帶領的冰面健行，選適合自己的體力與交通安排。','Compare easy walks at the state recreation site with guided glacier walks, choosing the exertion and transport that suit you.'))]),
  ('travel-practical',cards[2],[
  ('days/anchorage/',t('Anchorage：城市補給與銜接','Anchorage: city stops & connections'),'spots/anchorage-center.jpg',t('在長途旅行之間安排補給、用餐與市區走走，讓下一段出發更從容。','Fit in supplies, meals and city walks between longer travel legs, leaving breathing room before the next departure.')),
  ('routes/alaska/',t('阿拉斯加：火車、船班與飛行','Alaska: trains, boats & flights'),'kenai.jpg',t('沿九日旅行紀錄，看 Seward 船班、Denali 鐵路與 Katmai 航程如何銜接。','Follow a nine-day journey to see how Seward sailings, Denali rail travel and Katmai flights fit together.')),
  ('travel/airports/',t('SJC 與 LAS：機場貴賓室','SJC & LAS: airport lounges'),None,t('按機場查閱位置與信用卡使用資格。','Browse lounge locations and credit-card access by airport.'))])]
 for slug,card,items in groups:
  title=card[2];s=head(title,'../../')+'<nav class="breadcrumbs"><a href="../../index.html">'+t('主題首頁','Theme homepage')+'</a> / '+title+'</nav><section class="theme-intro"><p class="eyebrow">THEME '+card[1]+'</p><h1>'+title+'</h1><p>'+card[4]+'</p></section><div class="theme-grid">'
  for url,n,img,desc in items:
   s+='<article class="theme-card">'
   if img:
    if not (D/'assets'/img).exists():img='kenai.jpg'
    s+='<a class="theme-image" href="../../'+url+'">'+photo(img,n+'景觀',T[n]+' landscape','../../')+'</a>'
   s+='<div><h2>'+n+'</h2><p>'+desc+'</p><a class="cta" href="../../'+url+'">'+t('閱讀詳細導覽 →','Read the detailed guide →')+'</a></div></article>'
  s+='</div>'+footer('../../');p=D/'themes'/slug;p.mkdir(parents=True,exist_ok=True);(p/'index.html').write_text(s)
 # Preserve global home branding while making park-overview links return to the park theme.
 for p in D.rglob('*.html'):
  if 'en' in p.relative_to(D).parts:continue
  text=p.read_text()
  if p!=D/'index.html':
   def link(m):
    a=m.group(0)
    if 'class="brand"' in a:return a
    if any(x in a for x in ['國家公園總覽','選國家公園','index.html#parks','index.html#routes','index.html#nearby']):
     a=a.replace('href="../../index.html','href="../../themes/us-national-parks/index.html')
    return a
   text=re.sub(r'<a\b[^>]*>.*?</a>',link,text,flags=re.S)
  text=brand(text).replace('<span class="seal">山</span>','<span class="seal" aria-hidden="true">∞</span>')
  if p!=D/'index.html':text=text.replace('<div class="actions">','<a class="home-theme-link" href="../../index.html#themes">'+t('主題首頁','Theme homepage')+'</a><div class="actions">',1)
  # Translate new titles as whole strings, matching the existing static i18n builder.
  for title in [BRAND,'美國國家公園','自然景觀與戶外','交通與旅行準備']:
   t(title+'｜'+BRAND,(ENBRAND if title==BRAND else T[title])+' | '+ENBRAND)
  t(BRAND,ENBRAND)
  p.write_text(text)
