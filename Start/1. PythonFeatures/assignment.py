# Example file for Advanced Python by Joe Marini
# The assignment expression operator := (or the "walrus" operator)

import pprint


# regular assignment statements assign a value
x = 5
# print(x)

# the assignment operator is part of an expression
(x := 10)
# print(x)

# The assignment expression is useful for writing concise code

# without assignment operator
# str = input("Enter str value: ")
# while(str != "exit"):
#     print(str)
#     str = input("Enter str value: ")

# with assignment operator
# while(str := input("Enter str value: ")) != "exit":
#     print(str)
# The walrus operator can help reduce redundant function calls

#wihtout using assignment operator
values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
# l = len(values)
# s = sum(values)
# val_data = {
#     "length": l,
#     "total": s,
#     "average": s/l
# }
#with using assignment operator
val_data = {
    "length": (l := len(values)),
    "total": (s := sum(values)),
    "average": s/l
}
print(val_data)
pprint.pp(val_data)