import pandas as pd
import pandas_datareader.data as web
import datetime
import pdb
import numpy as np
import sys
import modules.util

# Use this to get price data for any ticker from Yahoo! Finance
# as such: python series_getter.py VTI

def main():
	start = datetime.datetime(1940, 1, 1)
	end = datetime.datetime.now()

	tickers = sys.argv[1:]

	for ticker in tickers:
		print ticker
		tick_df = get_returns(ticker, start, end)
		print np.std(tick_df['Returns'])
		tick_df.to_csv("%s.csv" % ticker)

main()