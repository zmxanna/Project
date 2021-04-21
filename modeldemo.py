"""yahoo_fin"""
import yahoo_fin as yfin
import yahoo_fin.stock_info as yfin_si
from yahoo_fin.stock_info import get_data

# Prints all of the historical data available for a stock with a specified interval between two dates [data is returned in a pandas dataframe]
# interval: "1d" = daily, "1wk" = weekly, "1mo" = monthly
apple_weekly= get_data("aapl", start_date="01/04/2021", end_date="04/12/2021", index_as_date = True, interval="1wk")
# print(apple_weekly)

# Create list of tickers, empty dictionary, & iterate through list appending each pandas dataframe to empty dictionary
ticker_list = ["amzn", "aapl", "googl"]
historical_datas = {}
for ticker in ticker_list:
    historical_datas[ticker] = get_data(ticker)
# print(historical_datas["aapl"])

# Returns a list of all the tickers in the Dow Jones
# Nasdaq: tickers_nasdaq()
# S&P500: tickers_sp500()
# Dow Jones: tickers_dow()
dow_list = yfin_si.tickers_dow()
# print(dow_list)

# Iterate through list of tickers, appending each time to dictionary
dow_historical = {}
for ticker in dow_list:
    dow_historical[ticker] = yfin_si.get_data(ticker, start_date="01/04/2021", end_date="01/05/2021", interval="1d")
# print(dow_historical)

# Return summary of fundamental data
quote_table = yfin_si.get_quote_table("aapl", dict_result=False)
# print(quote_table)]

# Return the P/E ratio only
quote_table = yfin_si.get_quote_table("aapl", dict_result=True)
# print(quote_table["PE Ratio (TTM)"])

# ---Returns Statistics of a Stock---
# print(yfin_si.get_stats("aapl"))
# print(yfin_si.get_stats_valuation("aapl"))

# Grab fundamentals data for a list of tickers at once & then have a go at picking out a single attribut to rank all stocks by
import pandas as pd
# Get list of Dow Jones tickers
dow_list = yfin_si.tickers_dow()
dow_stats = {}
for ticker in dow_list:
    temp = yfin_si.get_stats_valuation(ticker)
    temp = temp.iloc[:,:2]
    temp.columns = ["Attribute", "Recent"]
    dow_stats[ticker] = temp
# print(dow_stats)
combined_stats = pd.concat(dow_stats)
combined_stats = combined_stats.reset_index()
# print(combined_stats)
del combined_stats["level_1"]
# Update column names
combined_stats.columns = ["Ticker", "Attribute", "Recent"]
# print(combined_stats)
# Comparing by a particular attribute
pe_ratios = combined_stats[combined_stats["Attribute"]=="Trailing P/E"].reset_index()
# pe_ratios = combined_stats[combined_stats.Attribute.str.contains("Trailing P/E")
# print(pe_ratios)
# Order the 'Recent' column to find the best/worst earners
pe_ratios_sorted = pe_ratios.sort_values("Recent", ascending = False).reset_index()
# print(pe_ratios_sorted)

# Additional Utility
income_statement = yfin_si.get_income_statement("aapl")
# print(income_statement)
balance_sheet = yfin_si.get_balance_sheet("aapl")
# print(balance_sheet)
cash_flow_statement = yfin_si.get_cash_flow("aapl")
# print(cash_flow_statement)

# Pull price data for all stocks in S&P500
sp = yfin_si.tickers_sp500()
price_data = {ticker: yfin_si.get_data(ticker) for ticker in sp}
from functools import reduce
combined = reduce(lambda x,y: x.append(y), price_data.values())
# print(combined)

#------------------------------------------------------------------------------

""" yfinance"""
import yfinance as yf

# Prints all the information for a stock including stock price, market cap, historical stock price, etc.
aapl = yf.Ticker("aapl")
# print(aapl.info)

# Return historical data
aapl_historical = aapl.history(start="2020-06-02", end="2020-06-07", interval="1m")
# Interval: “1m”, “2m”, “5m”, “15m”, “30m”, “60m”, “90m”, “1h”, “1d”, “5d”, “1wk”, “1mo”, “3mo”
print(aapl_historical)

# Return historical data for multiple tickers at once
data = yf.download("AMZN AAPL GOOG", start="2017-01-01", end="2017-04-30")
# print(data)
# Return historical data for multiple tickers at once grouped by tickers
data = yf.download("AMZN AAPL GOOG", start="2017-01-01", end="2017-04-30", group_by='tickers')
# print(data)
# Export data as CSV
# data.to_csv('amzn_aapl_goog.csv')

# Return specifically the PE ratio from dictionary
# print(aapl.info['forwardPE'])

# Grab fundamentals data for a bunch of tickers at once & compare by particular attribute
import pandas as pd
tickers_list = ["aapl", "goog", "amzn", "bac", "ba"]
tickers_data = {} # empty dictionary
for ticker in tickers_list:
    ticker_object = yf.Ticker(ticker)
    # Convert info() output from dictionary to dataframe
    temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
    temp.reset_index(inplace=True)
    temp.columns = ["Attribute", "Recent"]
    # add (ticker, dataframe) to main dictionary
    tickers_data[ticker] = temp
# print(tickers_data)
combined_data = pd.concat(tickers_data)
combined_data = combined_data.reset_index()
# print(combined_data)
del combined_data["level_1"]
combined_data.columns = ["Ticker", "Attribute", "Recent"]
# print(combined_data)
# Comparing by a particular attribute
employees = combined_data[combined_data["Attribute"]=="fullTimeEmployees"].reset_index()
del employees["index"] # clean up unnecessary column
# print(employees)
employees_sorted = employees.sort_values('Recent',ascending=False)
# print(employees_sorted)