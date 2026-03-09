---
layout: layouts/page.njk
title: Research
description: "Explore research areas, projects, and publications in computational physics, quantum computing, and machine learning"
---

## Research Overview

My research program focuses on developing and applying computational methods to understand and design materials at the atomic scale. By combining quantum mechanics, machine learning, and high-performance computing, I tackle problems ranging from fundamental physics to practical applications.

## Research Pillars

### Multiscale Nanomaterial Modeling

Understanding how properties emerge across length and time scales is crucial for designing advanced materials. I develop methods that bridge quantum mechanical accuracy with mesoscopic simulation capabilities.

**Key applications:**
- Diamond nanoparticles under extreme conditions
- Carbon-based nanomaterials
- Phase transitions in nanostructures

### Quantum Computing for Chemistry

Quantum computers promise to revolutionize our ability to simulate molecular systems. I work on developing efficient quantum algorithms for chemistry applications.

**Focus areas:**
- Variational Quantum Eigensolver (VQE) ansätze optimization
- Gibbs state preparation for finite-temperature properties
- Error mitigation strategies for near-term quantum devices

### Machine Learning Interatomic Potentials (MLIPs)

Traditional force fields lack accuracy, while DFT is computationally expensive. MLIPs offer the best of both worlds: DFT-level accuracy at force-field computational cost.

**Expertise:**
- Active learning workflows for training data generation
- Moment Tensor Potentials (MTP)
- Neural Network Potentials (NNP)
- Gaussian Approximation Potentials (GAP)

### Scientific Data & Bibliometrics

Understanding trends in scientific research helps identify emerging fields and collaboration opportunities. I apply data science methods to analyze scientific literature.

**Current project:**
- Large-scale analysis of AI applications in chemistry research

## Current Projects

{% for project in projects %}
{% include "components/project-card.njk" %}
{% endfor %}

## Publications

{% for publication in publications %}
{% include "components/publication-card.njk" %}
{% endfor %}

## Preprints & Works in Progress

Several manuscripts are currently in preparation. Feel free to reach out if you're interested in any of these topics.

## Collaborations

I welcome collaborations with researchers from academia and industry. My expertise spans:

- Computational materials science
- Quantum algorithm development
- Machine learning for scientific applications
- High-throughput computational screening

**Interested in collaborating?** [Get in touch](/contact/)
