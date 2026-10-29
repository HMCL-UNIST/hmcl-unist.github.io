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

## Interaction

Simple white sticky header with the actual HMCL logo and black navigation,
matching the user's reference. Design-preview notice and official link live in the footer.
Desktop navigation supports pointer hover, keyboard focus and submenu toggles.
Mobile uses an explicit Menu button and separate submenu buttons. Escape closes
open navigation. Visible focus outlines and reduced-motion rules are included.

## Implementation and CMS transfer

`assets/css/site-preview.css` owns shared styling. `assets/js/site-preview.js`
owns the preview shell and presents original member/gallery markup as cards.
The static citations, names and source media remain in their original pages.
All existing HTML entry points load this theme; `_site` is generated output and
is not edited. No framework, package installation, or build step is introduced.

For JiniWorks transfer, map the header/footer, sub-template, main-template and
body components to CMS equivalents. Scope styles to HMC; do not paste an entire
standalone document into one CMS content block. Publish there only after review.

## Preview operation

Run `python3 -m http.server 8765 --bind 127.0.0.1` at the repository root.
Check the home, publications, alumni and gallery at desktop and mobile widths.
GitHub preview pages carry `noindex, nofollow`; the separate UnicornRacing site
is not modified. The UNIST CMS is never changed by a Git push.
