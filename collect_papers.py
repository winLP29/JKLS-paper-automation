import csv
import os
import ssl
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

import certifi


# =========================
# SETTINGS
# =========================

QUERY = "large language model"
MAX_RESULTS = 100

OUTPUT_FILE = "data/papers.csv"


# =========================
# COLLECT PAPERS FROM arXiv
# =========================

def collect_papers():
    print("Searching arXiv...")
    print(f"Topic: {QUERY}")
    print(f"Number of papers: {MAX_RESULTS}")

    params = {
        "search_query": f"all:{QUERY}",
        "start": 0,
        "max_results": MAX_RESULTS,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }

    url = (
        "https://export.arxiv.org/api/query?"
        + urllib.parse.urlencode(params)
    )

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "JKLS-Paper-Automation/1.0"
        }
    )

    ssl_context = ssl.create_default_context(
    cafile=certifi.where()
    )

    with urllib.request.urlopen(
        request,
        context=ssl_context
    ) as response:
        xml_data = response.read()


    root = ET.fromstring(xml_data)

    namespace = {
        "atom": "http://www.w3.org/2005/Atom"
    }

    papers = []
    seen_ids = set()

    for entry in root.findall("atom:entry", namespace):

        arxiv_id = entry.findtext(
            "atom:id",
            default="",
            namespaces=namespace
        )

        title = entry.findtext(
            "atom:title",
            default="",
            namespaces=namespace
        ).strip().replace("\n", " ")

        abstract = entry.findtext(
            "atom:summary",
            default="",
            namespaces=namespace
        ).strip().replace("\n", " ")

        published = entry.findtext(
            "atom:published",
            default="",
            namespaces=namespace
        )

        doi = ""

        # Look for DOI information if available
        for link in entry.findall("atom:link", namespace):
            href = link.attrib.get("href", "")
            if "doi.org" in href:
                doi = href.replace("https://doi.org/", "")
                break

        # Remove duplicate papers
        if arxiv_id in seen_ids:
            continue

        seen_ids.add(arxiv_id)

        papers.append({
            "title": title,
            "abstract": abstract,
            "published": published,
            "doi": doi,
            "url": arxiv_id,
        })

    return papers


# =========================
# SAVE CSV
# =========================

def save_csv(papers):
    os.makedirs("data", exist_ok=True)

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        fieldnames = [
            "title",
            "abstract",
            "published",
            "doi",
            "url",
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(papers)

    print()
    print(f"Saved {len(papers)} papers.")
    print(f"Output: {OUTPUT_FILE}")


# =========================
# MAIN
# =========================

if __name__ == "__main__":

    papers = collect_papers()

    save_csv(papers)

    print()
    print("Done!")
