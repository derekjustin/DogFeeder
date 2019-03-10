

class dogClass:

    # dogClass Constructor
    def __init__(self):
        self._weight = 0
        self._age = 0
        self._name = ""

    def __gt__(self, anotherPet):
        return self._name[0] > anotherPet._name[0]

    # Member Variable Setters
    def setName(self, nameIn):
        self._name = nameIn

    def setAge(self, ageIn):
        self._age = ageIn

    def setWeight(self,weightIn):
        self._weight = weightIn


    # Member Variable Getters
    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getWeight(self):
        return self._weight






