# Ex-11
# Accomplish the following using string slicing
# Print excluding first 2 characters
# Print first 4 characters
# Print every alternate letter
# Reverse the string

# sol:
def print_string_excluding_2_chars(string):
    print(string[2:])
def print_first_4_chars(string):
    print(string[:4])
def print_alternate_chars(string):
    print(string[::2])
def print_reversed_string(string):
    print(string[::-1])

animal = 'elephant'
print_string_excluding_2_chars(animal)
print_first_4_chars(animal)
print_alternate_chars(animal)
print_reversed_string(animal)