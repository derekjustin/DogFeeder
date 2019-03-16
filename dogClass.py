from PositiveReinforcementClass import *

class dogClass:

    # dogClass Constructor
    def __init__(self, row=None):
        if row == None:
            self._name = ""
            self._age = 0
            self._weight = 0
            self._dogDirectory = ""
            #self._positiveReinforcement = PositiveReinforcementClass()
        else:
            self._name = row[0]
            self._age = row[1]
            self._weight = row[2]



    # Member Variable Setters
    def setName(self, nameIn):
        self._name = nameIn

    def setAge(self, ageIn):
        self._age = ageIn

    def setWeight(self,weightIn):
        self._weight = weightIn

    def setDogDirectory(self, dogDirectoryIn):
        self._dogDirectory = dogDirectoryIn

    # Member Variable Getters
    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getWeight(self):
        return self._weight

    def getDogDirectory(self):
        return self._dogDirectory

    #Member Functions



    # Operator Overloads
    def __gt__(self, anotherPet):
        return str(self._name).upper() > anotherPet._name.upper()

    def __ge__(self, anotherPet):
        return str(self._name).upper() >= anotherPet._name.upper()

    def __lt__(self, anotherPet):
        return str(self._name).upper() < anotherPet._name.upper()

    def __le__(self, anotherPet):
        return str(self._name).upper() <= anotherPet._name.upper()

    def __str__(self):
        return "Pet Name: " + str(self._name) + "\nPet Age: " + str(self._age) + "\nPet Weight: " + str(self._weight)

    # File formatting functions
    def toFile(self):
        return str(self._name), str(self._age), str(self._weight)#, str(self._directory)
        # Add attributes when positiveReinforcement complete
        # , str(self._positiveReinforcement.getFeed_1()),\
        # str(self._positiveReinforcement.getFeed_2())
