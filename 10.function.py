# Theory of FUNCTIONS

# FUNCTION BUILT-IN

# random
import random

a = [1,2,3,4]
print(random.choice(a))
print(random.sample(a,2))

# itertool
import itertools as it
#cycle
for index, item in enumerate(it.cycle(a)):
    print(index, item, "Edmar")
    if index >= 10:
        break

b = it.repeat(a,4)
print(list(b))
# output > [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]


# accumulate > Return series of accumulated sums (or other binary function results).
c = it.accumulate(a)
print(list(c))
#output > [1, 3, 6, 10]
print(it.accumulate.__doc__)

# PERMUTATIONS
"""
Return successive r-length permutations of elements in the iterable.
permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)
"""

d = it.permutations("ABC", 2)
print(list(d))
print(d.__doc__) 
# output > [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# COMBINATION
"""
Return successive r-length combinations of elements in the iterable.
combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)
"""
e = it.combinations("ABC", 2)
print(list(e))
print(e.__doc__)
#output > [('A', 'B'), ('A', 'C'), ('B', 'C')]

import functools as ft
# It is used to moniterate function
