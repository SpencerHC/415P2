from sqlalchemy.sql.elements import Null


class client:
    childCount = 0
    parentCount = 0

    def __init__(self):
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
        self.parents['client{0}'.format(client_number)] = newParent

    def addChild(self, newChild, client_number):
        self.children['client{0}'.format(client_number)] = newChild

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
