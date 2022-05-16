import numpy as np
import pandas as pd
import math

"""
This script contains all functions for indicators coded for 
strategy_pretester.py. They are based on MT5 indicators
"""

def simple_atr(aDf, period=14):
    """
    Calculate atr of df for set period
    tr = max[(high-low),abs(high-prev. close), abs(low-prev close)]
    atr = simple moving average of tr over time period
    input: single market dataframe index=date, cols=[open,high,low,volume,tickVol]
    output: modifies df to add tr and atr columns
    reference:
    https://en.wikipedia.org/wiki/Average_true_range
    """
    df = aDf.copy(deep=True)
    df['tr'] = np.nan
    for i in range(0,len(df.index)):
        tr = 0
        tr_A = 0
        tr_B = 0
        if i == 0:
            tr = df.iloc[i,1] - df.iloc[i,2]
        else:
            tr = df.iloc[i,1] - df.iloc[i,2]
            tr_A = abs(df.iloc[i,1] - df.iloc[i-1,3])
            tr_B = abs(df.iloc[i,2] - df.iloc[i-1,3])
        index_date = df.index[i]
        df.loc[index_date, 'tr'] = max(tr,tr_A, tr_B)
    df['atr'] = df['tr'].rolling(window=period).mean().round(5)
    return df



def lwma(df, column=3, period=14):
    """
    Calculates linear weigthed moving average for selected column
    (default is close) and the selected period (default=14)
    input: dataframe, int, int
    return: series (separate column) with lwma
    """
    aSeries = df.iloc[:, column]
    weights = list(range(1,period+1))
    sumWeights = sum(weights)
    result = aSeries.rolling(window=period).apply(lambda x: np.sum(weights * x)
                                            / sumWeights, raw=False)
    return result


def ema(df, column=3, period=14):
    """
    Calculates exponential moving average for selected column
    (default is close) and selected period (default 14)
    input: df,int, int
    return: series with dates / ema
    """
    aSeries = df.iloc[:,column]
    return aSeries.ewm(span=period, min_periods=period).mean()


def ssl(maType, df, period=13, hi=1,low=2):
    """
    Calculates high lwma, low lwma and returns ssl signal column
    based on them.
    input: function for a ma, df, int, int, int
    return: series with signal: str('buy'/'sell') or np.nan
    """
    newdf = pd.DataFrame(index=df.index, data=df.iloc[:,3])
    newdf['hiMa']= maType(df, hi, period) # newDf col 1
    newdf['loMa'] = maType(df, low, period) # newDf col 2
    newdf['ssl'] = np.nan # signal column 3
    hlv = 0
    trend = 0 # flag
    for day in range(period,len(newdf.index)-1):
        closePrice = newdf.iloc[day,0] # day close price
        hiMa = newdf.iloc[day,1]
        loMa = newdf.iloc[day,2]  
        # Establish what is a signal
        if closePrice > hiMa:
            hlv = 1
        elif closePrice < loMa:
            hlv = -1
        else:
            hlv = 0
        # if signal:
        if hlv != 0:
            if hlv < 0:
                if trend != -1:
                    newdf.iloc[day,3]  = 'SELL'
                trend = -1
            else:
                if trend != 1:
                    newdf.iloc[day,3]  = 'BUY'
                trend = 1                 
    return newdf['ssl']

def hma(maType, df, period=7,column=3):
    """
    Calculates a hull moving average of maType
    input: function maType, df, int, int
    return: series with hma for df dataset
    """
    newdf = pd.DataFrame(index=df.index, data=df.iloc[:,column])
    half = math.floor(period / 2)
    sqrtVar = math.floor(math.sqrt(period))
    newdf['ma'] = maType(df, column, period)
    newdf['half'] = maType(df, column,half)
    newdf['both'] = 2 * newdf['half'] - newdf['ma']
    newdf['hma'] = maType(newdf,3,sqrtVar)
    return newdf['hma']

def direction(df):
    """
    Calculates which way the market is going
    input: df
    return: list with str 'long' or 'short'
    """
    alist = []
    for day in range(len(df.index)):
        if df.iloc[day,0] < df.iloc[day,3]:
            alist.append('long')
        else:
            alist.append('short')
    return alist

def wPerR(df, period=14):
    """
    Calculates William's percentage R for df
    input: dataframe, int
    return: list with percentage R for input df
    """
    newDf = pd.DataFrame(index=df.index, data=df['close'])
    newDf['max'] = df['high'].rolling(window=period, min_periods=period).max()
    newDf['min'] = df['low'].rolling(window=period, min_periods=period).min()
    newDf['perR'] = np.nan
    for i in range(len(df.index)):
        if i < period:
            continue
        else:
            newDf.iloc[i,3] = (((newDf.iloc[i,1] - newDf.iloc[i,0]) / 
            (newDf.iloc[i,1] - newDf.iloc[i,2])) * -100).round(2)
    return newDf['perR']
    


    

