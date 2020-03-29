from clientClass import client


def main():
    inputFile = open("input.txt", 'r')
    print(inputFile.read())
    list = createClientList()
    print(list)
    #constructDAG(list)
    # print(list['client1'].getStart())
    # example above on how to access the attributes in client

    OptimalPath(list)


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
        arrOfClients[clientNum] = s
        s = client()
        value = ''
    startNode = client()
    startNode.setPay(0)
    EndNode = client()
    EndNode.setPay(0)
    arrOfClients[0] = startNode
    arrOfClients[len(arrOfClients)] = EndNode
    constructDAG(arrOfClients)
    return arrOfClients


def constructDAG(clients):
    edgeHelper(clients)


def edgeHelper(listOfClients):
    for i in range(1, len(listOfClients) - 1):
        for j in range(1, len(listOfClients) - 1):
            if listOfClients[i].getEnd() <= listOfClients[j].getStart():
                listOfClients[i].addChild(listOfClients[j], j)
                listOfClients[j].addParent([i], i)
                print('child of client' + str(i) + ' is client' + str(j))

    for i in range(1, len(listOfClients) - 1):
        if listOfClients[i].getParent() == {}:
            listOfClients[0].addChild(listOfClients[i], i)
            listOfClients[i].addParent(listOfClients[0], 0)

        if listOfClients[i].getChild() == {}:
            listOfClients[len(listOfClients)-1].addParent(listOfClients[i], i)
            listOfClients[i].addChild(listOfClients[len(listOfClients)-1],len(listOfClients)-1)
    print(len(listOfClients))



    #print(listOfClients['client{0}'.format('End')].getParent())


def OptimalPath(list):
    foundNodes = []
    for i in range (len(list)):
        foundNodes.append([None,0])


    for i in range(len(list)-1,-1,-1):
        max = 0
        highestFound = None
        for item in list[i].getChild().items():
            print(item[0])
            if foundNodes[item[0]][1] >= max:

                max = foundNodes[item[0]][1]
                highestFound = item[0]
        print(type(i))
        foundNodes[int(i)][0] = highestFound
        foundNodes[int(i)][1] = max + list[i].getPay()
    
    print(foundNodes)
















main()
