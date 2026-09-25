**JKLS Paper Automation**

1.Overview

This project automatically collects research papers from arXiv for the JKLS Big Data Analysis project.

The goal is to reduce the time required to manually search for papers and organize their information.

2.Workflow

arXiv API
    
    ↓

Python paper collection
    
    ↓

Duplicate removal
    
    ↓

CSV dataset

3.Collected Data

The program collects:

1)Paper title

2)Abstract

3)Publication date

4)DOI, when available

5)arXiv URL

4.How to Run

Install the required package:

pip install -r requirements.txt


Run the paper collector:

python collect_papers.py


The collected papers are saved to:

data/papers.csv

5.Configuration

The search topic and number of papers can be changed in collect_papers.py.

For example:

QUERY = "large language model"

MAX_RESULTS = 100


The final research topic will be decided by the team.

Role in the JKLS Project

This project handles the automated paper collection and initial data preparation stage.

The collected dataset will later be used for LLM-based paper classification, summarization, and monthly research-trend analysis.

6.Current Status

The first version successfully collects papers from arXiv and saves them as a CSV dataset.

Future improvements may include:

Date-range filtering

More advanced duplicate detection

Additional paper sources

Larger-scale data collection
