from scipy import stats
import math

mean_A = 1000
std_A = 100
n_A = 30
mean_B = 950
std_B = 120
n_B = 30
alpha = 0.05

t_stat = (mean_A - mean_B) / math.sqrt((std_A**2 / n_A) + (std_B**2 / n_B))

df = ((std_A**2 / n_A + std_B**2 / n_B)**2) / (
    ((std_A**2 / n_A)**2 / (n_A - 1)) +
    ((std_B**2 / n_B)**2 / (n_B - 1))
)

p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=df))

print(f"T-statistic: {t_stat:.3f}")
print(f"Degrees of freedom: {df:.2f}")
print(f"P-value: {p_value:.5f}")

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the average sales of the two stores.")
else:
    print("Fail to reject the null hypothesis: No significant difference between the average sales of the two stores.")

