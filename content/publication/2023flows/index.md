---
title: 'Modeling Uncertainty in Personalized Emotion Prediction with Normalizing Flows'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
- Piotr Miłkowski
- admin
- Patryk Wielopolski
- Jan Kocoń
- Przemysław Kazienko
- Maciej Zięba
author_notes:
- "Equal contribution"
- "Equal contribution"

# Author notes (optional)

date: '2023-12-04'
doi: '10.1109/ICDMW60847.2023.00103'

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *2023 IEEE International Conference on Data Mining Workshops*
publication_short: In *ICDMW2023*

abstract: 'Designing predictive models for subjective problems in natural language processing (NLP) remains challenging. This is mainly due to its non-deterministic nature and different perceptions of the content by different humans. It may be solved by Personalized Natural Language Processing (PNLP), where the model exploits additional information about the reader to make more accurate predictions. However, current approaches require complete information about the recipients to be straight embedded. Besides, the recent methods focus on deterministic inference or simple frequency-based estimations of the probabilities. In this work, we overcome this limitation by proposing a novel approach to capture the uncertainty of the forecast using conditional Normalizing Flows. This allows us to model complex multimodal distributions and to compare various models using negative log-likelihood (NLL). In addition, the new solution allows for various interpretations of possible reader perception thanks to the available sampling function. We validated our method on three challenging, subjective NLP tasks, including emotion recognition and hate speech. The comparative analysis of generalized and personalized approaches revealed that our personalized solutions significantly outperform the baseline and provide more precise uncertainty estimates. The impact on the text interpretability and uncertainty studies are presented as well. The information brought by the developed methods makes it possible to build hybrid models whose effectiveness surpasses classic solutions. In addition, an analysis and visualization of the probabilities of the given decisions for texts with high entropy of annotations and annotators with mixed views were carried out.'

# Summary. An optional shortened abstract.
summary: 'This work proposes a novel approach to capture the uncertainty of the forecast using conditional Normalizing Flows, which allows us to model complex multimodal distributions and to compare various models using negative log-likelihood (NLL).'

tags: 
- NLP
- Personalized NLP
- Generative models
- probabilistic machine learning

# Display this page in the Featured widget?
featured: true


url_pdf: 'https://arxiv.org/pdf/2312.06034.pdf'
url_code: 'https://github.com/CLARIN-PL/personalized-emotion-prediction-with-normalizing-flows'
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