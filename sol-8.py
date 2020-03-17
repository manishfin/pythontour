# Ex-8
# Write a function isPrime, that takes a number as argument.
# Returns true if it is a prime number, false if it is not.
# Eg: is_prime(20) -> False, is_prime(13) -> True

# sol:
def is_prime(num):
    if (num <= 1):
        return False
    if (num <= 3):
        return True
    if (num % 2 == 0 or num % 3 == 0):
        return False
    i = 5
    while(i * i <= num) :
        if (num % i == 0 or num % (i + 2) == 0) :
            return False
        i = i + 6
    return True

if __name__ == "__main__":
    print (is_prime(20))
    print (is_prime(13))