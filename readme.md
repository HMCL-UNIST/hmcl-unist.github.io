# HMCL UNIST Website Editing Guide

이 저장소는 정적 사이트입니다. 빌드 도구 없이 HTML/CSS/JS를 직접 수정해 배포합니다.

## 1) 프로젝트 구조
- 루트 페이지: `index.html`
- 섹션 페이지: `research/`, `members/`, `projects/`, `publications-hmc/`, `gallery/`
- 공통 자산:
  - `wp-content/themes/readme/` (테마 CSS/JS/이미지/폰트)
  - `wp-content/plugins/`, `wp-includes/` (플러그인/공용 스크립트)
- 페이지별 이미지: 각 페이지 폴더의 `media/<year>/...`

예시:
- 페이지: `members/graduate/index.html`
- 이미지: `members/graduate/media/2019/xxx.jpg`

## 2) 로컬 실행 및 테스트
```bash
cd /home/hmcl/hmcl-unist.github.io
python3 -m http.server 8000
```
브라우저에서 `http://localhost:8000` 접속. 

필수 점검:
1. 수정한 페이지가 정상 렌더링되는지
2. 이미지/CSS/JS 404가 없는지 (브라우저 DevTools Network)
3. 모바일 뷰(Responsive)에서 레이아웃 깨짐이 없는지
4. 상단 메뉴/내부 링크 이동이 정상인지

## 3) 페이지 수정 방법
1. 해당 폴더의 `index.html` 수정
2. 이미지 추가 시 같은 페이지의 `media/<year>/`에 파일 저장
3. HTML 경로 연결

예시:
```html
<img src="/members/graduate/media/2026/new-photo.jpg" alt="new-photo" />
```

## 4) 갤러리 게시물 추가
규칙:
- 게시물 경로: `gallery/<year>/<post-slug>/index.html`
- 게시물 이미지: `gallery/<year>/<post-slug>/media/<year>/...`

절차:
1. 기존 게시물 폴더 복사
2. 폴더명(slug) 변경
3. `index.html`의 제목/본문/이미지 경로 수정
4. `gallery/<year>/index.html`에 새 카드(링크 + 썸네일) 추가

## 5) Git 커밋/푸시
현재 기본 브랜치는 `master`입니다.

```bash
git status
git add .
git commit -m "update gallery post"
git push origin master
```

## 6) GitHub 인증 문제 해결 (중요)
GitHub는 비밀번호 push를 지원하지 않습니다. `PAT` 사용 필요.

- `403 Permission denied`가 뜨면:
1. 원격 확인: `git remote -v`
2. 자격 삭제:
```bash
printf "protocol=https\nhost=github.com\n" | git credential reject
```
3. `repo` 권한 PAT로 재인증 후 `git push origin master`
4. 조직 계정이면 PAT에 `Configure SSO` 승인

## 7) GitHub Pages 반영 확인
1. 저장소 `Settings > Pages`
2. `Source: Deploy from a branch`
3. `Branch: master`, Folder: `/(root)`
4. 저장 후 `Actions`에서 배포 성공(초록 체크) 확인
5. 접속: `https://hmcl-unist.github.io/`
