import json,re
from park_notes import render_notes
from extensions import render_extensions, matanuska_body
from actual_rides import render_rides
from pathlib import Path

def render_hub(parks,head,foot,esc,ROOT,D):
 def write(path,body):
  p=D/path/'index.html';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(body)
 def image(key,prefix='../../'):
  return f'<img src="{prefix}assets/{key}.jpg" alt="{esc(key)} 景觀照片" width="1200" height="750" loading="lazy">'
 def footer(prefix='../../'):
  return '</main><footer><strong>公園隨行 · National Park Field Guide</strong><p>旅行故事、景點介紹與交通安排。阿拉斯加記錄實際旅程；美西頁面為出發前的行程安排。班次與開放資訊以當季公告為準。</p><p><a href="'+prefix+'index.html">國家公園總覽</a> · <a href="'+prefix+'routes/alaska/">阿拉斯加九日</a> · <a href="'+prefix+'routes/southwest/">美西公園與峽谷</a></p><p class="fine">AI-assisted build · 圖片來源保留於各頁及照片資訊檔。</p><p id="offline-status" role="status" aria-live="polite"></p></footer></body></html>'
 # Preserve the complete Alaska itinerary under a stable regional route.
 alaska=(D/'index.html').read_text()
 def relocate(m):
  a,u=m.groups()
  if u.startswith(('#','http','mailto:','data:')):return m.group(0)
  return f'{a}="../../{u}"'
 alaska=re.sub(r'(href|src)="([^"]+)"',relocate,alaska)
 alaska=alaska.replace('https://cy-demo.github.io/Travel_DeathVelly_GrandCanyon/','../southwest/')
 alaska=alaska.replace('<section id="days">','<section class="chapter" id="our-route"><h2>我們實際搭乘的銜接與調整</h2><p>從 Anchorage 出發，搭火車看峽灣與 Denali，再飛到 Brooks Camp 看熊，最後自駕到 Copper Center。Katmai 第一次起飛後因天氣折返，隔天換業者才成行，成為這趟旅行最難忘的轉折。</p><div class="quick-stops"><a href="../../parks/kenai-fjords/#our-connections">火車與 Seward 船班</a><a href="../../parks/denali/#our-connections">Denali 飯店、飛行與巴士接駁</a><a href="../../parks/katmai/#our-connections">Katmai 原訂航程、折返與補飛</a></div></section><section id="days">')
 alaska=alaska.replace('</main>', '<section><h2>想延伸行程？</h2><div class="quick-stops"><a href="../../parks/katmai/#alternatives">Katmai 過夜與看熊季節</a><a href="../../parks/wrangell-st-elias/#alternatives">McCarthy 與 Root Glacier</a><a href="../../nearby/matanuska/">Matanuska 冰川健行</a></div></section></main>')
 write(Path('routes/alaska'),alaska)
 write(Path('nearby/matanuska'),head('Matanuska 冰川觀景與健行','../../')+matanuska_body()+footer())
 for p in [*D.glob('parks/*/index.html'),D/'days/anchorage/index.html',D/'routes/alaska/index.html']:
  if p.parent.name in ('grand-canyon','death-valley','yellowstone','grand-teton'):continue
  text=p.read_text().replace('../../index.html#days','../../routes/alaska/#days')
  text=text.replace('<nav class="breadcrumbs">','<nav class="breadcrumbs"><a href="../../index.html">國家公園總覽</a><span>／</span>')
  text=text.replace('<a href="../../routes/alaska/#days">返回逐日行程 ↑</a>','<a href="../../index.html">國家公園總覽 ↑</a> · <a href="../../routes/alaska/#days">阿拉斯加行程</a>')
  if p.parent.name in [x['slug'] for x in parks]:
   jump='<nav class="quick-stops" aria-label="閱讀這座公園"><a href="#'+('our-connections' if p.parent.name in ('kenai-fjords','denali','katmai') else 'day-8')+'">旅行紀錄</a><a href="#park-notes">景點與心得</a>'+('<a href="#alternatives">延伸玩法</a>' if p.parent.name in ('katmai','wrangell-st-elias') else '')+'</nav>'
   text=text.replace('<nav class="tabs day-tabs">',jump+render_rides(p.parent.name)+render_notes(p.parent.name,esc)+render_extensions(p.parent.name)+'<nav class="tabs day-tabs">')
  p.write_text(text)
 c=json.loads((ROOT/'canyon-content.json').read_text())
 days={x['id']:x for x in c['days']}
 paths={'death':'parks/death-valley','grand':'parks/grand-canyon','page':'nearby/page','airport':'travel/airports'}
 labels={'death':'死亡谷','grand':'大峽谷','page':'羚羊谷與馬蹄灣','airport':'機場貴賓室'}
 def refs(keys):
  return '<div class="refs">'+''.join(f'<a href="{esc(c["sources"][k][1])}" target="_blank" rel="noopener">{esc(c["sources"][k][0])} ↗</a>' for k in keys if k in c['sources'])+'</div>'
 for key,day in days.items():
  title=labels[key];body=head(title,'../../')+f'<nav class="breadcrumbs"><a href="../../index.html">國家公園總覽</a>／<a href="../../routes/southwest/">美西行程</a>／{title}</nav>'
  if key!='airport':body+=f'<section class="park-hero"><div>{image(key)}</div><div class="hero-copy"><p class="eyebrow">{"NATIONAL PARK" if key in ("death","grand") else "NEARBY EXPLORATIONS"}</p><h1>{title}</h1><p>{esc(day["subtitle"])}</p><p>{esc(day["summary"].replace("原行程參考","行程參考"))}</p></div></section>'
  else:body+='<h1>機場貴賓室</h1><p>依機場展開，查位置與可用信用卡。</p>'
  body+='<nav class="tabs"><a href="../../index.html#parks">選國家公園</a><a href="../../routes/southwest/">相關完整行程</a><a href="../../nearby/page/">Page 周邊景點</a><a href="../../travel/airports/">機場資訊</a></nav>'
  if key in ('death','grand'):body+=render_notes('death-valley' if key=='death' else 'grand-canyon',esc)
  if key=='airport':
   for code,name in [('SJC','聖荷西'),('LAS','拉斯維加斯')]:
    body+=f'<details class="chapter" open><summary>{code} {name}機場</summary>'
    for ch in day['chapters']:
     if ch['title'].startswith(code):body+=f'<article id="{esc(ch["id"])}"><h2>{esc(ch["title"])}</h2><p style="white-space:pre-line">{esc(ch["lead"])}</p>'+refs(ch['sources'])+'</article>'
    body+='</details>'
  else:
   body+='<div class="section-title"><h2>分站導覽</h2><button id="expand">展開詳細介紹</button></div><div class="park-reading"><nav class="park-nav">'+''.join(f'<a href="#{esc(ch["id"])}">{esc(ch["title"])}</a>' for ch in day['chapters'])+'</nav><div>'
   for ch in day['chapters']:
    body+=f'<article class="chapter" id="{esc(ch["id"])}"><p class="eyebrow">{esc(ch["en"])}</p><h2>{esc(ch["title"])}</h2><span class="time-kind">{esc(ch.get("status","").replace("原行程","行程停留"))} · {esc(ch.get("time",""))}</span><p class="lead">{esc(ch["lead"])}</p>'
    if ch.get('table'):
     t=ch['table'];body+='<div class="table-wrap"><table><caption>'+esc(t['caption'])+'</caption><thead><tr>'+''.join('<th>'+esc(x)+'</th>' for x in t['headers'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+esc(v)+'</td>' for v in row)+'</tr>' for row in t['rows'])+'</tbody></table></div>'
    body+='<details><summary>詳細介紹與形成故事</summary>'+''.join('<p>'+esc(x)+'</p>' for x in ch['paras'])+'</details><p><strong>現場看什麼</strong><br>'+esc(ch['look'])+'</p><p><strong>簡單走走與行程提醒</strong><br>'+esc(ch['walk'])+'</p>'+refs(ch['sources'])+'</article>'
   body+='</div></div>'
  write(Path(paths[key]),body+footer())
 # Park cards expose both the individual guide and its wider itinerary.
 entries=[{'slug':'grand-canyon','name':'大峽谷','en':'Grand Canyon','image':'grand','region':'southwest','desc':'南緣觀景、Yavapai 地質博物館與直升機體驗。','route':'routes/southwest/','route_label':'拉斯維加斯・大峽谷・Page','near':'nearby/page/','near_label':'羚羊谷與馬蹄灣'}, {'slug':'death-valley','name':'死亡谷','en':'Death Valley','image':'death','region':'southwest','desc':'鹽灘、沙丘與彩色山丘，逐站認識沙漠地景。','route':'routes/southwest/','route_label':'拉斯維加斯往返與串遊','near':'routes/southwest/#death-route','near_label':'鬼城與公路沿途'}]
 for p in parks:
  entries.append(dict(slug=p['slug'],name=p['name'],en=p['en'],image=p['image'],region='alaska',desc=p['intro'],route='routes/alaska/',route_label='阿拉斯加九日完整行程',near=('nearby/matanuska/' if p['slug']=='wrangell-st-elias' else 'days/anchorage/'),near_label=('Matanuska 觀景與冰川健行' if p['slug']=='wrangell-st-elias' else 'Anchorage 與交通安排')))
 from park_map import entries as new_entries,render_map,filters
 entries=new_entries()+entries
 for item in entries:
  if item['region']=='southwest':item['region']='west'
 cards=''
 for e in entries:
  cards+=f'<article class="park-card hub-card" data-region="{e["region"]}">{image(e["image"],"")}<div><p class="eyebrow">{"ALASKA" if e["region"]=="alaska" else "AMERICAN WEST"}</p><h3>{e["name"]}<small>{e["en"]}</small></h3><p>{e["desc"]}</p><a class="cta primary" href="parks/{e["slug"]}/">進入公園導覽 →</a><div class="card-links"><a href="{e["route"]}">{e["route_label"]} ↗</a><a href="{e["near"]}">{e["near_label"]} ↗</a></div></div></article>'
 home=head('國家公園總覽')+'<nav class="tabs"><a href="#map">公園地圖</a><a href="#parks">選國家公園</a><a href="#routes">完整行程</a><a href="#nearby">周邊景點</a><a href="travel/airports/">機場貴賓室</a></nav>'
 home+=f'<section class="hero"><div class="hero-photo">{image("grand","")}</div><div class="hero-copy"><p class="eyebrow">NATIONAL PARKS / PERSONAL JOURNEYS</p><h1>從一座公園，<br>展開一趟旅行。</h1><p>看懂地景，也知道怎麼安排。<br>把親身經驗、景點故事與逐日路線放在一起。</p><a class="cta" href="#parks">選擇想去的國家公園 ↗</a></div></section><div class="overview-strip"><span>8 座國家公園</span><span>3 條區域行程</span><span>中文／English・照片・離線閱讀</span></div>'
 home+=render_map(ROOT)
 home+='<section id="parks"><div class="section-title"><p class="eyebrow">CHOOSE YOUR PARK</p><h2>國家公園總覽</h2><p>先選一座公園，再連到完整路線與周邊景點。</p></div>'+filters()+'<div class="park-grid">'+cards+'</div></section>'
 home+='<section id="routes"><div class="section-title"><p class="eyebrow">FOLLOW THE JOURNEY</p><h2>想直接照著安排？選完整行程。</h2></div><div class="reading-grid route-options"><article><p class="eyebrow">YELLOWSTONE / GRAND TETON</p><h3>熱泉・野生動物・提頓山脈</h3><p>Bozeman 進出，四日串遊兩園；景點取捨、短步道與第五日延伸。</p><a class="cta" href="routes/yellowstone-grand-teton/">看黃石與大提頓路線 →</a></article><article><p class="eyebrow">SOUTHWEST</p><h3>拉斯維加斯・沙漠與峽谷</h3><p>死亡谷一日，加上大峽谷與 Page 兩日路線；串聯羚羊谷、馬蹄灣與沿途停留。</p><a class="cta" href="routes/southwest/">看美西行程 →</a></article><article><p class="eyebrow">ALASKA / 9 DAYS</p><h3>鐵路・冰川・四座國家公園</h3><p>Seward 遊船、Denali 火車與飛行、Katmai 看熊，再沿公路到 Copper Center。</p><a class="cta" href="routes/alaska/">看阿拉斯加九日 →</a></article></div></section>'
 home+='<section id="nearby"><div class="section-title"><p class="eyebrow">AROUND THE PARKS</p><h2>周邊景點與旅行配套</h2><p>這些是路線上的延伸停留，另列於國家公園之外。</p></div><div class="reading-grid"><article><h3>Page：羚羊谷與馬蹄灣</h3><p>砂岩、科羅拉多河、包威爾湖與水壩。</p><a href="nearby/page/">進入周邊導覽 →</a></article><article><h3>Matanuska 觀景與冰川健行</h3><p>比較州立休憩區短走與有導遊的冰面健行，選擇自駕或 Anchorage 接送。</p><a href="nearby/matanuska/">看交通與一日安排 →</a></article><article><h3>Anchorage 與機場</h3><p>城市補給、行程緩衝與 SJC／LAS 貴賓室位置。</p><a href="days/anchorage/">Anchorage 安排 →</a><br><a href="travel/airports/">依機場查貴賓室 →</a></article></div></section>'
 home+='<script src="hub.js" defer></script>'+footer('')
 (D/'index.html').write_text(home)
 # A regional itinerary connects independent southwest guides.
 sw=head('美西公園與峽谷行程','../../')+'<nav class="breadcrumbs"><a href="../../index.html">國家公園總覽</a>／美西行程</nav><section class="park-hero"><div>'+image('death')+'</div><div class="hero-copy"><p class="eyebrow">LAS VEGAS / SOUTHWEST</p><h1>沙漠、峽谷，<br>與光影中的河流。</h1><p>以拉斯維加斯為出發點：死亡谷往返一日，再搭配大峽谷與 Page 兩日路線。實際接送、停留與出團日期以訂購業者確認為準。</p></div></section><section id="death-route"><h2>建議路線順序</h2><div class="days-grid">'
 for key,tag in [('death','第 1 日 · 拉斯維加斯往返'),('grand','第 2 日 · 南緣 → Page'),('page','第 3 日 · Page → 拉斯維加斯')]:
  d=days[key];sw+=f'<a class="day-link" href="../../{paths[key]}/"><span class="eyebrow">{tag}</span><h3>{labels[key]}</h3><p>{esc(d["subtitle"])}</p><b>看分站導覽 →</b></a>'
 sw+='</div><div class="schedule-note"><strong>交通日另留時間</strong><p>這是三個遊覽日的組合，不含抵達及離開拉斯維加斯的航班日。大峽谷與 Page 的兩日團需配合出團日；回城日不安排需要準時趕上的晚班飛機。</p></div></section><section><h2>選一座公園，或搭配周邊</h2><div class="quick-stops"><a href="../../parks/death-valley/">死亡谷</a><a href="../../parks/grand-canyon/">大峽谷</a><a href="../../nearby/page/">羚羊谷與馬蹄灣</a><a href="../../travel/airports/">機場貴賓室</a></div></section>'+footer()
 write(Path('routes/southwest'),sw)
 (D/'parks.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2))
 # One offline bundle covers both regions and every child page.
 swpath=D/'sw.js';text=swpath.read_text();a=text.index('const FILES=');b=text.index(';',a)
 files=['./']+['./'+str(p.relative_to(D)) for p in D.rglob('*') if p.is_file() and p.name!='sw.js']+['./'+str(p.parent.relative_to(D))+'/' for p in D.rglob('index.html') if p.parent!=D]
 text=text[:a]+'const FILES='+json.dumps(files)+text[b:];text=text.replace('alaska-field-guide-v2:','parks-field-guide-v3:');swpath.write_text(text)
