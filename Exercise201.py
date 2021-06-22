from math import sqrt
import random


class Rocket:
    """Rocket class
    """

    def __init__(self, speed=5, altitude=0, position=10, name="SampleRocket", height=5, prodDate=2021, base="Gdańsk"):
        """Constructor
        """
        print("Rocket initialized")
        self.name = name
        self.height = height
        self.speed = speed
        self.prodDate = prodDate
        self.base = base
        self.altitude = altitude
        self.position = position

    def moveUp(self):
        self.altitude += self.speed * random.randrange(0, 10)

    def __str__(self):
        return "Rakieta jest na wysokości " + str(self.altitude) + " m"

    def getdistance(self, rocket):
        ab = (rocket.altitude - self.altitude) ** 2
        bc = (rocket.position - self.position) ** 2
        return sqrt(ab + bc)


class RocketBoard:
    """RocketBoard class
    """

    def __init__(self, AmountOfRockets):
        self.rockets = [Rocket(random.randint(1, 6))
                        for _ in range(AmountOfRockets)]

        for _ in range(10):
            rocketIndexToMove = random.randint(0, len(self.rockets)-1)
            self.rockets[rocketIndexToMove].moveUp()

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].altitude = value


"""
RocketList = [
    Rocket("ORP Pułaski", 40, 300, 2005, "Katowice"),
    Rocket("ORP Sienkiewicz", 35, 1100, 2011, "Gdynia"),
    Rocket("ORP Jan Paweł II", 45, 2200, 1995, "Wadowice"),
    Rocket("ORP Kaczynski I", 15, 500, 2010, "Smolensk"),
    Rocket("ORP Kaczynski II", 10, 100, 2018, "Warszawa")
]
"""
