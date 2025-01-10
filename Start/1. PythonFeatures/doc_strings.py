# Example file for Advanced Python by Joe Marini
# Demonstrate the use of documentation strings


def myFunction(arg1, arg2=None):
    """
    myFunction(arg1, arg2=None) --> Do nothing
    
    Parameters:
    arg1: the first argument
    arg2: the second argument which is None by defualt.
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
