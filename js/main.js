(function(){
  document.documentElement.classList.add('js');
  var $=function(s,c){return (c||document).querySelector(s)};
  var $$=function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s))};

  // reveal on scroll
  if(/[?&]static/.test(location.search)){ document.documentElement.classList.add('shot'); $$('img[loading=lazy]').forEach(function(i){i.loading='eager'}); $$('.reveal').forEach(function(el){el.classList.add('in')}) }
  else if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -6% 0px'});
    $$('.reveal').forEach(function(el){io.observe(el)});
  } else { $$('.reveal').forEach(function(el){el.classList.add('in')}) }

  // nav burger
  var navIn=$('.nav-inner'), burger=$('.burger');
  if(burger){burger.addEventListener('click',function(){var o=navIn.classList.toggle('open');burger.setAttribute('aria-expanded',o)});
    $$('.nav-links a').forEach(function(a){a.addEventListener('click',function(){navIn.classList.remove('open');burger.setAttribute('aria-expanded',false)})})}

  // active link
  var links=$$('.nav-links a');
  var secs=links.map(function(a){return $(a.getAttribute('href'))}).filter(Boolean);
  function onScroll(){
    var y=window.scrollY+window.innerHeight*.35, cur=null;
    secs.forEach(function(s){if(s.offsetTop<=y)cur=s.id});
    links.forEach(function(a){a.classList.toggle('active',a.getAttribute('href')==='#'+cur)});
    var mb=$('.mbar'); if(mb) mb.classList.toggle('show',window.scrollY>window.innerHeight*.7);
  }
  window.addEventListener('scroll',onScroll,{passive:true}); onScroll();

  // gallery filter
  var tiles=$$('.tile');
  $$('.tab').forEach(function(t){t.addEventListener('click',function(){
    $$('.tab').forEach(function(x){x.setAttribute('aria-pressed',x===t)});
    var f=t.dataset.f, isV=(f==='video');
    $('.grid').hidden=isV; $('.video-panel').hidden=!isV;
    if(isV)return;
    tiles.forEach(function(el){el.classList.toggle('hide',f!=='all'&&el.dataset.c.split(' ').indexOf(f)<0)});
  })});

  // video v galerii: soubor media/prohlidka.mp4 se použije automaticky, jakmile existuje
  var vp=$('.video-panel');
  if(vp && window.fetch && location.protocol.indexOf('http')===0){
    fetch('media/prohlidka.mp4',{method:'HEAD'}).then(function(r){
      if(!r.ok)return;
      vp.innerHTML='<video controls playsinline preload="metadata"><source src="media/prohlidka.mp4" type="video/mp4"></video>';
    }).catch(function(){});
  }

  // lightbox
  var lb=$('.lb'), lbImg=$('img',lb), lbCap=$('figcaption',lb), lbCount=$('.count',lb), cur=0, set=[];
  function visible(){return tiles.filter(function(t){return !t.classList.contains('hide')})}
  function show(i){
    cur=(i+set.length)%set.length; var t=set[cur];
    lbImg.src=t.dataset.full; lbImg.alt=t.dataset.cap; lbCap.textContent=t.dataset.cap;
    lbCount.textContent=(cur+1)+' / '+set.length;
    var nx=set[(cur+1)%set.length]; if(nx){(new Image()).src=nx.dataset.full}
  }
  function open(t){set=visible();cur=set.indexOf(t);lb.classList.add('open');document.body.style.overflow='hidden';show(cur);$('.x',lb).focus()}
  function close(){lb.classList.remove('open');document.body.style.overflow='';lbImg.removeAttribute('src')}
  tiles.forEach(function(t){t.addEventListener('click',function(){open(t)})});
  $('.x',lb).addEventListener('click',close);
  $('.p',lb).addEventListener('click',function(){show(cur-1)});
  $('.n',lb).addEventListener('click',function(){show(cur+1)});
  lb.addEventListener('click',function(e){if(e.target===lb)close()});
  document.addEventListener('keydown',function(e){
    if(!lb.classList.contains('open'))return;
    if(e.key==='Escape')close(); else if(e.key==='ArrowLeft')show(cur-1); else if(e.key==='ArrowRight')show(cur+1);
  });
  var sx=null; lb.addEventListener('touchstart',function(e){sx=e.touches[0].clientX},{passive:true});
  lb.addEventListener('touchend',function(e){if(sx===null)return;var dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>50)show(cur+(dx<0?1:-1));sx=null});

  // hero video: použije se automaticky, jakmile je v media/hero.mp4
  var hm=$('.hero-media');
  if(hm && window.fetch && location.protocol.indexOf('http')===0){
    fetch('media/hero.mp4',{method:'HEAD'}).then(function(r){
      if(!r.ok)return;
      var v=document.createElement('video');
      v.muted=true;v.loop=true;v.autoplay=true;v.playsInline=true;v.setAttribute('playsinline','');v.preload='auto';
      v.poster=$('img',hm).currentSrc||'';
      var s=document.createElement('source');s.src='media/hero.mp4';s.type='video/mp4';v.appendChild(s);
      v.addEventListener('canplay',function(){hm.appendChild(v);v.play()},{once:true});
    }).catch(function(){});
  }
})();
