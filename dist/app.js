'use strict';
const scriptURL=new URL(document.currentScript.src),base=new URL('./',scriptURL);
const english=document.documentElement.lang==='en';
const t=(zh,en)=>english?en:zh;
const font=document.getElementById('font');
function setLarge(on){document.body.classList.toggle('large',on);font.setAttribute('aria-pressed',String(on));font.textContent=on?t('標準字','Standard text'):t('大字','Larger text');}
try{setLarge(localStorage.getItem('alaska-large')==='true')}catch{}
font.addEventListener('click',()=>{const on=!document.body.classList.contains('large');setLarge(on);try{localStorage.setItem('alaska-large',on)}catch{}});
// Preserve the current section when switching language, with usable HTML links as fallback.
function languageLinks(){document.querySelectorAll('.language-switch a').forEach(a=>{const u=new URL(a.href);u.hash=location.hash;a.href=u.href;});}
languageLinks();addEventListener('hashchange',languageLinks);
const expand=document.getElementById('expand');
if(expand)expand.addEventListener('click',()=>{const details=[...document.querySelectorAll('.chapter details')];const open=details.some(d=>!d.open);details.forEach(d=>d.open=open);expand.textContent=open?t('收合詳細介紹','Collapse detailed guides'):t('展開詳細介紹','Expand detailed guides');});
let ready;
function deadline(p,ms,message){let timer;return Promise.race([p,new Promise((_,reject)=>{timer=setTimeout(()=>reject(new Error(message)),ms)})]).finally(()=>clearTimeout(timer));}
async function worker(){
 if(!('serviceWorker' in navigator))throw new Error(t('此瀏覽器不提供離線儲存。請將網址貼到 Safari 或 Chrome。','Offline storage is unavailable. Paste this URL into Safari or Chrome.'));
 if(!ready)ready=(async()=>{
  const reg=await deadline(navigator.serviceWorker.register(new URL('sw.js',base),{scope:base.pathname,updateViaCache:'none'}),15000,t('離線服務連線逾時。請確認網路後再按下載。','Offline service connection timed out. Check your connection and retry.'));
  // Do not force a second update while the first installation is running.
  let activationPoll;try{await deadline(new Promise(resolve=>{activationPoll=setInterval(()=>{if(reg.active?.state==='activated')resolve()},100)}),15000,t('離線服務尚未啟動，請重新整理網頁。','Offline service has not activated. Reload this page.'));}finally{clearInterval(activationPoll)}
  return reg;
 })();
 try{return await ready}catch(err){ready=null;throw err}
}
const button=document.getElementById('offline'),status=document.getElementById('offline-status');
const box=document.createElement('section');box.className='offline-panel';box.style.cssText='margin:1rem;padding:1rem;border:1px solid #b7c6bf;border-radius:12px';
box.innerHTML='<strong>'+t('離線閱讀','Offline reading')+'</strong><p>'+t('先連線下載，完成後使用同一個 Safari／Chrome 開啟此網址。大峽谷・死亡谷包包含佩吉、行程、中文／英文與照片。','Download while online, then reopen this URL in the same Safari/Chrome browser. The Southwest pack includes Grand Canyon, Death Valley, Page, both languages and photos.')+'</p><label>'+t('下載範圍：','Download: ')+'<select id="offline-pack"><option value="southwest">'+t('大峽谷・死亡谷・佩吉','Grand Canyon · Death Valley · Page')+'</option><option value="all">'+t('整個網站','Entire website')+'</option></select></label><p id="offline-progress" role="status" aria-live="polite"></p>';
button.closest('header').after(box);const progress=box.querySelector('#offline-progress'),select=box.querySelector('select');
function say(message){progress.textContent=message;status.textContent=message;}
function request(reg,type,onprogress){return new Promise((resolve,reject)=>{
 const channel=new MessageChannel();let timer;const finish=(err,result)=>{clearTimeout(timer);channel.port1.close();channel.port2.close();if(err){ready=null;reject(err)}else resolve(result)};
 const reset=()=>{clearTimeout(timer);timer=setTimeout(()=>finish(new Error(t('離線服務沒有回應。請重新整理網頁後再下載；已儲存資料會保留。','Offline service did not respond. Reload and retry; saved files are retained.'))),type==='STATUS'?10000:30000)};
 reset();channel.port1.onmessage=e=>{reset();if(e.data.progress){onprogress?.(e.data);return}if(e.data.error){finish(new Error(e.data.error));return}finish(null,e.data)};
 try{if(!reg.active||reg.active.state!=='activated')throw new Error(t('離線服務尚未就緒，請重新整理。','Offline service is not ready. Reload this page.'));reg.active.postMessage({type,pack:select.value},[channel.port2]);}catch(err){finish(err)}
 });}
let downloading=false;
async function check(){if(downloading)return;try{const r=await request(await worker(),'STATUS');if(downloading)return;if(r.ok){button.textContent=t('已可離線閱讀 ✓','Ready offline ✓');say(t('已儲存此行程的文字與照片。可開飛航模式，重新整理測試。外部連結需要網路。','Text and photos saved. Test by enabling airplane mode and reloading. External links need internet.'))}else{button.textContent=t('離線下載','Download offline');say(t('尚未完成離線下載。','Offline download is not complete.'))}}catch(err){say(err.message)}}
select.addEventListener('change',check);check();
button.addEventListener('click',async()=>{
 if(downloading)return;downloading=true;button.disabled=true;select.disabled=true;button.textContent=t('連接中…','Connecting…');say(t('正在連接離線服務，請保持此頁開啟…','Connecting to offline storage. Keep this page open…'));ready=null;
 try{
  const reg=await worker();button.textContent=t('下載中…','Saving…');
  const r=await request(reg,'DOWNLOAD',r=>say(t('已儲存 ','Saved ')+r.done+' / '+r.total+(r.file?' · '+r.file:'')));
  if(!r.ok)throw new Error(t('未完成 ','Incomplete ')+(r.total-r.done)+' / '+r.total+' — '+(r.failed?.slice(0,2).join('; ')||t('請檢查網路或儲存空間。','Check connection or storage space.')));
  button.textContent=t('已可離線閱讀 ✓','Ready offline ✓');say(t('行程、排版與照片已全部儲存。可開飛航模式後重新整理測試。','Itinerary, layout and photos saved. Enable airplane mode and reload to test.'));
 }catch(err){ready=null;button.textContent=t('繼續下載','Resume download');say(t('下載未完成：','Download incomplete: ')+(err.message||err.name));}
 finally{downloading=false;button.disabled=false;select.disabled=false}
});
