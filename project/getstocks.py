"""
A stock portfolio generator application using Flask that helps users explore
different portfolio options based on their inputs.

This file scrapes lists of large cap, mid cap, and small cap stocks from Wikipedia, 
including S&P 500, S&P 400, and S&P 600. Data extracted includes stock ticker, company
name, and its corresponding GICS sector. Data from three lists are stored into three
separate csv files under the folder "data".
"""

from bs4 import BeautifulSoup
import csv
import urllib.request 


# S&P LargeCap 500
largecap = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
# S&P MidCap 400
midcap = "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies"
# S&P SmallCap 600
smallcap = "https://en.wikipedia.org/wiki/List_of_S%26P_600_companies"


def download_page(url):
    return urllib.request.urlopen(url)


def parse(html):
    soup = BeautifulSoup(html, features="html.parser")
    table = soup.find("table", attrs={"class": "wikitable sortable"})
    cap = html.url[-13]
    data = []
    rows = table.findAll("tr")
    for row in rows:
        fields = row.findAll("td")
        if fields:
            if cap == "4":
                symbol = fields[1].text.rstrip()
                name = fields[0].text.replace(",", "").strip()
                sector = fields[2].text.rstrip()                
            elif cap == "6":
                symbol = fields[1].text.rstrip()
                name = fields[0].text.replace(",", "").strip()
                sector = fields[2].text.rstrip()
            else:
                symbol = fields[0].text.rstrip()
                name = fields[1].text.replace(",", "")
                sector = fields[3].text.rstrip()
            data.append([symbol, name, sector])

    header = ["Symbol", "Name", "Sector"]
    file_name = "./data/"
    largecap_file = "largecap.csv"
    midcap_file = "midcap.csv"
    smallcap_file = "smallcap.csv"
    
    if cap == "5":
        writer = csv.writer(open(file_name+largecap_file, "w"), lineterminator="\n")
    elif cap == "4":
        writer = csv.writer(open(file_name+midcap_file, "w"), lineterminator="\n")
    elif cap == "6":
        writer = csv.writer(open(file_name+smallcap_file, "w"), lineterminator="\n")
    
    writer.writerow(header)
    data.sort(key=lambda s: s[1].lower())
    writer.writerows(data)


def process():
    parse(download_page(largecap))
    parse(download_page(midcap))
    parse(download_page(smallcap))


if __name__ == "__main__":
    process()