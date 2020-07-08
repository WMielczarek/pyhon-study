class ParkingLot:

    def __init__(self,id,numberOfSpots):
        self.ID = id
        self.numberOfSpots = numberOfSpots
        self.status = 1
        self.users = []
        self.light = 0
        self.music = 0

    @property
    def music(self):
        return self.__music
    @music.setter
    def music(self, nuta):
        if nuta > 1:
            self.__music = 1
        elif nuta < 0:
            self.__music = 0

    @property
    def light(self):
        return self.__light
    @light.setter
    def light(self, lig):
        if lig > 1:
            self.__light = 1
        elif lig < 0:
            self.__light = 0

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status):
        if status > 1:
            self.__status = 1
        elif status < 0:
            self.__status = 0

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self,id):
        self.__ID = id
    @property
    def users(self):
        return self.__users
    @users.setter
    def users(self, users):
        self.__users = users
    @property
    def numberOfSpots(self):
        return self.__numberOfSpots
    @numberOfSpots.setter
    def numberOfSpots(self, number):
        self.__numberOfSpots = number

    def __str__(self):
        return str(self.ID)

    def toString(self):
        print("ParkingLot{ID = ",self.ID,",number of users: ",len(self.users),", numberOfSpots: ",self.numberOfSpots)



