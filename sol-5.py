# Ex-5
# Read about the module random, it has method randint().
# https://docs.python.org/2/library/random.html
# Create a list with 100 random integers.

# sol:
from random import randint

def getRandomIntegers(length, start=0, end=100):
    return [randint(start, end) for i in range(length + 1)]

if __name__ == "__main__":
    print(getRandomIntegers(100))