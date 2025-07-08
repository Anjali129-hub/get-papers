# cli/main.py
import typer
from get_papers.api import fetch_papers
from get_papers.writer import write_output

app = typer.Typer()

@app.command()
def main(
    query: str,
    file: str = typer.Option("", "--file", "-f", help="CSV output file"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug output")
):
    """Fetch PubMed papers and filter by company authors"""
    if debug:
        print(f"Running PubMed query: {query}")
    papers = fetch_papers(query, debug)
    write_output(papers, file)

if __name__ == "__main__":
    app()
