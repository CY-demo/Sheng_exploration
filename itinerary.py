import json

# Public example schedule: times are not a private booking record.
DAYS=[
{'n':1,'title':'Anchorage 抵達與補給','page':'days/anchorage/','sleep':'Anchorage','summary':'午後抵達示範 → 入住 → 準備隔日隨身物品 → 早休息','intro':'抵達日只負責把隔天的火車行程準備好。此頁以午後抵達為例；若晚班機才到，就直接入住，不必補跑市區。','rows':[
('14:00–15:30','建議','抵達、領行李與前往住宿','這是抵達日時間配置示範，不是指定航班。選擇能安排隔天清晨交通的 Anchorage 住宿。',''),
('15:30–16:30','建議','入住、確認去車站的方式','隔天 05:45 要到 Anchorage Depot。若火車與住宿一起訂，今天核對套裝安排的清晨飯店接送時間與候車位置；其他旅客則向住宿確認火車站接駁或提前預約車輛。',''),
('16:30–17:30','建議','補給：水、早餐、點心','Kenai Fjords Tours 的鐵路搭配產品列有午餐，但仍應依所訂產品確認。準備保暖防水外套、暈船用品與相機，留下大行李，只帶當日用品。',''),
('17:30–19:00','建議','晚餐，整理車票與船票','核對列車、船公司、接駁點、報到要求與延誤處理。把票券下載到手機；隔天很早出門，今晚不安排晚結束的表演。',''),
('20:00 起','建議','休息','明天是 06:45 出發、22:15 回到 Anchorage 的長日行程。','')], 'notes':[]},
{'n':2,'title':'Kenai Fjords｜火車＋冰川遊船','page':'parks/kenai-fjords/','sleep':'Anchorage','summary':'05:45 報到 → 06:45 火車 → 11:20 Seward → 遊船 → 18:00 火車 → 22:15 Anchorage','intro':'一天串聯 Coastal Classic 景觀鐵路與海上冰川。本表採 12:00 出航、約 17:30 回港的 5.5 小時船班；訂票時選擇能配合鐵路的產品，並確認專用接駁與報到安排。','rows':[
('05:45','建議','Anchorage Depot 報到','預留一小時換票、身分核驗與登車準備。住宿到車站的車程另計；不要到 06:45 才抵達車站。','rail'),
('06:45–11:20','班表','Coastal Classic：Anchorage → Seward','沿 Turnagain Arm 與 Kenai 半島山谷南下。早餐可先吃或按所選車廂的餐飲安排；不要在途中下車拍照而錯過列車。','coastal'),
('11:20–12:00','銜接','下車後直接搭船公司接駁','11:20 抵達 Seward 後，直接搭預約好的船公司接駁，完成報到、上廁所與登船。約四十分鐘包含所有轉乘程序；訂船時註明搭火車抵達。曾在這段空檔快訪港區遊客中心，來回約十分鐘，但很趕；先確認報到與登船截止時間，有餘裕才去。','transfer'),
('12:00–17:30','所選船班','Kenai Fjords 國家公園冰川遊船','以船上觀景、冰川與海洋動物為主，途中用餐。航線與冰川停留順序由船長依當日情況安排，不能替每個海上景點設定固定時刻。','cruise'),
('17:30–18:00','銜接','靠港後直接搭接駁回車站','依船公司安排回 Alaska Railroad Depot，立即辦理返程登車。沒有額外逛街或吃晚餐的空檔；須事先確認此銜接符合你的鐵路報到安排。','return'),
('18:00–22:15','班表','Coastal Classic：Seward → Anchorage','晚餐可依車廂方案在車上安排。22:15 是列車抵站時間，回到住宿通常還需領行李與市區交通時間。','rail'),
('約 22:30–23:00','估時','回住宿休息','隔天仍要早起搭北上列車。若不想連續兩天早起，應在 Anchorage 加一個休息日，後續日期整體順延。','')],
 'notes':[
('5.5 小時鐵路套裝怎麼選？','本表使用 12:00 船班。Alaska Railroad 列有可銜接鐵路的 5.5 小時產品；其他船班可能 11:30 出發，不能混用報到時間。購買時確認出航、靠港及車站接駁三項。'),
('想蓋章，當天能去遊客中心嗎？','親身經驗：曾在轉船空檔到港區遊客中心，來回約十分鐘，但非常趕，沒有時間仔細看展。先向船公司確認報到及登船截止時間，並核對遊客中心是否開門；有人排隊、列車誤點或報到延誤就應放棄，不以十分鐘作保證。若想從容參觀，可以 Day 2 留宿 Seward，Day 3 上午參觀遊客中心、另安排 Exit Glacier，18:00 搭火車回 Anchorage；Denali 段順延一天，整趟至少十天。'),
('列車遲到怎麼辦？','船公司表示可能改提供其他尚有空位的航程；不是保證等候，也不保證替代航程仍會看到潮水冰川。要照這份行程走，先確認延誤與改團條件。')]},
{'n':3,'title':'Denali｜景觀火車＋冰川飛行','page':'parks/denali/','sleep':'Denali 園區入口周邊','summary':'07:20 報到 → 08:20 火車 → 15:40 抵達 → 入住 → 約 18:00 Fly Denali 冰川飛行','intro':'上午搭景觀鐵路北上，下午入住，傍晚搭 Fly Denali 小飛機看 Ruth Glacier。親自體驗，非常推薦！住宿應選能安排車站接駁的地點，並提前確認飛行業者的接送與報到時間。','rows':[
('06:30–07:00','建議','早餐、退房','提前安排住宿到 Anchorage Depot 的交通。回程仍住 Anchorage 的旅客，可詢問是否能寄放部分行李；不要假定飯店一定提供。',''),
('07:20','建議','Anchorage Depot 報到','比 08:20 發車提前一小時。預订 Anchorage → Denali，不是直接訂到 Fairbanks。','rail'),
('08:20–15:40','班表','Denali Star：Anchorage → Denali','午餐在車上依票種安排。火車經 Talkeetna 一帶往內陸，沿途山谷與河川是今天的主要景觀。','denali-rail'),
('15:40–16:30','估時','下車、領行李、住宿接駁','火車與住宿一起訂時，依套裝安排搭飯店接送。車站到飯店的時間依住宿不同；事先確認候車位置、行李處理與是否需預約。',''),
('16:30–17:00','建議','入住、核對隔天巴士接送','Tundra Wilderness Tour 應已提前訂好，出發前 48 小時可查實際時刻；今天再次確認集合時間和地點。只有獲配早班，才能照 Day 4 的下午犬舍＋河谷安排走。','bus'),
('17:00–17:30','建議','先吃簡餐，準備飛行衣物','準備保暖外套與相機。先吃點東西，飛行結束後再安排晚餐；若業者要求更早接送，應縮短入住整理時間。',''),
('約 17:30 起','估時','接送至 Fly Denali、報到與安全說明','接送時間需事先由業者確認，本表只是預留安排。出發基地為 Healy River Airport；請確認住宿是否在接送範圍、幾點候車及行李限制。',''),
('約 18:00–20:15','預約活動','Fly Denali｜Ruth Glacier 冰川飛行','親自體驗，非常推薦。傍晚約六點搭小飛機，從空中欣賞山峰、冰流與冰川谷地。官網目前 2027 傍晚班列為 18:15，冰川著陸產品約 100 分鐘飛行＋20 分鐘冰上停留；實際時間、航線及是否著陸以所訂產品與當天天氣為準。','flight'),
('約 20:15–21:00','估時','返抵基地、接送回住宿','本表依傍晚班及約兩小時活動預留回程；不是保證回飯店時間。提早確認晚餐最晚供餐時間，也可預備餐食。',''),
('約 21:00 起','建議','晚餐與休息','隔天巴士可能很早出發，今晚先整理好水、點心與保暖衣物。','')],
 'notes':[('預訂與火車銜接','Fly Denali 需提前預訂，提供火車約 15:40 抵達及住宿資訊，確認晚間班可銜接。不要假設飛行含在所有阿拉斯加鐵路套裝中；是否加購、接送及遇火車誤點的處理方式都先確認。'),('天候調整','飛行和冰川著陸受天候影響，安全由飛行員判斷。若取消，依業者政策處理改期或退款；隔天已有 Tundra Wilderness Tour，不能直接把飛行塞入未確認的空檔。')]},
{'n':4,'title':'Denali｜巴士、雪橇犬與 Savage River','page':'parks/denali/','sleep':'Denali 園區入口周邊','summary':'早班巴士 → 14:00 雪橇犬 → 河谷短走（視接駁）→ 晚間 Cabin Nite 晚餐劇場','intro':'這是一個完整公園日。以下以約 06:00 出發的 Tundra Wilderness Tour 示範；營運季每天有團，必須提前報名訂位；出發前 48 小時才公布／確認實際集合時刻，不是前兩天才開始報名。訂位時先保留整天；收到時間後，再調整犬舍與河谷活動。','rows':[
('05:15–05:45','建議','早餐、到指定集合點','按票券指示提早候車，攜帶水與點心。上車位置可能是飯店或指定站點，不能自行改到其他站等車。',''),
('約 06:00–11:30','示範','Tundra Wilderness Tour','NPS 列的行程長度約 5–5.5 小時；主表預留 5.5 小時，飯店接送可能另加時間。這不是可隨意中途下車再搭下一班的 transit bus。','bus'),
('11:30–12:15','估時','返回入口區，移動到遊客中心','預留接駁／步行時間；若實際回程晚於 12:30，請啟用下方替代方案。',''),
('12:15–13:00','建議','午餐、廁所與簡短看展','先吃飯，遊客中心完整參觀及蓋章安排在 Day 5，避免為了看展錯過犬舍接駁。','center'),
('13:10 候車；13:20 出發','季節班表','DVC → 雪橇犬舍','到 Denali Visitor Center 的 Sled Dog Demonstration Shuttle 站等車；公布夏季表列約 13:40 抵達。','dogs'),
('14:00–14:30','季節活動','Sled Dog Demonstration','認識雪橇犬與公園巡護工作。示範約半小時；是否能接觸犬隻，依 ranger 現場指示。','dogs'),
('14:40–15:00','季節班表','犬舍接駁回 DVC','官方夏季範例表列 14:40 離犬舍、約 15:00 回遊客中心。先核對 Savage River 的下一班與回程班次。',''),
('約 15:30–16:30','估時','搭 Savage River Shuttle 進河谷','保守預留一小時單程與沿途停靠；實際發車分鐘以當季站牌為準，不把它寫成固定 15:30 班次。','savage'),
('約 16:30–17:15','建議','Savage River 短走','安排 30–45 分鐘近河谷散步，按體力折返；本表不安排完整長步道或 Savage Alpine。','savage'),
('約 17:15–18:30','估時','候車與返回公園入口','回程留出等車時間，事先確認飯店最後接駁；不能只看公園巴士仍營運就假設回得了飯店。',''),
('約 18:30–19:15','估時','前往 Denali Park Village、劇場報到','提前確認從住宿接駁或自行前往的方式。若票券的接送時間早於河谷回程，應取消 Savage River，犬舍結束後直接回住宿休息與等車，不要錯過劇場接送。',''),
('晚間七點多；參考 19:45','預約活動','Alaska Cabin Nite Dinner Theatre｜晚餐＋表演','親自參加，覺得很有趣！在 Denali Park Village 的木屋劇場用餐、欣賞歌唱與互動演出。2026 夏季主要營運時段的晚場為 19:45，其他年度及季初末可能不同；請提前預訂並依票券報到。晚餐包含在此活動中，不另排同時段餐廳。','cabin'),
('散場後','依場次','依約定接駁回住宿','訂票時一併確認散場及返程接送時間；這裡不把未確認的散場時刻寫成固定班表。隔天早上遊客中心、12:30 南下火車，今晚整理好行李再休息。','')],
 'notes':[('訂位順序：先報名，再等出發時刻','規劃旅程時先訂 Tundra Wilderness Tour 並確認日期、接送地點與訂位條件；把這一天保留給公園。出發前 48 小時查集合時刻，再決定犬舍與 Savage River 的先後或刪減，不要先訂不可調整的下午活動。'),('若 Tundra Wilderness Tour 不是早班','若約 08:00 才出發，可能到 13:30 才結束，不能再趕 13:20 接駁。可改當季有開的 16:00 犬舍示範，並取消下午 Savage River；若巴士更晚，就把犬舍排到其他完整一天。'),('跨年度使用','犬舍接駁的精確分鐘取自 NPS 公布的 2026 夏季表；2027 或其他季節須重新核對。若班表不同，保持「示範前約 40 分鐘搭車」的銜接原則。')]},
{'n':5,'title':'Denali｜遊客中心與南下火車','page':'parks/denali/','sleep':'Anchorage','summary':'09:00 遊客中心 → 11:30 車站 → 12:30 Denali Star → 20:00 Anchorage','intro':'早上留給遊客中心與蓋章，不再搭車深入園區。中午南下回 Anchorage，為隔天小飛機準備。','rows':[
('08:00–09:00','建議','早餐、退房與寄存行李','和飯店確認行李要自己帶到車站，或有明確約定的運送服務。先把行李處理好，再去遊客中心。',''),
('09:00–10:30','建議','Denali Visitor Center 看展、蓋章','依當季開門時間調整。Junior Ranger 手冊與審核先詢問 ranger；不要等火車快開才開始辦理。','center'),
('10:30–11:15','建議','入口周邊短走、取行李','只選能準時回到車站的附近步道。準備車上午餐或確認餐車服務。',''),
('11:30','建議','Denali Depot 報到','主表保留一小時報到餘裕。車票目的地選 Anchorage；若需取回飯店寄送行李，今天事先確認交接流程。','rail'),
('12:30–20:00','班表','Denali Star：Denali → Anchorage','車上觀景、午餐與晚餐依票種安排。火車抵達時間不等於抵達市區飯店時間。','denali-rail'),
('約 20:15–21:00','估時','回住宿，確認 Katmai 集合資訊','小飛機可能從不同機場或業者基地出發，依確認信安排接送；不要一律導航到 Anchorage 主航廈。','')], 'notes':[]},
{'n':6,'title':'Katmai｜Brooks Camp 看熊一日','page':'parks/katmai/','sleep':'Anchorage','summary':'約 07:00–08:00 出發 → 轉乘進 Brooks Camp → 地面看熊 → 約 18:30–19:00 回 Anchorage','intro':'以 Katmai Air 的 Anchorage 當日往返產品作交通例子。業者公布出發與回城時間範圍，Brooks Camp 的實際抵離時間仍須以配班為準；以下園內時段是示範分配。','rows':[
('約 06:00–07:00','示範','指定基地集合、報到','依最終通知倒推早餐與住宿接送；確認集合基地地址，不要直接前往主航廈。','arrival'),
('07:00–08:00 間','業者範圍','Anchorage 起飛，經 King Salmon 銜接','此產品包含到 Brooks 的往返航空交通；轉機與水上飛機安排由業者確認，兩段之間不要自行安排其他活動。','arrival'),
('約 10:00–10:45','示範','抵達 Brooks Camp、熊安全說明','實際抵達可能較早或較晚。先完成必須的安全說明、存放食物與有氣味物品，再開始活動。','arrival'),
('約 10:45–11:30','示範','Lower River 看熊況','先問 ranger 當天熊在哪裡、平台是否排隊。看熊路線可調整，但不要追著熊移動。','route'),
('約 11:30–12:15','示範','指定區域吃午餐、上廁所','帶簡單食物可節省用餐時間；只在允許進食的位置吃，食物不要帶著邊走邊吃。',''),
('約 12:15–15:00','示範','Brooks Falls Trail、Riffles、瀑布平台','把這一整段留給步行與看熊，平台候位和熊阻擋通行都算在內。不保證每處都能停留相同時間。','route'),
('約 15:00–16:00','示範','回 Lower River、取物、返回集合區','以業者指定的離營集合時間往前抓至少一小時緩衝；若班機更早，必須縮短前段看熊，不是照表走到最後。','backup'),
('約 16:00–18:30','示範','離開 Brooks Camp、轉乘回 Anchorage','離營與轉機時間未固定，依當日配班。請保持集合訊息可取得，勿依網站示範時間自行晚到。',''),
('18:30–19:00 間','業者範圍','抵達 Anchorage','Katmai Air 公布的回城時間範圍。今天留在 Anchorage 吃晚餐與休息，不再接四、五小時的 Copper Center 長途駕駛。','')],
 'notes':[('若天候取消','Day 7 原本保留作緩衝。若能改到 Day 7 看熊，當晚仍住 Anchorage；Copper Center 段順延一天，或刪去，不能把原本 Day 7 下午的自駕硬接在晚間回城後。'),('如果你訂的是其他業者','不要沿用這張飛行時間表。用你訂到的起飛、離營集合與回城時間替換交通列，再按比例縮短或拉長園內看熊。')]},
{'n':7,'title':'Anchorage 緩衝與 Copper Center 移動','page':'days/anchorage/','sleep':'正常版：Copper Center；看熊補飛版：Anchorage','summary':'上午彈性市區 → 12:30 取車 → 13:00 自駕 → 約 18:00 Copper Center','intro':'先確認 Day 6 看熊已完成，再執行下午的公路段。這一天只安排半天市區，不把所有博物館與景點塞滿。','rows':[
('09:00–10:30','建議','Alaska Public Lands Information Center','開門日可認識阿拉斯加公共土地與詢問蓋章；若休館，改成早餐與市區散步，不另繞遠路。','anchorage-center'),
('10:30–11:30','建議','Ship Creek 市區短走','沿河岸散步，觀察城市與鮭魚河流的連結；看鮭魚受季節影響。若前一天疲累，可把這一小時改為休息。','ship-creek'),
('11:30–12:30','建議','午餐、領行李','確認租車取車點。若租車在機場，要另留市區到機場的時間，下午開車時間可順延。',''),
('12:30–13:00','建議','取車、補給與加油','確認可行駛道路與保險，準備水、點心及離線地圖。',''),
('13:00–18:00','估時','Anchorage → Glenn Highway → Copper Center','預留約五小時給駕駛和途中休息，視路況調整。今天不另外排 Matanuska 冰川導覽；那需要獨立預約與額外時段。','road'),
('18:00–19:30','建議','入住 Copper Center、晚餐','目的只是把住宿移到隔天遊客中心附近。提前確認用餐選項與最晚供餐時間。','')],
 'notes':[('Day 7 改作 Katmai 補飛時','整天使用 Katmai 分頁的示範時間表，取消今天租車與開往 Copper Center 的安排。若一定要保留 Wrangell–St. Elias，就在原九天之外加一天；不能仍保證 Day 9 返程不受影響。')]},
{'n':8,'title':'Wrangell–St. Elias＋Matanuska 冰川觀景','page':'parks/wrangell-st-elias/','sleep':'Anchorage','summary':'09:00 遊客中心 → Ahtna 文化中心 → 13:00 出發 → Matanuska 短步道 → 約 19:00 Anchorage','intro':'這一天是遊客中心與短步道入門版，不包含 McCarthy、Kennecott 或 Root Glacier。從 Copper Center 出發，上午看展與散步；下午沿 Glenn Highway 回城，可在 Matanuska Glacier State Recreation Site 短走、遠眺冰川。','rows':[
('08:00–09:00','建議','早餐、退房，前往遊客中心','附近住宿到園區的時間依位置而異。先核對當季開門時間；若晚於 09:00，往後平移上午活動。',''),
('09:00–10:30','建議','Wrangell–St. Elias Visitor Center','看地圖、影片與展覽，詢問蓋章、Junior Ranger 及短步道路況。','center'),
('10:30–11:15','建議','Ahtna Cultural Center','若有開放，認識當地原住民族與河流生活；若休館，把時間留給遊客中心展覽，不將此站寫成保證可入內。','culture'),
('11:15–12:00','建議','遊客中心周邊短步道','依現場可開放路線，安排約 30–45 分鐘散步。這不是走上冰川的行程。','landscape'),
('12:00–13:00','建議','午餐與返程準備','可事先準備野餐，使用允許的用餐區；出發前上廁所、確認油量。',''),
('13:00–15:30','估時','Copper Center → Matanuska 觀景休憩區','沿 Glenn Highway 西行，預留約 2.5 小時含短休息。目的地為 Mile 101 的 Matanuska Glacier State Recreation Site，不是冰川導覽集合點。','road'),
('約 15:30–16:30','建議停留','Matanuska Glacier State Recreation Site｜健行、遠眺冰川','親自走過，當時還看到野生駝鹿（moose）！從休憩區走 Edge Nature Trail，穿過森林前往冰川觀景平台。官方介紹步行約 20 分鐘，本表留一小時給散步、觀景、拍照與休息。這裡可以看冰川，但沒有通往冰川表面的步道。','matanuska'),
('16:30–19:00','估時','沿 Glenn Highway 返回 Anchorage','預留約 2.5 小時含短休息；道路施工或天候可能延後抵達。若不加觀景步道，可直接回城，較早入住休息。',''),
('約 19:00–20:30','建議','入住 Anchorage、晚餐','翌日再還車和搭機，不把當天長途駕駛與必須準時起飛的返程航班硬接在一起。','')], 'notes':[('兩種看 Matanuska 冰川的選擇','本表的州立休憩區適合森林短走、隔著谷地看冰川，不需要把數小時的冰川導覽塞進返程。若想實際踏上冰川，須另訂合適導覽、確認交通入口與裝備，並重排當日時間；不能沿這條觀景步道走上冰川。'),('駝鹿是旅途中的偶遇','曾在此遇到野生駝鹿，但不保證每次到訪都看得到。保持距離，讓動物保有移動空間；若牠擋住步道，先停下或退開，不為拍照靠近。'),('想深入公園怎麼加？','McCarthy／Kennecott 與冰川活動應獨立規劃交通、住宿與導覽。本日只完成 Copper Center 入口體驗，沒有涵蓋那些地點。')]},
{'n':9,'title':'Anchorage 整理與返程','page':'days/anchorage/','sleep':'—','summary':'早餐 → 收行李 → 還車 → 依班機時間到機場','intro':'依你訂到的返程班機，倒推還車、報到與出門時間；早班機應省略市區活動。','rows':[
('上午','建議','早餐、收行李與退房','依住宿退房時間安排，先確認所有票券、證件與租車物品。',''),
('起飛前約 4 小時','建議','加油、出發還車','把住宿到加油站、租車場與航廈移動都算進去；地點不同需調整。',''),
('起飛前約 2–3 小時','建議','到航廈報到、托運及安檢','這是規劃緩衝，不取代航空公司針對你的航班與目的地所訂的報到要求。','')], 'notes':[]}
]

from experience_days import apply
apply(DAYS)

SOURCES=[('Alaska State Parks｜Matanuska 觀景與 Edge Nature Trail','https://dnr.alaska.gov/parks/aspunits/matsu/matsuglsrs.htm'),('Cabin Nite｜場次、訂位、餐飲與接駁','https://www.denaliparkvillage.com/things-to-do/alaska-cabin-nite-dinner-theatre/'),('Fly Denali｜冰川飛行、時長與班次','https://www.flydenali.com/glacier-landing'),('Fly Denali｜接送與天候問題','https://www.flydenali.com/faqs'),('Reserve Denali｜出發前 48 小時查詢時刻','https://www.reservedenali.com/tours-transits/the-denali-tour-experience/tour-information/'),('Alaska Railroad｜列車班表（目前為 2027 夏季）','https://www.alaskarailroad.com/ride-a-train/schedules'),('Alaska Railroad｜報到規定','https://www.alaskarailroad.com/ride-a-train/terms-and-conditions'),('Kenai Fjords Tours｜鐵路接駁與船班 FAQ','https://www.alaskacollection.com/day-tours/kenai-fjords-tours/faqs/'),('Alaska Railroad｜5.5 小時遊船產品','https://www.alaskarailroad.com/travel-planning/day-trips/kenai-fjords-national-park-cruise'),('NPS｜Denali 巴士時長與預約','https://www.nps.gov/dena/planyourvisit/bus-tours.htm'),('NPS｜Denali 免費接駁班表','https://www.nps.gov/dena/planyourvisit/courtesy-shuttle-buses.htm'),('Katmai Air｜Brooks Falls 當日往返','https://katmaiair.com/bear-viewing/brooks-falls-day-tours/')]

def render(parks,head,foot,picture,esc,ROOT,D):
 credits=json.loads((D/'assets/credits.json').read_text())
 # All visitor-facing copy is direct guidance, not commentary about source notes.
 details={
 'matanuska':('Matanuska｜在森林與谷地之間讀懂冰川','從高處觀景平台，可以把遠方冰川、前方谷地與兩側山坡放進同一個畫面。這是看冰川整體尺度的方式；近距離冰上導覽則觀察冰面與裂隙，兩者視角不同。Edge Nature Trail 穿過森林通往觀景位置，適合當作公路旅行中的步行休息站。'),
 'cabin':('Cabin Nite｜阿拉斯加木屋晚餐劇場','表演在 Denali Park Village 的 Miners Plaza 木屋劇場進行，以輕鬆歌唱、故事與觀眾互動呈現昔日阿拉斯加氛圍。餐點採家庭分享式供餐；飲食需求提前告知。活動需預訂，接送只涵蓋業者列出的部分住宿，不代表所有飯店都有接駁。'),
 'flight':('Ruth Glacier｜從空中看冰川與山壁','冰川沿山谷緩慢流動，從空中能看清冰流、裂隙與兩側高聳山壁的關係。Fly Denali 的冰川著陸產品前往 Ruth Glacier 一帶；若當天可著陸，依飛行員指示在允許範圍活動。這裡是 Denali 的 Ruth Glacier，與 Wrangell–St. Elias 的 Root Glacier 不同。'),
 'coastal':('窗外看什麼','沿 Turnagain Arm 海岸轉入 Kenai 半島山谷，看潮汐水域、山壁、河川與冰川地形。這段不是只為了抵達碼頭，火車本身就是今天的第一個景點。'),
 'cruise':('Kenai Fjords｜景點介紹','Harding Icefield 的冰川向海岸流動，冰長時間磨蝕山谷；冰退去後海水進入，形成峽灣。看船外時，留意冰川、裸岩、山壁與海水的位置。海洋動物和崩冰都不是定時表演，實際停靠由船長決定。'),
 'denali-rail':('Denali Star｜景點介紹','從海岸城市進入內陸，鐵路帶你看河川、森林與山谷。若天氣晴朗，可留意遠方山峰；山景是否露出不保證，選座也不能取代好天氣。'),
 'bus':('Denali｜沿著 Park Road 讀懂荒野','有解說的觀景巴士適合以坐車為主的旅客。留意森林與低矮苔原交界、河谷和動物活動。它與可中途下車健行的 transit bus 是不同產品；實際開放終點需核對 NPS 當季公告。'),
 'dogs':('雪橇犬｜不是單純的動物表演','解說會把犬隻與公園巡護工作連在一起。跟著 ranger 認識犬舍與工作方式；任何主題徽章或紀念品都依現場活動，不列為行程保證。'),
 'savage':('Savage River｜怎麼簡單走','把河流與開闊谷地當主角，短走後原路折返即可。Savage Alpine 是不同的較費力路線，不要看到名稱相似就臨時改走。留意熊與其他動物，並預先看回程站牌。'),
 'arrival':('Brooks Camp｜先了解規則再看熊','這裡沒有從 Anchorage 直接開車可到的公路。進營地後先接受熊安全說明，再依指示存放食物。熊與人共用這片環境，通行有時必須等待。'),
 'route':('Brooks River｜看熊要看食物與水域','熊會跟著鮭魚與食物位置移動，Lower River、Riffles 和 Brooks Falls 都值得按現場熊況分配時間。經典瀑布畫面不代表每天都能看到許多熊同時抓魚。'),
 'backup':('回程緩衝為什麼重要','熊活動可能暫時阻擋路線。提前回到集合區比多拍幾張照片重要；航空接駁還要配合轉機，不能只看自己的步行速度。'),
 'road':('公路沿線｜另一個阿拉斯加視角','Glenn Highway 串起山谷與內陸地景，與鐵路的視角不同。只在允許停車且安全的觀景位置停留；網站預留的車程含短休息，不含冰川導覽。'),
 'culture':('Ahtna Cultural Center｜理解這片土地上的生活','展覽補上原住民族的文化與河流生活，讓山川不只是空曠的風景。此中心與 NPS 遊客中心的開門安排可能不同。'),
 'landscape':('Wrangell–St. Elias｜從入口看尺度','公園範圍廣闊，山地、冰川與河流分布在不同區域。Copper Center 的影片、地圖與步道提供入門視角，不能等同到過 Kennecott 或 Root Glacier。')}
 spot_manifest=json.loads((D/'assets/spots/manifest.json').read_text())
 def stop_photo(key,park,title):
  if key=='center' and park and park['slug']=='kenai-fjords':return ''
  mapped={'center':('denali-center' if park and park['slug']=='denali' else 'wrangell-center'),'route':'brooks-falls','arrival':'brooks-river','backup':'brooks-river','landscape':'wrangell-center'}.get(key,key)
  if key=='cruise':
   return f'<figure class="stop-photo">{picture(parks[0],"../../")}<figcaption>海上冰川與峽灣景觀 · {esc(credits["kenai"]["credit"])}</figcaption></figure>'
  if key=='bus':
   return f'<figure class="stop-photo">{picture(parks[1],"../../")}<figcaption>Denali 景觀示意；當日能見度與巴士路線依現場安排 · {esc(credits["denali"]["credit"])}</figcaption></figure>'
  if mapped not in spot_manifest:return ''
  m=spot_manifest[mapped]
  license_link=f' · <a href="{esc(m["license_url"])}">{esc(m.get("license","授權"))}</a>' if m.get('license_url') else ''
  return f'<figure class="stop-photo"><img src="../../assets/spots/{esc(m["file"])}" alt="{esc(m["alt"])}" width="1200" height="800" loading="lazy"><figcaption>{esc(m["alt"])} · {esc(m["credit"])} · <a href="{esc(m["source"])}" target="_blank" rel="noopener">照片來源</a>{license_link}</figcaption></figure>'
 def chapter_details(key,park):
  if key=='center':
   text=('遊客中心｜看展、蓋章與 Junior Ranger','先詢問當天服務與手冊要求，再分配展覽和短步道。蓋章與徽章不是同一項活動；審核需要 ranger 與足夠時間。')
  elif key in details:text=details[key]
  elif key=='anchorage-center':text=('Alaska Public Lands Information Center｜旅行的起點','用地圖與展覽先分清阿拉斯加各片公共土地的位置，再詢問 ranger 哪些區域適合當季拜訪。它是市區資訊中心，不代表抵達任一遠方國家公園。')
  elif key=='ship-creek':text=('Ship Creek｜城市裡的鮭魚河流','從河岸觀察潮水、溪流和城市如何相接。鮭魚回游時，水下活動會讓這段市區散步多一層生態故事；不同季節看到的景象不同。')
  else:return ''
  extra={
   'coastal':'觀察重點：海灣的潮汐水域、山壁與內陸谷地的切換。留意窗外景色，列車只是經過，不表示各地都能下車遊覽。',
   'cruise':'現場看什麼：先找冰川與海水交界，再看兩側裸岩和植被。浮冰、海鳥與海洋哺乳動物可能出現，但崩冰與動物不是固定節目。甲板風冷，觀景後可回船艙休息。',
   'bus':'現場看什麼：先看森林轉為低矮苔原的位置，再找河谷與山坡上的動物。山峰可能被雲遮住，動物也可能很遠，準備望遠鏡比期待近距離更實際。巴士停車與下車依司機指示。',
   'dogs':'參觀方式：跟著 ranger 理解雪橇犬如何協助冬季巡護。拍照時先看工作人員指示，不自行餵食或靠近未開放接觸的犬隻。',
   'savage':'簡單走法：從下車點沿河選短段走 15–20 分鐘，再原路折返；預留候車時間。不要把較費力的 Savage Alpine 當成同一條河岸散步路線。',
   'route':'現場看什麼：Lower River、Riffles 與瀑布提供不同視角。觀察熊等待、移動與覓食的方式；當天魚況和季節會改變熊的位置。平台可能排隊，熊也可能暫時擋住步道。',
   'landscape':'現場看什麼：用地圖把 Copper Center、遠方山系和冰川的位置連起來，再走園區附近短步道。這段只認識公園入口，不把遠處冰川或礦鎮算成已造訪。',
   'road':'沿途停留：挑安全且允許停車的觀景點，短暫伸展和拍照；不在公路路肩臨時停車。遇施工或天候變化，先確保抵達住宿，再刪減觀景。',
  }.get(key,'看展與散步以當天開放區域為準，保留前往下一站的交通時間。')
  return f'<details class="spot-info"><summary>{esc(text[0])}</summary><p>{esc(text[1])}</p><p>{esc(extra)}</p></details>'
 def schedule(day,park=None):
  rows=[];shown=set()
  for idx,(time,kind,title,body,key) in enumerate(day['rows']):
   photo=stop_photo('brooks-river' if key=='route' and 'Lower River' in title else key,park,title) if key and key not in shown else ''
   if key=='route' and 'Lower River' in title:shown.add('lower')
   else:shown.add(key)
   rows.append(f'<li class="time-row" id="day-{day["n"]}-stop-{idx}"><div class="time-stamp"><strong>{esc(time)}</strong><span class="time-kind">{esc(kind)}</span></div><div><h3>{esc(title)}</h3><p>{esc(body)}</p>{photo}{chapter_details(key,park)}</div></li>')
  quick='<nav class="quick-stops" aria-label="當天景點">'+''.join(f'<a href="#day-{day["n"]}-stop-{idx}">{esc(title)}</a>' for idx,(_,_,title,_,key) in enumerate(day['rows']) if key in ['coastal','cruise','denali-rail','bus','dogs','savage','center','route','culture','landscape','anchorage-center','ship-creek','flight','cabin','matanuska'])+'</nav>'
  arranged='<div class="schedule-note"><strong>行程安排：Alaska Railroad 阿拉斯加鐵路</strong><p>Day 2–5 為由阿拉斯加鐵路安排的鐵路套裝行程段。預訂時請核對套裝所含列車、活動、住宿與接駁，以確認文件列出的內容和集合資訊為準。Denali 巴士仍需提前訂位，實際出發時刻於 48 小時前確認。</p></div>' if 2<=day['n']<=5 else ''
  notes=''.join(f'<div class="schedule-note"><strong>{esc(title)}</strong><p>{esc(body)}</p></div>' for title,body in day['notes'])
  links=''.join(f'<a class="cta" href="../../{d["page"]}#day-{d["n"]}">{"← 前一天" if d["n"]<day["n"] else "下一天 →"} · Day {d["n"]}</a>' for d in DAYS if abs(d['n']-day['n'])==1)
  return f'<section class="day-section" id="day-{day["n"]}"><div class="section-title"><p class="eyebrow">DAY {day["n"]:02}</p><h2>{esc(day["title"])}</h2><p>{esc(day["intro"])}</p><p class="overnight">當晚住宿：{esc(day["sleep"])}</p></div>{arranged}{quick}<ol class="timeline">{"".join(rows)}</ol>{notes}<nav class="day-jump" aria-label="相鄰日行程">{links}</nav></section>'
 def refs(items):return '<section class="references"><h2>班表與景點資料</h2>'+''.join(f'<a href="{url}" target="_blank" rel="noopener">{esc(name)} ↗</a>' for name,url in items)+'</section>'
 legend='<div class="schedule-note"><strong>怎麼讀時間表</strong><p>時間皆為阿拉斯加當地時間。表內保留當次搭乘與接駁時間，未記下精確時刻的活動以早上、下午或活動順序呈現。規劃自己的旅程時，請核對當季班表與訂位通知。</p></div>'
 cards=''.join(f'<a class="day-link" href="{day["page"]}#day-{day["n"]}"><span class="eyebrow">DAY {day["n"]:02}</span><h3>{esc(day["title"])}</h3><p>{esc(day["summary"])}</p><small>住宿：{esc(day["sleep"])}</small><b>看當天時間表 ↗</b></a>' for day in DAYS)
 home=head('阿拉斯加九日旅行')+f'<nav class="tabs"><a href="#days">逐日行程</a><a href="#booking">火車怎麼訂</a><a href="#connection">銜接與替代</a><a href="https://cy-demo.github.io/Sheng_exploration/">峽谷隨行 ↗</a></nav><section class="hero"><div class="hero-photo">{picture(parks[0])}<span class="photo-credit">{esc(credits["kenai"]["credit"])}</span></div><div class="hero-copy"><p class="eyebrow">9 DAYS / SUMMER ITINERARY</p><h1>沿著鐵路，<br>走進冰川與荒野。</h1><p>火車、冰川、看熊與公路旅行。<br>九天走過四座國家公園的搭乘與旅行經驗。</p><a class="cta" href="#days">從 Day 1 開始 ↗</a></div></section><section id="days"><div class="section-title"><p class="eyebrow">DAY BY DAY</p><h2>九天八夜，從 Anchorage 出發。</h2><p>適用於夏季火車、遊船與公園活動同時營運的時段。一天只有一座國家公園時，點進去就是該公園的完整當日行程；Denali 三天集中在同一分頁。</p></div>{legend}<div class="days-grid">{cards}</div></section><section id="booking"><div class="section-title"><p class="eyebrow">BOOK THE CONNECTIONS</p><h2>先訂交通與主活動，再排小景點。</h2></div><div class="schedule-note"><strong>Day 2–5：由 Alaska Railroad 阿拉斯加鐵路安排</strong><p>這幾天以鐵路套裝串聯 Seward 與 Denali；請向阿拉斯加鐵路確認當季可訂方案及包含項目。套裝的活動、住宿及接駁以確認文件為準。</p><strong>建議訂位順序</strong><p>先確認 Katmai 看熊與 Denali 住宿／Tundra Wilderness Tour 的名額，再一起確認四段火車及 Seward 12:00 船班，最後安排住宿接駁與租車。Tundra 團需提前報名；48 小時前公布的是實際出發時刻。</p></div><div class="table-wrap"><table><thead><tr><th>日次</th><th>列車與區間</th><th>出發 → 抵達</th><th>安排方式</th></tr></thead><tbody><tr><td>Day 2 去程</td><td>Coastal Classic<br>Anchorage → Seward</td><td>06:45 → 11:20</td><td>選當天往返；同時確認可接火車的遊船。</td></tr><tr><td>Day 2 回程</td><td>Coastal Classic<br>Seward → Anchorage</td><td>18:00 → 22:15</td><td>遊船須約 17:30 回港，接駁直接回車站。</td></tr><tr><td>Day 3</td><td>Denali Star<br>Anchorage → Denali</td><td>08:20 → 15:40</td><td>住 Denali 兩晚；預先安排車站接駁。</td></tr><tr><td>Day 5</td><td>Denali Star<br>Denali → Anchorage</td><td>12:30 → 20:00</td><td>早上只留遊客中心與入口活動。</td></tr></tbody></table></div><div class="reading-grid"><article><h3>火車＋船：一起核對</h3><p>可向 Alaska Railroad 詢問鐵路搭配遊船產品，或分開訂但向船公司註明列車時間。不要自行買到無法銜接的早班船。</p></article><article><h3>GoldStar 或 Adventure Class</h3><p>依預算選票種，另核對餐飲包含內容。車上是否用餐、餐點時間和座位由你的票種與現場安排決定；不用把市區午餐插進轉船空檔。</p></article><article><h3>一起訂住宿，確認套裝接送</h3><p>若透過阿拉斯加鐵路一起預訂住宿，套裝包含所安排飯店的接送；Denali 住宿飯店通常也提供接駁。訂住宿時一併確認 Anchorage 清晨接送、Denali 車站接送及飯店往返公園入口的班次、上下車位置與是否需預約。單買火車票的旅客，則需另外確認住宿交通。</p></article></div></section><section id="connection"><div class="section-title"><p class="eyebrow">KEEP THE DAYS CONNECTED</p><h2>三個不能硬接的地方。</h2></div><div class="reading-grid"><article><h3>Seward 遊客中心</h3><p>11:20 下車接 12:00 船班；曾在空檔快訪遊客中心，來回約十分鐘，但很趕。先完成必要報到並確認登船期限，有餘裕才去；想仔細看展可採留宿版。</p></article><article><h3>Denali 下午行程</h3><p>巴士每天有團，需提前預訂；出發前 48 小時確認實際時刻。若獲配約 06:00 早班，才照 Day 4 主表排犬舍與河谷。晚班必須刪減下午活動，不是把整張表往後擠。</p></article><article><h3>Katmai 補飛與返程</h3><p>這次 Day 6 起飛後折返，Day 7 換業者成功看熊，回城後再租車前往 Copper Center。這段很緊湊；後續旅客可多留一天，避免晚間趕路。</p></article></div></section>'+refs(SOURCES)+foot()
 (D/'index.html').write_text(home)
 for p in parks:
  pagepath='parks/'+p['slug']+'/'
  days=[day for day in DAYS if day['page']==pagepath]
  nav=''.join(f'<a href="#day-{d["n"]}">Day {d["n"]} · {esc(d["title"].split("｜")[-1])}</a>' for d in days)
  image=picture(p,'../../');credit=esc(credits[p['image']]['credit'])
  body=head(p['name']+'・逐日行程','../../')+f'<nav class="breadcrumbs"><a href="../../index.html#days">九天行程總覽</a><span>／ {esc(p["en"])}</span></nav><section class="park-hero"><div>{image}<span class="photo-credit">{credit}</span></div><div class="hero-copy"><p class="eyebrow">'+ ' · '.join('DAY '+str(d['n']) for d in days)+f'</p><h1>{esc(p["name"])}</h1><p class="park-en">{esc(p["en"])}</p><p>{esc(p["intro"])}</p></div></section><nav class="tabs day-tabs">{nav}</nav>{legend}'+''.join(schedule(day,p) for day in days)+refs(p['sources']+SOURCES)+f'<p class="fine">照片：{credit} · <a href="{credits[p["image"]]["source"]}">來源</a></p><p><a class="cta" href="../../index.html#days">返回九天行程總覽 ↗</a></p>'+foot('../../')
  folder=D/'parks'/p['slug'];folder.mkdir(parents=True,exist_ok=True);(folder/'index.html').write_text(body)
 city=D/'days/anchorage';city.mkdir(parents=True,exist_ok=True)
 (city/'index.html').write_text(head('Anchorage 抵達、緩衝與返程','../../')+'<nav class="breadcrumbs"><a href="../../index.html#days">九天行程總覽</a><span>／ Anchorage</span></nav><div class="section-title"><p class="eyebrow">DAY 1 / 9</p><h1>安克拉治，串起每一段。</h1><p>抵達、補給、天候緩衝與返程集中在這裡。</p></div>'+legend+''.join(schedule(d) for d in DAYS if d['page']=='days/anchorage/')+refs(SOURCES)+foot('../../'))
 (D/'parks.json').write_text(json.dumps([{'slug':p['slug'],'name':p['name'],'en':p['en'],'url':'parks/'+p['slug']+'/'} for p in parks],ensure_ascii=False,indent=2))
 sw=D/'sw.js'
 source=sw.read_text()
 start=source.index('const FILES=');end=source.index(';',start)
 files=['./','./index.html','./style.css','./app.js','./parks.json','./days/anchorage/']+['./parks/'+p['slug']+'/' for p in parks]+['./'+str(p.relative_to(D)) for p in (D/'assets').rglob('*') if p.is_file()]
 source=source[:start]+'const FILES='+json.dumps(files)+source[end:]
 source=source.replace('alaska-field-guide-v1:', 'alaska-field-guide-v2:')
 sw.write_text(source)
