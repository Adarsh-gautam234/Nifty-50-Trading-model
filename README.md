# Nifty 50 Trading Model

## Overview

This repository contains two separate trading strategy implementations developed for quantitative trading research and signal generation.

The project includes:

1. A custom trading model (`trade2.0.ipynb`) built from scratch using technical indicators and backtesting.
2. A long-only signal generation model (`Strategy.py`) that generates Buy/Hold/Sell signals in the format required for submission.

---

## Project 1: trade2.0.ipynb

### Objective

Build a complete trading model using technical indicators, risk management rules, and backtesting.

### Features

* NIFTY 50 data from Yahoo Finance
* RSI (14)
* EMA (50)
* ATR (Average True Range)
* Volume Analysis
* Momentum Analysis
* Trend Strength Analysis

### Entry Logic

A BUY signal is generated when:

* Price is above EMA50
* RSI is below 50 (pullback in uptrend)
* Price starts recovering from the pullback

### Exit Logic

The model exits positions using:

* Profit targets
* Trailing stops
* ATR-based risk control
* Trend weakness detection

### Backtesting

The notebook contains:

* Trade execution simulation
* Profit/Loss calculation
* Win-rate calculation
* Trade logging
* Performance evaluation

### Visualization

The notebook also generates:

* Price charts
* EMA overlays
* Buy/Sell markers
* Strategy performance plots

---

## Project 2: Strategy.py

### Objective

Generate long-only trading signals on Nifty historical data.

### Signal Format

* 1 = Buy
* 0 = Hold
* -1 = Sell

### Indicators Used

* RSI (14)
* EMA (20)
* EMA (50)

### Buy Conditions

* EMA20 > EMA50
* RSI > 55
* Current Price > Previous Price
* No active position exists

### Sell Conditions

* EMA20 < EMA50
* OR RSI < 45
* Active position exists

### Long-Only Constraints

The strategy prevents:

* Short selling
* Multiple buy signals while already invested
* Multiple sell signals while flat

### Output

The strategy generates:

* `nifty_signals.csv`

which contains the final signal sequence for all timestamps.

---

## Repository Files

* `trade2.0.ipynb` – Trading model with backtesting and visualization
* `Strategy.py` – Long-only signal generation strategy
* `nifty_signals.csv` – Generated trading signals
* `Nifty 50 Historical Data (2).csv` – Historical dataset
* `requirements.txt` – Python dependencies

---

## Author

Adarsh Gautam Jha

IIT Bombay

Electrical Engineering (Dual Degree)
