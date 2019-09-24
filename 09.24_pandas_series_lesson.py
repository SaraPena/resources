import pandas as import pd

numbers = [4, 10,12,23, -2,-1,0,0,2,0,-6, 3,3, 3, 3,-7]

numbers = pd.Series(numbers)

type(numbers)
print(numbers)

numbers.index
numbers.name = "My list of numbers"
print(numbers)

vegetables = ["brussel sprouts", "yam", "arugula"]

vegetables = pd.Series(vegetables)
vegetables

pd.Series((1,2))

import numpy as np

numbers  = np.arange(1000000)
numbers = pd.Series(numbers)
numbers
numbers.head()
numbers.head(7)
numbers.tail()
numbers.head(1000) #ipython will truncate what it shows

#numbers.astype('str')
%timeit numbers * numbers

# same mask operations as numpy!
numbers % 2 == 0
numbers[numbers % 2 == 0]

vegetables == "yam"

vegetables[vegetables == "yam"]

(vegetables != "yam").any()
(vegetables == "eggplant").any()

(numbers % 2 == 0).any()
(numbers > 0).all()
(numbers > 0).any()

#do any values in the series match this comparison

numbers = [4, 10, 12, 23, -2, -1, 0, 0, 2, 0, -6, 3, 3, 3, 3,-7]
numbers = pd.Series(numbers)
numbers

x = numbers.value_counts()
numbers.unique()
type(x)
print("index is the list of unique values", x.index)
print("actual value counts", x.values)

numbers * pd.Series([1, 2, 3])

vowels = list('aeiou')
letters = list('abcdefghijk')
letters_series = pd.Series(letters)
letters_series.isin(vowels)

up_to_hundred_thousand = pd.Series(np.arange(100_000))
up_to_hundred_thousand.isin(numbers)
up_to_hundred_thousand.isin(numbers).head()

numbers

numbers.mean()
numbers.median()
numbers.describe()

vegetables.describe()

### Panda Series Apply Function ####

numbers = pd.Series(np.arange(100000))
numbers

def even_or_odd(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'

#old way:
even_or_odd(23)
even_or_odd('23') ## Type Error
even_or_odd([1, 2, 3]) ##Type Error
even_or_odd #Returns <function __main__.even_or_odd(number)> <---- Function Object


# .apply takes in a function definition into it's parens
numbers.apply(even_or_odd)
pd.Series(np.arange(100000)).apply(even_or_odd)

#another example:

len('banana') #len() is a function.

vegetables = pd.Series(['eggplant', 'tomato', 'leek', 'palm hearts', 'artichoke', 'okra'])
vegetables

vegetables.apply(len)

def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiou":
            count += 1
    return count

count_vowels("'banana'")

print(vegetables)
print(vegetables.apply(count_vowels))

# Lambdas

# Count the letter 'g' in each word

vegetables.apply(lambda x: x.count("g"))

vegetables.apply(lambda x: x.upper())

#Vectorized String Operations

vegetables.str.upper()
vegetables.str.capitalize()
vegetables.str.count("g")

vegetables.str.replace('a','z')

prices = pd.Series(['$8.99', '$4.99'])
prices.str.replace('$', "")

vegetables != 'leek'
vegetables[vegetables != 'leek']

def is_even_or_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False

mask = numbers.apply(is_even_or_odd)
mask
numbers[mask]

# Transforming Numerical to Catagorical Values

# .cut talks about binning
# w/continuous variables we can do regression - fitting a line to points on our model.
# What if we wanted to group continous data? ---> .cut opens the door for clasification alorgithms.
# [above] is on the horizon.

s = pd.Series(list(range(15)))
s

pd.cut(s, 3)
pd.cut(s, 2)
pd.cut(s, [-1, 3, 12, 16])

import matplotlib.pyplot as plt

series = pd.Series([100, 43, 26, 17])


series.plot()
series.plot.hist()

pd.Series(['a', 'b', 'a', 'c', 'b', 'a', 'd', 'a']).value_counts().plot.bar()
pd.Series(['a', 'b', 'a', 'c', 'b', 'a', 'd', 'a']).value_counts().plot.bar(color='firebrick', width=.9)
plt.title('Example Pandas Visualizations')
plt.show()


