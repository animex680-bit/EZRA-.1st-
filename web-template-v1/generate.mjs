#!/usr/bin/env node
// Web Template v1 — generate a rebranded landing page from a brand config.
// Usage:  node generate.mjs brands/<brand>.json [outDir]
//   reads ./template.html (a snapshot of the master build) + the brand config,
//   swaps the copy, prices and asset base, and writes <outDir>/index.html.
// Only the config changes between brands — see brands/donk.json for a full example
// and README.md for the field list.
import {readFileSync,writeFileSync,mkdirSync,existsSync} from 'fs';
import {fileURLToPath} from 'url';
import {dirname,join,isAbsolute,resolve} from 'path';

const DIR = dirname(fileURLToPath(import.meta.url));
const cfgArg = process.argv[2];
if(!cfgArg){ console.error('usage: node generate.mjs brands/<brand>.json [outDir]'); process.exit(1); }
const cfgPath = isAbsolute(cfgArg) ? cfgArg : join(DIR, cfgArg);
const C = JSON.parse(readFileSync(cfgPath,'utf8'));
// use the live master build if it's a sibling, else the committed snapshot
const masterPath = [join(DIR,'..','360-remix','index.html'), join(DIR,'template.html')].find(existsSync);
if(!masterPath){ console.error('master not found (need ../360-remix/index.html or ./template.html)'); process.exit(1); }
let T = readFileSync(masterPath,'utf8');

const miss=[];
const g=(o,path)=>path.split('.').reduce((a,k)=>(a==null?a:a[k]),o);
const rep=(find,val)=>{ if(val==null||val==='') return; if(T.indexOf(find)<0){ miss.push(find.slice(0,52)); return; } T=T.split(find).join(val); };
// convenience: replace an anchor with a config value at `key` (dot path)
const R=(find,key)=>{ if(typeof key!=='string') return; rep(find, g(C,key)); };

/* ---------------- head / meta ---------------- */
if(C.lang) rep('lang="en-GB"','lang="'+C.lang+'"');
if(C.name&&C.titleTail) rep('<title>MEDO automotive — Walk around it. Read every fault.</title>','<title>'+C.name+' — '+C.titleTail+'</title>');
R('Performance cars in stock, restomods built in our own bay and parts fitted on our ramp. Walk around the car, read its published 360° report, dial in your monthly and print your viewing pass.','metaDesc');
if(C.name&&C.ogTitle) rep('content="MEDO automotive — Cars sold, built &amp; parted"','content="'+C.ogTitle+'"');
R('content="Every car inspected 360° — and the report published, faults included."','ogDesc');
if(C.name) rep('"name":"MEDO automotive"','"name":"'+C.name+'"');
if(C.area) rep('"areaServed":"GB"','"areaServed":"'+C.area+'"');
if(C.phone) rep('+44 20 7946 0011', C.phone);
if(C.shortMark) rep("text-anchor='middle'>MEDO</text>","text-anchor='middle'>"+C.shortMark+"</text>");

/* ---------------- brand marks ---------------- */
if(C.name) rep('aria-label="MEDO automotive home"','aria-label="'+C.name+' home"');
if(C.wordmark) rep('<span>ME<b>D</b>O</span>','<span>'+C.wordmark+'</span>');
if(C.shortMark){ rep('<b>MEDO<i>//</i>CORE</b>','<b>'+C.shortMark+'<i>//</i>CORE</b>'); rep('aria-label="MEDO assistant"','aria-label="'+C.shortMark+' assistant"');
  rep('aria-label="Ask MEDO anything"','aria-label="Ask '+C.shortMark+' anything"');
  rep('Ask MEDO anything →','Ask '+C.shortMark+' anything →'); rep("'<span class=\"bk\">MEDO</span>'","'<span class=\"bk\">"+C.shortMark+"</span>'");
  rep('● MEDO online','● '+C.shortMark+' online'); rep("return 'MEDO-'","return '"+C.shortMark+"-'"); }
if(C.ig) rep('medoautomotive', C.ig);   // covers the URL, the @handle and the schema in one
if(C.paintGold){ rep("['MEDO Gold','#b38b45']","['"+C.paintGold+"','#b38b45']"); rep("n:'MEDO Gold'","n:'"+C.paintGold+"'"); }
if(C.name) rep('Hi MEDO','Hi '+C.name);

/* ---------------- hero (overview greeting) ---------------- */
if(C.hero&&C.hero.kicker) rep('<p class="wh-k">MEDO automotive</p>','<p class="wh-k">'+C.hero.kicker+'</p>');
R('Walk in.<br>Drive out <em>proven.</em>','hero.h1');
R('Performance cars inspected on the ramp, restomods built in our own bay — and every fault published before you pay.','hero.sub');
R('Scroll to choose your way in','hero.cue');

/* ---------------- ways cards (Buy / Sell / Finance / Build / Parts) ---------------- */
const waysAnchor=[
 "t:'Buy a car',w:'Buy',s:AVAIL.length+' on the floor · every one inspected'",
 "t:'Sell or part-ex',w:'Sell',s:'A real price in thirty seconds'",
 "t:'Finance it',w:'Finance',s:'Turn the dial, feel the monthly'",
 "t:'Build a restomod',w:'Build',s:'Pick from six real 3D cars, see the price live'",
 "t:'Find a part',w:'Parts',s:'Counter sale, or fitted on our ramp'"];
if(Array.isArray(C.ways)) C.ways.forEach((w,i)=>{ if(!w||!waysAnchor[i]) return; const s=i===0?"AVAIL.length+' "+w.s+"'":"'"+w.s+"'"; rep(waysAnchor[i],"t:'"+w.t+"',w:'"+w.w+"',s:"+s); });

/* ---------------- omega (the AI) ---------------- */
if(C.omega){ const o=C.omega;
  if(o.aria) rep("aria-label=\"Meet MEDO, the shop's intelligence\"","aria-label=\""+o.aria+"\"");
  rep('MEDO · the intelligence on the floor', o.kicker);
  rep('I grew up on this forecourt. Now I run it.', o.h);
  rep('Every car, build, part and price passes through me first. Tell me what you want and I will find it, value the one you are driving, spec a restomod to the pound, or book your viewing — a straight answer, at any hour.', o.sub);
  rep('<span>cars sold</span>', o.statCars?'<span>'+o.statCars+'</span>':null);
  rep('<span>parts fitted</span>', o.statParts?'<span>'+o.statParts+'</span>':null);
  const factAnchor=[
   "'71 cars sold — every one up on the same ramp, same six checks.'",
   "'Tell me your plate and I value your car in thirty seconds.'",
   "'Tip: finance here is a soft search — it won’t touch your score.'",
   "'34 restomods built in our own bay, start to finish.'",
   "'Try asking me: “Porsches under £200k”.'",
   "'Every one of our 128 reviews is tied to a real invoice.'",
   "'Tip: tap any car in the showroom to spec it live.'",
   "'I’m awake at 2am — ask me before you drive down.'"];
  if(Array.isArray(o.facts)) o.facts.forEach((f,i)=>{ if(factAnchor[i]&&f) rep(factAnchor[i], "'"+f.replace(/'/g,"\\'")+"'"); });
}

/* ---------------- CORE bot (before nav/booking so its chip array isn't half-swapped) ---------------- */
if(C.core){ const c=C.core;
  rep('I’m <b>CORE</b>, linked to the floor, the ramp and the bay. Ask for a car, a colour, a monthly or a part — I’ll take you there.', c.greeting);
  rep('● linked to the floor, the ramp &amp; the bay', c.termSmall);
  rep('I didn’t catch that. I can find a car (<b>“Urus”</b>, <b>“under £100k”</b>), repaint the GT3 RS, work out a monthly, value your car, find a part or book you in.', c.fallback);
  if(Array.isArray(c.chips)) rep("const TCH=['Porsches under £200k','Make it red','360 scan','Monthly on the M4','Value my car','Brakes','Book a viewing','Opening hours'];","const TCH=["+c.chips.map(x=>"'"+x.replace(/'/g,"\\'")+"'").join(',')+"];"); }

/* ---------------- scan ---------------- */
if(C.scan){ R('Six checks · every car','scan.kicker'); rep('Six checks. <em>Zero secrets.</em>', C.scan.h);
  rep('Watch the bay scan it. Every reading lands on the report you get before you pay — resprayed panels and old fault codes included.', C.scan.lede); rep('Send me a report', C.scan.cta); }

/* ---------------- transitions ---------------- */
if(C.transitions){ const t=C.transitions;
  rep('<span>What’s it worth?</span><em>Thirty seconds.</em>', t.plate);
  rep('<small>The showroom</small>Three on the floor.<em>Pick one.</em>', t.shutter);
  rep('<small>Last stop</small>See you <em>on the ramp.</em>', t.tear); }

/* ---------------- showroom ---------------- */
if(C.showroom){ const s=C.showroom;
  rep('Restomods, built in our bay', s.kicker); rep('Pick a car. <em>The rest clear the floor.</em>', s.h);
  rep('Three different machines on the showroom floor. Tap one — the others drive out — then bolt parts on, repaint it and watch the price move. Rather we design it? One call.', s.lede);
  rep('<small>Showroom · 3 cars</small><b>Tap a car to build it</b>', s.pick);
  rep('Drag to look round · tap a car', s.drag); rep('or send this spec on WhatsApp →', s.wa); }

/* ---------------- reviews ---------------- */
if(C.reviews){ const r=C.reviews; rep('What buyers say', r.kicker); rep('Straight dealing, <em>in their words.</em>', r.h);
  rep('Twelve buyers, twelve real invoices. Drag the ring, then tap a face — they’ll tell you the bit that didn’t fit in five stars.', r.lede);
  rep('verified reviews', r.verified); }

/* ---------------- finance / booking ---------------- */
if(C.finance){ rep('Finance, arranged in-house', C.finance.kicker); }
if(C.booking){ const b=C.booking; rep('Book a viewing', b.bookCta);
  rep('Print your pass. <em>It’ll be on the ramp.</em>', b.print);
  rep('<b>Green man’s on.</b>Walk in off the street — the kettle’s warm and the ramp is free. Or print a pass below and we’ll have the car waiting.', b.walk); }

/* ---------------- nav / footer ---------------- */
if(C.nav){ rep('>Value my car<', C.nav.value?'>'+C.nav.value+'<':null); rep('Value my car <span>30 sec</span>', C.nav.value?C.nav.value+' <span>30 sec</span>':null);
  rep('On the floor now', C.nav.stockHeader); rep('· Credit broker, not a lender', C.nav.footerTag?'· '+C.nav.footerTag:null); }

/* ---------------- extra one-off replacements ---------------- */
if(Array.isArray(C.extra)) C.extra.forEach(([a,b])=>{ if(T.indexOf(a)<0){ miss.push('[extra] '+a.slice(0,42)); } else T=T.split(a).join(b); });

/* ---------------- any remaining brand name / mark (comments, aria, etc.) ---------------- */
if(C.name) T=T.split('MEDO automotive').join(C.name);
if(C.shortMark) T=T.split('MEDO').join(C.shortMark);

/* ---------------- terminology globals ---------------- */
if(Array.isArray(C.terminology)) C.terminology.forEach(([a,b])=>{ T=T.split(a).join(b); });

/* ---------------- currency + asset base ---------------- */
if(C.currency&&C.currency!=='£') T=T.split('£').join(C.currency);
const assetBase = C.assetBase || '../360-remix/assets/';
T = T.split('assets/').join(assetBase);

/* ---------------- write ---------------- */
const outDir = process.argv[3] ? (isAbsolute(process.argv[3])?process.argv[3]:resolve(process.cwd(),process.argv[3]))
  : join(DIR,'..', C.output || 'brand-site');
mkdirSync(outDir,{recursive:true});
const outFile = join(outDir,'index.html');
writeFileSync(outFile, T);
console.log('✓ wrote', outFile, '('+T.length+' bytes)');
console.log('  brand:', C.name, '· ig: @'+(C.ig||'?'));
if(miss.length){ console.log('  ⚠ '+miss.length+' anchor(s) not found (template may have changed, or field unused):'); miss.forEach(m=>console.log('    -', m)); }
else console.log('  all anchors matched.');
