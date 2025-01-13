# Example file for Advanced Python by Joe Marini
# The for-else loop construct

names = ["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"]

# The else clause on a for loop is only executed if the loop completes every iteration
def findname(target):
    for name in names:
        if name == target:
            print("Name found");
            return True
    
    print("Name not found")
    return False

# print(findname("Creed"))
# print(findname("Tom"))

# Check if a number is prime
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime no")
            break
    else:
        print(num, 'is a prime no')
isPrime(31)
isPrime(10)