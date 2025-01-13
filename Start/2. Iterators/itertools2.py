# Example file for Advanced Python by Joe Marini
# Itertools: chain, chain.from_iterable

import itertools


# chain() creates a single iterable from multiple
combinedIterator = itertools.chain("ABCD", "1234", "XYZ")
print(list(combinedIterator))

# make a prepend function
def prepend(val, iterable):
    return itertools.chain([val], iterable)
print(list(prepend("A", "BCDE")))

# chain.from_iterable is an alternate usage of chain
s1 = "ABCDEFG"
s2 = [1,2,3,4,5]
s3 = ['$','%','@','&']
result = itertools.chain.from_iterable([s1, s2, s3])
print(list(result))