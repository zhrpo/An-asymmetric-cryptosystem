import sys, random, keyGen, keyCrypt

# Size of key in bits
keySize = 512
# A higher value will increase probability of correct isPrime() result
acc = 5 
choice = 0

while choice < 1 or choice > 3:
    print('Which user are you: ')
    print('1. Public User')
    print('2. Key Owner')
    print('3. Exit Program')
    choice = int(input('Enter Choice (1, 2, or 3): '))
    while choice > 0 and choice < 4: 
        if choice == 1: # Public User
            print('As Public User, you have the following choices:')
            print('1. Send an encrypted message')
            print('2. Authenticate a digital signature')
            print('3. Exit')
            choice = int(input('Enter Choice (1, 2, or 3): '))
            if choice == 1: # Send and encrypted message
                message = (input('Enter a message:'))
                # Encrypt and send message
                print(keyCrypt.encryptMessage(message))
                print('Encryption complete. Message sent')            
                choice = 1
            elif choice == 2: # Authenticate a digital signature
                #if #ofMessages == 0 
                    #print('No sigature to authenticate.')
                #else
                    #for int i = 0 i < #ofMessages; i++
                        #display messages
                #choice = input('Enter Choice')
                #check if signature is valid
                choice = 1
            elif choice == 3: # Exit
                choice = 4
        elif choice == 2: # Key Owner
            print('As Key Owner, you have the following choices:')
            print('1. Decrypt a recieved message')
            print('2. Digitally sign a message')
            print('3. Show the keys')
            print('4. Generate a new set of keys')
            print('5. Exit')
            choice = int(input('Enter Choice (1, 2, 3, 4, or 5): '))
            if choice == 1: # Decrypt a recieved message
                message = 'Hello, world'
                cypher = (keyCrypt.encryptMessage(message))
                print(cypher)
                #print(keyCrypt.decryptMessage(cypher))
                print(keyCrypt.decryptMessage_t(cypher))
                #if #ofencryptedmessages == 0 
                    #print('No messages to decrypt.')
                #else
                    #for int i = 0 i < #ofencryptedmessages ; i++
                        #display messages
                #choice = input('Enter Choice')
                #decrypt message
                #display decrypted message
                choice = 2 # Digitally sign a message
            elif choice == 2:
                #message = input('enter a message')
                #Sign and send message
                 choice = 2
            elif choice == 3: # Show the keys
                #display both private and public keys
                choice = 2
            elif choice == 4: # Generate a new set of keys
                name = input('Enter a name for the keys: ')
                keyGen.genKeyFiles(name, keySize, acc)
                print('Keys Created.')
                choice = 2    
        elif choice == 3: # Exit
            sys.exit('Program Exited')