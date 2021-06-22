from types import ClassMethodDescriptorType
import random


class Rocket:

    def __init__(self, name, height, firePower, prodDate, base):
        print("Rocket initialized")
        self.name = name
        self.height = height
        self.firePower = firePower
        self.prodDate = prodDate
        self.base = base
        self.posVert = 0


RocketList = {
    Rocket("ORP Pułaski", 40, 1000, 2005, "Katowice"),
    Rocket("ORP Sienkiewicz", 35, 1400, 2011, "Gdynia"),
    Rocket("ORP Jan Paweł II", 45, 6000, 1995, "Wadowice"),
    Rocket("ORP Kaczynski I", 15, 10, 2010, "Smolensk"),
    Rocket("ORP Kaczynski II", 10, 5, 2018, "Warszawa")
}


for element in RocketList:
    for i in range(0, 10):
        element.posVert += random.randrange(0, 1000)
    print("Rakieta " + element.name +
          " jest na wysokości " + str(element.posVert) + "m")
