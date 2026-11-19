import vm from 'node:vm';
import fs from 'node:fs/promises';
import assert from 'node:assert/strict';
const code=await fs.readFile('dist/sw.js','utf8');
for(const scope of ['https://test.local/','https://test.local/Sheng_exploration/']){
 let offline=false,fail=true;const handlers={},stores=new Map(),counts=new Map();
 const caches={open:async n=>{if(!stores.has(n))stores.set(n,new Map());const m=stores.get(n);return {match:async u=>m.get(u)?.clone(),put:async(u,r)=>m.set(u,r.clone())}},keys:async()=>[...stores.keys()]};
 const ctx={URL,Response,AbortController,setTimeout,clearTimeout,setInterval,clearInterval,caches,self:{registration:{scope},clients:{claim:async()=>{}},skipWaiting:async()=>{},addEventListener:(n,f)=>handlers[n]=f},fetch:async url=>{url=String(url);counts.set(url,(counts.get(url)||0)+1);if(offline||fail&&url.endsWith('badwater-hd.webp'))throw Error('network');const relative=new URL(url).pathname.slice(new URL(scope).pathname.length);try{const data=await fs.readFile('dist/'+relative);return new Response(data,{headers:{'Content-Type':relative.endsWith('.html')?'text/html':'application/octet-stream'}})}catch{return new Response('',{status:404})}}};
 vm.runInNewContext(code,ctx);
 async function download(pack='southwest'){let work;const messages=[];handlers.message({data:{type:'DOWNLOAD',pack},ports:[{postMessage:m=>messages.push(m)}],waitUntil:p=>work=p});await work;return messages.at(-1)}
 const first=await download();assert.equal(first.ok,false);assert(first.done>0);const already=counts.get(scope+'app.js');fail=false;const second=await download();assert.equal(second.ok,true);assert.equal(counts.get(scope+'app.js'),already,'Resume must reuse saved files');offline=true;
 async function read(path){let p;handlers.fetch({request:{method:'GET',url:scope+path},respondWith:r=>p=r});return p}
 for(const page of ['routes/southwest/','parks/grand-canyon','parks/death-valley/index.html?test=1','en/parks/grand-canyon/','nearby/page/']){const r=await read(page);assert.equal(r.status,200,page);assert.match(await r.text(),/<html/)}
 for(const file of ['style.css','app.js','assets/park-scenes/badwater-hd.webp','assets/park-scenes/mather-point-hd.webp'])assert.equal((await read(file)).status,200,file);
 assert.equal((await read('not-downloaded/')).status,503);

 offline=false;
 const all=await download('all');assert.equal(all.ok,true);
 offline=true;
 for(const page of ['routes/fairbanks-winter/','en/routes/fairbanks-winter/','fairbanks.css']){
  const r=await read(page);assert.equal(r.status,200,page);
  if(page.endsWith('/'))assert.match(await r.text(),/id="glass"/);
 }
 console.log('PASS full pack Fairbanks routes and stylesheet:',scope);
 console.log('PASS offline download, failed-file retry, partial resume, HTML aliases, bilingual pages, photos:',scope);
}
