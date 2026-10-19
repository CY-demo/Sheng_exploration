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
async function worker(){
 if(!('serviceWorker' in navigator))throw new Error(t('請用 Safari 或 Chrome 開啟此網站後下載。','Open this site in Safari or Chrome to download.'));
 if(!ready)ready=(async()=>{const reg=await navigator.serviceWorker.register(new URL('sw.js',base),{scope:base.pathname,updateViaCache:'none'});try{await reg.update()}catch{}const w=reg.installing||reg.waiting;if(w&&w.state!=='activated')await new Promise((resolve,reject)=>{const timer=setTimeout(()=>reject(new Error('Service worker activation timed out')),20000);w.addEventListener('statechange',()=>{if(w.state==='activated'){clearTimeout(timer);resolve()}else if(w.state==='redundant'){clearTimeout(timer);reject(new Error('Please reload and try again'))}});});return reg})();
 try{return await ready}catch(err){ready=null;throw err}
}
const button=document.getElementById('offline'),status=document.getElementById('offline-status');
const box=document.createElement('section');box.className='offline-panel';box.style.cssText='margin:1rem;padding:1rem;border:1px solid #b7c6bf;border-radius:12px';
box.innerHTML='<strong>'+t('離線閱讀','Offline reading')+'</strong><p>'+t('先連線下載，完成後使用同一個 Safari／Chrome 開啟此網址。大峽谷・死亡谷包包含佩吉、行程、中文／英文與照片。','Download while online, then reopen this URL in the same Safari/Chrome browser. The Southwest pack includes Grand Canyon, Death Valley, Page, both languages and photos.')+'</p><label>'+t('下載範圍：','Download: ')+'<select id="offline-pack"><option value="southwest">'+t('大峽谷・死亡谷・佩吉','Grand Canyon · Death Valley · Page')+'</option><option value="all">'+t('整個網站','Entire website')+'</option></select></label><p id="offline-progress" role="status" aria-live="polite"></p>';
button.closest('header').after(box);const progress=box.querySelector('#offline-progress'),select=box.querySelector('select');
function say(message){progress.textContent=message;status.textContent=message;}
function request(reg,type,onprogress){return new Promise((resolve,reject)=>{const channel=new MessageChannel();let timer;const reset=()=>{clearTimeout(timer);timer=setTimeout(()=>{channel.port1.close();reject(new Error(t('下載暫停；請保持頁面開啟再重試，已完成的檔案會保留。','Download paused. Keep this page open and retry; saved files are retained.')))},90000)};reset();channel.port1.onmessage=e=>{reset();if(e.data.progress){onprogress?.(e.data);return}clearTimeout(timer);channel.port1.close();resolve(e.data)};reg.active.postMessage({type,pack:select.value},[channel.port2]);});}
async function check(){try{const r=await request(await worker(),'STATUS');if(r.ok){button.textContent=t('已可離線閱讀 ✓','Ready offline ✓');say(t('已儲存此行程的文字與照片。可開飛航模式，重新整理測試。外部連結需要網路。','Text and photos saved. Test by enabling airplane mode and reloading. External links need internet.'))}else{button.textContent=t('離線下載','Download offline');say(t('尚未完成離線下載。','Offline download is not complete.'))}}catch(err){say(err.message)}}
select.addEventListener('change',check);check();
button.addEventListener('click',async()=>{button.disabled=true;select.disabled=true;button.textContent=t('下載中…','Saving…');try{const r=await request(await worker(),'DOWNLOAD',r=>say(t('儲存中 ','Saving ')+r.done+' / '+r.total));if(!r.ok)throw new Error(t('部分檔案未完成，請重試。已儲存的檔案會保留。','Some files could not be saved. Retry to resume.'));await check();try{await navigator.storage?.persist?.()}catch{}}catch(err){button.textContent=t('繼續下載','Resume download');say(err.message)}finally{button.disabled=false;select.disabled=false}});
