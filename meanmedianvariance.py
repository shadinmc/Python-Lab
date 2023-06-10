"""Aim:Table contains population and murder rates (in units of murders per
100,000
people per year) for different states. Compute the mean, median and variance
for
the population.
State Population Murder
Alabama 4,779,736 5.7
Alaska 710,231 5.6
Arizona 6,392,017 4.7
Arkansas 2,915,918 5.6
California 37,253,956 4.4
Colorado 5,029,196 2.8
Connecticut 3,574,097 2.4
Delaware 897,934 5.8""""

import numpy as np
import pandas as pd
data = {'State': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
'Connecticut', 'Delaware'],
'Population': [4779736, 710231, 6392017, 2915918, 37253956, 5029196,
3574097, 897934],
'Murder': [5.7, 5.6, 4.7, 5.6, 4.4, 2.8, 2.4, 5.8]}
df = pd.DataFrame(data)
# calculate mean
mean_pop = np.mean(df['Population'])
mean_murder = np.mean(df['Murder'])
print('Mean population:', mean_pop)
print('Mean murder rate:', mean_murder)
# calculate median
median_pop = np.median(df['Population'])
median_murder = np.median(df['Murder'])
print('Median population:', median_pop)
print('Median murder rate:', median_murder)

# calculate variance
var_pop = np.var(df['Population'])
var_murder = np.var(df['Murder'])
print('Variance of population:', var_pop)
print('Variance of murder rate:', var_murder)
