from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def ensure_contains(text: str, needle: str, failures: list[str], label: str) -> None:
    if needle not in text:
        failures.append(f"{label}: missing `{needle}`")


def ensure_not_contains(text: str, needle: str, failures: list[str], label: str) -> None:
    if needle in text:
        failures.append(f"{label}: still contains `{needle}`")


def ensure_exists(relative_path: str, failures: list[str]) -> None:
    if not (ROOT / relative_path).exists():
        failures.append(f"{relative_path}: expected file to exist")


def ensure_missing(relative_path: str, failures: list[str]) -> None:
    if (ROOT / relative_path).exists():
        failures.append(f"{relative_path}: expected file to be removed")


def main() -> int:
    failures: list[str] = []

    config = read_text("_config.yml")
    for needle in [
        'url: "https://shengrenhou.github.io"',
        'baseurl: ""',
        'repository: "ShengrenHOU/shengrenhou.github.io"',
        'locale: "en_US"',
        'title_separator: "|"',
        'og_image                 : "profile_hou.jpg"',
    ]:
        ensure_contains(config, needle, failures, "_config.yml")
    ensure_not_contains(config, "https://energyquantresearch.github.io", failures, "_config.yml")

    nav = read_text("_data/navigation.yml")
    titles = re.findall(r'title:\s*"([^"]+)"', nav)
    expected_titles = ["About", "News", "Research", "Publications", "CV", "Contact"]
    if titles[: len(expected_titles)] != expected_titles:
        failures.append(
            f"_data/navigation.yml: expected leading nav order {expected_titles}, got {titles[:len(expected_titles)]}"
        )

    for relative_path in [
        "_layouts/home-founder.html",
        "_layouts/single-clean.html",
        "_sass/_founder-site.scss",
        "assets/js/lang-toggle.js",
        "_pages/publications.md",
    ]:
        ensure_exists(relative_path, failures)
    ensure_missing("_pages/publications.html", failures)

    file_checks = {
        "_includes/masthead.html": ["site-language-switcher", 'data-lang-option="en"', 'data-lang-option="zh"'],
        "_includes/scripts.html": ["lang-toggle.js"],
        "_includes/head/custom.html": ["localStorage", "navigator.language", "data-site-lang"],
        "_includes/seo.html": ["page.seo_title", 'meta name="description"', "seo_site_name", '"sameAs"'],
        "assets/css/main.scss": ['@import "founder-site";'],
        "assets/js/lang-toggle.js": ["localStorage", "navigator.language", "data-site-lang", "data-lang-option"],
        "_sass/_founder-site.scss": ["justify-content: center;", '[data-site-lang="zh"] .founder-hero h1'],
    }
    for relative_path, markers in file_checks.items():
        if not (ROOT / relative_path).exists():
            continue
        file_text = read_text(relative_path)
        for marker in markers:
            ensure_contains(file_text, marker, failures, relative_path)

    page_expectations = {
        "_pages/about.md": {
            "layout": "layout: home-founder",
            "expected": [
                'excerpt: "Founder website of Hou Shengren',
                'data-lang="en"',
                'data-lang="zh"',
                "Beijing Reneng Technology, TU Delft, and Northpool.",
                "founder-hero",
                "current-focus",
                "selected-work",
                "research-foundations",
                "selected-publications",
                "recent-news",
                "contact-cta",
            ],
        },
        "_pages/news.md": {
            "layout": "layout: single-clean",
            "expected": [
                'excerpt: "Selected public milestones',
                'data-lang="en"',
                'data-lang="zh"',
                "news-timeline",
                "2026",
                "2025",
                "Completed an angel financing round in December 2025.",
                "2025 年 12 月完成天使轮融资。",
            ],
        },
        "_pages/research.md": {
            "layout": "layout: single-clean",
            "expected": ['excerpt: "Research themes spanning', 'data-lang="en"', 'data-lang="zh"', "research-grid", "Research Themes", "研究主题"],
        },
        "_pages/publications.md": {
            "layout": "layout: single-clean",
            "expected": ['excerpt: "Selected publications in energy systems', 'data-lang="en"', 'data-lang="zh"', "publication-list", "Google Scholar", "代表性论文"],
        },
        "_pages/cv.md": {
            "layout": "layout: single-clean",
            "expected": [
                'excerpt: "Public-profile CV of Hou Shengren',
                'data-lang="en"',
                'data-lang="zh"',
                "experience-list",
                "Selected Experience",
                "经历精选",
                "CEO, Beijing Reneng Technology",
                "北京任能科技 CEO",
            ],
        },
        "_pages/contact.md": {
            "layout": "layout: single-clean",
            "expected": ['excerpt: "Public contact details and collaboration topics', 'data-lang="en"', 'data-lang="zh"', "contact-methods", "Collaboration", "合作方向"],
        },
    }
    forbidden_page_strings = [
        "MM/YYYY",
        "Placeholder",
        "placeholder",
        "your-linkedin-profile",
        "formspree",
        "This contact form is currently for demonstration purposes only.",
        "Mekelweg 4",
        "2628 CD Delft",
        "+31-",
        "1997-03",
        "## English",
        "## 中文",
        "This page records public milestones only.",
        "本页只记录适合公开传播的里程碑信息",
        "OTC Flow",
        "Energy Quant CEO",
        "Launched the renewed founder-and-researcher public website.",
        "发布新版 Founder + Researcher 个人公共网站。",
    ]

    for relative_path, expectation in page_expectations.items():
        if not (ROOT / relative_path).exists():
            continue
        page_text = read_text(relative_path)
        ensure_contains(page_text, expectation["layout"], failures, relative_path)
        ensure_not_contains(page_text, "author_profile: true", failures, relative_path)
        for marker in expectation["expected"]:
            ensure_contains(page_text, marker, failures, relative_path)
        for forbidden in forbidden_page_strings:
            ensure_not_contains(page_text, forbidden, failures, relative_path)

    readme = read_text("README.md")
    for forbidden in ["Academic Pages", "academicpages.github.io"]:
        ensure_not_contains(readme, forbidden, failures, "README.md")

    authors = read_text("_data/authors.yml")
    ensure_contains(authors, 'uri         : "https://shengrenhou.github.io/"', failures, "_data/authors.yml")
    for forbidden in ["Name Name", "http://name.com", "name@name.com"]:
        ensure_not_contains(authors, forbidden, failures, "_data/authors.yml")

    posts_dir = ROOT / "_posts"
    post_files = sorted(path.name for path in posts_dir.glob("*.md"))
    if post_files:
        failures.append(f"_posts: expected no sample posts, found {post_files}")

    if failures:
        print("Founder-site verification failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Founder-site verification passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
