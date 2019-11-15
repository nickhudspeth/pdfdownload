import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import os
import sys

index_page_url = "https://www.mass.gov/info-details/municipal-vulnerability-preparedness-mvp-program-planning-reports"
dl_prefix = "https://www.mass.gov"

pdflist = []

outdir_prefix = "./files"

# Override the default user-agent string so the server does not reject our request
class URLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


def download_pdfs():
    # Get the HTML source from the PDF index page
    opener = URLopener()
    html = opener.open(index_page_url).read()

    # Parse the HTML into objects with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Build a list of pairs (url, filename) for all PDFs in the index
    for a in soup.find_all("a", href=True):
        text = a["href"]
        if ("/doc" in text) and (("/download" in text)):
            record = (dl_prefix + text, text.split("/")[2])
            pdflist.append(record)

    # Download all files to specified directory
    for idx, record in enumerate(pdflist):
        fprefix = outdir_prefix + "/" + record[1]
        fname = fprefix + ".pdf"
        print("Downloading " + record[1] + f"    ({idx + 1} of {len(pdflist)})")
        opener.retrieve(record[0], outdir_prefix + "/" + record[1])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        outdir_prefix = sys.argv[1]
    download_pdfs()

