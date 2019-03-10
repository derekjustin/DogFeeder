import random

def PositiveReinforcementClass():

    def variedFeeding1(self):
        feed_1 = random.randrange(0, self.cupsPerDay)      
        return feed_1

#Problems, variedFeeding1 must happen before variedFeeding2
    def variedFeeding2(self):
        feed_2 = (self.maxCaloricIntake() - self.variedFeeding1) 
        return feed_2


