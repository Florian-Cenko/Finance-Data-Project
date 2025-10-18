import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
# Optional Plotly Method Imports
import plotly
import cufflinks as cf
import plotly.graph_objects as go
cf.go_offline()

df = pd.read_pickle('all_banks')
# 1. Figure out how to get the stock data from Jan 1st 2006 to Jan 1st 2016 for each of these banks. Set each bank to be a separate dataframe, with the variable name for that bank being its ticker symbol. This will involve a few steps:**
# 1. Use datetime to set start and end datetime objects.
# 2. Figure out the ticker symbol for each bank.

start = datetime.datetime(2006,1,1)
end = datetime.datetime(2016,1,1)

df_filtered = df.loc[start:end]

BAC = df_filtered['BAC']
C  = df_filtered['C']
GS = df_filtered['GS']
JPM = df_filtered['JPM']
MS =  df_filtered['MS']
WFC = df_filtered['WFC']

# 2. Create a list of the ticker symbols (as strings) in alphabetical order. Call this list: tickers
tickers = ['BAC','C','GS','JPM','MS','WFC']

# 3.  Use pd.concat to concatenate the bank dataframes together to a single data frame called bank_stocks. Set the keys argument equal to the tickers list.
# Also pay attention to what axis you concatenate on.

bank_stocks = pd.concat([BAC,C,GS,JPM,MS,WFC],axis=1,keys=tickers)
print(bank_stocks.head())

# 4. Set the column name levels (this is filled out for you):
bank_stocks.columns.names = ['Bank Ticker','Stock Info']
print(bank_stocks.head())

# 5. What is the max Close price for each bank's stock throughout the time period?
max_Close = bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()
print(max_Close)

# 6. Create a new empty DataFrame called returns.
# This dataframe will contain the returns for each bank's stock. returns are typically defined by:
returns = pd.DataFrame()

# 7. We can use pandas pct_change() method on the Close column to create a column representing this return value.
# Create a for loop that goes and for each Bank Stock Ticker creates this returns column and set's it as a column in the returns DataFrame.
for tick in tickers:
    returns[tick + ' Returns'] = bank_stocks[tick]['Close'].pct_change()
print(returns.head())

# 8.  Create a pairplot using seaborn of the returns dataframe.
# What stock stands out to you? Can you figure out why?
sns.pairplot(returns)
# plt.show()

# 9. Using this returns DataFrame,
# figure out on what dates each bank stock had the best and worst single day
# returns. You should notice that 4 of the banks share the same day for the
# worst drop, did anything significant happen that day?

worst_Days = returns.idxmin()
print(worst_Days)

best_Days = returns.idxmax()
print(best_Days)

# 10.Take a look at the standard deviation of the returns,
# which stock would you classify as the riskiest over the entire time period?
# Which would you classify as the riskiest for the year 2015?
standard_deviation = returns.std()
print(standard_deviation)

standard_deviation2015 = returns.loc['2015-01-01':'2015-12-31'].std()
print(standard_deviation2015)

# 11.  Create a distplot using seaborn of the 2015 returns for Morgan Stanley
sns.displot(returns.loc['2015-01-01':'2015-12-31']['MS Returns'])
plt.show()

# 12.  Create a distplot using seaborn of the 2008 returns for CitiGroup
sns.displot(returns.loc['2008-01-01':'2008-12-31']['C Returns'])
plt.show()

# More Visualization
sns.set_style('whitegrid')

# 13. Create a line plot showing Close price for each bank for the entire index of time.
# for tick in tickers:
#     bank_stocks[tick]['Close'].plot(label=tick,figsize=(12,4))
# plt.legend()
# plt.show()
# OR
bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot()
plt.show()

# Moving Averages
# Let's analyze the moving averages for these stocks in the year 2008.

# 14. Plot the rolling 30 day average against the Close Price
# for Bank Of America's stock for the year 2008
# america_plot = bank_stocks.xs(key='BAC',axis=1,level=0)['Close'].loc['2008-01-01':'2008-12-31']
# print(america_plot)

BAC['Close'].loc['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg')
BAC['Close'].loc['2008-01-01':'2009-01-01'].plot(label='BAC CLOSE')
plt.show()

# 15. Create a heatmap of the correlation between the stocks Close Price.
b_stocks = bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr()
sns.heatmap(b_stocks,annot=True,cmap='coolwarm')
plt.show()

# Optional: Use seaborn's clustermap to cluster the correlations together:
sns.clustermap(b_stocks,annot=True,cmap='coolwarm')
plt.show()

# Part 2 (Optional)

# 16. Use .iplot(kind='candle) to create a candle plot of Bank of America's stock
# from Jan 1st 2015 to Jan 1st 2016.

bac15 = BAC.loc['2015-01-01':'2016-01-01']

go.Figure(data=[go.Candlestick(
    x=bac15.index,
    open=bac15['Open'],
    high=bac15['High'],
    low=bac15['Low'],
    close=bac15['Close']
)]).show()

# 17.
MS['Close'].loc['2015-01-01':'2016-01-01'].ta_plot(study='sma',periods=[13,21,55],title='Simple Moving Averages')

# 18.
BAC['Close'].loc['2015-01-01':'2016-01-01'].ta_plot(study='boll')