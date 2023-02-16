import math, random, os, sys, testPrime

# Extended Euclidean Algorithm
def egcd(a, b):
    x,y,x1,y1,oa,ob = 0,1,1,0,a,b
    while b != 0:
        q = a // b
        q = a // b
        (a, b) = (b, a % b)
        (x, x1) = ((x1 - (q * x)), x)
        (y, y1) = ((y1 - (q * y)), y)
    if x1 < 0:
        x1 += ob
    if y1 < 0:
        y1 += oa
    return a, x1, y1

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

# Displays Key pair 
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