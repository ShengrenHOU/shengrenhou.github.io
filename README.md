# Hou Shengren Public Site

This repository contains the public bilingual website for Hou Shengren. The site is positioned as a public personal profile for an energy technology entrepreneur and researcher, not as an internal company site or an academic-only homepage.

## Purpose and audience

- Present a public profile for readers in academia, industry, media, and collaboration networks.
- Explain current work across electricity markets, AI decision systems, storage and flexibility, and energy digitalization.
- Provide a curated record of public milestones without exposing private or internal information.

## Bilingual structure

The main site pages are maintained in both English and Chinese on the same routes:

- `About`
- `News`
- `Research`
- `Publications`
- `CV`
- `Contact`

## Public-content and privacy rules

- Use only public-safe summaries.
- Do not publish phone numbers, detailed addresses, birth dates, private identifiers, or internal company operating details.
- Do not publish financing structure, equity terms, customer specifics, contracts, hiring plans, internal meeting notes, or government-relations details.
- Treat the `News` page as a manually curated public milestones page, not as an internal changelog.

## Updating the site

- Update the page content under `_pages/`.
- Keep `News` reverse-chronological and public-safe.
- Run `py -3 scripts/verify_public_site.py` after content changes.
- If Ruby and Bundler are available, build locally with `bundle exec jekyll build`.
- If local Ruby is unavailable, rely on the GitHub Actions Pages workflow for build verification.

## Publishing model

This repository is treated as an organization-owned GitHub Pages project site.

- Target canonical public URL: `https://energyquantresearch.github.io/ShengrenHou.github.io/`
- Repository path: `EnergyQuantResearch/ShengrenHou.github.io`
- Default branch: `master`
- No custom domain is configured in this round.

## Verified publishing reality on March 14, 2026

- `git remote -v` points to `EnergyQuantResearch/ShengrenHou.github.io`.
- The current checked-out branch is `master`.
- No `CNAME` file exists in the repository.
- Before this governance pass, `_config.yml` did not define `url`, `baseurl`, or `repository`.
- `https://shengrenhou.github.io` returned HTTP `404` when checked from this environment on March 14, 2026.
- `https://energyquantresearch.github.io/ShengrenHou.github.io/` did not return a usable response from this environment before the Pages configuration was updated, so the old personal domain must not be treated as canonical.

## Deployment notes

- GitHub Actions builds the Jekyll site and deploys the generated `_site` output to GitHub Pages.
- The workflow is configured for organization-owned project Pages hosting rather than personal-username Pages hosting.
