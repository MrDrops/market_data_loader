# Market Data Loader
Originally coded somewhere between 09/2020-12/2020

## Description
A script that takes csv data from the graphical interface for MetaTrader 5. Using Python's Pyautogui library, it takes over the
keyboard and mouse and "manually" saves each currency pair's market data.
- Automates GUI collecting and saving market data exported as CSV files
- Takes CSV files and converts them to Pandas dataframes
- Returns a dictionary with the market data and metadata ready to use in market model

## Motivation
The purpose of this script was to support the development of a full market model to test ttrading hypothesis and run tests to find an edge in the market. To be able to get free market data to run initial tests, the use of a proprietary financial api that was overkill at the beginning stage of the project. Therefore, the only other market data available from the same Broker could only be retrieved by manually opening MetaTrader 5, opening each currency pair chart and saving the file. Since there were at least 28 separate currency pairs, it took a long time to retrieve test data. This script was the solution and reduced the time wasted doing the process manually.

## Build Status
Completed. It served its purpose

## Tech used
- Python
- Pyautogui
- Numpy
- Pandas



