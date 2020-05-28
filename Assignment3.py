#!/usr/bin/python3

from solarSystemClass import solarSystem

def main():
    solar = solarSystem()
    solar.info()
    print("\n")  
    solar.numOfOrbits(1000)

if __name__ == "__main__":
    main()