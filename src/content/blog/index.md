---
layout: layouts/page.njk
title: Blog
description: "Technical articles, research reflections, and science communication from Daniel Castillo Castro"
---

## Latest Articles

Welcome to my blog! Here I share technical notes, research insights, science communication pieces, and reflections on academia.

{% for post in collections.posts %}
{% include "components/blog-card.njk" %}
{% endfor %}

## Blog Categories

- **Technical Notes** — Code tutorials, methods, and how-tos
- **Research Reflections** — Insights and perspectives on scientific work
- **Science Communication** — Explainers on complex topics
- **Career & Academia** — PhD life, postdoc tips, and career advice

## Stay Updated

- [RSS Feed](/blog/feed.xml) — Subscribe to new posts
- [GitHub](https://github.com/Dacastillo) — Follow my code projects

---

**Want to contribute or suggest a topic?** [Get in touch](/contact/)
