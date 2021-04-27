"""
this model takes into consideration of all user input, and generates a portfolio 
for them to use as an initial screening tool.
"""
import csv
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import yahoo_fin as yfin
import yahoo_fin.stock_info as yfin_si


def message(age, time):
    timefactor = int(age) * int(time)
    if timefactor <= 100:
        investor_type = "short"
        message = f"You're a {investor_type} term investor, and your investment horizon is relatively short considering your age. You might be looking to generate high short term returns but it is important to note that investment returns require patience. On top of the portfolio we screened for you, it is recommended that you invest with more caution and look into some treasury bills and index funds to mitigate your risks."
    elif 100 < timefactor < 400:
        investor_type = "medium"
        message = f"You're a {investor_type} term investor. You're in a good position to invest. Use this program as an initial screening tool for what stocks you might want to take a closer look at."
    else:
        investor_type = "longer"
        message = f"You're a {investor_type} term investor. Other than the stocks this program generates for you, you should also take a look at other investment vehicles like alternative investments (real estate, hedge funds, venture capital, commodities, and etc) to broaden your investment portfolio."
    return message


def generate_port(capital, risk, sectors, marketcap):
    port = []

    # calculate how many stocks should come from each market cap category based on inputs
    if marketcap == "Low Cap":
        numSmall = 8
        if risk == "1":
            numLarge = 5
            numMid = 3
        elif risk == "2":
            numLarge = 4
            numMid = 4
        else:
            numLarge = 3
            numMid = 5
    elif marketcap == "Mid Cap":
        numMid = 8
        if risk == "1":
            numLarge = 5
            numSmall = 3
        elif risk == "2":
            numLarge = 4
            numSmall = 4
        else:
            numLarge = 3
            numSmall = 5
    else:
        numLarge = 8
        if risk == "1":
            numMid = 5
            numSmall = 3
        elif risk == "2":
            numMid = 4
            numSmall = 4
        else:
            numMid = 3
            numSmall = 5
    
    listLarge = []
    listMid = []
    listSmall = []
    
    if len(sectors) == 1:
    # allocate 2 stocks in preferred sector per market cap category
        with open("./data/largecap.csv","r", encoding='utf8', errors='ignore') as large:
            readerLarge = csv.reader(large)
            rows = list(readerLarge)
            rowLarge = len(rows)
            sectors_specific = []
            for i in rows:
                if i[2] == sectors[0]:
                    sectors_specific.append(rows.index(i)+1)
            for i in range(2):
                r = random.randint(0,len(sectors_specific)-1)
                if r not in listLarge:
                    listLarge.append(sectors_specific[r])
            for i in range(numLarge-2):
                r = random.randint(1,rowLarge)
                if r not in listLarge:
                    listLarge.append(r)
            for eachnum in listLarge:
                port.append(rows[eachnum-1])
            
        with open("./data/midcap.csv","r", encoding='utf8', errors='ignore') as mid:
            readerMid = csv.reader(mid)
            rows = list(readerMid)
            rowMid = len(rows)
            sectors_specific = []
            for i in rows:
                if i[2] == sectors[0]:
                    sectors_specific.append(rows.index(i)+1)
            for i in range(2):
                r = random.randint(0,len(sectors_specific)-1)
                if r not in listMid:
                    listMid.append(sectors_specific[r])
            for i in range(numMid-2):
                r = random.randint(1,rowMid)
                if r not in listMid:
                    listMid.append(r)
            for eachnum in listMid:
                port.append(rows[eachnum-1])
 
        with open("./data/smallcap.csv","r", encoding='utf8', errors='ignore') as small:
            readerSmall = csv.reader(small)
            rows = list(readerSmall)
            rowSmall = len(rows)
            sectors_specific = []
            for i in rows:
                if i[2] == sectors[0]:
                    sectors_specific.append(rows.index(i)+1)
            for i in range(2):
                r = random.randint(0,len(sectors_specific)-1)
                if r not in listSmall:
                    listSmall.append(sectors_specific[r])
            for i in range(numSmall-2):
                r = random.randint(1,rowSmall)
                if r not in listSmall:
                    listSmall.append(r)    
            for eachnum in listSmall:
                port.append(rows[eachnum-1])    

    elif len(sectors) >= 2:
    # allocate 1 stock in each of the first two preferred sectors per market cap category when two or more preferred sectors are selected
        with open("./data/largecap.csv","r", encoding='utf8', errors='ignore') as large:
            readerLarge = csv.reader(large)
            rows = list(readerLarge)
            rowLarge = len(rows)
            sectors_specific1 = []
            sectors_specific2 = []
            for i in rows:
                if i[2] == sectors[0]:
                    sectors_specific1.append(rows.index(i)+1)
                elif i[2] == sectors[1]:
                    sectors_specific2.append(rows.index(i)+1)
            for i in range(1):
                r = random.randint(0,len(sectors_specific1)-1)
                if r not in listLarge:
                    listLarge.append(sectors_specific1[r])
                r = random.randint(0,len(sectors_specific2)-1)
                if r not in listLarge:
                    listLarge.append(sectors_specific2[r])    
            for i in range(numLarge-1):
                r = random.randint(1,rowLarge)
                if r not in listLarge:
                    listLarge.append(r)
            for eachnum in listLarge:
                port.append(rows[eachnum-1])
            
        with open("./data/midcap.csv","r", encoding='utf8', errors='ignore') as mid:
            readerMid = csv.reader(mid)
            rows = list(readerMid)
            rowMid = len(rows)
            sectors_specific1 = []
            sectors_specific2 = []
            for i in rows:
                if i[2] == sectors[0]:
                    sectors_specific1.append(rows.index(i)+1)
                elif i[2] == sectors[1]:
                    sectors_specific2.append(rows.index(i)+1)
            for i in range(1):
                r = random.randint(0,len(sectors_specific1)-1)
                if r not in listMid:
                    listMid.append(sectors_specific1[r])
                r = random.randint(0,len(sectors_specific2)-1)
                if r not in listMid:
                    listMid.append(sectors_specific2[r])
            for i in range(numMid-1):
                r = random.randint(1,rowMid)
                if r not in listMid:
                    listMid.append(r)
            for eachnum in listMid:
                port.append(rows[eachnum-1])
 
        with open("./data/smallcap.csv","r", encoding='utf8', errors='ignore') as small:
            readerSmall = csv.reader(small)
            rows = list(readerSmall)
            rowSmall = len(rows)
            sectors_specific = []
            sectors_specific2 = []
            for i in rows:
                if i[2] == sectors[0]:
                    sectors_specific1.append(rows.index(i)+1)
                elif i[2] == sectors[1]:
                    sectors_specific2.append(rows.index(i)+1)
            for i in range(1):
                r = random.randint(0,len(sectors_specific1)-1)
                if r not in listSmall:
                    listSmall.append(sectors_specific1[r])
                r = random.randint(0,len(sectors_specific2)-1)
                if r not in listSmall:
                    listSmall.append(sectors_specific2[r])
            for i in range(numSmall-1):
                r = random.randint(1,rowSmall)
                if r not in listSmall:
                    listSmall.append(r)    
            for eachnum in listSmall:
                port.append(rows[eachnum-1])      
    
    else:
    # generate at random across all sectors
        with open("./data/largecap.csv","r", encoding='utf8', errors='ignore') as large:
            readerLarge = csv.reader(large)
            rows = list(readerLarge)
            rowLarge = len(rows)
            for i in range(numLarge):
                r = random.randint(1,rowLarge)
                if r not in listLarge:
                    listLarge.append(r)
            for eachnum in listLarge:
                port.append(rows[eachnum-1])

            
        with open("./data/midcap.csv","r", encoding='utf8', errors='ignore') as mid:
            readerMid = csv.reader(mid)
            rows = list(readerMid)
            rowMid = len(rows)
            for i in range(numMid):
                r = random.randint(1,rowMid)
                if r not in listMid:
                    listMid.append(r)
            for eachnum in listMid:
                port.append(rows[eachnum-1])        


        with open("./data/smallcap.csv","r", encoding='utf8', errors='ignore') as small:
            readerSmall = csv.reader(small)
            rows = list(readerSmall)
            rowSmall = len(rows)
            for i in range(numSmall):
                r = random.randint(1,rowSmall)
                if r not in listSmall:
                    listSmall.append(r)    
            for eachnum in listSmall:
                port.append(rows[eachnum-1]) 

    # add more stock information to display
    finalport = port.copy()
    for i in finalport:
        table = yfin_si.get_quote_table(i[0],dict_result=True)
        i.append(table["Market Cap"])
        i.append(table["Beta (5Y Monthly)"])
        i.append(table["PE Ratio (TTM)"])
        i.append(round(table["Quote Price"],2))
        i.append(table["52 Week Range"])
        i.append(table["1y Target Est"])
        i.append(1/16*100)
        i.append(round(int(capital)/16/table["Quote Price"],0))
        i.append(round((table["1y Target Est"]-table["Quote Price"])/table["Quote Price"]*100,2))
    finalport.sort(key = lambda x: x[12], reverse=True)

    # store all information in portfolio.csv
    header = ["Ticker", "Company Name", "Sector", "Market Cap", "Market Cap($)", "Beta", "PE", "Price", "52 Week Range", "1y Target", "Weight(%)", "Est Shares", "Potential Upside(%)"]
    with open("./data/portfolio.csv", "w", encoding='utf8', errors='ignore') as output:
        writer = csv.writer(output)
        writer.writerow(header)
        writer.writerows(finalport)

    # add title and header for results page
    dataframe = pd.read_csv("./data/portfolio.csv")
    text1 = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <title>Portfolio Generator Results</title>
    </head>

    <body>
        <h1 align="center">Portfolio Generator Results</h1>

        <h2 align="center">Your Unique Portfolio</h2>
    """

    # add visualization for portfolio results
    energy = 0
    materials = 0
    industrials = 0 
    consumerd = 0 
    consumers = 0 
    healthcare = 0 
    financials = 0 
    it = 0
    cs = 0 
    utilities = 0 
    re = 0

    length = len(port)
    for i in range(length):
        if port[i][2] == "Energy":
            energy += 1
        elif port[i][2] == "Materials":
            materials += 1
        elif port[i][2] == "Industrials":
            industrials += 1 
        elif port[i][2] == "Consumer Discretionary":
            consumerd += 1 
        elif port[i][2] == "Consumer Staples":
            consumers += 1 
        elif port[i][2] == "Health Care":
            healthcare += 1 
        elif port[i][2] == "Financials":
            financials += 1 
        elif port[i][2] == "Information Technology":
            it += 1 
        elif port[i][2] == "Communication Services":
            cs += 1 
        elif port[i][2] == "Utilities":
            utilities += 1 
        else:
            re += 1  

    s = np.array([energy, materials, industrials, consumerd, consumers, healthcare, financials, it, cs, utilities, re])
    labels = ["Energy", "Materials", "Industrials", "Consumer Discretionary", "Consumer Staples", "Health Care", "Financials", "Information Technology", "Communication Services", "Utilities", "Real Estate"]
    plt.pie(s, labels=labels, shadow=True, autopct='%1.1f%%', startangle=90)
    plt.title("Portfolio Breakdown by Sectors")
    plt.savefig('./templates/piechart.png')

    # text2 = """
    # <img src='templates/piechart.png'>
    # """

    # add return button
    text3 = """
    <br>
    <form align="center">
        <input type="button" value="Return to Search Page" onclick="document.location='./input'">
    </form>
    """

    htmldf = dataframe.to_html(justify="center",border="5")
    resultpage = open("./templates/portfolio.html","w")
    resultpage.write(text1)
    resultpage.write(htmldf)
    # resultpage.write(text2)
    resultpage.write(text3)
    resultpage.close()


def main():
    pass


if __name__ == '__main__':
    main()

