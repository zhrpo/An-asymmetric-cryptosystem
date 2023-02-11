def genMessFiles(cypher):
    fo = open('encryptedMessages.txt', 'a')
    i = 1
    for item in cypher:
        if i == len(cypher):
            fo.write('%s' % item)
        else:
            fo.write('%s,' % item)
        i += 1
    fo.write('\n')
    fo.close()

def getMessCount():
    fo = open('encryptedMessages.txt', 'r')
    x = len(fo.readlines())
    fo.close()
    return x

def getMessLen(numMess):
    fo = open('encryptedMessages.txt', 'r')
    for x in range (1, (numMess + 1)):
        values = fo.readline().strip().split(',')
        print(x, '. (length = ', len(values), ')')
    fo.close()

def delMess(choice, messNum):
    fo = open('encryptedMessages.txt', 'r')
    content = fo.readlines()
    i = 0
    fo.close()
    fo = open('encryptedMessages.txt', 'w')
    for line in content:
        if i != choice-1:
            fo.write(line)
        i += 1
    fo.close

