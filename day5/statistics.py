import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# parameter
lam = 4

# support (discrete values)
x = np.arange(0, 15)

# PMF and CDF
pmf = poisson.pmf(x, lam)
cdf = poisson.cdf(x, lam)

# random samples
samples = poisson.rvs(lam, size=1000)

# Plot
plt.figure(figsize=(12,4))

# PMF
plt.subplot(1,3,1)
plt.stem(x, pmf)
plt.title("Poisson PMF")

# CDF
plt.subplot(1,3,2)
plt.step(x, cdf)
plt.title("Poisson CDF")

# Histogram
plt.subplot(1,3,3)
plt.hist(samples, bins=range(15), density=True, alpha=0.7)
plt.title("Histogram (1000 samples)")

plt.tight_layout()
plt.show()

from scipy.stats import norm

# parameters
mu, sigma = 0, 1

# range
x = np.linspace(-4, 4, 100)

# PDF and CDF
pdf = norm.pdf(x, mu, sigma)
cdf = norm.cdf(x, mu, sigma)

# random samples
samples = norm.rvs(mu, sigma, size=1000)

# Plot
plt.figure(figsize=(12,4))

# PDF (not PMF for continuous!)
plt.subplot(1,3,1)
plt.plot(x, pdf)
plt.title("Normal PDF")

# CDF
plt.subplot(1,3,2)
plt.plot(x, cdf)
plt.title("Normal CDF")

# Histogram
plt.subplot(1,3,3)
plt.hist(samples, bins=30, density=True, alpha=0.7)
plt.title("Histogram (1000 samples)")

plt.tight_layout()
plt.show()

from scipy.stats import ks_2samp

# generate two datasets
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(0, 1, 1000)   # same distribution

# KS test
stat, p_value = ks_2samp(data1, data2)

print("KS statistic:", stat)
print("p-value:", p_value)