#By Ishan Bojja
#*MUST RUN "pip install yfinance tk" IN TERMINAL BEFORE RUNNING THE CODE*
#This program requires a txt file named "Stock_Preferences.txt". Replace the file path in line 11 if needed.

import yfinance as yf
import tkinter as tk
from tkinter import messagebox

print("Stock prices and recommendations are fetched from Yahoo Finance using the yfinance library. All Analysts are from places that include: Goldman Sachs, JPMorgan, Morgan Stanley, Morningstar, CFRA, UBS, Wells Fargo, BofA. A lower analyst rating is better.")#Disclaimers for users

FILE = "Stock_Preferences.txt"

root = tk.Tk()
root.title("Stock Price Alert")
window_width = 400
window_height = 700
root.geometry(f"{window_width}x{window_height}")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")#Centering window.

canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

try:
    with open(FILE, "r") as f:
        stocks = [s.strip().upper() for s in f.read().split(",") if s.strip()]
except FileNotFoundError:
    stocks = []

labels = {}

def save_stocks():
    with open(FILE, "w") as f:
        f.write(",".join(stocks))

def add_stock():
    ticker = entry.get().upper().strip()
    if not ticker:
        return

    if ticker in stocks:
        messagebox.showwarning("Duplicate", f"{ticker} already exists.")
        return

    stocks.append(ticker)
    save_stocks()
    create_stock_section(ticker)
    entry.delete(0, tk.END)

def create_label(ticker):
    var = tk.StringVar(value=f"{ticker}: Loading...")
    lbl = tk.Label(scrollable_frame, textvariable=var, font=("Arial", 12))
    lbl.pack(anchor="w", padx=20)
    labels[ticker] = var

def return_on_equity(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return info.get("returnOnEquity", "N/A")

def two_hundred_day_average(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return info.get("twoHundredDayAverage", "N/A")

def retrieve_stock_info(ticker):#Not used currently, but can retrieve all stock info if needed.
    return yf.Ticker(ticker).info

def buy_recommendation(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    recommendation = info.get("recommendationKey", "N/A")
    analyst_count = info.get("numberOfAnalystOpinions", 0)
    average_analyst_rating = info.get("averageAnalystRating", "N/A")

    return recommendation, analyst_count, average_analyst_rating

def six_month_low(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="6mo")
    return hist["Low"].min()

def six_month_high(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="6mo")
    return hist["High"].max()

def percent_change(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="6mo")
    low = hist["Low"].min()
    high = hist["High"].max()
    current_price = stock.info["currentPrice"]
    change_from_low = ((current_price - low) / low) * 100
    change_from_high = ((current_price - high) / high) * 100
    return change_from_low, change_from_high

def create_stock_section(ticker):
    create_label(ticker)

    low = six_month_low(ticker)
    tk.Label(
        scrollable_frame,
        text=f"6-Month Low: ${low:.2f}",
        font=("Arial", 10)
    ).pack(anchor="w", padx=40)

    high = six_month_high(ticker)
    tk.Label(
        scrollable_frame,
        text=f"6-Month High: ${high:.2f}",
        font=("Arial", 10)
    ).pack(anchor="w", padx=40)

    recommendation, analyst_count, average_analyst_rating = buy_recommendation(ticker)
    tk.Label(
        scrollable_frame,
        text=f"Recommendation: {recommendation}",
        font=("Arial", 10)
    ).pack(anchor="w", padx=40)
    tk.Label(
        scrollable_frame,
        text=f"{analyst_count} Analysts, Avg Rating: {average_analyst_rating}",
        font=("Arial", 10)
    ).pack(anchor="w", padx=40)

    roe= return_on_equity(ticker)
    tk.Label(
        scrollable_frame,
        text=f"Return on Equity: {roe if roe=='N/A' else f'{roe*100:.2f}%'}",
        font=("Arial", 10)
    ).pack(anchor="w", padx=40)

    two_hundred_day_avg = two_hundred_day_average(ticker)
    tk.Label(
        scrollable_frame,
        text=f"200-Day Average: ${two_hundred_day_avg if two_hundred_day_avg=='N/A' else f'{two_hundred_day_avg:.2f}'}",
        font=("Arial", 10)
    ).pack(anchor="w", padx=40)

    change_low, change_high = percent_change(ticker)
    tk.Label(
        scrollable_frame,
        text=f"Change from Low: {change_low:.2f}%",
        font=("Arial", 10),
        # fg="green" if change_low >= 20 else "red"#20% threshold for low.
    ).pack(anchor="w", padx=40)

#You want the thresholds to be close to the low and far from the high.

    tk.Label(
        scrollable_frame,
        text=f"Change from High: {change_high:.2f}%",
        font=("Arial", 10),
        # fg="green" if change_high >= -10 else "red"#10% threshold for high.
    ).pack(anchor="w", padx=40)

def update_prices():
    for ticker, var in labels.items():
        try:
            price = yf.Ticker(ticker).info["currentPrice"]
            var.set(f"{ticker}: ${price}")
        except:
            var.set(f"{ticker}: Error")
    root.after(10000, update_prices)

tk.Label(
    scrollable_frame,
    text="Tracked Stocks",
    font=("Arial", 16)
).pack(pady=10)

entry = tk.Entry(scrollable_frame)
entry.pack()

tk.Button(
    scrollable_frame,
    text="Add Stock",
    command=add_stock
).pack(pady=5)

for s in stocks:
    create_stock_section(s)

update_prices()
root.mainloop()
