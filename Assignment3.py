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
from solarSystemClass import solarSystem

mercury = Mercury()
print(mercury.info())

venus = Venus()
print(venus.info())

earth = Earth()
print(earth.info())

mars = Mars()
print(mars.info())

jupiter = Jupiter()
print(jupiter.info())

saturn = Saturn()
print(saturn.info())

uranus = Uranus()
print(uranus.info())

neptune = Neptune()
print(neptune.info())

pluto = Pluto()
print(pluto.info())

solar = solarSystem()
print(solar.numOfOrbits(1000))
#print(solar.numOfOrbitsV(1000))