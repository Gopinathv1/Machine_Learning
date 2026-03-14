import numpy as np
from scipy import stats

# Example: One-sample t-test
# Sample data
data = np.array([2.3, 2.5, 2.8, 3.0, 2.7, 2.9, 3.1, 2.6, 2.8, 3.2])
# Population mean to test against
mu = 2.5

# Perform one-sample t-test
t_stat, p_value = stats.ttest_1samp(data, mu)

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Interpret result
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: The sample mean is significantly different from the population mean.")
else:
    print("Fail to reject the null hypothesis: No significant difference between sample mean and population mean.")
