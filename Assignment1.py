#!/usr/bin/python3

import argparse
import re

idx = -1
counter=0
character = []
cWords = []
ignore = ["Enter", "Exit", "Exeunt"]
cIgnoreCount = []

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
with open(args.filename) as file:

# f = open("alls_wells_that_ends_well_short.txt", "r")
# f = open(args.file)

  line = file.readline() #read particular line in file
  while line:
      if (len(line.split()) == 1) and (((line.strip().isupper()) and (line.strip() not in character)) or (line.strip() == 'Page')): #check if line has only one word and is all in uppercase, 
                                                                                                                                    #has not already been encountered, or if it is Page
          character.append(line.strip()) #adds the "stripped" character word into the character list
          idx = character.index(line.strip()) #get the index of the stripped character word (ex. COUNTESS has index 0)
          cWords.append("") #initialize the list that will contain the words each character says. 
          cIgnoreCount.append(0) #keep track of words like "exit" or "enter" that will not be counted as the words a character says
      elif (len(line.split()) == 1) and (line.strip() in character): #check if line has only one word and already exists in the list of characters (ex. come across COUNTESS again)
          idx = character.index(line.strip()) 
      else:
        if idx != -1: #at least one character has been added to the character list
          cWords[idx] = cWords[idx] + line #begins adding the words in that line to the list (ex. CWords[0] will be getting populated with the lines of words COUNTESS says)
          if line.strip().startswith((tuple(ignore))): #check if line starts with any one of the ignore words like "exit" or "enter"
            # cIgnoreCount[idx] = cIgnoreCount[idx] + len(line.split()) #add the whole line to a list that will contain all the lines that start with one of the ignore words
            counts = dict()
            words = line.split()
            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
                cIgnoreCount[idx] = cIgnoreCount[idx] + counts[word]
          elif re.search(r"\s\W\s", line.strip()):
            cIgnoreCount[idx] = cIgnoreCount[idx] + 1 

        

      line = file.readline() #read next line

  character = [c.upper() for c in character]
  s = sorted(zip(character, cWords, cIgnoreCount)) #zip will first associate each character with its corresponding spoken lines, and it will then sorts character in alphabetical order 
  character, cWords, cIgnoreCount = map(list, zip(*s)) #map will split the newly zipped and sorted characters into its own list and will do the same for the spoken words

  for cCount in character:
    uniqueWords = []
    freq = []

    for word in sorted(cWords[counter].split()): #takes all the lines in a text and sorts them
        # line = line.strip() #strips them of their spaces
        if word not in uniqueWords: #checks to see if line is in words
            uniqueWords.append(word) #if not it adds it to the end words
            freq.append(1) #and adds 1 to the end of freq
        else:
            index = uniqueWords.index(word) #if it is it will find where in words
            freq[index] += 1
  
    f = sorted(zip(freq, uniqueWords), reverse = True)
    freq, uniqueWords = map(list, zip(*f))

    print(character[counter] +" ("+ str(len(cWords[counter].split()) - cIgnoreCount[counter]) + ")") #print character name and it's total spoken words excluding the ignore words
    print(cWords[counter]) #prints the character's spoken words including the ignore words
    print(character[counter] + " spoke the word '"+uniqueWords[0]+"' "+str(freq[0]) + " times.\n" )
    counter = counter+1 #move on to next character

