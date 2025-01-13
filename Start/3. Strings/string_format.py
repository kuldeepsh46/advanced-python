# Example file for Advanced Python by Joe Marini
# Formatting output strings

# Basic formatting - center(), ljust(), rjust()
# width = 40
# print("center".center(width, "-"))
# print("left".ljust(width, "."))
# print("right".rjust(width, ","))
# Formatting strings with format specification codes
# Format spec is: [[fill]align][sign]["z"]["#"]["0"][width][grouping_option]["."precision][type]
val1 = 1234.5678
val2 = 10987.65
val3 = 12.99
val4 = -280.7

# print(f"{val1}")
# print(f"{val2}")
# print(f"{val3}")
# print(f"{val4}")

# Specify a precision and type
# print(f"{val1:.2f}")
# print(f"{val2:.2e}")
# print(f"{val3:.2f}")
# print(f"{val4:.2e}")

# Use alignment and width and leading zeros
# < is left align, > is right align, ^ is centered
# print(f"{val1:>10.2f}")
# print(f"{val2:^10.2f}")
# print(f"{val3:<010.2f}")
# print(f"{val4:^30.2f}")

# Use a grouping option and +/- signs
# print(f"{val1:>+10,.2f}")
# print(f"{val2:^+10,.2f}")
# print(f"{val3:<+10,.2f}")
# print(f"{val4:^+30,.2f}")

# Insert a fill character
print(f"{val1:_>+10,.2f}")
print(f"{val2:_^+10,.2f}")
print(f"{val3:_<+10,.2f}")
print(f"{val4:_^+30,.2f}")

# Create format specifiers dynamically
width = 10
precision = 2
formatSpec = f"{123.456:{width}.{precision}f}"
print(formatSpec)

formatSpec = "{val:{width}.{precision}f}".format(val= val2, width = 10, precision= 2)
print(formatSpec)