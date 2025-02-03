---
# Leave the homepage title empty to use the site title
title: ''
date: 2024-04-15
type: landing

sections:
  - block: about.biography
    id: about
    content:
      title: Biography
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin

    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: '10em'
      # Make the slides full screen within the browser window?
      is_fullscreen: false
      # Automatically transition through slides?
      loop: false
      # Duration of transition between slides (in ms)
      interval: 2000

  - block: experience
    content:
      title: Experience
      # Date format for experience
      #   Refer to https://docs.hugoblox.com/customization/#date-format
      date_format: Jan 2006
      # Experiences.
      #   Add/remove as many `experience` items below as you like.
      #   Required fields are `title`, `company`, and `date_start`.
      #   Leave `date_end` empty if it's your current employer.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: Machine Learning Researcher
          company: Tooploox / eBay Research
          company_url: 'https://tooploox.com/'
          company_logo: tooploox
          location: Wrocław
          date_start: '2024-07-15'
          date_end: ''
          description: |2-
            Responsibilities:
              * Research on the generative models for image recontextualisation
              * Proposing new solutions to generative models
        - title: Machine Learning Specialist
          company: Biocam
          company_url: 'https://www.biocam.ai'
          company_logo: biocam
          location: Wrocław
          date_start: '2023-01-01'
          date_end: '2024-08-01'
          description: |2-
            Responsibilities:
              * Research on the application of generative models in medical images
              * Classification of medical images using deep learning
              * Research into new methods of augmenting medical data
        - title: Machine Learning Researcher
          company: CLARIN ERIC
          company_url: ''
          company_logo: CLARIN-PL_logo
          location: Wrocław
          date_start: '2021-08-01'
          date_end: '2023-02-01'
          description: |2-
            Responsibilities:
              * Development of an automatic speech recognition system in Polish
              * Research on personalised methods in NLP
              * Publication of research results in the field of NLP
        - title: Junior Data Scientist (Intern)
          company: esportsLABgg
          company_url: ''
          company_logo: 
          location: Warsaw (Remote)
          date_start: '2020-09-01'
          date_end: '2021-01-01'
          description: |2-
            Responsibilities:
              * Image classification using deep learning
              * Object detection using deep learning
    design:
      columns: '2'

  - block: accomplishments
    id: awards
    content:
      # Note: `&shy;` is used to add a 'soft' hyphen in a long heading.
      title: 'Awards'
      subtitle:
      # Date format: https://docs.hugoblox.com/customization/#date-format
      date_format: Jan 2006
      # Accomplishments.
      #   Add/remove as many `item` blocks below as you like.
      #   `title`, `organization`, and `date_start` are the required parameters.
      #   Leave other parameters empty if not required.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: Best graduate student at the Faculty of Information and Communication Technology of Wroclaw University of Technology
          # certificate_url: https://www.gov.pl/web/nauka/ogloszenie-wynikow-postepowania-w-sprawie-przyznania-stypendiow-ministra-nauki-dla-studentow-na-rok-akademicki-20232024
          date_end: ''
          date_start: '2024-10-12'
          description:
          icon: wust
          organization: Faculty of Information and Communication Technology of Wroclaw University of Technology
          organization_url: https://wit.pwr.edu.pl/en/
          description: I was named the best graduate student of 2024 at the faculty. 

        - title: Best master thesis defended at the Faculty of Information and Communication Technology of Wroclaw University of Technology
          # certificate_url: https://www.gov.pl/web/nauka/ogloszenie-wynikow-postepowania-w-sprawie-przyznania-stypendiow-ministra-nauki-dla-studentow-na-rok-akademicki-20232024
          date_end: ''
          date_start: '2024-09-01'
          description:
          icon: wust
          organization: Faculty of Information and Communication Technology of Wroclaw University of Technology
          organization_url: https://wit.pwr.edu.pl/en/
          description: My master's thesis, “Diffusion Probabilistic Models For Denoising Micrographs in Cryogenic Electron Microscopy,” was named the best defended 2024 in the faculty. 

        - title: Scholarships of the Minister of Science and Higher Education for Significant Achievements
          # certificate_url: https://www.gov.pl/web/nauka/ogloszenie-wynikow-postepowania-w-sprawie-przyznania-stypendiow-ministra-nauki-dla-studentow-na-rok-akademicki-20232024
          url: https://www.gov.pl/web/nauka/ogloszenie-wynikow-postepowania-w-sprawie-przyznania-stypendiow-ministra-nauki-dla-studentow-na-rok-akademicki-20232024
          date_end: ''
          date_start: '2024-03-25'
          description:
          icon: ministry_of_education
          organization: Ministry of Science and Higher Education of the Republic of Poland
          organization_url: https://www.gov.pl/web/nauka
          description: For my scientific activities, I was awarded a scholarship by the Minister of Science and Higher Education of the Republic of Poland for the best students in the country.
    design:
      columns: '2'

  - block: collection
    id: featured
    content:
      title: Featured Publications
      filters:
        folders:
          - publication
        featured_only: true
    design:
      columns: '2'
      view: card
  - block: collection
    content:
      title: Recent Publications
      text: |-
        {{% callout note %}}
        Quickly discover relevant content by [filtering publications](./publication/).
        {{% /callout %}}
      filters:
        folders:
          - publication
        exclude_featured: true
    design:
      columns: '2'
      view: citation
  # - block: collection
  #   id: talks
  #   content:
  #     title: Recent & Upcoming Talks
  #     filters:
  #       folders:
  #         - event
  #   design:
  #     columns: '2'
  #     view: compact
  - block: tag_cloud
    content:
      title: Popular Topics
    design:
      columns: '2'
  - block: contact
    id: contact
    content:
      title: Contact
      # subtitle:
      # text: 
      # Contact (add or remove contact options as necessary)
      # email: konrad.karanowski@gmail.com
      # Automatically link email and phone or display as text?
      # autolink: true
      # Email form provider
      form:
        provider: formspree
        formspree:
          id: mwkjkjvn
        netlify:
          # Enable CAPTCHA challenge to reduce spam?
          captcha: false
    design:
      columns: '2'
---
