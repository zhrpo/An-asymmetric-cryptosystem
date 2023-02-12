def genMsgFiles(cypher, fileName):
    fo = open(fileName, 'a')
    i = 1
    for item in cypher:
        if i == len(cypher):
            fo.write('%s' % item)
        else:
            fo.write('%s,' % item)
        i += 1
    fo.write('\n')
    fo.close()

def genSigMsg(message, fileName, siganture):
    fo = open(fileName, 'a')
    i = 1
    fo.write('%s,' % message)
    for item in siganture:
        if i == len(siganture):
            fo.write('%s' % item)
        else:
            fo.write('%s,' % item)
        i += 1
    fo .write('\n')
    fo.close

def getSig(sigNum, fileName):
    fo = open(fileName, 'r')
    for i in range(0, sigNum):
        value = fo.readline().strip().split(',')
        print(str(i+1)+'.', value[0])

def getMsgCount(fileName):
    fo = open(fileName, 'r')
    x = len(fo.readlines())
    fo.close()
    return x

def getMsgLen(msgNum, fileName):
    fo = open(fileName, 'r')
    for x in range (1, (msgNum + 1)):
        values = fo.readline().strip().split(',')
        print(x, '. (length = ', len(values), ')')
    fo.close()

def delMsg(choice, fileName):
    fo = open(fileName, 'r')
    content = fo.readlines()
    i = 0
    fo.close()
    fo = open(fileName, 'w')
    for line in content:
        if i != choice-1:
            fo.write(line)
        i += 1
    fo.close

