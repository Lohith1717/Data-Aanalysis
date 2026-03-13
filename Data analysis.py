import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("matplotlib_practice_dataset.csv")

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Summary:")
print(df.describe())


plt.scatter(df["Temperature_C"], df["IceCream_Sales"])

plt.title("Temperature vs Ice Cream Sales")
plt.xlabel("Temperature (°C)")
plt.ylabel("Ice Cream Sales")

plt.show()

print("\nInsight 1:")
print("Ice cream sales increase when the temperature rises.")

plt.plot(df["Day"], df["Visitors"])

plt.title("Visitors Trend Over Days")
plt.xlabel("Day")
plt.ylabel("Number of Visitors")

plt.show()

print("\nInsight 2:")
print("Visitor numbers change across different days showing peaks and drops.")