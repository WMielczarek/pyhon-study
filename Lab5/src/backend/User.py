class User:
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last
        self.plate = None
        self.enterStatus = 1
        self.paymentStatus = 0
        self.canEnter = 0
    @property
    def canEnter(self):
        return self.__canEnter
    @canEnter.setter
    def canEnter(self, can):
        self.__canEnter = can
    @property
    def firstName(self):
        return self.__firstName
    @firstName.setter
    def firstName(self, name):
        self.__firstName = name
    @property
    def lastName(self):
        return self.__lastName
    @lastName.setter
    def lastName(self, last):
        self.__lastName = last
    @property
    def plate(self):
        return self.__plate
    @plate.setter
    def plate(self, plate):
        self.__plate = plate
    @property
    def enterStatus(self):
        return self.__enterStatus
    @enterStatus.setter
    def enterStatus(self, status):
        self.__enterStatus = status
    @property
    def paymentStatus(self):
        return self.__paymentStatus
    @paymentStatus.setter
    def paymentStatus(self,pay):
        self.__paymentStatus = pay

    def __eq__(self, other):
        return ((self.lastName,self.firstName,self.plate)==(other.lastName,other.firstName,other.plate))

    def __str__(self):
        return self.firstName

    def toString(self):
        print("User{firstName: ",self.firstName,", lastName: ",self.lastName,", plate: ",self.plate)

a = User("a","b")
