import math, random, os, sys, testPrime

# Extended Euclidean Algorithm
# Time Complexity: O(log(max(A,B)))
def egcd(a, b):
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a
    ob = b

    while b != 0:
        q = a // b
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob
    if ly < 0:
        ly += oa
    return a, lx, ly

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
    e = 65537
    while True:
        
        if math.gcd(e, (p - 1) * (q - 1)) == 1:
            break
        else:
            e = e+1
    d = modInv(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)
    return (publicKey, privateKey)

# Generates files to store key pairs in
def genKeyFiles(keySize, acc):
    publicKey, privateKey = genKey(keySize, acc)
    fo = open('publickey.txt', 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()

    fo = open('privatekey.txt', 'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()

def displaykeys(pubKey, privKey):
    fo = open(pubKey, 'r')
    values = fo.readline().strip().split(',')
    print('##########')
    print('PUBLIC KEY')
    print('##########')
    print('n: ', values[1])
    print('e: ', values[2])
    fo.close()
    fo = open(privKey, 'r')
    values = fo.readline().strip().split(',')
    print('##########')
    print('PRIVATE KEY')
    print('##########')
    print('n: ', values[1])
    print('d: ', values[2])
    fo.close()

