import numpy as np
numbers = list(range(100000))
numbers = np.array(numbers)
type(numbers)

len(numbers)
numbers * 2
numbers.shape

x = np.array([1, 2, 3])
y = np.array([2, 3, 4])
x +y
x-y
x * y
x.dot(y)
x / y

numbers
numbers.mean()
numbers.min()
numbers.max()
numbers + 3

# Add one to every number in a list of ten million numbers.
numbers = list(range(10000000))
%timeit [number + 1 for number in numbers]
numbers = np.array(numbers)
%timeit numbers + 1

#Generate a thousand random numbers between 1 and 1000
import random
%timeit [random.randint(1, 10000) for _ in range(1000)]

%timeit np.random.randint(1000, size = 1000)

#Exercise help:
numbers
divisible_by_fifteen = numbers[numbers % 15 == 0]
divisible_by_fifteen[1:5]

evens = numbers[numbers % 2 == 0]
evens

x = np.array([1, 2, 3])
x/x
x-x
np.zeros(10)
np.ones(10)

ones = np.ones((30, 3))
ones

numbers = np.array([-5, 10, 11, 13, 15, -5, 0, 0, 0, 1, 1,3, -4, -4])
numbers == 10 # Boolean mask, this statment returned an array of booleans.

mask_above_ten = numbers >= 10
numbers[mask_above_ten]


# Can work on this with pandas
fruits = np.array(["banana", "kiwi", "strawberry", "mango", "tomato"])
type(fruits)
type(fruits[0])

for fruit in fruits:
    print(fruit)

#working with random numbers
import random
np.random.rand(10)


numbers.min()
numbers.max()
numbers.mean()
numbers.sum()
numbers.std()
np.median(numbers)

np.arange(100,200)

np.full(10, 3.3)
