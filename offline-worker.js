const key=path=>{const u=new URL(path,self.registration.scope);u.search='';u.hash='';if(u.pathname.endsWith('/'))u.pathname+='index.html';else if(!u.pathname.split('/').pop().includes('.'))u.pathname+='/index.html';return u.href;};
self.addEventListener('install',e=>e.waitUntil(self.skipWaiting()));
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('message',e=>{
 if(!['DOWNLOAD','STATUS'].includes(e.data?.type))return;
 e.waitUntil((async()=>{
  const port=e.ports[0],cache=await caches.open(CACHE),urls=[...new Set((e.data.pack==='southwest'?SOUTHWEST:FILES).map(key))];
  if(e.data.type==='STATUS'){let count=0;for(const url of urls)if(await cache.match(url))count++;port.postMessage({ok:count===urls.length,done:count,total:urls.length});return;}
  let cursor=0,done=0;const failed=[];
  const report=(file='')=>port.postMessage({progress:true,done,total:urls.length,file});
  report();
  const heartbeat=setInterval(()=>report(),5000);
  try{await Promise.all(Array.from({length:4},async()=>{while(cursor<urls.length){const url=urls[cursor++];try{
   if(!await cache.match(url)){
    let response;for(let retry=0;retry<3;retry++){const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),20000);try{response=await fetch(url,{cache:'reload',signal:controller.signal});if(!response.ok)throw new Error(String(response.status));if(!url.endsWith('.html')&&(response.headers.get('content-type')||'').includes('text/html'))throw new Error('Unexpected HTML');break;}catch(err){if(retry===2)throw err;}finally{clearTimeout(timer);}}
    await cache.put(url,response);
   }done++;report();
  }catch(err){failed.push(new URL(url).pathname+': '+err.name+' '+err.message);report();}}}));}finally{clearInterval(heartbeat)}
  port.postMessage({ok:failed.length===0,done,total:urls.length,failed});
 })().catch(err=>e.ports[0].postMessage({error:err.message})));
});
self.addEventListener('fetch',e=>{
 if(e.request.method!=='GET'||!e.request.url.startsWith(self.registration.scope))return;
 e.respondWith((async()=>{
  const cache=await caches.open(CACHE),url=key(e.request.url),saved=await cache.match(url);
  if(saved)return saved;
  try{return await fetch(e.request);}catch{
   for(const name of (await caches.keys()).reverse()){if(!name.startsWith('parks-'))continue;const old=await caches.open(name);const response=await old.match(url);if(response)return response;}
   return new Response('尚未儲存此頁。請連線後下載行程。 This page has not been saved offline.',{status:503,headers:{'Content-Type':'text/plain;charset=utf-8'}});
  }
 })());
});
