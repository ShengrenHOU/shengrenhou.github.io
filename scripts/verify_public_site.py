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


def main() -> int:
    failures: list[str] = []

    config = read_text("_config.yml")
    ensure_contains(
        config,
        'url: "https://energyquantresearch.github.io"',
        failures,
        "_config.yml",
    )
    ensure_contains(
        config,
        'baseurl: "/ShengrenHou.github.io"',
        failures,
        "_config.yml",
    )
    ensure_contains(
        config,
        'repository: "EnergyQuantResearch/ShengrenHou.github.io"',
        failures,
        "_config.yml",
    )
    ensure_not_contains(config, "https://shengrenhou.github.io", failures, "_config.yml")

    nav = read_text("_data/navigation.yml")
    titles = re.findall(r'title:\s*"([^"]+)"', nav)
    expected_titles = ["About", "News", "Research", "Publications", "CV", "Contact"]
    if titles[: len(expected_titles)] != expected_titles:
        failures.append(
            f"_data/navigation.yml: expected leading nav order {expected_titles}, got {titles[:len(expected_titles)]}"
        )

    page_expectations = {
        "_pages/about.md": ["## English", "## 中文", "Current Focus", "当前关注", "/news/"],
        "_pages/news.md": ["## English", "## 中文", "2026", "2025"],
        "_pages/research.md": ["## English", "## 中文", "Research Themes", "研究主题"],
        "_pages/publications.html": ["## English", "## 中文", "Google Scholar", "Selected Publications"],
        "_pages/cv.md": ["## English", "## 中文", "Selected Experience", "经历精选"],
        "_pages/contact.md": ["## English", "## 中文", "Collaboration", "合作方向"],
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
    ]

    for relative_path, expected_markers in page_expectations.items():
        page_text = read_text(relative_path)
        for marker in expected_markers:
            ensure_contains(page_text, marker, failures, relative_path)
        for forbidden in forbidden_page_strings:
            ensure_not_contains(page_text, forbidden, failures, relative_path)

    publications_page = read_text("_pages/publications.html")
    ensure_not_contains(
        publications_page,
        'http-equiv="refresh"',
        failures,
        "_pages/publications.html",
    )

    readme = read_text("README.md")
    for forbidden in ["Academic Pages", "academicpages.github.io"]:
        ensure_not_contains(readme, forbidden, failures, "README.md")

    authors = read_text("_data/authors.yml")
    for forbidden in ["Name Name", "http://name.com", "name@name.com"]:
        ensure_not_contains(authors, forbidden, failures, "_data/authors.yml")

    posts_dir = ROOT / "_posts"
    post_files = sorted(path.name for path in posts_dir.glob("*.md"))
    if post_files:
        failures.append(f"_posts: expected no sample posts, found {post_files}")

    if failures:
        print("Public-site governance verification failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Public-site governance verification passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
