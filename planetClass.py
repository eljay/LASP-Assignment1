#!/usr/bin/python3

class Planet(object):
    def __init__(self, distance, orbitalPeriod):
        self.distanceToSun = distance
        self.orbitalPeriod = orbitalPeriod

    def getDistanceToSun(self):
        return self.distanceToSun

    def getOrbitalPeriod(self):
        return self.orbitalPeriod

    def info(self):
        return "The Planet is {} km to its sun and takes {} Earth years to orbit its sun.".format(self.getDistanceToSun(), self.getOrbitalPeriod())

    def setDistanceToSun(self, distance):
        self.distanceToSun = distance

    def setOrbitalPeriod(self, orbitalPeriod):
        self.orbitalPeriod = orbitalPeriod

 

class Mercury(Planet):
    def __init__(self):
        Planet.__init__(self, 57900000, 88.0)
        self.diameter = 4879
        self.gravity = 3.7
    
    def getDiameter(self):
        return self.diameter
    
    def getGravity(self):
        return self.gravity

    def info(self):
        return "Mercury is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())

class Venus(Planet):
    def __init__(self):
        Planet.__init__(self, 108200000, 224.7)
        self.diameter = 12104
        self.gravity = 8.9
    
    def getDiameter(self):
        return self.diameter
    
    def getGravity(self):
        return self.gravity

    def info(self):
        return "Venus is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())

class Earth(Planet):
    def __init__(self):
        Planet.__init__(self, 149600000, 365.2)
        self.diameter = 12756
        self.gravity = 9.8
    
    def getDiameter(self):
        return self.diameter
    
    def getGravity(self):
        return self.gravity

    def info(self):
        return "Earth is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())

class Mars(Planet):
    def __init__(self):
        Planet.__init__(self, 227900000, 687.0)
        self.diameter = 6792
        self.gravity = 3.7
    
    def getDiameter(self):
        return self.diameter
    
    def getGravity(self):
        return self.gravity

    def info(self):
        return "Mars is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())

class Jupiter(Planet):
    def __init__(self):
        Planet.__init__(self, 778600000, 4331.0)
        self.diameter = 142984
        self.gravity = 23.1
    
    def getDiameter(self):
        return self.diameter
    
    def getGravity(self):
        return self.gravity

    def info(self):
        return "Jupiter is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())

class Saturn(Planet):
    def __init__(self):
        Planet.__init__(self, 1433500000, 10747.0)
        self.diameter = 120536
        self.gravity = 9.0
    
    def getDiameter(self):
        return self.diameter
    
    def getGravity(self):
        return self.gravity

    def info(self):
        return "Saturn is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())

class Uranus(Planet):
    def __init__(self):
        Planet.__init__(self, 2872500000, 30589.0)
        self.diameter = 51118
        self.gravity = 8.7
    
    def getDiameter(self):
        return self.diameter
    
    def getGravity(self):
        return self.gravity

    def info(self):
        return "Uranus is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())
  
class Neptune(Planet):
    def __init__(self):
        Planet.__init__(self, 4495100000, 59800.0)
        self.diameter = 49528
        self.gravity = 11.0
    
    def getDiameter(self):
        return self.diameter
    
    def getGravity(self):
        return self.gravity

    def info(self):
        return "Neptune is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())

class Pluto(Planet):
    def __init__(self):
        Planet.__init__(self, 5906400000, 90560.0)
        self.diameter = 2370
        self.gravity = 0.7
    
    def getDiameter(self):
        return self.diameter
    
    def getGravity(self):
        return self.gravity

    def info(self):
        return "Pluto is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())