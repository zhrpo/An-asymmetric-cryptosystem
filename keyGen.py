import math, random, os, sys, testPrime

# Extended Euclidean Algorithm
# Time Complexity: O(log(max(A,B)))
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    (g, y, x) = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

# Modular inverse
def modInv(a,m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m
        
# RSA Algorithm
def genKey(keySize, acc):
    p = testPrime.generateLargePrime(keySize, acc)
    q = testPrime.generateLargePrime(keySize, acc)
    n = p * q
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if math.gcd(e, (p - 1) * (q - 1)) == 1:
            break
    d = modInv(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)
    return (publicKey, privateKey)

# Generates files to store key pairs in
def genKeyFiles(name, keySize, acc):
    publicKey, privateKey = genKey(keySize, acc)
    fo = open('%s_publickey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()

    fo = open('%s_privatekey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()