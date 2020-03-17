# Ex-7
# Read about the module random, it has method randint().
# https://docs.python.org/2/library/random.html
# Create a list with 100 random integers.
# Find out the frequency (how many times each integers is repeated in the list)
# Output should be a dictionary key as the random integer and value is the frequency
# Eg: random_integers_list = [1,2,3,4,1,3,6]
# outputs: frequencies = {1:2, 2:1, 3:2, 4: 1, 6: 1}

# sol:
from random import randint

def getRandomIntegers(length, start=0, end=100):
    integersList = []
    while length > 0:
        integersList.append(randint(start, end))
        length -= 1
    return integersList

def getFrequencies(numbers):
    output = {}
    for i in numbers:
        if output.get(i):
            output[i] += 1
        else:
            output[i] = 1
    return output

if __name__ == "__main__":
    randomIntegers = getRandomIntegers(100)
    print(getFrequencies(randomIntegers))