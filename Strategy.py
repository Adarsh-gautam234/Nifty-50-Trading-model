import pandas as pd
import numpy as np
from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator

# ==========================
# LOAD DATA
# ==========================

df = pd.read_csv("Nifty 50 Historical Data.csv")

# Adjust if your column names differ
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace(",", "")
    .astype(float)
)

df["Date"] = pd.to_datetime(df["Date"])

df = df.sort_values("Date").reset_index(drop=True)

# ==========================
# INDICATORS
# ==========================

df["RSI"] = RSIIndicator(
    close=df["Price"],
    window=14
).rsi()

df["EMA20"] = EMAIndicator(
    close=df["Price"],
    window=20
).ema_indicator()

df["EMA50"] = EMAIndicator(
    close=df["Price"],
    window=50
).ema_indicator()

# Previous values

df["RSI_prev"] = df["RSI"].shift(1)
df["Price_prev"] = df["Price"].shift(1)

df = df.dropna().reset_index(drop=True)

# ==========================
# SIGNAL GENERATION
# ==========================

signals = []

position = 0

for i in range(len(df)):

    row = df.iloc[i]

    buy_condition = (

        row["EMA20"] > row["EMA50"]

        and

        row["RSI"] > 55

        and

        row["Price"] > row["Price_prev"]

    )

    sell_condition = (

        row["EMA20"] < row["EMA50"]

        or

        row["RSI"] < 45

    )

    # BUY
    if buy_condition and position == 0:

        signals.append(1)

        position = 1

    # SELL
    elif sell_condition and position == 1:

        signals.append(-1)

        position = 0

    # HOLD
    else:

        signals.append(0)

df["Signal"] = signals

# ==========================
# VERIFICATION
# ==========================

running_position = 0

for signal in df["Signal"]:

    running_position += signal

    assert running_position >= 0, (
        "Invalid signal sequence: short position detected"
    )

    assert running_position <= 1, (
        "Invalid signal sequence: double buy detected"
    )

print("Signal verification passed")

# ==========================
# EXPORT CSV
# ==========================

output = df[["Date", "Signal"]]

output.to_csv(
    "nifty_signals.csv",
    index=False
)

print("\nSignals saved to:")
print("nifty_signals.csv")

print("\nSignal Counts:")
print(output["Signal"].value_counts())