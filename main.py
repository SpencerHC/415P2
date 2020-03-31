from clientClass import client
import copy
import time


def main():

    filename = input("Enter the file to read data: ")
    dataNumber = filename[4]


    list = createClientList(filename)



    topSorted = topSort(list)




    optimal = OptimalPath(topSorted)
    


    path = ''
    next = optimal[0][0]
    while next != len(optimal) - 1:
        path = path + ", " + str(next)
        next = optimal[next][0]

    print("Optimal revenue earned is " + str(optimal[0][1]))
    print("\nClients contributing to this optimal revenue: " + path)

    outputFile = 'outdata' + dataNumber + '.txt'
    output = open(outputFile, "w")
    output.write("Optimal revenue earned is " + str(optimal[0][1]))
    output.write("\nClients contributing to this optimal revenue: " + path)

def createClientList(filename):
    # creates a list of clients
    clientNum = 0
    count = 1
    value = ''
    inputFile = open(filename, 'r')
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
            else:
                value += ch
        if count == 3:
            s.setPay(int(value))
            count += 1
            value = ''
        count = 1
        clientNum += 1
        s.setName(str(clientNum))
        arrOfClients[clientNum] = s
        s = client()
        value = ''
    startNode = client()
    startNode.setPay(0)
    startNode.setName(str(0))
    EndNode = client()
    EndNode.setName(str(len(arrOfClients) + 1))
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

    for i in range(1, len(listOfClients) - 1):
        if listOfClients[i].getParent() == {}:
            listOfClients[0].addChild(listOfClients[i], i)
            listOfClients[i].addParent(listOfClients[0], 0)

        if listOfClients[i].getChild() == {}:
            listOfClients[len(listOfClients) - 1].addParent(listOfClients[i], i)
            listOfClients[i].addChild(listOfClients[len(listOfClients) - 1], len(listOfClients) - 1)






def OptimalPath(list):
    foundNodes = []
    for i in range(len(list)):
        foundNodes.append([None, 0])

    for i in range(len(list) - 1, -1, -1):
        max = 0
        highestFound = None
        for item in list[i].getChild().items():


            if foundNodes[item[0]][1] >= max:
                max = foundNodes[item[0]][1]


                highestFound = item[0]

        foundNodes[int(i)][0] = highestFound
        foundNodes[int(i)][1] = max + list[i].getPay()

    return foundNodes

def topSort(list):
    topSortedList = {}
    copyList = copy.deepcopy(list)
    copyList2 = list
    listOfEdgeCount = []
    for i in range(len(copyList2)):
        listOfEdgeCount.append(len(copyList[i].getParent()))
    j = 0
    pos = 0
    while j != len(listOfEdgeCount):
        if listOfEdgeCount[j] == 0:
            topSortedList[pos] = copyList2[j]
            listOfEdgeCount[j] = -1
            for key in copyList[j].getChild():
                listOfEdgeCount[key] = listOfEdgeCount[key] - 1
            j = 0
            pos += 1
        j += 1

    changeChildrenNames(topSortedList)
    return topSortedList

def changeChildrenNames(list):

    conversionList = []

    for item in list.items():
        conversionList.append([item[0],int(item[1].getName())])






    for node in list.values():
        node.reearrangeChildrenKeys(conversionList)




main()
