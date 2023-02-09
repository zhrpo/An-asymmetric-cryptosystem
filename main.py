import random, sys, os, rabinMiller, euclidAlg

def main():
    keySize = 1024
    choice = 0

    while choice < 1 or choice > 3:
        print('Which user are you: ')
        print('1. Public User')
        print('2. Key Owner')
        print('3. Exit Program')
        choice = int(input('Enter Choice (1, 2, or 3): '))
        while choice > 0 and choice < 4: 
            if choice == 1:
                print('As Public User, you have the following choices:')
                print('1. Send an encrypted message')
                print('2. Authenticate a digital signature')
                print('3. Exit')
                choice = int(input('Enter Choice (1, 2, or 3): '))
                if choice == 1:
                    message = (input('Enter a message:'))
                    # Encrypt and send message
                    print(encryptMessage(message))
                    print('Encryption complete. Message sent')
                    
                    choice = 1
                elif choice == 2:
                    #if #ofMessages == 0 
                        #print('No sigature to authenticate.')
                    #else
                        #for int i = 0 i < #ofMessages; i++
                            #display messages
                    #choice = input('Enter Choice')
                    #check if signature is valid
                    choice = 1
                elif choice == 3:
                    choice = 4
            elif choice == 2:
                print('As Key Owner, you have the following choices:')
                print('1. Decrypt a recieved message')
                print('2. Digitally sign a message')
                print('3. Show the keys')
                print('4. Generate a new set of keys')
                print('5. Exit')
                choice = int(input('Enter Choice (1, 2, 3, 4, or 5): '))
                if choice == 1:
                    #if #ofencryptedmessages == 0 
                        #print('No messages to decrypt.')
                    #else
                        #for int i = 0 i < #ofencryptedmessages ; i++
                            #display messages
                    #choice = input('Enter Choice')
                    #decrypt message
                    #display decrypted message
                    choice = 2
                elif choice == 2:
                    #message = input('enter a message')
                    #Sign and send message
                    choice = 2
                elif choice == 3:
                    #display both private and public keys
                    choice = 2
                elif choice == 4:
                    name = input('Enter a name for the keys: ')
                    genKeyFiles(name, keySize)
                    print('Keys Created.')
                    choice = 2    
            elif choice == 3:
                sys.exit('Program Exited')

def genKey(keySize):
    p = rabinMiller.generateLargePrime(keySize)
    q = rabinMiller.generateLargePrime(keySize)
    n = p * q
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if euclidAlg.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    d = euclidAlg.modInverse(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)
    return (publicKey, privateKey)

def genKeyFiles(name, keySize):
    publicKey, privateKey = genKey(keySize)
    fo = open('%s_publickey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()

    fo = open('%s_privatekey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()
    
def encryptMessage(message):
    fo = open('New Keys_publickey.txt' , 'r')
    values = fo.readline().strip().split(',')
    n = values[0]
    e = values[1]
    cypher = pow(int.from_bytes(bytes(message,"utf-8"),"big"), int(e), int(n))
    return cypher
    

main()