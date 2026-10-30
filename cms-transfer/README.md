# HMC CMS transfer — 2026-10-29

Main website: https://hmcl-unist.github.io/
Separately maintained CMS: https://www.unist.ac.kr/hmc/

This folder archives the approved GitHub design adapted to the CMS. The files
were saved through the JiniWorks editor, not deployed by a GitHub push.

- `main-template.jsp`: original CMS header, professor panel and footer imports;
  approved home sections replace the previous stock introduction and widget slots.
- `footer.jsp`: original footer with corrected lab contact details, scoped page
  styles, member-photo fixes, logo replacement, and dependency-free motion.
- `research-overview.html`: existing CPS purpose paragraphs and diagram plus
  existing AD/AF topic names. No new research claims or framework.
- `shared.css` and `shared.js`: extracted reviewable source for the footer additions.
- `source-home.html` and `source-research.html`: frozen CMS inputs, independent
  of GitHub's restored original layout.
- `build_transfer.py`: generates these artifacts from those inputs and the
  locally backed-up CMS originals. Existing CMS URLs are mapped explicitly.

October 30 corrections applied through JiniWorks: replace the misleading
LABORATORY/member card with a Members card and relevant photograph, replace the
UAV architecture thumbnail with the existing CPS diagram, label journal links
accurately, correct the professor-profile button, connect the department URL,
and point YouTube to the existing Unicorn Racing channel. Before-edit backups:
`/home/hmcl/cms-backups/20261030-before-rollback/`.

Research Overview is a new CMS page at `/hmc/research-overview.do`, using the
existing `common.jsp` head and `sub-template.jsp` layout, linked to menu 6185.
The native AD (11) and AF (10) pages retain their original records. The native
professor panel remains visible and sticky on desktop; mobile uses native menus.

Native browser file upload was unavailable because Chrome extension file access
was disabled. No permission settings were changed. New photos and the HMCL logo
therefore reference the existing public GitHub images. Moving those assets into
CMS storage later does not require redesign; replace their source URLs.

Original main template and footer are backed up outside the repository in
`/home/hmcl/cms-backups/20261029/`. Restore the corresponding text through the
CMS editor if rollback is needed. Existing CPS pages were not overwritten.
