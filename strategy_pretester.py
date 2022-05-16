import numpy as np
import pandas as pd
import os
import re
import pair_obj_creator as poc
import indicators

"""
Market model to test No Nonsense Forex Based Strategies
Needs modules:
-market_data_loader.py: use script before strategy_pretester.py
to load all updated market data files from MT5
-indicators.py: import module. Contains all indicators that have
been coded so far
-script to actually run: inputs, and display data, options for test data
storage
"""

# sample to test model to avoid full load of files
load_df = pd.read_csv('C:\\Users\\Drops\\Documents\\Trading_Files_python\\chart_data_files\\AUDCADDaily.csv',
            encoding='utf-16',names=['date', 'open', 'high', 'low', 'close', 'volume', 'tickVol'],
            index_col='date',header=1, parse_dates=True, infer_datetime_format=True)
sample = load_df.loc['2017-01-02':'2020-09-01']
# end of sample





# this will load indicators to test, make mock True value columns
# for all not tested conditions and create all the needed columns
# minimum: entry, exit indicator (can be the same)
# entry, exit, baseline

# function to load all test conditions (sl, tp, risk, etc)

# script to run test with all input and generate full result data

# functions to store result data