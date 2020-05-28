#!/usr/bin/python3

class Planet(object):
    def __init__(self, distance, orbitalPeriod):
        self.distanceToSun = distance
        self.orbitalPeriod = orbitalPeriod

    def getDistanceToSun(self):
        """ 
            Finds the distance to the sun for Planet
            input: self - Planet <class>
            output: returns distance to sun for planet
        """
        return self.distanceToSun
        

    def getOrbitalPeriod(self):
        """ 
            Finds the orbital period for Planet
            input: self - Planet <class>
            output: returns orbital period for planet
        """
        return self.orbitalPeriod
      

    def info(self):
        return "The Planet is {} km to its sun and takes {} Earth years to orbit its sun.".format(self.getDistanceToSun(), self.getOrbitalPeriod())

    def setDistanceToSun(self, distance):
        """ 
            Sets the distance to the sun for Planet
            input: self, distance <class>
        """
        self.distanceToSun = distance

    def setOrbitalPeriod(self, orbitalPeriod):
        """ 
            Sets the orbital period for Planet
            input: self, orbitalPeriod <class>
        """
        self.orbitalPeriod = orbitalPeriod

 

class Mercury(Planet):
    def __init__(self):
        Planet.__init__(self, 57900000, 88.0)
        self.diameter = 4879
        self.gravity = 3.7
    
    def getDiameter(self):
        """ 
            Finds the diameter of Mercury
            input: self - Mercury <class>
            output: returns diameter of Mercury
        """
        return self.diameter
    
    def getGravity(self):
        """ 
            Finds the gravitational acceleration of Mercury
            input: self - Mercury <class>
            output: returns gravitational acceleration of Mercury
        """
        return self.gravity

    def info(self):
        return "Mercury is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())

class Venus(Planet):
    def __init__(self):
        Planet.__init__(self, 108200000, 224.7)
        self.diameter = 12104
        self.gravity = 8.9
    
    def getDiameter(self):
        """ 
            Finds the diameter of Venus
            input: self - Venus <class>
            output: returns diameter of Venus
        """
        return self.diameter
    
    def getGravity(self):
        """ 
            Finds the gravitational acceleration of Venus
            input: self - Venus <class>
            output: returns gravitational acceleration of Venus
        """
        return self.gravity

    def info(self):
        return "Venus is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())

class Earth(Planet):
    def __init__(self):
        Planet.__init__(self, 149600000, 365.2)
        self.diameter = 12756
        self.gravity = 9.8
    
    def getDiameter(self):
        """ 
            Finds the diameter of Earth
            input: self - Earth <class>
            output: returns diameter of Earth
        """
        return self.diameter
    
    def getGravity(self):
        """ 
            Finds the gravitational acceleration of Earth
            input: self - Earth <class>
            output: returns gravitational acceleration of Earth
        """
        return self.gravity

    def info(self):
        return "Earth is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())

class Mars(Planet):
    def __init__(self):
        Planet.__init__(self, 227900000, 687.0)
        self.diameter = 6792
        self.gravity = 3.7
    
    def getDiameter(self):
        """ 
            Finds the diameter of Mars
            input: self - Mars <class>
            output: returns diameter of Mars
        """
        return self.diameter
    
    def getGravity(self):
        """ 
            Finds the gravitational acceleration of Mars
            input: self - Mars <class>
            output: returns gravitational acceleration of Mars
        """
        return self.gravity

    def info(self):
        return "Mars is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())

class Jupiter(Planet):
    def __init__(self):
        Planet.__init__(self, 778600000, 4331.0)
        self.diameter = 142984
        self.gravity = 23.1
    
    def getDiameter(self):
        """ 
            Finds the diameter of Jupiter
            input: self - Jupiter <class>
            output: returns diameter of Jupiter
        """
        return self.diameter
    
    def getGravity(self):
        """ 
            Finds the gravitational acceleration of Jupiter
            input: self - Jupiter <class>
            output: returns gravitational acceleration of Jupiter
        """
        return self.gravity

    def info(self):
        return "Jupiter is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())

class Saturn(Planet):
    def __init__(self):
        Planet.__init__(self, 1433500000, 10747.0)
        self.diameter = 120536
        self.gravity = 9.0
    
    def getDiameter(self):
        """ 
            Finds the diameter of Saturn
            input: self - Saturn <class>
            output: returns diameter of Saturn
        """
        return self.diameter
    
    def getGravity(self):
        """ 
            Finds the gravitational acceleration of Saturn
            input: self - Saturn <class>
            output: returns gravitational acceleration of Saturn
        """
        return self.gravity

    def info(self):
        return "Saturn is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())

class Uranus(Planet):
    def __init__(self):
        Planet.__init__(self, 2872500000, 30589.0)
        self.diameter = 51118
        self.gravity = 8.7
    
    def getDiameter(self):
        """ 
            Finds the diameter of Uranus
            input: self - Uranus <class>
            output: returns diameter of Uranus
        """
        return self.diameter
    
    def getGravity(self):
        """ 
            Finds the gravitational acceleration of Uranus
            input: self - Uranus <class>
            output: returns gravitational acceleration of Uranus
        """
        return self.gravity

    def info(self):
        return "Uranus is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())
  
class Neptune(Planet):
    def __init__(self):
        Planet.__init__(self, 4495100000, 59800.0)
        self.diameter = 49528
        self.gravity = 11.0
    
    def getDiameter(self):
        """ 
            Finds the diameter of Neptune
            input: self - Neptune <class>
            output: returns diameter of Neptune
        """
        return self.diameter
    
    def getGravity(self):
        """ 
            Finds the gravitational acceleration of Neptune
            input: self - Neptune <class>
            output: returns gravitational acceleration of Neptune
        """
        return self.gravity

    def info(self):
        return "Neptune is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())

class Pluto(Planet):
    def __init__(self):
        Planet.__init__(self, 5906400000, 90560.0)
        self.diameter = 2370
        self.gravity = 0.7
    
    def getDiameter(self):
        """ 
            Finds the diameter of Pluto
            input: self - Pluto <class>
            output: returns diameter of Pluto
        """
        return self.diameter
    
    def getGravity(self):
        """ 
            Finds the gravitational acceleration of Pluto
            input: self - Pluto <class>
            output: returns gravitational acceleration of Pluto
        """
        return self.gravity

    def info(self):
        return "Pluto is {} km to its sun, takes {} Earth years to orbit its sun, has a diameter of {} km, and its gravitational acceleration is {} m/s^2.".format(self.getDistanceToSun(), self.getOrbitalPeriod(), self.getDiameter(), self.getGravity())