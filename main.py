import sys, random, keyGen, keyCrypt, manageFiles

#comment
# Size of key in bits
keySize = 512
# A higher value will increase probability of correct isPrime() result
acc = 5 
choice = 0
encryptMsgs = 'encryptedMessages.txt'
signedMsgs = 'signedMessages.txt'
pubKey = 'publickey.txt'
privKey = 'privatekey.txt'

while choice < 1 or choice > 3:
    print('Which user are you: ')
    print('1. Public User')
    print('2. Key Owner')
    print('3. Exit Program')
    while True:
        try: 
            choice = int(input('Enter Choice: '))
            if choice < 0 or choice > 3:
                print("\nERROR: Please select value between 1-3.")

        except ValueError:
            print("\nERROR: Please select value between 1-3.\n")
            continue
        else:
            break
        
            
    while choice > 0 and choice < 4: 
        if choice == 1: # Public User
            print('As Public User, you have the following choices:')
            print('1. Send an encrypted message')
            print('2. Authenticate a digital signature')
            print('3. Exit')
            while True:
                try: 
                    choice = int(input('Enter Choice: '))
                    if choice < 1 or choice > 3:
                        print("\nERROR: Please select value between 1-3.")

                except ValueError:
                    print("\nERROR: Please select value between 1-3.\n")
                    continue
                else:
                    break
            if choice == 1: # Send and encrypted message
                message = (input('Enter a message: '))
                manageFiles.genMsgFiles(keyCrypt.encryptMessage(message.encode('utf-8'), pubKey),encryptMsgs)
                print('Encryption complete. Message sent')           
                choice = 1
            elif choice == 2: # Authenticate a digital signature
                sigNum = manageFiles.getMsgCount(signedMsgs)
                if sigNum != 0:
                    print('You have ', sigNum, 'messages:' )
                    manageFiles.getSig(sigNum, signedMsgs)
                    choice = int(input('Enter Choice: '))
                    valid = keyCrypt.verify(choice, pubKey, signedMsgs)
                    if valid:
                        print('Signature is Valid')
                    else:
                        print('Signature is NOT valid')
                    manageFiles.delMsg(choice, signedMsgs)
                else:
                    print('No signatures found')
                choice = 1
            elif choice == 3: # Exit
                choice = 4
        elif choice == 2: # Key Owner
            print('As Key Owner, you have the following choices:')
            print('1. Decrypt a received message')
            print('2. Digitally sign a message')
            print('3. Show the keys')
            print('4. Generate a new set of keys')
            print('5. Exit')
            while True:
                try: 
                    choice = int(input('Enter Choice: '))
                    if choice < 1 or choice > 5:
                        print("\nERROR: Please select value between 1-5.")

                except ValueError:
                    print("\nERROR: Please select value between 1-5.\n")
                    continue
                else:
                    break
            if choice == 1: # Decrypt a recieved message
                msgNum = manageFiles.getMsgCount(encryptMsgs)
                if msgNum != 0:
                    print('You have ', msgNum, ' messages:' )
                    manageFiles.getMsgLen(msgNum,encryptMsgs)
                    choice = int(input('Enter Choice: '))
                    print('Decrypted message: ', keyCrypt.decryptMessage((choice), privKey, encryptMsgs))
                    manageFiles.delMsg(choice, encryptMsgs)
                else:
                    print('You have zero messages')
                choice = 2 
            elif choice == 2: # Digitally sign a message
                message = input('Enter a message: ')
                signature = keyCrypt.encryptMessage(message.encode('utf-8'), privKey)
                manageFiles.genSigMsg(message, signedMsgs, signature)
                print('Signed Message sent')  
                choice = 2
            elif choice == 3: # Show the keys
                keyGen.displaykeys(pubKey, privKey)
                choice = 2
            elif choice == 4: # Generate a new set of keys
                if manageFiles.getMsgCount(encryptMsgs) > 0:
                    ui = input('All remaining messages and signatures will no longer be valid and will be deleted. Continue? (Y/N): ')     
                    if ui == 'Y' or ui == 'y':
                        fo = open(encryptMsgs, 'r+')
                        fo.truncate(0)
                        fo.close()
                        fo = open(signedMsgs, 'r+')
                        fo.truncate(0)
                        fo.close()
                        keyGen.genKeyFiles(keySize, acc)
                        print('Keys Created.')
                else:
                    keyGen.genKeyFiles(keySize, acc)
                    print('Keys Created.')
                choice = 2
        elif choice == 3: # Exit
            sys.exit('Program Exited')