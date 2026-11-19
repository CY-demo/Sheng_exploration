"""Bilingual, privacy-safe Fairbanks winter route."""
from html import escape

DATA = {
'zh': {
 'lang':'zh-Hant','title':'費爾班克斯｜六天五夜冬季追光','link':'費爾班克斯冬季追光','intro':'不用租車，以費爾班克斯市區為據點：白天看雪橇犬、泡溫泉和逛博物館，晚上在暖屋等極光。最後一晚留給休息，不必每天追到凌晨。',
 'home':'主題首頁','theme':'自然景觀與戶外','skip':'跳至內容','plan':'六天總覽','tours':'三個團怎麼玩','pack':'穿著與打包','refs':'實用資訊',
 'notice':'這是可照著安排的路線範例，不是已走訪紀錄。團體時刻皆為阿拉斯加當地時間；接送、站序和回程依各團通知。',
 'days':[
 ('抵達費爾班克斯','若搭晚班機，建議在落地前吃晚餐。先核對住宿的機場接駁方式；領完行李再聯絡飯店估接車時間。'),
 ('狗拉雪橇、馴鹿與暖屋追光','白天去 Borealis Basecamp；晚餐後再去 Aurora Borealis Lodge。暖屋團的接車通常為深夜前，約翌日 02:30 回飯店。'),
 ('珍娜溫泉＋夜間追光','白天留給補眠和採買。下午飯店接送，依序安排冰雕館、晚餐、泡湯與回程追極光。'),
 ('市區巡禮＋玻璃屋','下午逛遊客中心、博物館、輸油管和聖誕老人之家；回市區先吃飯，晚間去 Cleary Summit 玻璃屋。含接送方案約五小時，名義場次 21:30；實際接車看簡訊。'),
 ('休息日／感恩節備案','如果碰到感恩節，午餐先核對餐廳營業與訂位。晚上不排團，可問飯店是否有極光叫醒服務。雲厚就早點休息。'),
 ('退房與返程','前一晚約住宿接駁。假期飛離 FAI 時，至少提早兩小時到機場；仍以自己的航班與行李需求調整。')],
 'details':[
 ('sled','狗拉雪橇＋馴鹿','Borealis Basecamp｜白天團',[
 ('09:15 就緒；09:30–10:00 接車','依團方指示分組，坐狗拉雪橇穿過雪地林間，再近距離觀察馴鹿；兩項先後依當天安排。'),
 ('午餐｜Latitude 65','此方案列每人 US$20 午餐抵用額，超額自付；確認你選的票券是否包含。'),
 ('約 17:15–17:45 回市區','估 16:30–17:00 離開營地，路況及各飯店下車順序會影響時間。')]),
 ('chena','珍娜溫泉＋追極光','Alaska Wild Lights｜下午至翌日',[
 ('16:00–16:30 接車','約 17:30 抵達度假村；先看冰雕館，門票列在此方案內。'),
 ('19:00–21:00 晚餐','餐費自付；可先準備點心。'),
 ('21:00–23:30 泡湯和自由活動','方案含泡湯入場；若不想一直待在戶外，可以回室內暖和一下。'),
 ('深夜追光；約翌日 02:00 回飯店','視雲況、路況和極光活動，導遊會調整回程停靠點。')]),
 ('heritage','市區巡禮','Heritage Tour｜下午班例 13:00–約 18:30',[
 ('Morris Thompson 遊客中心','先去 Public Lands Information Center 櫃檯蓋國家公園章，再看原住民文化和自然展。已看到極光的話，也可問旅遊櫃檯有沒有極光證書。'),
 ('北方博物館','室內看阿拉斯加地景、野生動物與原住民文化。確認票券列的門票項目。'),
 ('跨阿拉斯加輸油管','戶外短停、看高架輸油管和拍照。'),
 ('North Pole 聖誕老人之家','逛聖誕主題商店；不保證遇到聖誕老人。導遊可能依季節調整站序。')])],
 'wear':[
 ('雪橇','排汗底層、刷毛中層、防風外套、雪褲；厚羊毛襪、保暖防滑雪靴、連指手套、毛帽、脖圍和備用手套。先核對票券含哪些雪地裝備。'),
 ('溫泉','照樣穿冬裝，另帶泳衣、毛巾、防滑拖鞋、乾襪和濕物袋。置物櫃每個需兩枚 25 美分硬幣，毛巾租用另計。'),
 ('市區與夜間','市區室內外切換多，選好脫穿的中層、羽絨外套和防滑鞋，帶一本國家公園護照或空白卡。夜間下車追光再戴脖圍、厚手套，備妥暖暖包。')],
 'links':['Basecamp 行程','珍娜溫泉團','珍娜溫泉置物櫃','Heritage 路線','極光與暖屋','Cleary Summit 玻璃屋','FAI 旅客資訊'],
},
'en': {
 'lang':'en','title':'Fairbanks | Six days of winter and northern lights','link':'Fairbanks winter aurora itinerary','intro':'A car-free Fairbanks base for dog sledding, hot springs, a city tour and heated aurora lodges. Leave the final night open so the trip does not mean staying out late every night.',
 'home':'Theme homepage','theme':'Nature & Outdoors','skip':'Skip to content','plan':'Six-day overview','tours':'Three tours in detail','pack':'Clothing and packing','refs':'Visitor resources',
 'notice':'This is a planning route, not a record of a completed trip. Tour times are local to Alaska. Follow your operator’s pickup notice for exact times, stops and drop-off.',
 'days':[
 ('Arrive in Fairbanks','For a late flight, eat before landing. Check your lodging’s airport shuttle procedure and call for pickup after collecting bags.'),
 ('Dog sledding, reindeer and aurora lodge','Visit Borealis Basecamp by day and Aurora Borealis Lodge after dinner. The lodge tour returns at approximately 2:30 a.m. the next morning.'),
 ('Chena Hot Springs and aurora','Sleep in and buy supplies in the morning. Follow the evening tour through the ice museum, dinner, hot springs and aurora stops on the way back.'),
 ('Fairbanks sights and aurora glass house','Visit the visitor center, museum, pipeline and Santa Claus House. Eat back in town, then head to the Cleary Summit glass house. The transit-inclusive tour takes about five hours and is listed at 9:30 p.m.; check the operator text for pickup.'),
 ('Rest day or Thanksgiving','Check holiday restaurant hours and reserve lunch if needed. Leave the evening open and ask your hotel about an aurora wake-up call. If clouds settle in, get a good night’s sleep.'),
 ('Checkout and departure','Arrange your airport shuttle the night before. For holiday departures from FAI, arrive at least two hours early and allow extra time as needed.')],
 'details':[
 ('sled','Dog sledding and reindeer','Borealis Basecamp | Day trip',[
 ('Ready at 9:15 a.m.','Pickup is typically 9:30–10:00 a.m. Group assignments determine the order of the forest dog-sled ride and the reindeer encounter.'),
 ('Lunch at Latitude 65','This option lists a US$20 lunch voucher per person. Pay any difference and check that your chosen ticket includes it.'),
 ('Return around 5:15–5:45 p.m.','Estimated camp departure is 4:30–5:00 p.m.; driving conditions and drop-off order affect the return.')]),
 ('chena','Chena Hot Springs and aurora','Alaska Wild Lights | Afternoon to early morning',[
 ('4:00–4:30 p.m.','Hotel pickup. Approximate resort arrival is 5:30 p.m.; the listed package includes the ice museum.'),
 ('7:00–9:00 p.m.','Dinner is at your own expense. Bring a snack if helpful.'),
 ('9:00–11:30 p.m.','Hot springs and free time. Pool access is included in this option. Warm up indoors if needed.'),
 ('About 2:00 a.m. next day','The operator adjusts roadside aurora stops according to clouds, road conditions and aurora activity.')]),
 ('heritage','Fairbanks Heritage Tour','Example afternoon departure: 1:00–about 6:30 p.m.',[
 ('Morris Thompson Visitor Center','Start at the Public Lands Information Center for a National Parks passport stamp, then visit the cultural and nature exhibits. If you have seen the northern lights, ask the tourism desk about a certificate.'),
 ('Museum of the North','Explore Alaska landscapes, wildlife and Alaska Native culture indoors. Check the admission details on your ticket.'),
 ('Trans-Alaska Pipeline','A short outdoor stop for photos and a look at the aboveground pipeline.'),
 ('Santa Claus House in North Pole','Browse the holiday shop and take photos; a Santa appearance is not guaranteed. Stop order may change seasonally.')])],
 'wear':[
 ('Sledding','Moisture-wicking base layer, fleece, windproof jacket, snow pants, wool socks and insulated grippy boots. Bring mittens, a hat, a neck gaiter and spare gloves. Check what winter gear the ticket includes.'),
 ('Hot springs','Wear winter layers and pack a swimsuit, towel, grippy sandals, dry socks and a wet bag. Bring two quarters per locker; towel rental is extra.'),
 ('Town and aurora','Wear a removable middle layer, warm coat and grippy footwear. Bring a parks passport or spare paper. Add thick gloves, a neck gaiter and hand warmers for aurora stops.')],
 'links':['Basecamp day trip','Chena tour','Chena lockers','Heritage route','Aurora at the lodge','Cleary Summit glass house','Fairbanks airport'],
}}
URLS=[
 'https://www.viator.com/tours/Fairbanks/Dogsled-and-Reindeer-Day-Trip-to-Borealis-Basecamp/d5269-165060P18',
 'https://alaskawildlights.com/northern-lights-tours/chena-hot-springs/',
 'https://www.chenahotsprings.com/pool-house/',
 'https://alaskawildlights.com/summer-tours/fairbanks-heritage-tour/',
 'https://auroracabin.com/aurora-viewing-tours-fairbanks-2/',
 'https://www.viator.com/tours/Fairbanks/Aurora-Viewing-at-Lodge-5-Hours/d5269-467876P2',
 'https://dot.alaska.gov/faiiap/',
]
def render(dist):
 for lang,c in DATA.items():
  is_en=lang=='en'
  base=dist/'en' if is_en else dist
  route=base/'routes/fairbanks-winter'
  route.mkdir(parents=True,exist_ok=True)
  root='../../../' if is_en else '../../'
  alt=root + ('routes/fairbanks-winter/' if is_en else 'en/routes/fairbanks-winter/')
  own=root+('en/' if is_en else '')
  nav=''.join(f'<a href="#{key}">{c[key]}</a>' for key in ('plan','tours','pack','refs'))
  dates=''.join(f'<li><a href="#day-{i}">Day {i}</a></li>' for i in range(1,7))
  days=''.join(f'<article class="fb-day" id="day-{i}"><p class="eyebrow">DAY {i:02}</p><h3>{escape(title)}</h3><p>{escape(body)}</p>{f"""<a href="#{("sled","chena","heritage")[i-2]}">{("Tour details" if is_en else "看詳細行程")}</a>""" if i in (2,3,4) else ""}</article>' for i,(title,body) in enumerate(c['days'],1))
  detail=''
  for slug,title,sub,stops in c['details']:
   detail+=f'<details class="fb-detail" id="{slug}" open><summary><strong>{escape(title)}</strong><small>{escape(sub)}</small></summary><ol>'+''.join(f'<li><strong>{escape(t)}</strong><p>{escape(p)}</p></li>' for t,p in stops)+'</ol></details>'
  wear=''.join(f'<li><strong>{escape(t)}</strong><p>{escape(p)}</p></li>' for t,p in c['wear'])
  refs=''.join(f'<li><a href="{u}">{escape(n)}</a></li>' for n,u in zip(c['links'],URLS))
  brand=f'<a class="brand" href="{own}index.html"><span class="seal" aria-hidden="true">∞</span><span>Sheng Exploration<small>SHENG EXPLORATION</small></span></a>'
  links=f'<a lang="zh-Hant" hreflang="zh-Hant" href="{alt if is_en else "./"}">中文</a><a lang="en" hreflang="en" href={"./" if is_en else alt}>English</a>'
  home=f'<a href="{own}index.html">{c["home"]}</a>'
  (route/'index.html').write_text(f'''<!doctype html>
<html lang="{c['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#123439"><title>{escape(c['title'])}｜Sheng Exploration</title><meta name="description" content="{escape(c['intro'])}"><link rel="stylesheet" href="{root}style.css"><link rel="stylesheet" href="{root}fairbanks.css"><script src="{root}app.js" defer></script></head>
<body><a class="skip" href="#main">{c['skip']}</a><header>{brand}<nav class="language-switch" aria-label="Language">{links}</nav></header><main id="main" class="fb"><nav class="breadcrumbs">{home} / <a href="{own}themes/nature-outdoors/">{c['theme']}</a></nav>
<section class="fb-hero"><p class="eyebrow">ALASKA IN WINTER</p><h1>{escape(c['title'])}</h1><p>{escape(c['intro'])}</p></section>
<nav class="tabs">{nav}</nav><p class="fb-note">{escape(c['notice'])}</p>
<section id="plan"><h2>{c['plan']}</h2><ol class="fb-jump">{dates}</ol><div class="fb-grid">{days}</div></section>
<section id="tours"><h2>{c['tours']}</h2>{detail}</section>
<section id="pack"><h2>{c['pack']}</h2><ul class="fb-wear">{wear}</ul></section>
<section id="refs"><h2>{c['refs']}</h2><ul class="fb-links">{refs}</ul></section></main>
<footer><strong>Sheng Exploration</strong><p>{home}</p><p id="offline-status" role="status"></p></footer></body></html>''')
  homepath=base/'index.html'
  hp=homepath.read_text()
  link=f'<a class="fb-home-link" href="routes/fairbanks-winter/">{escape(c["link"])}</a>'
  if link not in hp: homepath.write_text(hp.replace('</nav><section class="expedition-hero">',link+'</nav><section class="expedition-hero">',1))
  theme=base/'themes/nature-outdoors/index.html'
  tp=theme.read_text()
  card=f'<article class="theme-card"><div><p class="eyebrow">ALASKA IN WINTER</p><h2>{escape(c["link"])}</h2><p>{escape(c["intro"])}</p><a class="cta" href="../../routes/fairbanks-winter/">{escape(c["plan"])}</a></div></article>'
  if card not in tp: theme.write_text(tp.replace('</div></main><footer>',card+'</div></main><footer>',1))
 (dist/'fairbanks.css').write_text('''
.fb{max-width:73rem;margin-inline:auto}.fb-hero{padding:clamp(1.5rem,6vw,4rem);border-radius:1.3rem;color:#f5fffc;background:radial-gradient(ellipse at 78% 6%,#267461 0%,transparent 59%),linear-gradient(130deg,#102537,#1a4654);margin:1rem 0}.fb-hero h1{color:inherit;font-size:clamp(2rem,5.5vw,4rem);line-height:1.16;margin:.4em 0}.fb-hero .eyebrow{color:#ace4d4}.fb-hero p{max-width:57ch}.fb-note{border-left:4px solid #53968a;padding:.6rem 1rem;margin-block:1rem}.fb-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem}.fb-day,.fb-detail,.fb-wear li{background:#f3f8f7;color:#163137;padding:1.1rem 1.2rem;border:1px solid #c7ded9;border-radius:.85rem}.fb-day h3,.fb-day p{margin:.4rem 0 .7rem}.fb section{scroll-margin-top:7rem}.fb article,.fb details{scroll-margin-top:7rem}.fb-detail{margin-bottom:1rem}.fb-detail summary{cursor:pointer;font-size:1.18rem}.fb-detail summary small{display:block;margin:.35rem 0 0 1.2rem;font-size:.94rem}.fb-detail li p,.fb-wear p{margin:.25rem 0 .7rem}.fb-wear,.fb-jump,.fb-links{display:flex;flex-wrap:wrap;gap:.7rem;list-style:none;padding:0}.fb-wear>li{flex:1 1 15rem}.fb-jump a,.fb-links a,.fb-home-link{display:inline-block;padding:.45rem .68rem}.fb a:focus-visible{outline:3px solid #245f57;outline-offset:3px}@media(max-width:52rem){.fb-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:36rem){.fb-grid{grid-template-columns:1fr}.fb-hero{padding:1.5rem}.fb-detail ol{padding-left:1.35rem}}''')
