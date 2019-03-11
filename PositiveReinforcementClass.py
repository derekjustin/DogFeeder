import random

class PositiveReinforcementClass:

    def __init__(self):
        self.feed_1 = 0
        self.feed_2 = 0

    # Member variable setters
    def setFeed_1(self, feedIn):
        self.feed_1 = feedIn

    def setFeed_2(self, feedIn):
        self.feed_2 = feedIn

    # Member variable getters
    def getFeed_1(self):
        return self.feed_1

    def getFeed_2(self):
        return self.feed_2

    def variedFeeding1(self):
        self.feed_1 = random.randrange(0, self.cupsPerDay)
        return self.feed_1

#Problems, variedFeeding1 must happen before variedFeeding2
    def variedFeeding2(self):
        self.feed_2 = (self.maxCaloricIntake() - self.variedFeeding1)
        return self.feed_2


