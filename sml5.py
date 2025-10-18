import scipy.stats as stats
import numpy as np

# Given data
n = 20
mean_sample = 8
std_dev = 2
mu0 = 0  # Null hypothesis mean

# Calculate standard error and t-statistic
SE = std_dev / np.sqrt(n)
t_stat = (mean_sample - mu0) / SE
df = n - 1  # Degrees of freedom

# Two-tailed p-value
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))

# Critical t-value for 5% significance level (two-tailed)
t_critical = stats.t.ppf(1 - 0.025, df)

# Display results
print(f"Sample Mean: {mean_sample}")
print(f"Standard Deviation: {std_dev}")
print(f"T-Statistic: {t_stat:.4f}")
print(f"Degrees of Freedom: {df}")
print(f"Critical t-Value (±): {t_critical:.4f}")
print(f"P-Value: {p_value:.6f}")

# Decision
if p_value < 0.05:
    print("\nConclusion: Reject the null hypothesis — the drug significantly affects heart rate.")
else:
    print("\nConclusion: Fail to reject the null hypothesis — no significant effect detected.")

