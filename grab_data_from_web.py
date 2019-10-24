#!/usr/bin/env python
import requests
from subprocess import run
import bs4  # BeautifulSoup

MAIN_URL = "https://www.enmax.com/home#"
PDF_URL = "https://www.enmax.com/AboutUsSite/Reports/2016-Annual-Report.pdf"

response = requests.get(MAIN_URL)
if response.status_code == requests.codes.OK:
    raw_page = response.content
    page = raw_page.decode()
    print(page)
else:
    print("Sorry, unable to reach", MAIN_URL)

response = requests.get(PDF_URL)
if response.status_code == requests.codes.OK:
    pdf_data = response.content
    with open('enmax.pdf', 'wb') as enmax_out:
        enmax_out.write(pdf_data)
    run("enmax.pdf", shell=True)

else:
    print("Sorry, unable to grab PDF")
