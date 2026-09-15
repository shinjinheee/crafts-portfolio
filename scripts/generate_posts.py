#!/usr/bin/env python3
"""One-off generator for builds/*/index.html and archives/*/index.html detail pages.
Run once from the project root: python3 scripts/generate_posts.py
Not linked from the site; kept only so the page set can be regenerated if content changes.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV_ICONS = '''    <a href="mailto:hello@example.com" aria-label="Email">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>
    </a>
    <span class="icon-divider"></span>
    <a href="#" data-search-trigger aria-label="Search">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
    </a>'''

def page(title, description, active, back_href, back_label, eyebrow, post_title,
         body_html, nav_prev, nav_next, root_prefix="../../"):
    r = root_prefix
    nav_links = f'''    <a href="{r}index.html"{' class="active"' if active == "index" else ""}>Index</a>
    <a href="{r}crafts.html"{' class="active"' if active == "crafts" else ""}>Pixels</a>
    <a href="{r}archives.html"{' class="active"' if active == "archives" else ""}>Archive</a>'''

    nav_items = ""
    if nav_prev:
        nav_items += f'''      <li><a href="{nav_prev[1]}">{nav_prev[0]}</a></li>\n'''
    if nav_next:
        nav_items += f'''      <li><a href="{nav_next[1]}">{nav_next[0]}</a></li>\n'''
    nav_block = ""
    if nav_items:
        nav_block = f'''
<nav class="post-nav" aria-label="Related">
  <ul class="post-nav-list">
{nav_items}  </ul>
</nav>
'''

    return f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<title>{title}</title>
<meta name="description" content="{description}" />
<link rel="icon" href="{r}favicon.svg" type="image/svg+xml" />

<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.css" />

<link rel="stylesheet" href="{r}style.css" />
</head>
<body>

<div class="nav-blur" aria-hidden="true">
  <div class="nav-blur-layer"></div>
  <div class="nav-blur-layer"></div>
  <div class="nav-blur-layer"></div>
  <div class="nav-blur-layer"></div>
  <div class="nav-blur-layer"></div>
</div>
<nav class="pill-nav" aria-label="Primary">
  <div class="pill-nav-inner">
{nav_links}
  </div>
  <div class="pill-nav-icons">
{NAV_ICONS}
  </div>
</nav>

<div class="search-overlay" id="searchOverlay">
  <div class="search-scrim"></div>
  <div class="search-box" role="dialog" aria-modal="true" aria-label="Search">
    <div class="search-panel">
      <div class="search-input-row">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
        <input type="text" id="searchInput" class="search-input" placeholder="검색어 입력" autocomplete="off" spellcheck="false" />
      </div>
      <ul class="search-results" id="searchResults" hidden></ul>
    </div>
  </div>
</div>

<article class="post">
  <header class="post-header">
    <h1 class="post-title">{post_title}</h1>
    <p class="post-eyebrow">{eyebrow}</p>
  </header>
  <div class="post-divider"></div>
  <div class="post-body">
{body_html}
  </div>
  <p class="post-endnote">이 페이지는 플레이스홀더 콘텐츠입니다. 실제 프로젝트/글 내용으로 교체해 사용하세요.</p>
</article>
{nav_block}
<footer class="site-footer">
  <span>© 2026</span>
  <div class="footer-links">
    <a href="https://instagram.com" target="_blank" rel="noopener">Instagram</a>
    <a href="https://linkedin.com" target="_blank" rel="noopener">Linkedin</a>
    <a href="#" >Resume</a>
  </div>
</footer>

<script src="{r}search-data.js"></script>
<script src="{r}script.js"></script>
</body>
</html>
'''

BUILDS = [
    {
        "slug": "flow-mobile-design-system",
        "title": "Flow Mobile Design System",
        "eyebrow": "Design System · Flow team, Product Designer · 2022. 3 ~ Present",
        "paragraphs": [
            "Flow Mobile Design System(이하 'FMS')은 Flow 팀에서 새롭게 구성한 모바일 전용 디자인 시스템입니다. 기존 웹 시스템과는 다른 제약과 조합 방식을 갖도록 설계했습니다.",
            "모바일 환경에서는 다뤄야 할 화면이 많고 인력은 제한적이었기 때문에, 미리 정의된 조합을 최대한 활용해서 빠르게 화면을 구성할 수 있는 방향을 택했습니다.",
        ],
        "headings": [
            ("파운데이션", "색상, 타이포그래피, 아이콘 등 기본 토큰을 먼저 정리하고, 이후 컴포넌트들이 이 토큰을 기준으로 일관된 형태를 유지하도록 설계했습니다."),
            ("주요 컴포넌트", "리스트, 인풋, 모달 등 사용 빈도가 높은 컴포넌트부터 순서대로 정의했고, 각 컴포넌트는 실제 화면에서 바로 조합해 쓸 수 있는 형태로 제공했습니다."),
        ],
    },
    {
        "slug": "flow-product-feature",
        "title": "Flow Product Feature Design",
        "eyebrow": "Product Design · Flow team, Product Designer · 2021. 6 ~ 2022. 3",
        "paragraphs": [
            "Flow 제품의 여러 도메인 기능을 설계하며 팀 내 디자인 표준을 맞추는 역할을 함께 담당했습니다.",
            "기능 단위로 빠르게 검증하고 반복하는 프로세스를 통해 짧은 주기로 여러 기능을 출시했습니다.",
        ],
        "headings": [
            ("작업 방식", "매 스프린트마다 우선순위가 높은 기능을 골라 빠르게 프로토타입을 만들고, 실제 사용자 피드백을 반영해 다듬는 방식으로 진행했습니다."),
        ],
    },
    {
        "slug": "flow-design-system",
        "title": "Flow Design System",
        "eyebrow": "Design System · Flow team, Product Designer · 2020. 11 ~ 2021. 6",
        "paragraphs": [
            "Flow의 첫 웹 디자인 시스템을 구축한 프로젝트입니다. 팀 전체가 공통으로 사용할 수 있는 컴포넌트와 가이드를 정리했습니다.",
            "초기 단계였기 때문에 확장성보다는 일관성을 먼저 확보하는 데 집중했습니다.",
        ],
        "headings": [
            ("컴포넌트 정리", "여러 화면에서 제각각 쓰이던 버튼, 인풋, 카드 스타일을 하나로 통합하고, 각 컴포넌트에 사용 가이드를 함께 문서화했습니다."),
        ],
    },
    {
        "slug": "nova-store-service",
        "title": "Nova Store Service Design",
        "eyebrow": "Service Design · Nova Store · 2019. 4 ~ 2020. 10",
        "paragraphs": [
            "Nova Store의 커머스 서비스 전반을 설계한 프로젝트입니다. 상품 탐색부터 결제까지 이어지는 플로우를 새로 정리했습니다.",
            "기존 서비스의 사용성 문제를 개선하는 데 집중했고, 이후 지표 개선으로 이어졌습니다.",
        ],
        "headings": [
            ("탐색과 결제", "상품을 찾는 과정과 결제까지 이어지는 단계를 줄이고, 각 단계에서 이탈이 발생하던 지점을 우선적으로 개선했습니다."),
        ],
    },
]

ARCHIVES = [
    ("year-in-review", "Year in Review", "2025. 12. 20", "#Life, #Retro"),
    ("studio-notes", "Studio Notes", "2025. 8. 4", "#Design, #Note"),
    ("getting-back-to-basics", "Getting Back to Basics", "2025. 3. 18", "#Life, #Note"),
    ("detail-habit", "디테일 다듬는 습관", "2024. 11. 15", "#Design, #Polishing"),
    ("attitude", "어떤 태도에 대하여", "2024. 10. 19", "#Life, #Note"),
    ("refreshing-toolkit", "Refreshing the Toolkit", "2024. 6. 2", "#Design, #Tools"),
    ("new-project", "새로운 프로젝트를 시작하며", "2024. 1. 21", "#Life, #Note"),
    ("2023-wrap", "2023년을 마무리하며", "2023. 12. 31", "#Life, #Retro"),
    ("estimate-time", "작업 시간 가늠해보기", "2023. 7. 15", "#Design, #Process"),
    ("becoming-senior", "On Becoming Senior", "2023. 5. 23", "#Career, #Note"),
    ("late-retrospect", "뒤늦은 회고", "2023. 2. 3", "#Life, #Retro"),
    ("design-feedback", "On Design Feedback", "2022. 8. 19", "#Design, #Process"),
    ("oo-thinking", "Object-Oriented Thinking", "2022. 6. 22", "#Design, #Note"),
    ("design-theme", "디자인 테마에 대하여", "2022. 4. 8", "#Design, #Note"),
    ("writing-start", "글쓰기를 시작하며", "2021. 1. 26", "#Life, #Note"),
    ("after-resignation", "퇴사 후 돌아보기", "2021. 3. 27", "#Career, #Retro"),
]

ARCHIVE_BODY = [
    "이 글은 플레이스홀더 콘텐츠입니다. 실제 글 내용으로 교체하면 됩니다.",
    "제목, 날짜, 태그 형식은 레퍼런스 사이트의 아카이브 글 구조를 참고해서 구성했어요.",
]


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    # ---- Builds ----
    for i, b in enumerate(BUILDS):
        body_html = "\n".join(f"    <p>{p}</p>" for p in b["paragraphs"])
        for h, p in b.get("headings", []):
            body_html += f"\n    <h2>{h}</h2>\n    <p>{p}</p>"

        prev_item = BUILDS[i - 1] if i > 0 else None
        next_item = BUILDS[i + 1] if i < len(BUILDS) - 1 else None
        nav_prev = (prev_item["title"], f"../{prev_item['slug']}/") if prev_item else None
        nav_next = (next_item["title"], f"../{next_item['slug']}/") if next_item else None

        html = page(
            title=f"{b['title']} · jinhee.shin",
            description=b["eyebrow"],
            active="index",
            back_href="../../index.html",
            back_label="Index",
            eyebrow=b["eyebrow"],
            post_title=b["title"],
            body_html=body_html,
            nav_prev=nav_prev,
            nav_next=nav_next,
        )
        write(os.path.join(ROOT, "builds", b["slug"], "index.html"), html)

    # ---- Archives ----
    for i, (slug, title, date, tags) in enumerate(ARCHIVES):
        body_html = "\n".join(f"    <p>{p}</p>" for p in ARCHIVE_BODY)
        eyebrow = f"{tags} · {date}"

        prev_item = ARCHIVES[i - 1] if i > 0 else None
        next_item = ARCHIVES[i + 1] if i < len(ARCHIVES) - 1 else None
        nav_prev = (prev_item[1], f"../{prev_item[0]}/") if prev_item else None
        nav_next = (next_item[1], f"../{next_item[0]}/") if next_item else None

        html = page(
            title=f"{title} · jinhee.shin",
            description=eyebrow,
            active="archives",
            back_href="../../archives.html",
            back_label="Archive",
            eyebrow=eyebrow,
            post_title=title,
            body_html=body_html,
            nav_prev=nav_prev,
            nav_next=nav_next,
        )
        write(os.path.join(ROOT, "archives", slug, "index.html"), html)

    print(f"Generated {len(BUILDS)} build pages and {len(ARCHIVES)} archive pages.")


if __name__ == "__main__":
    main()
