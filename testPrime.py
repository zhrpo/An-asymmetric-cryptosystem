import random

# Similar to and preferred over Fermat's method
# Time Complexity: O(k log n)
def rabinMill(d, num):
    rnum = 2 + random.randint(1, num - 4)
    x = pow(rnum, d, num)
    if (x == 1 or x == num - 1):
        return True
    while(d != num - 1):
        x = (x * x) % num
        d *= 2
        if (x == 1):
            return False
        if (x == num - 1):
            return True
    return False

# Test to determine if number is prime
def isPrime(num, acc):
    if (num <= 1 or num == 4):
        return False
    if (num <= 3):
        return True
    d = num - 1
    while (d % 2 == 0):
        d //= 2
    for i in range(acc):
        if (rabinMill(d, num) == False):
            return False
    return True

# Generates large numbers to be tested if prime
def generateLargePrime(keySize, acc):
    while True:
        num = random.randrange(2**(keySize-1), 2**(keySize))
        if isPrime(num, acc):
            return num

