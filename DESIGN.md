# HMCL preview design

## Authority and scope

User-approved reference: the migrated UNIST HMC site, viewed October 29, 2026.
This repository is the test environment and source archive. JiniWorks remains
the official publishing platform. The design is adapted to real HMCL content,
not to the reference site's unrelated introduction or stock laboratory images.

## Implemented system

- Navy `#071e53` for navigation, headings, the page title band, and footer.
- Teal `#087d80` for links and the main heading emphasis. White content panels
  on a pale `#f3f6fa` background. Shared line color `#dce3ec`.
- Arial with Korean sans-serif fallbacks, selected for the institutional
  reference. Headings use a compact bold hierarchy; citations remain readable
  paragraphs with year headings and DOI links.
- A 1,400px maximum container, 48px desktop outside margins, 20px mobile
  margins. Breakpoints at 1,100px and 700px.
- Existing HMCL logo and actual research, racing, and lab photos. No generated
  photographs, institutional claims, metrics, or testimonials.
- Home: a dominant, uncropped lab group photo with a navy introduction panel;
  the reference's campus Laboratory card and navy Research Topic card beneath.
  Mobile puts the group photo first. Further sections include research topics, recent
  publications, lab members, gallery, recruitment, and the existing racing video.
- Subpages: shared title band, professor profile sidebar on large screens,
  white main panel, navigation tabs for members and publication categories.
- Alumni and other member rows become two-column cards on desktop, one column
  on mobile. Gallery indexes use four columns on desktop and two on mobile.
- Home and subpage professor panels follow the CMS structure: portrait, name,
  Major Research Field, Lab (Bldg. 112 Rm. 806), Email and Contact. They remain
  sticky below the header, stop before the footer, and can scroll internally on
  short screens. Compact screens hide the panel; Professor and Contact remain
  available in navigation. The home group photograph appears only in the hero;
  the repeated group-photo section and its replacement racing promotion have
  been removed at the user's request.

## Interaction

Simple white sticky header with the actual HMCL logo and black navigation,
matching the user's reference. Design-preview notice and official link live in the footer.
Desktop navigation supports pointer hover, keyboard focus and submenu toggles.
Mobile uses an explicit Menu button and separate submenu buttons. Escape closes
open navigation. Visible focus outlines and reduced-motion rules are included.

## Implementation and CMS transfer

### Research overview, members and motion

Research Overview reuses the existing CPS research-purpose paragraphs and
the original CPS control-methods diagram, with existing AD/AF research-topic
headings and photographs. Do not invent a new research narrative, sequence or
framework: the user explicitly requires existing descriptions to be reused.
Graduate membership follows the official CMS AD and AF pages checked 2026-10-29:
AD 11, AF 10. Email identifiers distinguish the two Sanghun Lee entries.
Member photos occupy their own rounded image area on white, without a gray
column continuing below the photograph. Original biography content is preserved.

CMS transfer must include these interaction behaviors: linked photographs zoom
2.5% on hover and 4% while pressed; buttons show a brief pressed state; member,
gallery and research lists enter once as they reach the viewport (450ms,
70ms stagger capped at 140ms). There is no looping or scroll hijacking.
IntersectionObserver and Web Animations implement this without dependencies.
Content stays visible if JavaScript fails. Reduced-motion disables spatial
effects, and changing the preference cancels active entrance animations.
Port the behavior to CMS components or its animation settings and verify both
desktop and mobile there; copying static HTML alone is insufficient.

`assets/css/site-preview.css` owns shared styling. `assets/js/site-preview.js`
owns the preview shell and presents original member/gallery markup as cards.
The static citations, names and source media remain in their original pages.
All existing HTML entry points load this theme; `_site` is generated output and
is not edited. No framework, package installation, or build step is introduced.

For JiniWorks transfer, map the header/footer, sub-template, main-template and
body components to CMS equivalents. Scope styles to HMC; do not paste an entire
standalone document into one CMS content block. Publish there only after review.

## Preview operation

## Official CMS application — 2026-10-29

At the user's explicit request, the approved home layout, HMCL logo, original-
content Research Overview, member-photo whitespace fixes and motion were saved
through JiniWorks. The native professor panel and AD/AF records were retained.
See `cms-transfer/README.md` for the applied source, original backup location,
CMS routes and the current dependency on public GitHub image URLs.

## Preview operation

Run `python3 -m http.server 8765 --bind 127.0.0.1` at the repository root.
Check the home, publications, alumni and gallery at desktop and mobile widths.
GitHub preview pages carry `noindex, nofollow`; the separate UnicornRacing site
is not modified. The UNIST CMS is never changed by a Git push.
