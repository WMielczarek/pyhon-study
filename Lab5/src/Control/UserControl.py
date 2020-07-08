class Control:

    def __init__(self):
        self.users = []

    def addUser(self, user):

        self.users.append(user);

    def findUser(self, user):
        for x in self.users:
            if (x == user):
                return user;
            else:
                print("Cannot find user")

    def __eq__(self, other):
        return ((self.users.firstName,self.users.lastName,self.users.plate) == (other.users.firstName,other.users.lastName,other.users.plate))


    def removeUser(self, user):
        try:
            for x in self.users:
                if x == user:
                    self.users.remove(x)
                    print("Usunieto uzytkownika")
        except ValueError:
            print("Nie ma takiego użytkownika")

    def checkUserExistance(self,  user):
        for x in self.users:
            if x == user:
                return False
            else:
                return True

    def checkPayment(self):
        for x in self.users:
            if (x.paymentStatus == False):
                x.canEnter = 0

    def showUsersCantEnter(self):
        for x in self.users:
            if x.canEnter == False:
                print(x)

    def showUsers(self):
        try:
            if len(self.users)>0:
                for x in self.users:
                    print("User{firstName: ", x.firstName, ", lastName: ", x.lastName, ", plate: ", x.plate)
        except ValueError:
            print("Nie ma użytkowników")



