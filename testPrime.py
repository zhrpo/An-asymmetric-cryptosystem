import random

# Testing primality using Fermat's Little Theorem
def isPrime(num, acc):
    for i in range(acc):
        randNum = random.randint(2, num - 2)
        if pow(randNum, num-1, num) != 1:
            return False
    return True


# Generates large numbers to be tested if prime
def generateLargePrime(keySize, acc):
    while True:
        num = random.randrange(2**(keySize-1), 2**(keySize))
        #if isPrime(num, acc):
        #    return num
        if isPrime(num, acc):
            return num

