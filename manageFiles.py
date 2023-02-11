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

