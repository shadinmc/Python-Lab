"""Aim:if X is binomial distributed with six trials and a probability of success
equal to 0.25 at each attempt ,what is the probabilty of :a)exactly 4 success
b)Atleast one success"""

import math
def binomial_probability(n, k, p):
# Calculate the binomial coefficient
binomial_coefficient = math.comb(n, k)
# Calculate the probability
probability = binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))
return probability
# Calculate the probability of exactly 4 successes
n = 6
k = 4
p = 0.25
prob_4_successes = binomial_probability(n, k, p)
print(f"The probability of exactly 4 successes is: {prob_4_successes}")
# Calculate the probability of at least 1 success
prob_at_least_1_success = 1 - binomial_probability(n, 0, p)
print(f"The probability of at least 1 success is: {prob_at_least_1_success}")
