from scipy import stats

# Percent point function (inverse of cdf — percentiles).
c = stats.norm.ppf(1-0.008, loc=0, scale=1)
print('c')
print(c.round(4))

c1 = stats.norm.ppf(0.5+0.016, loc=0, scale=1)
print('c1')
print(c1.round(4))

print(c1+c)
