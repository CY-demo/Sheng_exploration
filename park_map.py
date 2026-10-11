"""Geographic locator, native SVG; no third-party scripts or map requests."""
import json
from html import escape as e
from rockies import t,T
PARKS=[('grand-canyon',36.06,-112.14,'west','大峽谷','Grand Canyon',245,345),('death-valley',36.46,-116.87,'west','死亡谷','Death Valley',75,295),('yellowstone',44.6,-110.5,'west','黃石','Yellowstone',320,150),('grand-teton',43.75,-110.8,'west','大提頓','Grand Teton',320,200),('denali',63.1,-151,'alaska','丹奈利','Denali',105,465),('kenai-fjords',59.9,-149.8,'alaska','基奈峽灣','Kenai Fjords',270,625),('katmai',58.6,-155,'alaska','卡特邁','Katmai',70,610),('wrangell-st-elias',61.7,-142.9,'alaska','蘭格—聖伊萊亞斯','Wrangell–St. Elias',295,520)]
def projection(lon,lat,region):
 if region=='alaska':return 55+(lon+170)*10,455+(72-lat)*8
 if region=='hawaii':return 530+(lon+161)*20,530+(23-lat)*20
 return 55+(lon+125)*14,70+(50-lat)*13

def render_map(root):
 # The image is intentionally illustrative; exact geographic outline is separately available.
 points=[('yellowstone',290,142,375,116),('grand-teton',286,175,382,198),('death-valley',124,266,38,232),('grand-canyon',228,302,304,337),('denali',176,460,30,419),('kenai-fjords',206,510,282,536),('katmai',143,529,25,570),('wrangell-st-elias',228,480,301,478)]
 byslug={x[0]:x for x in PARKS}
 s='<section id="map"><p class="eyebrow">AN ILLUSTRATED PARK ATLAS</p><h2>'+t('沿著地圖，走進荒野','Follow the map into the wild')+'</h2><p>'+t('從峽谷到冰川，點選 8 座公園的標記開始閱讀。插畫呈現旅行氛圍，標記為概略位置；下方卡片也提供相同連結。','From canyons to glaciers, select one of eight park markers to begin. This illustrated atlas conveys the spirit of travel; markers are approximate. The cards below provide the same links.')+'</p><div class="map-scroll illustrated" tabindex="0" role="region" aria-label="'+t('美國公園插畫地圖，可橫向捲動','Illustrated United States park map, horizontally scrollable')+'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 627" role="group" aria-labelledby="map-title map-desc"><title id="map-title">'+t('美國國家公園插畫導覽','Illustrated guide to United States national parks')+'</title><desc id="map-desc">'+t('美西四座、阿拉斯加四座；下方卡片提供相同公園連結。','Four parks in the West and four in Alaska. The cards below provide the same park links.')+'</desc><image href="assets/us-illustrated-map.webp" x="0" y="0" width="940" height="627"></image>'
 for slug,x,y,lx,ly in points:
  _,lat,lon,reg,zh,en,_,_=byslug[slug];name=t(zh,en)
  s+=f'<a href="parks/{slug}/" class="map-park" data-region="{reg}" aria-label="{name}"><title>{name}</title><path class="leader" d="M{x},{y} L{lx},{ly-6}"></path><circle cx="{x}" cy="{y}" r="7"></circle><text x="{lx}" y="{ly}">{name}</text></a>'
 s+='</svg></div><p class="fine">'+t('AI 生成旅行插畫，非實景照片或導航地圖。阿拉斯加與夏威夷為不同比例的插圖；實際入口、道路與距離請查各公園官方地圖。','AI-generated travel illustration, not a photograph or navigation map. Alaska and Hawaii are inset at different scales. Consult official park maps for entrances, roads and distances.')+'</p></section>'
 return s

def filters():
 opts=[('all','全部 8 座','All 8 parks'),('west','美西 · 4','West · 4'),('east','美東 · 0','East · 0'),('midwest','中西部 · 0','Midwest · 0'),('south','美南 · 0','South · 0'),('alaska','阿拉斯加 · 4','Alaska · 4'),('hawaii','夏威夷 · 0','Hawaii · 0')]
 return '<div class="filter-bar" role="group" aria-label="依地區篩選">'+''.join(f'<button data-filter="{k}" aria-pressed="{str(k=="all").lower()}">{t(z,en)}</button>' for k,z,en in opts)+'</div><p id="region-empty" class="schedule-note" hidden role="status">'+t('此地區尚無旅行導覽，請選擇其他地區或查看全部公園。','No travel guides are available for this region yet. Choose another region or view all parks.')+'</p>'

def entries():
 return [dict(slug=slug,name=t(z,en),en=en,image='yellowstone/'+img,region='west',desc=t(zh,eng),route='routes/yellowstone-grand-teton/',route_label=t('黃石・大提頓四日路線','Yellowstone & Grand Teton four-day route'),near='parks/'+other+'/',near_label=t(oz,oe)) for slug,z,en,img,zh,eng,other,oz,oe in [
 ('yellowstone','黃石','Yellowstone','grand-prismatic','熱泉、峽谷、清晨觀獸與遊客中心，分區安排短走。','Thermal basins, canyons, morning wildlife and visitor centers, with short walks by area.','grand-teton','串遊大提頓','Continue to Grand Teton'),
 ('grand-teton','大提頓','Grand Teton','jenny-lake','斷層山脈、冰川湖泊與蛇河，從北部湖區到歷史穀倉。','Fault-block mountains, glacial lakes and the Snake River, from northern lakeshores to historic barns.','yellowstone','串遊黃石','Continue to Yellowstone')]]
