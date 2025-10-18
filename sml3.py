import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset: Car details
data = {
    'EngineSize': [1.3, 1.5, 2.0, 2.2, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5],
    'FuelEfficiency': [35, 33, 30, 28, 25, 22, 20, 18, 16, 15],
    'CarPrice': [15000, 18000, 22000, 25000, 30000, 35000, 40000, 45000, 50000, 60000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Pair plot to visualize relationships
sns.pairplot(df, diag_kind='kde', kind='reg')
plt.suptitle('Pair Plot of Car Data', y=1.02, fontsize=14)
plt.show()

# Correlation matrix
corr = df.corr()
print("Correlation Matrix:\n", corr, "\n")

# Heatmap for correlation visualization
plt.figure(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix Heatmap")
plt.show()

# Interpretation
print("Interpretation:")
print("• Engine size and car price show a strong positive correlation — larger engines usually mean higher-priced cars.")
print("• Engine size and fuel efficiency have a strong negative correlation — bigger engines consume more fuel.")
print("• Practically, this means customers pay more for powerful cars but get lower mileage.")

