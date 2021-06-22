from types import ClassMethodDescriptorType
import random


class Rocket:

    def __init__(self, name, height, speed, prodDate, base):
        print("Rocket initialized")
        self.name = name
        self.height = height
        self.speed = speed
        self.prodDate = prodDate
        self.base = base
        self.altitude = 0

    def moveUp(self, speed):
        self.altitude += speed * random.randrange(0, 10)


RocketList = {
    Rocket("ORP Pułaski", 40, 300, 2005, "Katowice"),
    Rocket("ORP Sienkiewicz", 35, 1100, 2011, "Gdynia"),
    Rocket("ORP Jan Paweł II", 45, 2200, 1995, "Wadowice"),
    Rocket("ORP Kaczynski I", 15, 500, 2010, "Smolensk"),
    Rocket("ORP Kaczynski II", 10, 100, 2018, "Warszawa")
}

for element in RocketList:
    for i in range(0, 10):
        element.moveUp(element.speed)
    print("Rakieta " + element.name +
          " jest na wysokości " + str(element.altitude) + "m")
