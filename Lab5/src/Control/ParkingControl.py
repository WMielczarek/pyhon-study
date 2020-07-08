class ParkingControl():
    def __init__(self,parking):
        self.parking = parking

    def closeParking(self):
        self.parking.status = 0

    def openParking(self):
        self.parking.status = 1

    def checkNumberOfFreeSpots(self):
        return self.parking.numberOfSpots-len(self.parking.users)

    def addUserToParkingLot(self,user):
        try:
            if self.checkNumberOfFreeSpots() > 0 and user.enterStatus == 1 and user.canEnter == 1:
                self.parking.users.append(user)
                print("Uzytkownik właśnie wjeżdża")
            elif (user.enterStatus == 0):
                print("Uzytkownik jest w srodku")
            else:
                print("Uzytkownik nie zapłacił")
        except ValueError:
            print("Brak miejsca na parkingu")

    def removeUserFromParkingLot(self,user):
        try:
            for x in self.parking.users:
                if x == user:
                    self.parking.users.remove(x)
                    print("Uzytkownik właśnie wyjechał")
        except ValueError:
            print("Nie ma takiego użytkownika")
    def turnOnLight(self):
        self.parking.light = 1
    def turnOffLight(self):
        self.parking.light = 0
    def turnOnMusic(self):
        self.parking.music = 1
    def turnOffMusic(self):
        self.parking.music = 0

