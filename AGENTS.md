# Repository Guidelines

## Project Structure & Module Organization
This repository is a static website (no application runtime or package manager). Top-level routes such as `index.html`, `research/`, `members/`, `projects/`, and `publications-hmc/` map directly to public pages. Theme assets live under `wp-content/themes/readme/`:
- `css/` for stylesheets
- `js/` for site scripts and vendor plugins
- `images/` and font files for media

Keep route-specific content near its folder (`research/cps/index.html`, etc.) and shared styling/behavior in the theme directories.

## Build, Test, and Development Commands
No build step is required; files are served as-is.
- `python3 -m http.server 8000` from repo root: run a local preview server
- `open http://localhost:8000` (or browser equivalent): verify navigation and assets
- `git status` and `git diff --stat`: review change scope before commit

## Coding Style & Naming Conventions
Use existing formatting in touched files:
- HTML/CSS/JS: 2-space indentation
- Prefer lowercase, hyphenated directory names (for example `autonomous-flight`)
- Keep page filenames as `index.html` within route folders
- Reuse existing theme classes/scripts before adding new ones

Do not introduce new frameworks or bundlers unless explicitly discussed.

## Testing Guidelines
There is no automated test suite in this repo. Validate changes with focused manual checks:
- Load changed pages on local server and confirm no missing CSS/JS/media
- Test desktop and mobile viewport behavior in browser devtools
- For navigation edits, click through affected internal links

Document manual verification steps in the PR description.

## Commit & Pull Request Guidelines
Current history uses short, direct commit messages (`bug fix`, `add media files`). Follow the same concise style, preferably imperative:
- `update research page copy`
- `fix broken gallery image path`

PRs should include:
- Brief summary of changed pages/assets
- Why the change was needed
- Before/after screenshots for visual updates
- Linked issue (if applicable) and manual test notes
