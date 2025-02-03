---
title: 'HyperShot: Few-Shot Learning by Kernel HyperNetworks'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
- Marcin Sendera
- Marcin Przewięźlikowski
- admin
- Maciej Zięba
- Jacek Tabor
- Przemysław Spurek

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'

date: '2022-03-21'
doi: '10.1109/WACV56688.2023.00250'

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *IEEE Workshop/Winter Conference on Applications of Computer Vision 2022*
publication_short: In *WACV2022*

abstract: Few-shot models aim at making predictions using a minimal number of labeled examples from a given task. The main challenge in this area is the one-shot setting where only one element represents each class. We propose HyperShot - the fusion of kernels and hypernetwork paradigm. Compared to reference approaches that apply a gradient-based adjustment of the parameters, our model aims to switch the classification module parameters depending on the task’s embedding. In practice, we utilize a hypernetwork, which takes the aggregated information from support data and returns the classifier’s parameters handcrafted for the considered problem. Moreover, we introduce the kernel-based representation of the support examples delivered to hypernetwork to create the parameters of the classification module. Consequently, we rely on relations between embeddings of the support examples instead of direct feature values provided by the backbone models. Thanks to this approach, our model can adapt to highly different tasks.

# Summary. An optional shortened abstract.
summary: The proposed HyperShot - the fusion of kernels and hypernetwork paradigm aims to switch the classification module parameters depending on the task’s embedding, and relies on relations between embeddings of the support examples instead of direct feature values provided by the backbone models.

tags: 
- few-shot learning
- meta learning
- computer vision

# Display this page in the Featured widget?
featured: true


url_pdf: 'https://openaccess.thecvf.com/content/WACV2023/papers/Sendera_HyperShot_Few-Shot_Learning_by_Kernel_HyperNetworks_WACV_2023_paper.pdf'
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
  focal_point: ''
  preview_only: false
---