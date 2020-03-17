# Ex-2
# Write a function say_hello which takes arbitrary number of names as argument
#and prints hello, <name>

'''
say_hello('goutham')

# Output: Hello, goutham

say_hello('goutham','ng','pg')
'''
# Output:
# Hello, goutham
# Hello, ng
# Hello, pg

# sol:
def say_hello(*names):
    for name in names:
        print ("Hello,", name)

if __name__ == "__main__":
    say_hello('goutham','ng','pg')