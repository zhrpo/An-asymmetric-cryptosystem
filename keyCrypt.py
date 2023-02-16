# Encrypts message using public key
# Also signs a message using private key
# Fast Modular Exponentiation
def encryptMessage(message, key):
    fo = open(key, 'r')
    values = fo.readline().strip().split(',')
    n = values[1]
    e_or_d = values[2]
    fo.close()
    cypher= []
    for x in range(len(message)):
        to_cypher = pow(message[x], int(e_or_d), int(n))
        cypher.append(to_cypher)
    return cypher

# Decrypts message using private key
# Fast Modular Exponentiation
def decryptMessage(choice, key, msg):
    fo = open(key , 'r')
    values = fo.readline().strip().split(',')
    n = values[1]
    e_or_d = values[2]
    fo.close()
    fo = open(msg)
    if choice != 1:
        for i in range (1, choice+1):
            if i == choice:
                cypher = fo.readline().strip().split(',')
            else:
                fo.readline()
    else:
        cypher = fo.readline().strip().split(',')
    fo.close
    message = ""
    for x in range(len(cypher)):
        to_message= pow(int(cypher[x]), int(e_or_d), int(n))
        message += chr(to_message)
    return str(message)

# Verifies a signature using public key
# Fast Modular Exponentiation
def verify(choice, key, sig):
    fo = open(key , 'r')
    values = fo.readline().strip().split(',')
    n = values[1]
    e_or_d = values[2]
    fo.close()
    fo = open(sig)
    if choice != 1:
        for i in range (1, choice+1):
            if i == choice:
                cypher = fo.readline().strip().split(',')
            else:
                fo.readline()
    else:
        cypher = fo.readline().strip().split(',')
    orig_sig = cypher[0]
    cypher.pop(0)
    fo.close
    message = ""
    for x in range(len(cypher)):
        to_message= pow(int(cypher[x]), int(e_or_d), int(n))
        message += chr(to_message)
    return (orig_sig == message)