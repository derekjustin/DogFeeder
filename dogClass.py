

class dogClass:

    # dogClass Constructor
    def __init__(self):
        self._weight = 0
        self._age = 0
        self._name = ""

    def __gt__(self, anotherPet):
        return str(self._name) > anotherPet._name

    def __ge__(self, anotherPet):
        return str(self._name) >= anotherPet._name

    def __lt__(self, anotherPet):
        return str(self._name) < anotherPet._name

    def __le__(self, anotherPet):
        return str(self._name) <= anotherPet._name

    def __str__(self):
        return "Pet Name: " + str(self._name) + "\n Pet Age: " + str(self._age) + "\n Pet Weight: " + str(self._weight)

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






