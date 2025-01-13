# Example file for Advanced Python by Joe Marini


sample_text = "The quick brown fox jumps over the lazy dog."
tempStr = sample_text.lower()
# Using find() to find the first occurrence of a substring
# print("First occurrence of 'the' is:", sample_text.find("the"))
# print("First occurrence of 'the' is:", tempStr.find("the"))

# Example with optional start and end parameters
# print("First occurrence of 'the' is:", tempStr.find("the", 5, 36))

# Using index() to find the first occurrence of a substring (raises ValueError if not found)
print("First occurrence of 'fox':", tempStr.index("fox"))
# print("First occurrence of 'fox':", tempStr.index("faox"))

try:
    print("First occurrence of 'fox':", tempStr.index("fax"))
    
except ValueError:
    print("Not Found.")
# The 'in' operator can be used for Boolean testing:
print("Is 'fox' present:", "fox" in tempStr)

# Using rfind() to find the last occurrence of a substring
print("Last occurence of 'the':", tempStr.rfind("the"))

# Using rindex() to find the last occurrence of a substring (raises ValueError if not found)
# print("Last occurence of 'the':", tempStr.rindex("ethe"))
try:
    print("Last occurence of 'the':", tempStr.rindex("ethe"))
    
except ValueError:
    print("Not Found.")

# The replace() function will find content in the string and replace it
replacedString = sample_text.replace("lazy", "tired")
print(replacedString)
