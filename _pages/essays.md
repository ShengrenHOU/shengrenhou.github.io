---
layout: single-clean
title: "Essays"
excerpt: "Selected essays and reflections by Hou Shengren on AI, power markets, entrepreneurship, and life."
description: "Selected essays and reflections by Hou Shengren on AI, power markets, entrepreneurship, and life."
permalink: /essays/
---

{% assign essays = site.essays | sort: "date" | reverse %}

<div class="lang-block" data-lang="en">
  <div class="page-panel">
    <div class="section-heading">
      <p class="section-kicker">Essays</p>
      <h2>Selected Essays</h2>
      <p>A Chinese-first collection of reflections on AI, power markets, entrepreneurship, and life, with English subtitles and abstracts.</p>
    </div>
  </div>

  <div class="page-grid essay-index">
    {% for essay in essays %}
    <article class="page-card essay-card">
      <p class="essay-card__date">{{ essay.date | date: "%Y-%m-%d" }}</p>
      <h3><a href="{{ essay.url | relative_url }}">{{ essay.title_zh | default: essay.title }}</a></h3>
      <p class="essay-card__subtitle">{{ essay.subtitle }}</p>
      <p class="essay-card__meta">{{ essay.tags | join: " · " }}</p>
      <p class="essay-card__excerpt">{{ essay.excerpt }}</p>
      <a class="page-link-chip" href="{{ essay.url | relative_url }}">Read Essay</a>
    </article>
    {% endfor %}
  </div>
</div>

<div class="lang-block" data-lang="zh">
  <div class="page-panel">
    <div class="section-heading">
      <p class="section-kicker">随笔</p>
      <h2>随笔</h2>
      <p>这里记录关于 AI、电力市场、创业与人生的长期思考。中文为主写作，附英文副标题与英文摘要。</p>
    </div>
  </div>

  <div class="page-grid essay-index">
    {% for essay in essays %}
    <article class="page-card essay-card">
      <p class="essay-card__date">{{ essay.date | date: "%Y-%m-%d" }}</p>
      <h3><a href="{{ essay.url | relative_url }}">{{ essay.title_zh | default: essay.title }}</a></h3>
      <p class="essay-card__subtitle">{{ essay.subtitle }}</p>
      <p class="essay-card__meta">{{ essay.tags | join: " · " }}</p>
      <p class="essay-card__excerpt">{{ essay.excerpt }}</p>
      <a class="page-link-chip" href="{{ essay.url | relative_url }}">阅读随笔</a>
    </article>
    {% endfor %}
  </div>
</div>
