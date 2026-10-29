/* Shared preview shell. Original citations and member details stay in page HTML. */
(() => {
  'use strict';
  document.body.classList.add('hmcl-preview-site');
  const path = location.pathname.replace(/index\.html$/, '').replace(/\/$/, '') || '/';
  const official = 'https://www.unist.ac.kr/hmc/';
  const sections = [
    {name: 'Research', href: '/research/', links: [
      ['Research overview', '/research/'], ['Cyber-Physical Systems', '/research/cps/'],
      ['Autonomous Driving', '/research/autonomous-driving/'], ['Autonomous Flight', '/research/autonomous-flight/'],
      ['Videos & GitHub', '/gallery/videos/']
    ]},
    {name: 'Members', href: '/members/', links: [
      ['Professor', '/members/professor/'], ['Post-Doc', '/members/post-doc/'],
      ['Graduate Students', '/members/graduate/'], ['Alumni', '/members/alumni/']
    ]},
    {name: 'Publications', href: '/publications-hmc/', links: [
      ['Journal Articles', '/publications-hmc/journal-articles-hmc/'],
      ['Conference Proceedings', '/publications-hmc/conference-proceedings-hmc/'],
      ['Book Chapters', '/publications-hmc/book-chapters-hmc/'], ['Patents', '/publications-hmc/patents-hmc/']
    ]},
    {name: 'Projects', href: '/projects/'}, {name: 'Gallery', href: '/gallery/2026/'},
    {name: 'Contact', href: '/contact/'},
    {name: 'UnicornRacing', href: 'https://hmcl-unist.github.io/unicorn-racing/'}
  ];
  const matches = href => (href.replace(/\/$/, '') || '/') === path;
  const escape = s => s.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const link = ([name, href]) => `<a href="${href}"${matches(href) ? ' aria-current="page"' : ''}>${name}</a>`;
  const current = sections.find(s => s.links?.some(([,url]) => matches(url)) || (s.href.startsWith('/') && path.startsWith(s.href.split('/').slice(0,2).join('/'))));
  const header = document.querySelector('#masthead');
  if (header) {
    header.className = 'hmcl-header';
    header.innerHTML = `<a class="hmcl-skip" href="#main">Skip to content</a>
      <div class="hmcl-container hmcl-header-row">
        <a href="/" class="hmcl-brand" aria-label="HMCL home"><img src="/media/2020/lab_Logo.jpg" alt="High-assurance Mobility Control Lab. · UNIST" width="240" height="58"></a>
        <button class="hmcl-menu-button" type="button" aria-controls="hmcl-nav" aria-expanded="false">Menu</button>
        <nav class="hmcl-nav" id="hmcl-nav" aria-label="Main navigation"><ul>${sections.map((s,i) => `<li${s===current?' class="is-current"':''}>${link([s.name,s.href])}${s.links ? `<button class="hmcl-submenu-toggle" type="button" aria-label="${s.name} submenu" aria-expanded="false" aria-controls="hmcl-submenu-${i}"><svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="m3 6 5 5 5-5" stroke="currentColor" stroke-width="1.5"/></svg></button><ul id="hmcl-submenu-${i}" class="hmcl-submenu">${s.links.map(l=>`<li>${link(l)}</li>`).join('')}</ul>`:''}</li>`).join('')}</ul></nav>
      </div>`;
    const button = header.querySelector('.hmcl-menu-button');
    const nav = header.querySelector('.hmcl-nav');
    button.addEventListener('click', () => {
      const open = button.getAttribute('aria-expanded') !== 'true';
      button.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('is-open', open);
    });
    header.querySelectorAll('.hmcl-submenu-toggle').forEach(toggle => {
      toggle.addEventListener('click', () => {
        const open = toggle.getAttribute('aria-expanded') !== 'true';
        toggle.setAttribute('aria-expanded', String(open));
        toggle.parentElement.classList.toggle('is-open', open);
      });
    });
    header.addEventListener('keydown', event => {
      if (event.key !== 'Escape') return;
      header.querySelectorAll('.is-open').forEach(el=>el.classList.remove('is-open'));
      header.querySelectorAll('[aria-expanded]').forEach(el=>el.setAttribute('aria-expanded','false'));
      button.focus();
    });
  }
  const footer = document.querySelector('#colophon');
  if (footer) {
    footer.className = 'hmcl-footer';
    footer.innerHTML = `<div class="hmcl-container"><div class="hmcl-footer-top">
      <div><h2>High-assurance Mobility<br>Control Lab.</h2><p>Department of Mechanical Engineering<br>Ulsan National Institute of Science and Technology</p></div>
      <div><h3>Visit & contact</h3><p>50 UNIST-gil, Ulju-gun<br>Ulsan, Republic of Korea · 44919</p><p><a href="mailto:kwonc@unist.ac.kr">kwonc@unist.ac.kr</a><br><a href="tel:+82522172433">+82 52 217 2433</a></p></div>
      <div><h3>Explore HMCL</h3><p><a href="${official}">Official UNIST website ↗</a></p><p><a href="https://github.com/HMCL-UNIST">Open-source research on GitHub ↗</a></p><p><a href="/gallery/videos/">Research videos</a> · <a href="/members/">Our people</a></p></div>
      </div><div class="hmcl-footer-bottom"><p>© ${new Date().getFullYear()} HMCL · UNIST. All rights reserved.</p><p>Design preview. Approved changes are transferred to the official website.</p></div></div>`;
  }
  const icon = shape => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">${shape}</svg>`;
  const aside = document.createElement('aside');
  aside.className = 'hmcl-profile';
  aside.setAttribute('aria-label','Professor and laboratory information');
  aside.innerHTML = `<a href="/members/professor/" class="hmcl-profile-photo"><img src="/members/professor/media/2019/cheolhyeon-kwon.jpg" alt="Cheolhyeon Kwon" width="300" height="300"></a><div class="hmcl-profile-name"><span>Associate Professor</span><h2>CHEOLHYEON KWON</h2></div><div class="hmcl-profile-details">
    <div><h3>${icon('<path d="M20 13 13 20a2 2 0 0 1-3 0l-7-7V3h10l7 7a2 2 0 0 1 0 3Z"/><circle cx="7.5" cy="7.5" r="1"/>')}Major Research Field</h3><p>Cyber-Physical System (CPS), Intelligent and High Assurance Autonomy, Networked Multi-Agent Systems (MAS), Fault Tolerant Control (FTC)</p></div>
    <div><h3>${icon('<path d="M20 10c0 6-8 11-8 11S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="3"/>')}Lab</h3><p>Bldg. 112 Rm. 806</p></div>
    <div><h3>${icon('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>')}Email</h3><p><a href="mailto:kwonc@unist.ac.kr">kwonc@unist.ac.kr</a></p></div>
    <div><h3>${icon('<path d="m8 3 3 5-3 3a16 16 0 0 0 5 5l3-3 5 3v3a2 2 0 0 1-2 2C10 21 3 14 3 5a2 2 0 0 1 2-2Z"/>')}Contact</h3><p><a href="tel:+82522172433">052-217-2433</a></p></div></div>`;
  if (document.body.classList.contains('hmcl-home')) {
    const main = document.querySelector('#main');
    const shell = document.createElement('div');
    shell.className = 'hmcl-home-layout';
    main.before(shell);
    shell.append(aside, main);
    return;
  }
  const entry = document.querySelector('.entry-content');
  const titleNode = document.querySelector('.entry-title');
  const layout = document.querySelector('.layout-fixed');
  if (!entry || !layout || !titleNode) return;
  const title = titleNode.textContent.trim();
  const banner = document.createElement('section');
  banner.className = 'hmcl-page-banner';
  banner.innerHTML = `<div class="hmcl-container"><h1>${escape(title)}</h1><p><a href="/">Home</a> / ${escape(current?.name || title)}${current?.name !== title ? ' / '+escape(title):''}</p></div>`;
  layout.before(banner);
  layout.classList.add('hmcl-with-sidebar');
  layout.prepend(aside);
  if (path.startsWith('/publications-hmc')) document.body.classList.add('hmcl-publications');
  if (current?.links && (path.startsWith('/publications-hmc') || path.startsWith('/members'))) {
    const tabs = document.createElement('nav');
    tabs.className = 'hmcl-tabs';
    tabs.setAttribute('aria-label', current.name+' pages');
    tabs.innerHTML = current.links.map(link).join('');
    entry.before(tabs);
  }
  if (/^\/members\/(alumni|graduate|post-doc)(\/|$)/.test(path)) {
    const grid = document.createElement('div');
    grid.className = 'hmcl-members-grid';
    for (const row of [...entry.querySelectorAll('.vc_row')]) {
      const photo = row.querySelector('.vc_col-sm-3 img');
      const copy = row.querySelector('.vc_col-sm-6 .wpb_text_column .wpb_wrapper');
      if (photo && copy) {
        const card = document.createElement('article');
        card.className = 'hmcl-member';
        photo.loading = 'lazy';
        card.append(photo);
        const text = document.createElement('div');
        text.className = 'hmcl-member-copy';
        while(copy.firstChild) text.append(copy.firstChild);
        card.append(text);
        grid.append(card);
        row.remove();
      } else {
        const heading = row.querySelector('h2');
        if (heading) { grid.append(heading); row.remove(); }
      }
    }
    if (grid.querySelector('.hmcl-member')) entry.prepend(grid);
  }
  if (/^\/gallery\/(20\d{2}|2019-2020)$/.test(path)) {
    document.body.classList.add('hmcl-gallery');
    const grid = document.createElement('div');
    grid.className = 'hmcl-gallery-grid';
    const oldRows = new Set();
    entry.querySelectorAll('.vc_col-sm-3').forEach(column => {
      if (!column.querySelector('a img')) return;
      oldRows.add(column.closest('.vc_row'));
      column.querySelectorAll('img').forEach(img=>{img.loading='lazy';});
      grid.append(column);
    });
    oldRows.forEach(row=>{if (row && !row.querySelector('.wpb_column')) row.remove();});
    const years = document.createElement('nav');
    years.className = 'hmcl-tabs hmcl-gallery-years';
    years.setAttribute('aria-label','Gallery years');
    years.innerHTML = ['2026','2025','2024','2023','2022','2021','2019-2020'].map(year=>link([year,'/gallery/'+year+'/'])).join('');
    if (grid.children.length) {
      entry.prepend(years, grid);
      entry.querySelectorAll('.vc_row').forEach(row=>{if(row.querySelector('.vc_btn3-container')) row.remove();});
    }
  }
})();
