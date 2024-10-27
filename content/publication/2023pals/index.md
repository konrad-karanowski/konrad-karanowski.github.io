---
title: 'PALS: Personalized Active Learning for Subjective Tasks in NLP'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
- Kamil Kanclerz
- admin
- Julita Bielaniewicz
- Marcin Gruza
- Piotr Miłkowski
- Jan Kocoń
- Przemysław Kazienko

# Author notes (optional)

date: '2023-12-06'
doi: '10.18653/v1/2023.emnlp-main.823'

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *Conference on Empirical Methods in Natural Language Processing 2023*
publication_short: In *EMNLP2023*

abstract: 'For subjective NLP problems, such as classification of hate speech, aggression, or emotions, personalized solutions can be exploited. Then, the learned models infer about the perception of the content independently for each reader. To acquire training data, texts are commonly randomly assigned to users for annotation, which is expensive and highly inefficient. Therefore, for the first time, we suggest applying an active learning paradigm in a personalized context to better learn individual preferences. It aims to alleviate the labeling effort by selecting more relevant training samples. In this paper, we present novel Personalized Active Learning techniques for Subjective NLP tasks (PALS) to either reduce the cost of the annotation process or to boost the learning effect. Our five new measures allow us to determine the relevance of a text in the context of learning users’ personal preferences. We validated them on three datasets: Wiki discussion texts individually labeled with aggression and toxicity, and on the Unhealthy Conversations dataset. Our PALS techniques outperform random selection even by more than 30%. They can also be used to reduce the number of necessary annotations while maintaining a given quality level. Personalized annotation assignments based on our controversy measure decrease the amount of data needed to just 25%-40% of the initial size.'

# Summary. An optional shortened abstract.
summary: 'Novel Personalized Active Learning techniques for Subjective NLP tasks (PALS) to either reduce the cost of the annotation process or to boost the learning effect are presented.'

tags: 
- NLP
- Personalized NLP
- active learning

# Display this page in the Featured widget?
featured: false


url_pdf: 'https://aclanthology.org/2023.emnlp-main.823.pdf'
url_code: 'https://github.com/CLARIN-PL/personalized-nlp/releases/tag/2023-emnlp'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
---