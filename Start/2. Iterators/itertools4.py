# Example file for Advanced Python by Joe Marini
# Itertools: combinations and permutations

import itertools


# product() produces the cartesian product of input iterables
cards = "A23456789TJQK"
suits = "SCHD"
deck = list(itertools.product(cards, suits))
# print(len(deck), "Cards")
# print(deck)
# permutations() creates tuples of a given length with no repeated elements
#suppose each team will play with all other teams twice (home and away). Find total no of matches for a team
teams = ("A","B","C","D")
totalMatches = itertools.permutations(teams, 2)
# print(list(totalMatches))


# combinations() will create combinations of a given length with no repeats
combinaions = itertools.combinations("ABCD", 2)
combinaions = itertools.combinations(teams, 3)
print(list(combinaions))

# combinations_with_replacement() will create combinations of a given length with repeats
totalCombinations = itertools.combinations_with_replacement("ABCD", 2)
print(list(totalCombinations))