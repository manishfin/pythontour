# Ex-12
# Write a class Prime.
# It supports the following operations:
# Check out this article to find primes in an optimized way.
# http://stackoverflow.com/a/5813926/2131120
'''
p = Prime()
p.nthprime(100) # prints 100th prime
p.nextprime(2) # 3. It should return 2 for all numbers <= 1
p.previousprime(3) # 2. It should return 2 for all numbers <=2
p.getallprimes(10) # 2, 3, 5, 7
'''

# sol:
from itertools import count, islice

class Prime:
    def isPrime(self, num):
        return all(num % i for i in range(2, int(num**0.5) + 1)) and num > 1

    def generatePrimes(self):
        yield 2
        for num in count(3, 2):
            if self.isPrime(num): yield num
    
    def nthPrime(self, num):
        return next(islice(self.generatePrimes(), num, None))

    def nextPrime(self, num):
        if num <= 1: return 2
        nextNum = num + 1
        while True:
            if self.isPrime(nextNum): return nextNum
            nextNum += 1
        
    def previousPrime(self, num):
        if num <= 2: return 2
        preNum = num - 1
        while True:
            if self.isPrime(preNum): return preNum
            preNum -= 1

    def getAllPrimes(self, num):
        return [i for i in range(2, num+1) if self.isPrime(i)]

p = Prime()
print(p.nthPrime(100))
print(p.nextPrime(2))
print(p.previousPrime(3))
print(p.getAllPrimes(10))