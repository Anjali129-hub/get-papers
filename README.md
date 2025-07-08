# 📚 get-papers

A command-line Python tool to fetch PubMed research papers with at least one non-academic (pharma or biotech) author, and export results to CSV.

---

## 🔍 Features

- Search PubMed using full query syntax (e.g., `"covid vaccine"`, `"cancer AND immunotherapy"`)
- Identify non-academic authors by checking affiliation strings
- Extract:
  - PubMed ID
  - Paper title
  - Publication date
  - Author names (non-academic)
  - Company/organization name
  - Corresponding author's email
- Save results to CSV or print to console

---

## 📦 Tools & Technologies Used

| Tool | Purpose |
|------|---------|
| Poetry | Dependency management & packaging |
| Biopython | PubMed API integration |
| Typer | CLI interface |
| Pytest | Unit testing |
| Rich | (Optional) pretty printing |

---

## 🚀 Installation

```bash
git clone https://github.com/Anjali129-hub/get-papers.git
cd get-papers
poetry install
