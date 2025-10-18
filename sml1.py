import numpy as np

# Dataset of house prices
prices = [250000, 300000, 320000, 400000, 500000, 600000, 700000, 1200000]

# Calculate quartiles and IQR
q1 = np.percentile(prices, 25)
q3 = np.percentile(prices, 75)
iqr = q3 - q1

# Display results
print(f"25th Percentile (Q1): {q1}")
print(f"75th Percentile (Q3): {q3}")
print(f"Interquartile Range (IQR): {iqr}")

# Interpretation
print("\nInterpretation:")
print(f"The middle 50% of the house prices lie between {q1} and {q3}.")
print(f"IQR of {iqr} shows the spread of the central house prices.")
print("A smaller IQR means prices are more clustered, while a larger IQR indicates higher variability.")

