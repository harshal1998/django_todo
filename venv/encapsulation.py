class enc:
    def __init__(self):
        self.__amt = 5000

    def getamt(self):
        print(self.__amt)

    def setamt(self, a):
        self.__amt = a


obj = enc()
obj.getamt()
obj.setamt(100)
obj.getamt()
