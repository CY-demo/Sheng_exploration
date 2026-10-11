from pathlib import Path
import json, html

ROOT=Path(__file__).parent
D=ROOT/'dist'
def esc(s): return html.escape(s,quote=True)
parks=[{'slug': 'kenai-fjords',
  'image': 'kenai',
  'name': '基奈峽灣',
  'en': 'Kenai Fjords',
  'intro': '從 Seward 出海，看山谷中的冰緩緩抵達海洋。海岸線的形狀，是冰川留下的立體筆記。',
  'sources': [('NPS｜Kenai Fjords', 'https://www.nps.gov/kefj/index.htm'),
              ('NPS｜Exit Glacier 與步道', 'https://www.nps.gov/kefj/planyourvisit/exit-glacier-area.htm'),
              ('Alaska Railroad｜Coastal Classic',
               'https://www.alaskarailroad.com/ride-a-train/route-map/coastal-classic')]},
 {'slug': 'denali',
  'image': 'denali',
  'name': '丹奈利',
  'en': 'Denali',
  'intro': '用一段巴士旅程讀懂內陸荒野，再用短步道和遊客中心，把遠方的山變成眼前的故事。',
  'sources': [('NPS｜Denali 旅遊規劃與巴士', 'https://www.nps.gov/dena/planyourvisit/index.htm'),
              ('NPS｜當前路況', 'https://www.nps.gov/dena/planyourvisit/conditions.htm'),
              ('Alaska Railroad｜Denali Star',
               'https://www.alaskarailroad.com/ride-a-train/route-map/denali-star')]},
 {'slug': 'katmai',
  'image': 'katmai',
  'name': '卡特邁',
  'en': 'Katmai',
  'intro': '看熊的重點不只是站上瀑布平台，而是讀懂河流、食物與季節，給動物足夠的空間。',
  'sources': [('NPS｜Brooks Camp 與安全說明', 'https://www.nps.gov/katm/planyourvisit/brooks-camp.htm'),
              ('NPS｜看熊與食物季節', 'https://www.nps.gov/katm/planyourvisit/bear-watching.htm')]},
 {'slug': 'wrangell-st-elias',
  'image': 'wrangell',
  'name': '蘭格—聖伊萊亞斯',
  'en': 'Wrangell–St. Elias',
  'intro': '從 Copper Center 的展覽與短步道開始，認識這片巨大荒野；若想進入 Kennecott，請另留一段旅程。',
  'sources': [('NPS｜Copper Center 遊客中心',
               'https://www.nps.gov/wrst/planyourvisit/wrangell-st-elias-visitor-center.htm'),
              ('NPS｜Wrangell–St. Elias', 'https://www.nps.gov/wrst/index.htm')]}]

def head(title,prefix=''):
 return f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#123439"><title>{esc(title)}｜公園隨行</title><meta name="description" content="國家公園中文導覽，從大峽谷與死亡谷到阿拉斯加，選公園、看行程與周邊景點。"><link rel="stylesheet" href="{prefix}style.css"><script defer src="{prefix}app.js"></script></head><body><a class="skip" href="#main">跳至內容</a><header><a class="brand" href="{prefix}index.html"><span class="seal">山</span><span>公園隨行<small>NATIONAL PARK FIELD GUIDE</small></span></a><div class="actions"><button id="font" aria-pressed="false">大字</button><button id="offline">離線下載</button></div></header><main id="main">'''

def foot(prefix=''):
 return f'''</main><footer><div><strong>公園隨行 · National Park Field Guide</strong><p>一趟串聯鐵路、冰川與荒野的夏季旅行。時間皆為阿拉斯加當地時間。<br>季節與停留安排是規劃參考；開放、接駁、天氣及活動以官方與業者當期公告為準。</p></div><a href="{prefix}index.html#days">返回逐日行程 ↑</a><p class="fine">核對：2026 年 10 月｜火車官網已公布 2027 夏季班表；公園活動參考目前公布季節資訊｜照片為景觀示意，不代表到訪時的景色。<br>網站以 AI 協助編寫，以旅遊規劃需求整理內容。</p><p id="offline-status" role="status" aria-live="polite"></p></footer></body></html>'''

def picture(p,prefix='',cls=''):
 return f'<img class="{cls}" src="{prefix}assets/{p["image"]}.jpg" alt="{esc(p["en"])} 國家公園景觀" loading="lazy" width="1200" height="750">'


from itinerary import render
if __name__=="__main__":
 render(parks,head,foot,picture,esc,ROOT,D)
 from hub import render_hub
 render_hub(parks,head,foot,esc,ROOT,D)

if __name__=="__main__":
 from rockies import render as render_rockies
 render_rockies(ROOT,D,head)
 from bilingual import render_bilingual
 render_bilingual(ROOT,D)
