/* Anime.js V3.2.2 is loaded from CDN. Animation is decorative and gracefully optional. */
(() => {
 const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 const cards = document.querySelectorAll('.shelf-card');
 if (reduced || !window.anime) return;
 const anim = window.anime;
 anim({targets:'.mascot', rotate:[-9,0,-9], duration:5500, direction:'alternate', easing:'easeInOutSine',loop:true});
 anim({targets:'.leaf-orbit',translateY:[0,-15,0],rotate:[0,25,0],duration:6500,easing:'easeInOutSine',loop:true});
 const label = document.querySelector('.hero .eyebrow');
 if(label) anim({targets:label,opacity:[0,1],translateY:[12,0],duration:950,easing:'easeOutCubic'});
 const shelf = document.querySelector('#shelf');
 if(!shelf || !cards.length)return;
 const reveal = () => anim({targets:cards,opacity:[0,1],translateY:[95,0],rotateX:[-16,0],scale:[.94,1],delay:anim.stagger(190),duration:1050,easing:'easeOutExpo'});
 let appeared=false;
 const io=new IntersectionObserver(entries=>{
   if(entries.some(e=>e.isIntersecting) && !appeared){appeared=true;reveal();}
 },{threshold:.18});
 io.observe(shelf);
 cards.forEach(c=>{
   c.addEventListener('mouseenter',()=>anim({targets:c,translateY:-12,scale:1.02,duration:360,easing:'easeOutQuad'}));
   c.addEventListener('mouseleave',()=>anim({targets:c,translateY:0,scale:1,duration:400,easing:'easeOutQuad'}));
 });
 const nodes=document.querySelectorAll('.diagram-node');
 const section=document.querySelector('#features');
 if(section&&nodes.length){
   let started=false;
   new IntersectionObserver(entries=>{
     if(entries.some(e=>e.isIntersecting)&&!started){
       started=true;
       anim({targets:nodes,opacity:[0,1],scale:[.85,1],delay:anim.stagger(180),duration:800,easing:'easeOutBack'});
     }
   },{threshold:.25}).observe(section);
 }
})();
