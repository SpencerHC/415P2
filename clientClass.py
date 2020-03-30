from sqlalchemy.sql.elements import Null


class client:
    childCount = 0
    parentCount = 0

    def __init__(self):
        self.name = ''
        self.start = 0
        self.end = 0
        self.pay = 0
        self.children = {}
        self.parents = {}
        self.isStart = False
        self.isEnd = False

    def setStart(self, startDate):
        self.start = startDate

    def setEnd(self, endDate):
        self.end = endDate

    def setPay(self, newPay):
        self.pay = newPay

    def addParent(self, newParent, client_number):
        self.parents[client_number] = newParent

    def addChild(self, newChild, client_number):
        self.children[client_number] = newChild

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def getPay(self):
        return self.pay

    def getParent(self):
        return self.parents

    def getChild(self):
        return self.children

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def delParent(self, index):
        del self.parents[index]

    def reearrangeChildrenKeys(self, keyConversions):
        newMap = {}
        for conversion in keyConversions:
            if conversion[1] in self.children:
                newMap[conversion[0]] = self.children[conversion[1]]
        self.children = newMap
