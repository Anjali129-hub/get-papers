# get_papers/writer.py
import csv
from typing import List
from get_papers.types import Paper

def write_output(papers: List[Paper], filename: str):
    if not papers:
        print("No matching papers found.")
        return

    if filename:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "PubmedID", "Title", "Publication Date",
                "Non-academic Author(s)", "Company Affiliation(s)",
                "Corresponding Author Email"
            ])
            for paper in papers:
                writer.writerow([
                    paper.pubmed_id,
                    paper.title,
                    paper.publication_date,
                    "; ".join(paper.non_academic_authors),
                    "; ".join(paper.company_affiliations),
                    paper.corresponding_email
                ])
        print(f"Saved to {filename}")
    else:
        for paper in papers:
            print("=" * 60)
            print(f"ID: {paper.pubmed_id}")
            print(f"Title: {paper.title}")
            print(f"Date: {paper.publication_date}")
            print(f"Authors: {', '.join(paper.non_academic_authors)}")
            print(f"Companies: {', '.join(paper.company_affiliations)}")
            print(f"Email: {paper.corresponding_email}")
