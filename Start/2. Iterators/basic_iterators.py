# Example file for Advanced Python by Joe Marini
# Working with basic iterators

# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

# use regular interation over the days
# for d in days:
#     print(d)

# use iter() to create an iterator over a collection
i = iter(days)

# the next() function retrieves the next value from an iterator
# print(next(i))

# iterate using a function and a sentinel
with open("/workspaces/advanced-python/Start/2. Iterators/testfile.txt", "r") as fp:
    for line in iter(fp.readline, ''):
        print(line)