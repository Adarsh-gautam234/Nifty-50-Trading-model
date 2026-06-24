# Nifty 50 Long Only Strategy

## Overview

This project implements a long-only trading strategy on Nifty 50 historical data.

The objective is to generate trading signals in the format:

* 1 = Buy
* 0 = Hold
* -1 = Sell

while enforcing the following constraints:

* No short selling
* No repeated buy signals while already holding a position
* No sell signal before a corresponding buy signal
* Only one active position at a time

## Strategy Logic

The strategy uses:

* RSI (14)
* EMA (20)
* EMA (50)

### Buy Conditions

A buy signal is generated when:

* EMA20 > EMA50
* RSI > 55
* Current price > Previous price
* No active position exists

### Sell Conditions

A sell signal is generated when:

* EMA20 < EMA50
* OR RSI < 45
* An active position exists

### Hold

If neither buy nor sell conditions are met:

* Signal = 0

## Signal Verification

The generated signals are validated to ensure:

* No short positions occur
* No double-buy events occur
* Position state remains valid throughout the dataset

## Output

The final output is a CSV file containing:

| Date       | Signal     |
| ---------- | ---------- |
| YYYY-MM-DD | 1 / 0 / -1 |

## Technologies Used

* Python
* Pandas
* NumPy
* TA (Technical Analysis Library)

## Author

Adarsh Gautam Jha
IIT Bombay
