Stock Price Alert & Analysis Tool

Author: Ishan Bojja,
Language: Python,
GUI Framework: Tkinter,
Data Source: Yahoo Finance (via yfinance)

This application allows users to track multiple stocks, view real-time prices, and analyze key financial indicators such as analyst recommendations, 6-month price ranges, return on equity, and more — all inside a scrollable desktop GUI.

Features:
Real-Time Stock Tracking

Displays live stock prices fetched from Yahoo Finance

Automatically updates prices every 10 seconds

Supports tracking multiple stocks simultaneously

Analyst Insights

Shows:

Overall analyst recommendation (buy, hold, sell, etc.)

Number of analyst opinions

Average analyst rating

Analyst data may include firms such as:

Goldman Sachs

JPMorgan

Morgan Stanley

Morningstar

CFRA

UBS

Wells Fargo

Bank of America

Note: Lower analyst ratings are better

Price Range Analysis

For each stock:

6-Month Low

6-Month High

Percentage change from:

6-Month Low

6-Month High

These metrics help identify whether a stock is trading closer to its lows or highs.

Financial Metrics

Return on Equity (ROE) (displayed as a percentage)

200-Day Moving Average

Persistent Stock List

Stocks are saved in a text file

Automatically reloads tracked stocks on startup

Prevents duplicate tickers

User-Friendly Interface

Centered application window

Scrollable layout (handles many stocks cleanly)

Simple input field to add new tickers

Warning messages for duplicates

Installation & Setup
1. Install Python Packages

Make sure Python 3.10+ is installed, then run:

pip install yfinance tk

2. Create the Stock Preferences File

Create a file named:

Stock_Preferences.txt


Example contents:

AAPL,MSFT,AMZN,GOOGL


You can place this file anywhere, but make sure the path matches this line in the code:

FILE = "Projects/Stocks/Stock_Preferences.txt"

3. Run the Program
python your_script_name.py

How to Use

Launch the program

Existing stocks from Stock_Preferences.txt load automatically

Enter a stock ticker (e.g., AAPL) into the input box

Click Add Stock

The stock is immediately analyzed and displayed

Prices refresh automatically every 10 seconds

Displayed Information Per Stock

For each tracked ticker, the app shows:

Current Price (live)

6-Month Low

6-Month High

Analyst Recommendation

Number of Analysts & Average Rating

Return on Equity (ROE)

200-Day Moving Average

% Change from 6-Month Low

% Change from 6-Month High

Important Notes

Data accuracy depends on Yahoo Finance availability

Some tickers may not have all metrics available (N/A)

Excessive API requests may cause temporary data issues

This tool is for educational purposes only and not financial advice

Thanks, Ishan Bojja(Developer)

Contact me at:
Gmail- "ishanbojja@gmail.com"
Discord- "ishanbojja_12798"
