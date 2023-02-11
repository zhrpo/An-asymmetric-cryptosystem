def encryptMessage(message):
    fo = open('test_publickey.txt' , 'r')
    values = fo.readline().strip().split(',')
    n = values[1] # Changed because values[0] equals keySize
    e = values[2]
    cypher= []
    for x in range(len(message)):
        to_cypher = pow(message[x], int(e), int(n))
        cypher.append(to_cypher)
    return cypher
    #return to_cypher

# Copy of function above 
def decryptMessage(cypher):
    fo = open('test_privatekey.txt' , 'r')
    values = fo.readline().strip().split(',')
    n = values[1]
    d = values[2]
    message = ""
    for x in range(len(cypher)):
        to_message= pow(cypher[x], int(d), int(n))
        message += chr(to_message)
    return str(message)