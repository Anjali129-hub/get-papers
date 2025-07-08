# get_papers/api.py
from typing import List
from Bio import Entrez
import xml.etree.ElementTree as ET
from get_papers.types import Paper
from get_papers.filter import is_non_academic

Entrez.email = "anjali720gupta@gmail.com"  

def fetch_papers(query: str, debug: bool = False) -> List[Paper]:
    handle = Entrez.esearch(db="pubmed", term=query, retmax=20)
    record = Entrez.read(handle)
    ids = record["IdList"]

    if debug:
        print(f"Found {len(ids)} papers.")

    handle = Entrez.efetch(db="pubmed", id=",".join(ids), rettype="xml", retmode="xml")
    root = ET.parse(handle).getroot()

    papers: List[Paper] = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle", "")
        pub_date = extract_pub_date(article)
        authors = article.findall(".//Author")

        non_acad_authors = []
        companies = []
        corresponding_email = ""

        for author in authors:
            aff = author.findtext("AffiliationInfo/Affiliation", "")
            email = extract_email(aff)

            if is_non_academic(aff):
                full_name = get_author_name(author)
                if full_name:
                    non_acad_authors.append(full_name)
                    companies.append(aff)

            if not corresponding_email and email:
                corresponding_email = email

        if non_acad_authors:
            papers.append(Paper(
                pubmed_id=pmid,
                title=title,
                publication_date=pub_date,
                non_academic_authors=non_acad_authors,
                company_affiliations=companies,
                corresponding_email=corresponding_email
            ))

    return papers

def extract_pub_date(article) -> str:
    date = article.find(".//PubDate")
    if date is None:
        return "Unknown"
    year = date.findtext("Year")
    month = date.findtext("Month", "")
    day = date.findtext("Day", "")
    return f"{year or ''}-{month or ''}-{day or ''}".strip("-")

def get_author_name(author) -> str:
    last = author.findtext("LastName", "")
    fore = author.findtext("ForeName", "")
    return f"{fore} {last}".strip()

def extract_email(text: str) -> str:
    import re
    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return match.group() if match else ""
