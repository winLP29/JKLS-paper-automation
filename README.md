# JKLS Paper Automation
## Overview

This project automatically collects research papers from arXiv for the JKLS Big Data Analysis project.

The goal is to reduce the time required to manually search for papers and organize their information.

## Workflow

```text
arXiv API
    ↓
Python paper collection
    ↓
Duplicate removal
    ↓
CSV dataset
```

## Collected Data

The program collects:

Paper title

Abstract

Publication date

DOI, when available

arXiv URL

## How to Run

1. Install the required package:

    ```bash
    pip install -r requirements.txt
    ```


2. Run the paper collector:

    ```python
    python collect_papers.py
    ```


3. The collected papers are saved to:

    ```
    data/papers.csv
    ```

## Configuration

The search topic and number of papers can be changed in collect_papers.py.

For example:

QUERY = "large language model"
MAX_RESULTS = 100


The final research topic will be decided by the team.

## Role in the JKLS Project

This project handles the automated paper collection and initial data preparation stage.

The collected dataset will later be used for LLM-based paper classification, summarization, and monthly research-trend analysis.

## Current Status

The first version successfully collects papers from arXiv and saves them as a CSV dataset.

Future improvements may include:

- Date-range filtering

- More advanced duplicate detection

- Additional paper sources

- Larger-scale data collection
