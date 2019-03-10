def dogClass(nameIn, ageIn, weightIn):

    # dogClass Constructor
    def __init__(self, nameIn, ageIn, weightIn):
        self.__weight = weightIn
        self.__age = ageIn
        self.__name = nameIn

    def __gt__(self, anotherPet):
        return self.__name[0] > anotherPet.__name[0]

    # Member Variable Setters
    def setName(self, nameIn):
        self.__name = nameIn

    def setAge(self, ageIn):
        self.__age = ageIn

    def setWeight(self,weightIn):
        self.__weight = weightIn





    # Member Variable Getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getWeight(self):
        return self.weight






