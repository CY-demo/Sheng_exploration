
// Keep saved links to the previous park homepage usable after theme separation.
const hash=location.hash;
const english=document.documentElement.lang==='en';
const legacy={death:'parks/death-valley/',grand:'parks/grand-canyon/',page:'nearby/page/',airport:'travel/airports/'};
const part=hash.slice(1).split('/');
if(legacy[part[0]])location.replace(new URL(legacy[part[0]]+(part[1]?'#'+encodeURIComponent(part[1]):''),document.baseURI).href);
else if(['map','parks','routes','nearby'].includes(part[0]))location.replace(new URL('themes/us-national-parks/'+hash,document.baseURI).href);
else if(['days','booking','connection'].includes(part[0]))location.replace(new URL('routes/alaska/'+hash,document.baseURI).href);
