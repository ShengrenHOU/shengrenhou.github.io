# Essays Feature Design

**Goal:** Add a dedicated public writing space for essays about AI, power markets, entrepreneurship, and life, while keeping the site primarily a founder-and-researcher profile rather than turning it into a generic blog.

## Product Direction

- Add a top-level `Essays` navigation entry.
- Create a dedicated `/essays/` index page.
- Create individual essay pages under a Jekyll collection rather than `_posts`.
- Surface recent featured essays on the homepage before `Recent News`.
- Keep `News` for objective milestones and `Essays` for views, judgment, reflection, and personal writing.

## Content Model

Each essay should carry:

- Chinese title
- English subtitle or short English summary
- Date
- Tags such as `AI`, `Power Markets`, `Life`
- Chinese main body
- English abstract
- Optional `featured: true` for homepage surfacing

## UX Rules

- Essays are Chinese-first, with an English subtitle and English abstract.
- The site-wide language toggle still controls surrounding interface text, but essays remain Chinese-main by design.
- The essays index should look like a curated ideas page rather than a chronological blog archive.
- The homepage should only surface the latest featured essays, not every essay.

## Scope

This round includes:

- `Essays` navigation item
- `_essays/` collection
- `/essays/` index page
- Single-essay layout
- Homepage `Selected Essays` section
- One seed essay based on the approved sample text

This round does not include:

- Comments
- Search
- Tag landing pages
- Pagination
- Dedicated cover-image system
