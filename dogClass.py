from PositiveReinforcementClass import *
import os

class dogClass:

    # dogClass Constructor
    def __init__(self, row=None):
        if row == None:
            self._name = " "
            self._age = 0
            self._weight = 0
            self._baseDirectory = " "
            self._buttonPushDirectory = " "
            self._motionSenseDirectory = " "
            self._dailyStepsDirectory = " "
            self._heartRateDirectory = " "
            #self._positiveReinforcement = PositiveReinforcementClass()
        else:
            self._name = row[0]
            self._age = row[1]
            self._weight = row[2]
            self._baseDirectory = row[3]
            self._buttonPushDirectory = row[4]
            self._motionSenseDirectory = row[5]
            self._dailyStepsDirectory = row[6]
            self._heartRateDirectory = row[7]
            self.createDirectory(self.getBaseDirectory())
            self.createDirectory(self.getButtonPushDirectory())
            self.createDirectory(self.getMotionSenseDirectory())
            self.createDirectory(self.getDailyStepsDirectory())
            self.createDirectory(self.getHeartRateDirectory())



    # Member Variable Setters
    def setName(self, nameIn):
        self._name = nameIn

    def setAge(self, ageIn):
        self._age = ageIn

    def setWeight(self,weightIn):
        self._weight = weightIn

    def setBaseDirectory(self, baseDirectoryIn):
        self._baseDirectory = "dogs/" + baseDirectoryIn

    def setButtonPushDirectory(self, baseDirectoryIn):
        self._buttonPushDirectory = baseDirectoryIn + "/button_push"

    def setMotionSenseDirectory(self, baseDirectoryIn):
        self._motionSenseDirectory = baseDirectoryIn + "/motion_sense"

    def setDailyStepsDirectory(self, baseDirectoryIn):
        self._dailyStepsDirectory = baseDirectoryIn + "/daily_steps"

    def setHeartRateDirectory(self, baseDirectoryIn):
        self._heartRateDirectory = baseDirectoryIn + "/heart_rate"



    # Member Variable Getters
    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getWeight(self):
        return self._weight

    def getBaseDirectory(self):
        return self._baseDirectory

    def getButtonPushDirectory(self):
        return self._buttonPushDirectory

    def getMotionSenseDirectory(self):
        return self._motionSenseDirectory

    def getDailyStepsDirectory(self):
        return self._dailyStepsDirectory

    def getHeartRateDirectory(self):
        return self._heartRateDirectory



    #Member Functions
    def createDirectory(self, pathIn):
        try:
            # Create target Directory
            os.makedirs(pathIn)
        except FileExistsError:
            pass

    def getSetDogInfo(self):
        self.setName(input("What is your dogs name: "))
        self.setAge(input("How old is your dog: "))
        self.setWeight(input("How much does your dog weigh in pounds: "))
        self.setBaseDirectory(self.getName())
        self.setButtonPushDirectory(self.getBaseDirectory())
        self.setMotionSenseDirectory(self.getBaseDirectory())
        self.setDailyStepsDirectory(self.getBaseDirectory())
        self.setHeartRateDirectory(self.getBaseDirectory())

    def createDogDirectorySystem(self):
        self.createDirectory(self.getBaseDirectory())
        self.createDirectory(self.getButtonPushDirectory())
        self.createDirectory(self.getMotionSenseDirectory())
        self.createDirectory(self.getDailyStepsDirectory())
        self.createDirectory(self.getHeartRateDirectory())

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
        return str(self._name), str(self._age), str(self._weight), str(self._baseDirectory),\
               str(self._buttonPushDirectory), str(self._motionSenseDirectory), str(self._dailyStepsDirectory),\
               str(self._heartRateDirectory)
        # Add attributes when positiveReinforcement complete
        # , str(self._positiveReinforcement.getFeed_1()),\
        # str(self._positiveReinforcement.getFeed_2())
