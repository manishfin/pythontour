# Ex-5
# Read about the module random, it has method randint().
# https://docs.python.org/2/library/random.html
# Create a list with 100 random integers.

# sol:
from random import randint

def getRandomIntegers(length, start=0, end=100):
    integersList = []
    while length > 0:
        integersList.append(randint(start, end))
        length -= 1
    return integersList

if __name__ == "__main__":
    print(getRandomIntegers(100))