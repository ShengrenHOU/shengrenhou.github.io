# Essays Feature Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a Chinese-first Essays section with a dedicated index page, individual essay pages, homepage highlights, and one initial essay.

**Architecture:** Use a Jekyll collection named `essays` so the feature stays distinct from the old blog/post model. Render the index page through `single-clean`, render individual essays through a dedicated `essay` layout, and reuse the founder visual language with a small set of essay-specific styles. The homepage will query the collection and show up to two featured essays before the news block.

**Tech Stack:** Jekyll collections, Liquid templates, Markdown, SCSS, Python verification script

---

### Task 1: Add failing verification for the Essays feature

**Files:**
- Modify: `E:/科研项目/personal/ShengrenHou.github.io/scripts/verify_public_site.py`

**Step 1: Write the failing test**

Add checks for:

- `_config.yml` contains an `essays` collection
- `_data/navigation.yml` includes `Essays`
- `_pages/essays.md` exists and contains the expected structure
- `_layouts/essay.html` exists
- `_essays/2026-03-17-do-not-wait.md` exists
- homepage contains a `selected-essays` block

**Step 2: Run test to verify it fails**

Run:

```powershell
py -3 scripts/verify_public_site.py
```

Expected: fail because the Essays feature has not been added yet.

### Task 2: Add the collection and navigation

**Files:**
- Modify: `E:/科研项目/personal/ShengrenHou.github.io/_config.yml`
- Modify: `E:/科研项目/personal/ShengrenHou.github.io/_data/navigation.yml`

**Step 1: Implement minimal config**

- Add `essays` to `collections` with public output and permalink
- Add defaults for the essays collection
- Add `Essays` to top navigation

**Step 2: Re-run verification**

Run:

```powershell
py -3 scripts/verify_public_site.py
```

Expected: still fail, but for missing pages/layout/content instead of config/navigation.

### Task 3: Add essay pages and layout

**Files:**
- Create: `E:/科研项目/personal/ShengrenHou.github.io/_layouts/essay.html`
- Create: `E:/科研项目/personal/ShengrenHou.github.io/_pages/essays.md`
- Create: `E:/科研项目/personal/ShengrenHou.github.io/_essays/2026-03-17-do-not-wait.md`
- Modify: `E:/科研项目/personal/ShengrenHou.github.io/_sass/_founder-site.scss`

**Step 1: Implement pages**

- Build the essays index with a bilingual header and essay cards
- Build the essay layout with title, subtitle, metadata, tags, body, English abstract, and previous/next links
- Add styling for essay index cards and single-essay longform reading
- Seed the first essay from the approved draft

**Step 2: Re-run verification**

Run:

```powershell
py -3 scripts/verify_public_site.py
```

Expected: still fail if the homepage has not yet been updated.

### Task 4: Surface essays on the homepage

**Files:**
- Modify: `E:/科研项目/personal/ShengrenHou.github.io/_pages/about.md`

**Step 1: Implement homepage highlights**

- Insert a `Selected Essays / 随笔` block before `Recent News`
- Show up to two featured essays with title, subtitle, date, tags, excerpt, and CTA

**Step 2: Run final verification**

Run:

```powershell
py -3 scripts/verify_public_site.py
git -C E:\科研项目\personal\ShengrenHou.github.io diff --check
```

Expected: both commands pass.

### Task 5: Deploy and confirm the live site

**Files:**
- None

**Step 1: Commit and push**

```powershell
git -C E:\科研项目\personal\ShengrenHou.github.io add .
git -C E:\科研项目\personal\ShengrenHou.github.io commit -m "feat: add essays section"
git -C E:\科研项目\personal\ShengrenHou.github.io push origin master
```

**Step 2: Confirm deployment**

- Wait for the GitHub Pages workflow to succeed
- Check the homepage, `/essays/`, and the first essay page
