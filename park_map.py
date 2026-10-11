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
 polys=json.loads((root/'us-outline.geojson').read_text())['features'][0]['geometry']['coordinates']
 s='<section id="map"><p class="eyebrow">EXPLORE THE UNITED STATES</p><h2>'+t('從地圖選公園','Choose a park on the map')+'</h2><p>'+t('標出本站已有導覽的 8 座公園。點擊標記進入景點介紹，或用下方地區分類選擇。','Explore the eight parks with guides on this site. Select a map marker for a park guide, or browse the regional categories below.')+'</p><div class="map-scroll" tabindex="0" role="region" aria-label="'+t('美國公園地圖，可橫向捲動','United States park map, horizontally scrollable')+'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 680" role="img" aria-labelledby="map-title map-desc"><title id="map-title">'+t('美國國家公園位置圖','United States national park locator')+'</title><desc id="map-desc">'+t('美西四座、阿拉斯加四座；下方卡片提供相同公園連結。','Four parks in the West and four in Alaska. The cards below provide the same park links.')+'</desc>'
 for poly in polys:
  ring=poly[0];lon,lat=ring[0];region='alaska' if lat>50 else 'hawaii' if lon<-140 else 'west'
  if region=='alaska' and lon>0:continue
  pts=[projection(x,y,region) for x,y in ring if not(region=='alaska' and x>0)]
  if pts:s+='<path class="land" d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+' Z"></path>'
 for x,y,zh,en in [(195,115,'美西','West'),(520,190,'中西部','Midwest'),(780,220,'美東','East'),(580,345,'美南','South'),(55,435,'阿拉斯加','Alaska'),(530,510,'夏威夷','Hawaii')]:s+=f'<text class="map-region" x="{x}" y="{y}">{t(zh,en)}</text>'
 for slug,lat,lon,reg,zh,en,lx,ly in PARKS:
  x,y=projection(lon,lat,reg);name=t(zh,en)
  s+=f'<a href="parks/{slug}/" class="map-park" data-region="{reg}" aria-label="{name}"><title>{name}</title><path class="leader" d="M{x:.1f},{y:.1f} L{lx},{ly-6}"></path><circle cx="{x:.1f}" cy="{y:.1f}" r="7"></circle><text x="{lx}" y="{ly}">{name}</text></a>'
 s+='</svg></div><p class="fine">'+t('位置為公園概略定位，不是入口或行車導航。阿拉斯加與夏威夷採獨立比例；地區分類用於本站瀏覽。','Markers locate parks approximately, not entrances or driving routes. Alaska and Hawaii use separate scales. Regions are browsing categories for this site.')+' <a href="https://github.com/johan/world.geo.json/blob/master/countries/USA.geo.json">Map outline · world.geo.json</a></p></section>'
 return s

def filters():
 opts=[('all','全部 8 座','All 8 parks'),('west','美西 · 4','West · 4'),('east','美東 · 0','East · 0'),('midwest','中西部 · 0','Midwest · 0'),('south','美南 · 0','South · 0'),('alaska','阿拉斯加 · 4','Alaska · 4'),('hawaii','夏威夷 · 0','Hawaii · 0')]
 return '<div class="filter-bar" role="group" aria-label="依地區篩選">'+''.join(f'<button data-filter="{k}" aria-pressed="{str(k=="all").lower()}">{t(z,en)}</button>' for k,z,en in opts)+'</div><p id="region-empty" class="schedule-note" hidden role="status">'+t('此地區尚無旅行導覽，請選擇其他地區或查看全部公園。','No travel guides are available for this region yet. Choose another region or view all parks.')+'</p>'

def entries():
 return [dict(slug=slug,name=t(z,en),en=en,image='yellowstone/'+img,region='west',desc=t(zh,eng),route='routes/yellowstone-grand-teton/',route_label=t('黃石・大提頓四日路線','Yellowstone & Grand Teton four-day route'),near='parks/'+other+'/',near_label=t(oz,oe)) for slug,z,en,img,zh,eng,other,oz,oe in [
 ('yellowstone','黃石','Yellowstone','grand-prismatic','熱泉、峽谷、清晨觀獸與遊客中心，分區安排短走。','Thermal basins, canyons, morning wildlife and visitor centers, with short walks by area.','grand-teton','串遊大提頓','Continue to Grand Teton'),
 ('grand-teton','大提頓','Grand Teton','jenny-lake','斷層山脈、冰川湖泊與蛇河，從北部湖區到歷史穀倉。','Fault-block mountains, glacial lakes and the Snake River, from northern lakeshores to historic barns.','yellowstone','串遊黃石','Continue to Yellowstone')]]
