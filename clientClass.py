from sqlalchemy.sql.elements import Null


class client:

    def __init__(self):
        self.parent = None
        self.start = 0
        self.end = 0
        self.pay = 0

    def setStart(self, startDate):
        self.start = startDate

    def setEnd(self, endDate):
        self.end = endDate

    def setPay(self, newPay):
        self.pay = newPay

    def setParent(self, newParent):
        self.parent = newParent

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def getPay(self):
        return self.pay

    def getParent(self):
        return self.parent
