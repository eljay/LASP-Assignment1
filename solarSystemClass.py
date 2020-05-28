#!/usr/bin/python3

# from planetClass import Planet
# from planetClass import Mercury
# from planetClass import Venus
# from planetClass import Earth 
# from planetClass import Mars 
# from planetClass import Jupiter 
# from planetClass import Saturn 
# from planetClass import Uranus 
# from planetClass import Neptune 
# from planetClass import Pluto

class solarSystem():
    def __init__(self):
        self.planetList = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
        self.distance = [57900000, 108200000, 149600000, 227900000, 778600000, 1433500000, 2872500000, 4495100000, 5906400000]
        self.orbitalPeriod = [88, 225, 365, 687, 4331, 10747, 30589, 59800, 90560]
        self.diameter = [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528, 2370]
        self.gravity = [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0, 0.7]

    def info(self):
        """
            prints all info (distance, orbital period, diameter, and gravity) for each planet from the list of planets
            input: self - planet
            output: printed info for each planet
        """
        for planet in self.planetList:
            idx = self.planetList.index(planet)
            print("The planet {} is {} km to its sun and takes {} earth years to orbit its sun. It's diameter is {} km and orbital velocity is {} km/s".format(planet, self.distance[idx],  self.orbitalPeriod[idx], self.diameter[idx], self.gravity[idx]))

    def numOfOrbits(self,days):
        """
            prints the number of orbits each planet makes in x number of days for each planet from the list of planets
            input: self, number of days
            output: prints number of orbits in x days
        """
        for planet in self.planetList:
            idx = self.planetList.index(planet)
            numberOfOrbits = days / self.orbitalPeriod[idx]
            print("The number of times {} has orbited the sun in {} days is {} orbits".format(planet, days, str(round(numberOfOrbits,2))))