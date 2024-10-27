---
title: "The general framework for few-shot learning by kernel HyperNetworks"
authors:
- Marcin Sendera
- Marcin Przewięźlikowski
- Jan Miksa
- Mateusz Rajski
- admin
- Maciej Zięba
- Jacek Tabor
- Przemysław Spurek
author_notes:
- "Equal contribution"
- "Equal contribution"
date: "2023-05-23"
doi: "10.1007/s00138-023-01403-4"

# Schedule page publish date (NOT publication's date).
publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Machine Vision and Applications*"
publication_short: ""

abstract: 'Few-shot models aim at making predictions using a minimal number of labeled examples from a given task. The main challenge in this area is the one-shot setting, where only one element represents each class. We propose the general framework for few-shot learning via kernel HyperNetworks—the fusion of kernels and hypernetwork paradigm. Firstly, we introduce the classical realization of this framework, dubbed HyperShot. Compared to reference approaches that apply a gradient-based adjustment of the parameters, our models aim to switch the classification module parameters depending on the task’s embedding. In practice, we utilize a hypernetwork, which takes the aggregated information from support data and returns the classifier’s parameters handcrafted for the considered problem. Moreover, we introduce the kernel-based representation of the support examples delivered to hypernetwork to create the parameters of the classification module. Consequently, we rely on relations between the support examples’ embeddings instead of the backbone models’ direct feature values. Thanks to this approach, our model can adapt to highly different tasks. While such a method obtains very good results, it is limited by typical problems such as poorly quantified uncertainty due to limited data size. We further show that incorporating Bayesian neural networks into our general framework, an approach we call BayesHyperShot, solves this issue.'

# Summary. An optional shortened abstract.
summary: 'The general framework for few-shot learning via kernel HyperNetworks—the fusion of kernels and hypernetwork paradigm is proposed, and it is shown that incorporating Bayesian neural networks into the general framework, an approach called BayesHyperShot, solves this issue.'

tags:
- few-shot learning
- meta learning
- computer vision

featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://link.springer.com/content/pdf/10.1007/s00138-023-01403-4.pdf
url_code: 'https://github.com/gmum/few-shot-hypernets-public'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: ''
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
---
