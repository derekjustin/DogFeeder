def dogClass():

    # dogClass Constructor
    def __init__(self, weightIn, ageIn):
        self.weight = weightIn
        self.age = ageIn

    # Member Variable Setters
    def setWeight(self,weightIn): #In pounds
        self.weight = weightIn

    def setAge(self, ageIn):
        self.age = ageIn

    # Member Variable Getters
    def getWeight(self):
        return self.weight

    def getAge(self):
        return self.age


