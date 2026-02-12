# HMCL UNIST Website Editing Guide

이 저장소는 정적 사이트입니다. 별도 빌드 없이 HTML/CSS/JS 파일을 직접 수정합니다.

## 1) 로컬 실행
```bash
cd /home/hmcl/hmcl-unist.github.io
python3 -m http.server 8000
```
브라우저에서 `http://localhost:8000` 접속.

## 2) 기본 구조
- 루트 페이지: `index.html`
- 섹션 페이지: `research/`, `members/`, `projects/`, `publications-hmc/`, `gallery/`
- 공통 스타일/스크립트: `wp-content/themes/readme/`, `wp-content/plugins/`, `wp-includes/`
- 페이지별 이미지: 각 페이지 폴더의 `media/<year>/...`

예시:
- `members/graduate/index.html`
- `members/graduate/media/2019/xxx.jpg`

## 3) 기존 페이지 수정 방법
1. 수정할 페이지의 `index.html` 편집
2. 새 이미지가 필요하면 같은 경로의 `media/<year>/`에 파일 추가
3. HTML의 이미지 경로를 해당 파일로 연결

예시:
```html
<img src="/members/graduate/media/2026/new-photo.jpg" alt="new-photo" />
```

## 4) 갤러리 새 게시물 만들기
현재 갤러리 상세는 아래 규칙 사용:
- 경로: `gallery/<year>/<post-slug>/index.html`
- 이미지: `gallery/<year>/<post-slug>/media/<year>/...`

작업 순서:
1. 기존 게시물 폴더 하나 복사
2. 폴더명을 새 slug로 변경
3. `index.html` 제목/본문 수정
4. 이미지 파일 추가 후 `<img>` 경로 교체
5. `gallery/<year>/index.html` 목록에 새 카드(링크/썸네일) 추가

## 5) 체크리스트 (필수)
- 깨진 이미지 없는지 확인
- 내부 링크가 `hmc.unist.ac.kr`로 남아있지 않은지 확인
- 모바일 폭에서도 레이아웃 깨짐 없는지 확인

## 6) 변경 확인 후 커밋
```bash
git status
git add .
git commit -m "update gallery post"
```
PR에는 변경 페이지, 이미지 추가 내역, 수동 점검 결과를 함께 기록하세요.
