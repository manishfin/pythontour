# Ex-6
# Write a function which takes a number as argument.
# Print all odd numbers till that number.


'''
print_odd_numbers(20)
'''
# Output:
#1
#3
#5
#7
#9
#11
#13
#15
#17
#19

# sol:
def print_odd_numbers(number):
    for i in range(number):
        if i % 2 != 0:
            print (i)

print_odd_numbers(20)