import pandas as pd
from scipy import stats
from pydataset import data
import matplotlib.pyplot as plt

mpg = data('mpg')

pop_city_mileage = mpg.cty.mean()

automatic_city_mileage = mpg[mpg.trans == 'auto'].cty

stats.ttest_1samp(automatic_city_mileage, pop_city_mileage)


# Do volkwagens get better highway mileage than average?

# - null there is no difference in the average
# alt - 

volks_hwy_mileage = mpg[mpg.manufacturer == 'volkswagen'].hwy

stats.ttest_1samp(volks_hwy_mileage, mpg.hwy.mean())

# Do compact or midsize cars get better city mileage

compact_mileage = mpg[mpg['class'] == 'compact'].cty
midsize_mileage = mpg[mpg['class']== 'midsize'].cty

stats.ttest_ind(compact_mileage,midsize_mileage)

mpg.groupby('class').hwy.mean()

# - ttest_1samp(sequence of values, population average)
# - ttest_ind(sequence of values 1: list, sequence of values 2: list)


## Correlation ##

# T-test, let us compare two catagorical variables.

# Correlation - let us compare two CONTINUOUS variables. **linear** relationship
    # number b/t -1 and 1
    # need the same amount of observations in each dataset
    # R coeffecient - means how stongly correlated the values are, and in what direction.
    # p value - how probable that the variables are correlated.

# Example: Is there a linear relationship between city mileage, and highway mileage?
    # H_0: There is no linear relationship between city mileage, and highway mileage
    # H_a: :There is a linear relationship between city mileage, and highway mileage

mpg.plot.scatter(x = 'hwy', y = 'cty')

x = mpg.hwy

y = mpg.cty

r, p =stats.pearsonr(x,y)

print(f'r = {r:.4}')
print(f'p = {p}')

# Example: Is there a linear relationship between engine displacement (displ) and city mileage (cty)?
    # H_0: There is no linear relationship between engine diplacement and city mileage.
    # H_a: There is a linear relationship between engine displacement and city mileage.

mpg.plot.scatter(x = 'displ', y = 'cty')

x = mpg.displ
y = mpg.cty

stats.pearsonr(x,y)

# Correlation IS NOT causation

