'use strict';
const legacy={death:'parks/death-valley/',grand:'parks/grand-canyon/',page:'nearby/page/',airport:'travel/airports/'};
const parts=location.hash.slice(1).split('/');
if(legacy[parts[0]])location.replace(new URL(legacy[parts[0]]+(parts[1]?'#'+encodeURIComponent(parts[1]):''),document.baseURI).href);
if(parts[0]==='days'||parts[0]==='booking'||parts[0]==='connection')location.replace(new URL('routes/alaska/'+location.hash,document.baseURI).href);
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{
 document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
 const empty=document.getElementById('region-empty');
 if(empty)empty.hidden=['all','west','alaska'].includes(button.dataset.filter);
 document.querySelectorAll('[data-region]').forEach(card=>{const hide=button.dataset.filter!=='all'&&card.dataset.region!==button.dataset.filter;if(hide)card.setAttribute('hidden','');else card.removeAttribute('hidden');});
}));
