import pandas as pd

file_path = r'C:\Users\macha\Documents\Uni\Year 3\Project in Maths\Ouse Data\Comparing stage at Viking and Skelton.csv'
df = pd.read_csv(file_path)

import matplotlib.pyplot as plt

df["Time"] = pd.to_datetime(df["Time"], format="%d/%m/%Y %H:%M")

# Scatter plot of Skelton vs. Viking stage levels
plt.figure(figsize=(8, 5))
plt.scatter(df["Skelton Stage"], df["Viking Stage"],
            alpha=0.5, s=30)
plt.xlabel("Skelton Stage (m)", fontsize=14, fontweight="bold")
plt.ylabel("Viking Stage (m)", fontsize=14, fontweight="bold")  
plt.grid(True)
plt.show()

import numpy as np

# Maximum lag to test
max_lag = 12  
correlations = []

# Test different lags
for lag in range(max_lag + 1):
    shifted_skelton = df["Skelton Stage"].shift(lag)
    correlation = shifted_skelton.corr(df["Viking Stage"])
    correlations.append(correlation)

# Find the optimal lag (max correlation)
best_lag = np.argmax(correlations)
best_corr = correlations[best_lag]

# Plot correlation vs. lag
plt.figure(figsize=(8, 5))
plt.plot(range(max_lag + 1), correlations,
         marker="o", linestyle="-")
plt.xlabel("Lag (15-minute intervals)",
           fontsize=14, fontweight="bold")
plt.ylabel("Correlation", fontsize=14,
           fontweight="bold")
plt.xticks(range(max_lag + 1))
plt.grid(True)
plt.show()

best_lag, best_corr


# Shift Skelton Stage by 75 minutes (5 intervals)
df["Skelton Stage Lagged"] = df["Skelton Stage"].shift(5)


df_lagged = df.dropna(subset=["Skelton Stage Lagged",
                              "Viking Stage"])

S = df_lagged["Skelton Stage Lagged"].values
V = df_lagged["Viking Stage"].values


S_mean = S.mean()
V_mean = V.mean()

# Compute slope (a)
a = sum((S - S_mean) * (V - V_mean)) / sum((S - S_mean) ** 2)

# Compute intercept (b)
b = V_mean - a * S_mean

print(f"Best-fit equation: Viking Stage = {a:.4f} * Skelton Stage + {b:.4f}")

