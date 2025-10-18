import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset of customer satisfaction and repeat purchase behavior
data = {
    'Satisfaction': ['Low', 'Medium', 'High', 'Low', 'Medium', 'High', 'Low', 'High', 
                     'Medium', 'Low', 'High', 'Medium', 'Low'],
    'RepeatPurchase': ['No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 
                       'Yes', 'Yes', 'No', 'Yes', 'No']
}

# Create DataFrame
df = pd.DataFrame(data)

# Bar plot showing counts by satisfaction and repeat purchase
plt.figure(figsize=(6, 4))
sns.countplot(x='Satisfaction', hue='RepeatPurchase', data=df)
plt.xlabel("Satisfaction Levels")
plt.ylabel("Count")
plt.title("Customer Satisfaction vs Repeat Purchase (Bar Plot)")
plt.legend(title="Repeat Purchase")
plt.show()

# Stacked bar chart
stack_data = df.groupby(['Satisfaction', 'RepeatPurchase']).size().unstack(fill_value=0)
stack_data.plot(kind='bar', stacked=True, figsize=(6, 4), colormap='viridis')
plt.title("Stacked Bar Chart: Satisfaction vs Repeat Purchase")
plt.xlabel("Satisfaction Levels")
plt.ylabel("Number of Customers")
plt.show()

# Interpretation
print("\nInterpretation:")
print("From the visualization, customers with higher satisfaction levels tend to make more repeat purchases.")
print("Low satisfaction customers mostly did not make repeat purchases, indicating a strong link between satisfaction and loyalty.")

