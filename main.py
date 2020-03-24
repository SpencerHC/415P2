from clientClass import client


def main():
    inputFile = open("input.txt", 'r')
    print(inputFile.read())
    list = createClientList()
    print(list)


def createClientList():
    clientNum = 0
    count = 1
    value = ''
    name = ''
    inputFile = open("input.txt", 'r')
    current = "placeholder"
    arrOfClients = {}
    s = client()
    for line in inputFile:
        for ch in line:
            if ch == ' ' or ch == '\n':
                if count == 1:
                    s.setStart(int(value))
                    count +=1
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
    return arrOfClients


main()
