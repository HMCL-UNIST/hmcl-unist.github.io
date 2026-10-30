"""Prepare the approved static design for the CMS's existing layout slots."""
from pathlib import Path
from bs4 import BeautifulSoup
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'cms-transfer'
BACKUP = Path('/home/hmcl/cms-backups/20261029')
routes = {
 '/research/':'/hmc/research-overview.do', '/research/cps/':'/hmc/cyber-physical-system-cps.do',
 '/research/cps/cps-theory/':'/hmc/cps-theory.do', '/research/cps/cps-application/':'/hmc/cps-application.do',
 '/research/autonomous-driving/':'/hmc/autonomous-driving.do', '/research/autonomous-flight/':'/hmc/autonomous-flight.do',
 '/members/':'/hmc/graduate-students.do', '/members/graduate/':'/hmc/graduate-students.do',
 '/members/professor/':'/hmc/professor.do', '/gallery/videos/':'/hmc/videos-github.do',
 '/publications-hmc/journal-articles-hmc/':'/hmc/journal-articles.do', '/gallery/2026/':'/hmc/professor/gallery.do',
 '/gallery/2026/2026-ifac-roboracer/':'/hmc/professor/gallery.do?mode=view&articleNo=308346',
 '/gallery/2026/2026-lunch-with-professor/':'/hmc/professor/gallery.do?mode=view&articleNo=308335',
 '/gallery/2026/2026-ifac-bootcamp/':'/hmc/professor/gallery.do?mode=view&articleNo=308334',
 '/gallery/2026/2026-unist-creative-design-festival/':'/hmc/professor/gallery.do?mode=view&articleNo=311451',
}
def convert(node):
 for a in node.select('a[href]'):
  a['href'] = routes.get(a['href'], a['href'])
 for img in node.select('img[src]'):
  if img['src'].startswith('/'): img['src']='https://hmcl-unist.github.io'+img['src']
 return str(node)

def scope_css(source):
 source=re.sub(r'/\*.*?\*/','',source,flags=re.S)
 result=[]; pos=0
 while pos<len(source):
  start=source.find('{',pos)
  if start<0: break
  header=source[pos:start].strip(); depth=1; end=start+1
  while end<len(source) and depth:
   if source[end]=='{':depth+=1
   elif source[end]=='}':depth-=1
   end+=1
  body=source[start+1:end-1]
  if header.startswith('@media'):
   result.append(header+'{'+scope_css(body)+'}')
  elif not header.startswith('@'):
   selectors=[]
   for selector in header.split(','):
    selector=selector.strip()
    if selector==':root': selectors.append('.hmc-cms-page'); continue
    if selector in ['html','body','html,body']: continue
    selector=re.sub(r'^body\s+', '', selector)
    selectors.append('.hmc-cms-page '+selector)
   if selectors:result.append(','.join(selectors)+'{'+body+'}')
  pos=end
 return '\n'.join(result)

home=BeautifulSoup((OUT/'source-home.html').read_text(),'html.parser').select_one('main')
home['class'].append('hmc-cms-page')
main_html=convert(home)
research=BeautifulSoup((OUT/'source-research.html').read_text(),'html.parser').select_one('.hmcl-research-overview')
research['class'].append('hmc-cms-page')
css=scope_css((ROOT/'assets/css/site-preview.css').read_text())
css+='''
.hmc-cms-page{--navy:#071e53;--teal:#087d80;--ink:#263449;--muted:#59677a;--line:#dce3ec;--surface:#f3f6fa;--radius:16px;font-family:Arial,"Noto Sans KR",sans-serif;color:var(--ink);line-height:1.7;min-width:0}
.hmc-cms-page .hmcl-container{width:calc(100% - 48px);max-width:none}
.hmc-cms-page.hmcl-home-main>.hmcl-container{width:100%}
.hmc-cms-page h1,.hmc-cms-page h2,.hmc-cms-page h3{color:#071e53;font-weight:700;line-height:1.25;letter-spacing:-.025em}
.hmc-cms-page .hmcl-home-intro h1,.hmc-cms-page .hmcl-highlight h2{color:white}
.hmc-cms-page .hmcl-home-intro>div{padding:30px}.hmc-cms-page .hmcl-home-intro h1{font-size:clamp(26px,2.2vw,36px)}
.hmc-cms-page .hmcl-home-intro p{font-size:14px}.hmc-cms-page img{max-width:100%}
.hmc-cms-page .hmcl-home-publications article{grid-template-columns:120px minmax(0,1fr) 50px;gap:20px}
.header-inner .logo img{content:url("https://hmcl-unist.github.io/media/2020/lab_Logo.jpg");width:240px!important;height:auto!important;max-height:none!important;object-fit:contain}.header-inner .logo a>span{display:none!important}
#cms-content .migration-hmc-members .member-card{background:white!important;border:0!important;border-bottom:1px solid #e4e9ef!important;border-radius:0!important;padding:20px 0}
#cms-content .migration-hmc-members .member-photo{background:transparent!important;flex:0 0 125px!important;width:125px!important;height:auto!important;align-self:flex-start!important}
#cms-content .migration-hmc-members .member-card .member-photo img{width:125px!important;height:auto!important;aspect-ratio:1;object-fit:cover!important;border-radius:12px}
#cms-content .migration-hmc-members .member-card-content{background:white!important;padding:0 0 0 18px!important}
.hmc-cms-page a:focus-visible{outline:3px solid #087d80;outline-offset:4px}
.wrap:not(.sub) .main-container{display:grid!important;grid-template-columns:300px minmax(0,1fr);gap:40px;align-items:start;padding-top:24px!important}
.wrap:not(.sub) .main-right{width:auto!important;min-width:0}
.wrap .main-left{position:sticky!important;top:110px!important;margin-top:0!important;height:auto!important;max-height:calc(100dvh - 130px);overflow-y:auto;align-self:start;scrollbar-width:thin}
.wrap .main-left-inner{position:static!important;top:auto!important;width:auto!important}
.wrap .main-left .main-left-fixed{display:none!important}.wrap .main-left .top{display:block!important}
.wrap .main-left [data-aos]{opacity:1!important;transform:none!important}
#cms-content .migration-hmc-members .member-name-card{background:white!important;border:0!important;border-radius:0!important;box-shadow:none!important}
@media(max-width:1000px){.wrap:not(.sub) .main-container{display:block!important;padding:12px 20px 45px!important}.wrap .main-left{display:none!important}.wrap:not(.sub) .main-right{width:100%!important}}
@media(max-width:767px){.hmc-cms-page .hmcl-home-intro{display:flex;flex-direction:column}.hmc-cms-page .hmcl-home-photo{order:-1}.hmc-cms-page .hmcl-home-highlights,.hmc-cms-page .hmcl-research-grid,.hmc-cms-page .hmcl-event-grid,.hmc-cms-page .hmcl-join{grid-template-columns:1fr}.hmc-cms-page .hmcl-home-publications article{grid-template-columns:1fr auto}.hmc-cms-page .hmcl-home-publications time{grid-column:1/-1}.header-inner .logo img{width:160px!important}.header-inner{padding:6px 0!important}}
@media(max-width:480px){#cms-content .migration-hmc-members .member-name-card{display:flex!important}#cms-content .migration-hmc-members .member-photo{flex-basis:100px!important;width:100px!important}#cms-content .migration-hmc-members .member-card .member-photo img{width:100px!important;margin:0!important}#cms-content .migration-hmc-members .member-card-content{padding-left:14px!important}}
@media(hover:hover) and (prefers-reduced-motion:no-preference){.migration-hmc-members .member-photo img{transition:transform 220ms ease-out}.migration-hmc-members .member-photo:hover img{transform:scale(1.025)}}
'''
script='''(() => { const init=()=>{
 document.querySelectorAll('.header-inner .logo a').forEach(a=>{a.setAttribute('aria-label','HMCL home');a.title='High-assurance Mobility Control Lab.';const img=a.querySelector('img');if(img){img.src='https://hmcl-unist.github.io/media/2020/lab_Logo.jpg';img.alt='HMCL · UNIST';}});
 document.querySelectorAll('header a').forEach(a=>{if(a.textContent.trim()==='Research'&&a.getAttribute('href')==='/hmc/cyber-physical-system-cps.do')a.href='/hmc/research-overview.do';if(a.getAttribute('href')==='/hmc/research-overview.do'&&a.textContent.trim()==='Research Overview'){const item=a.closest('li');if(item)item.parentElement.prepend(item);}});
 document.querySelectorAll('a[href*="articleNo=311451"] .b-img-box img').forEach(img=>{img.src='https://hmcl-unist.github.io/gallery/2026/media/2026/2026-unist-creative-design-festival-600x450.jpg';img.alt='2026 UNIST Creative Design Festival';});
 document.querySelectorAll('.main-left a').forEach(a=>{if(a.textContent.trim()==='More Informaiton'){a.textContent='Professor profile';a.href='/hmc/professor.do';}});
 document.querySelectorAll('.footer-inner a').forEach(a=>{if(a.getAttribute('href')==='https://www.youtube.com/'||a.getAttribute('href')==='https://youtube.com/')a.href='https://www.youtube.com/channel/UCJ8jHtSjObD5z89FeLyJuDw';});
 const reduce=matchMedia('(prefers-reduced-motion: reduce)');
 if(reduce.matches||!window.IntersectionObserver||!Element.prototype.animate)return;
 const observer=new IntersectionObserver(items=>{for(const item of items){if(!item.isIntersecting)continue;observer.unobserve(item.target);if(!reduce.matches)item.target.animate([{opacity:.35,transform:'translateY(16px)'},{opacity:1,transform:'translateY(0)'}],{duration:450,delay:Number(item.target.dataset.hmcDelay||0),easing:'cubic-bezier(.16,1,.3,1)'});}},{threshold:.08});
 document.querySelectorAll('.hmc-cms-page .hmcl-event,.hmc-cms-page .hmcl-research-item,.hmc-cms-page .hmcl-highlight,.hmc-cms-page .hmcl-research-directions>a,.migration-hmc-members .member-card').forEach((el,i)=>{el.dataset.hmcDelay=String(i%3*70);observer.observe(el);});
 reduce.addEventListener('change',()=>{if(reduce.matches){observer.disconnect();document.querySelectorAll('[data-hmc-delay]').forEach(el=>el.getAnimations().forEach(a=>a.cancel()));}});
 }; if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});else init();})();'''
original=(BACKUP/'main-template.jsp').read_text()
start=original.index('\t\t<div class="main-right">')
end=original.index('\n\t<footer>',start)
main_template=original[:start]+'\t\t<div class="main-right">\n'+main_html+'\n\t\t</div>\n\t</div>'+original[end:]
footer=(BACKUP/'footer.jsp').read_text().replace('School of Urban &amp;<br class="pc-hide"> Environmental Engineering','Department of Mechanical Engineering').replace('School of Urban &amp;Environmental Engineering','Department of Mechanical Engineering').replace('+82-52-217-2798','052-217-2433').replace('tel:052-217-6333','tel:052-217-2433').replace('052-217-6333','052-217-2433').replace('unist@unist.ac.kr','kwonc@unist.ac.kr').replace('COPYRIGHT 2025','COPYRIGHT 2026').replace('ALL RIGHTS RESEVERED.','ALL RIGHTS RESERVED.')
footer=re.sub(r'School of Urban &amp;\s*(?:<br[^>]*>\s*)?Environmental Engineering','Department of Mechanical Engineering',footer)
footer=footer.replace('<a href="#" title="새창열림">Department of Mechanical Engineering</a>', '<a href="https://me.unist.ac.kr/me/index.do" target="_blank" rel="noopener" title="새창열림">Department of Mechanical Engineering</a>')
footer+='\n<style>\n'+css+'\n</style>\n<script>\n'+script+'\n</script>'
files={'main-template.jsp':main_template,'footer.jsp':footer,'research-overview.html':convert(research),'shared.css':css,'shared.js':script}
print('*** Begin Patch')
for name,data in files.items():
 p=OUT/name
 if p.exists():
  print('*** Update File: '+str(p)+'\n@@')
  for line in p.read_text().splitlines():print('-'+line)
 else:print('*** Add File: '+str(p))
 for line in data.splitlines():print('+'+line)
print('*** End Patch')
