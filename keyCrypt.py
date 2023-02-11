def encryptMessage(message, fileName):
    fo = open(fileName , 'r')
    values = fo.readline().strip().split(',')
    n = values[1] # Changed because values[0] equals keySize
    e = values[2]
    fo.close()
    cypher= []
    for x in range(len(message)):
        to_cypher = pow(message[x], int(e), int(n))
        cypher.append(to_cypher)
    return cypher
    #return to_cypher

# Copy of function above 
def decryptMessage(choice, fileName):
    fo = open(fileName , 'r')
    values = fo.readline().strip().split(',')
    n = values[1]
    d = values[2]
    fo.close()
    fo = open('encryptedMessages.txt')
    for i in range (1, choice + 1):
        if i == choice:
            cypher = fo.readline().strip().split(',')
        else:
            fo.readline()
    fo.close
    message = ""
    for x in range(len(cypher)):
        to_message= pow(int(cypher[x]), int(d), int(n))
        message += chr(to_message)
    return str(message)