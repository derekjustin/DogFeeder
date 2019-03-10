def foodClass():

    # foodClass Constructor
    def __init__(self, calsPerCupIn):
        self.calsPerCup = calsPerCupIn

    # Member Variable Setters
    def setCalsPerCup(self, calsPerCupIn):
        self.calsPerCup = calsPerCupIn

    # Member Variable Getters
    def getCalsPerCup(self):
        return self.calsPerCup


#Derek, added
    def poundsToMetric(pounds):
        kilograms = pounds / 2.2
        grams = kilograms * 1000
        return int(kilograms), grams % 1000

#Derek, added
    def maxCaloricIntake(self):
        rER = 70 * ( poundsToMetric( self.getWeight() )^( 3/4 ) )   
        return rER
        
#Derek, added
    def cupsPerDay(self):
        cupsPerDay = self.maxCaloricIntake() / self.getCalsPerCup() 
        return cupsPerDay
'''
(Resting Energy Requirements or RER), which can be 
calculated by multiplying the animal’s body weight in 
kilograms raised to the ¾ power by 70, for example,
 a 10kg (22lb) adult neutered dog of healthy weight needs 
RER = 70(10kg)3/4 ≈ 400 Calories/day. 



https://vet.osu.edu/vmc/companion/our-services/nutrition-support-service/basic-calorie-calculator
'''