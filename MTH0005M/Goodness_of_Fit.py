import scipy.stats as stats

expected = [3.74, 6.25, 5.45, 2.49, 0.592]           #Input expected values
observed = [6, 8, 2, 3, 1]                           #Input observed values

x = stats.chisquare(f_obs=observed, f_exp=expected)  #Calculate chi-squared value and p value

print(x)