import numpy as np
import matplotlib.pyplot as plt

# Setting seed for reproducibility
np.random.seed(42)

# Population: Salaries following a skewed (lognormal) distribution
pop_sal = np.random.lognormal(mean=10, sigma=0.5, size=100000)

# Draw 10 random samples (each with 50 engineers) and compute their means
sample_means = []
for _ in range(10):
    sample = np.random.choice(pop_sal, size=50, replace=False)
    sample_means.append(np.mean(sample))

# Plot histogram of sample means
plt.figure(figsize=(8, 5))
plt.hist(sample_means, bins=6, color='skyblue', edgecolor='black')
plt.xlabel('Sample Mean Salary')
plt.ylabel('Frequency')
plt.title('Distribution of Sample Means (10 samples, n=50)')
plt.show()

# Display sample means
print("Sample Means:\n", np.round(sample_means, 2))

# Interpretation
print("\nInterpretation:")
print("Even though the population salary distribution is skewed (lognormal),")
print("the distribution of sample means appears approximately normal.")
print("According to the Central Limit Theorem, as sample size increases,")
print("the sampling distribution of the mean tends to become normal,")
print("regardless of the population’s original distribution.")

