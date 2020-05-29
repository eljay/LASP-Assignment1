#!/usr/bin/python3

from planetClass import Planet
from planetClass import Mercury
from planetClass import Venus
from planetClass import Earth 
from planetClass import Mars 
from planetClass import Jupiter 
from planetClass import Saturn 
from planetClass import Uranus 
from planetClass import Neptune 
from planetClass import Pluto

class solarSystem():
    def __init__(self):
        mercury = Mercury()
        venus = Venus()
        earth = Earth()
        mars = Mars()
        jupiter = Jupiter()
        saturn = Saturn()
        uranus = Uranus()
        neptune = Neptune()
        pluto = Pluto()

        self.planetList = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]

    def numOfOrbits(self, days):
        """
            prints the number of orbits each planet makes in x number of days for each planet from the list of planets
            input: self, number of days
            output: prints number of orbits in x days
        """
        for planet in self.planetList:
            planetName = planet.getName()
            numberOfOrbits = days / planet.getOrbitalPeriod()
            print("The number of times {} has orbited the sun in {} days is {} orbits".format(planetName, days, str(round(numberOfOrbits,2))))

    def info(self):
        """
            prints all info (distance, orbital period, diameter, and gravity) for each planet from the list of planets
            input: self - planet
            output: printed info for each planet
        """
        for planet in self.planetList:
            planetName = planet.getName()
            planetDistance = planet.getDistanceToSun()
            planetOrbitalPeriod = planet.getOrbitalPeriod()
            planetDiameter = planet.getDiameter()
            planetGravity = planet.getGravity()
            print("The planet {} is {} km to its sun and takes {} earth years to orbit its sun. It's diameter is {} km and orbital velocity is {} km/s".format(planetName, planetDistance, planetOrbitalPeriod, planetDiameter, planetGravity))
    