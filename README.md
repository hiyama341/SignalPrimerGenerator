# SignalPrimerGenerator

## Overview

Welcome to PrimeGenTool, the automated solution for your primer design needs. This repository hosts a tool capable of generating primers from FASTA or GenBank files effortlessly. Additionally, SignalPrimerGenerator integrates functionality to process SignalP outputs for the efficient removal of signal peptides from protein sequences. This utility is aimed at molecular biologists,or anyone in need of streamlined primer design for their genetic analysis and experiments.

## Features

- **Automated Primer Generation**: Input your FASTA or GenBank files, and receive optimal primer sequences for your PCR experiments.
- **Signal Peptide Processing**: Utilizes SignalP output to accurately identify and remove signal peptide sequences from proteins.
- **Customizable**: Allows for adjustable parameters to suit various experimental needs.

## Getting Started

### Prerequisites

Before running PrimeGenTool, ensure you have the following:

- Python >=3.8
- Biopython library
- teemi library
- pydna library

### Installation

To get started with SignalPrimerGenerator, clone this repository to your local machine using:

```bash
git clone https://github.com/hiyama341/SignalPrimerGenerator.git
```

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

### Project based on the cookiecutter data science project template.
