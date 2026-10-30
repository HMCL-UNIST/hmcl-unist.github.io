# HMCL website design

The user requested a complete return to the original GitHub layout on
October 30, 2026, following professor feedback. GitHub Pages is the main site.
Commit `f7d86e6` is the pre-redesign reference: original serif typography,
navigation, homepage group photo, research pages, member rows and gallery.

All public pages have stopped loading `assets/css/site-preview.css` and
`assets/js/site-preview.js`; the experimental preview's noindex tags are removed.
Those assets remain as historical source for the separately maintained CMS.
Do not reactivate them on GitHub.

Content updates survive the layout restoration: publication metadata, DOI links,
year headings, citation numbering, alumni categories, AD/AF membership and the
2026 UNIST Creative Design Festival album. Graduate groups use original member
rows under AD Group and AF Group headings. Gallery cards retain four-column
legacy rows, with the latest album first.

Research descriptions must come from existing lab content. Do not invent a new
research framework or use an aircraft architecture diagram as a general CPS
illustration. The old GitHub homepage has no LABORATORY-to-members card.

CMS changes are independent. Its Members card now accurately labels its
graduate-student destination and uses a lab members photograph; CPS uses the
existing security/safety/performance diagram. Journal-list links, professor
profile links, the department link and the YouTube channel are labeled and
connected to their corresponding destinations. See `cms-transfer/README.md`.

Serve locally with `python3 -m http.server 8765 --bind 127.0.0.1` and verify
desktop/mobile pages. Preserve the separate UnicornRacing site.
