from clientClass import client


def main():
    inputFile = open("input.txt", 'r')
    print(inputFile.read())
    list = createClientList()
    print(list)
    constructDAG(list)
    # print(list['client1'].getStart())
    # example above on how to access the attributes in client


def createClientList():
    # creates a list of clients
    clientNum = 0
    count = 1
    value = ''
    inputFile = open("input.txt", 'r')
    arrOfClients = {}
    s = client()
    for line in inputFile:
        for ch in line:
            if ch == ' ' or ch == '\n':
                if count == 1:
                    s.setStart(int(value))
                    count += 1
                    value = ''
                elif count == 2:
                    s.setEnd(int(value))
                    count += 1
                    value = ''
                elif count == 3:
                    s.setPay(int(value))
                    count += 1
                    value = ''

            else:
                value += ch
        count = 1
        clientNum += 1
        arrOfClients['client{0}'.format(clientNum)] = s
        s = client()
        value = ''
    startNode = client()
    EndNode = client()
    arrOfClients['client{0}'.format('Start')] = startNode
    arrOfClients['client{0}'.format('End')] = EndNode
    constructDAG(arrOfClients)
    return arrOfClients


def constructDAG(clients):
    edgeHelper(clients)


def edgeHelper(listOfClients):
    for i in range(1, len(listOfClients) - 1):
        for j in range(1, len(listOfClients) - 1):
            if listOfClients['client{0}'.format(i)].getEnd() <= listOfClients['client{0}'.format(j)].getStart():
                listOfClients['client{0}'.format(i)].addChild(listOfClients['client{0}'.format(j)], j)
                listOfClients['client{0}'.format(j)].addParent(listOfClients['client{0}'.format(i)], i)
                print('child of client' + str(i) + ' is client' + str(j))

    for i in range(1, len(listOfClients) - 1):
        if listOfClients['client{0}'.format(i)].getParent() == {}:
            listOfClients['client{0}'.format('Start')].addChild(listOfClients['client{0}'.format(i)], i)
            listOfClients['client{0}'.format(i)].addParent(listOfClients['client{0}'.format('Start')], 'Start')

        if listOfClients['client{0}'.format(i)].getChild() == {}:
            listOfClients['client{0}'.format('End')].addParent(listOfClients['client{0}'.format(i)], i)
            listOfClients['client{0}'.format(i)].addChild(listOfClients['client{0}'.format('End')], 'End')

    #print(listOfClients['client{0}'.format('End')].getParent())


main()
