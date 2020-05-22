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
        Mercury.__init__(self)
        Venus.__init__(self)
        Earth.__init__(self)
        Mars.__init__(self)
        Jupiter.__init__(self)
        Saturn.__init__(self)
        Uranus.__init__(self)
        Neptune.__init__(self)
        Pluto.__init__(self)

    def allInfo(self):
        print(Mercury.info())
        print(Venus.info())
        print(Earth.info())
        print(Mars.info())
        print(Jupiter.info())
        print(Saturn.info())
        print(Uranus.info())
        print(Neptune.info())
        print(Pluto.info())

    def numOfOrbits(self,days):

        numOrbits = days / Mercury.getOrbitalPeriod(self)
        print(Mercury.getOrbitalPeriod(self))
        print(numOrbits)
        #print("The number of orbits that Mercury has done in {} days is {}".format(days, str(round(numOrbits,2))))

        #numOrbitsV = days / float(Venus.getOrbitalPeriod(self))
        #print("The number of orbits that Venus has done in {} days is {}".format(days, str(round(numOrbitsV,2))))

        # numOrbits = days / float(Earth.getOrbitalPeriod(self))
        # print("The number of orbits that Earth has done in {} days is {}".format(days, str(round(numOrbits,2))))

        # numOrbits = days / float(Mars.getOrbitalPeriod(self))
        # print("The number of orbits that Mars has done in {} days is {}".format(days, str(round(numOrbits,2))))

        # numOrbits = days / float(Jupiter.getOrbitalPeriod(self))
        # print("The number of orbits that Jupiter has done in {} days is {}".format(days, str(round(numOrbits,2))))

        # numOrbits = days / float(Saturn.getOrbitalPeriod(self))
        # print("The number of orbits that Saturn has done in {} days is {}".format(days, str(round(numOrbits,2))))

        # numOrbits = days / float(Uranus.getOrbitalPeriod(self))
        # print("The number of orbits that Uranus has done in {} days is {}".format(days, str(round(numOrbits,2))))

        # numOrbits = days / float(Neptune.getOrbitalPeriod(self))
        # print("The number of orbits that Neptune has done in {} days is {}".format(days, str(round(numOrbits,2))))

        # numOrbits = days / float(Pluto.getOrbitalPeriod(self))
        # print("The number of orbits that Pluto has done in {} days is {}".format(days, str(round(numOrbits,2))))
