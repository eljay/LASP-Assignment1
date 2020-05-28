#!/usr/bin/python3

import argparse
import re

def readFile(file):
    idx = -1
    characterName = []
    characterWords = []
    ignoreWords = ["Enter", "Exit", "Exeunt"]
    charIgnoreWordCount = []

    line = file.readline() #read particular line in file
    while line:
        if (len(line.split()) == 1 and (line.strip().isupper() or (re.match(r'\S', line))) and (line.strip() not in characterName)):# or (len(line.split() == 1) and re.match(r'[ \t]', line) and line.strip() not in characterName):# or (len(line.split()) == 1 and re.match(r'[ \t]', line) and line.strip() not in characterName): #check if line has only one word and is all in uppercase, 
            characterName.append(line.strip()) #adds the "stripped" characterName word into the characterName list
            idx = characterName.index(line.strip()) #get the index of the stripped characterName word (ex. COUNTESS has index 0) (CURRENT CHAR INDEX)
            characterWords.append("") #initialize the list that will contain the words each characterName says. 
            charIgnoreWordCount.append(0) #for each characterName, initiaize this list that will contain ignored words
        elif (len(line.split()) == 1) and (line.strip() in characterName): #check if line has only one word and already exists in the list of characterNames (ex. come across COUNTESS again)
            idx = characterName.index(line.strip()) 
        else:
            if idx != -1: #at least one characterName has been added to the characterName list
                characterWords[idx] = characterWords[idx] + line #begins adding the words in that line to the list (ex. characterWords[0] will be getting populated with the lines of words COUNTESS says)
                if line.strip().startswith((tuple(ignoreWords))): #check if line starts with any one of the ignore words like "exit" or "enter"
                    # charIgnoreWordCount[idx] = charIgnoreWordCount[idx] + len(line.split()) #add the whole line to a list that will contain all the lines that start with one of the ignore words
                    storedIgnoreWords = dict()
                    words = line.split()
                    for word in words:
                        if word in storedIgnoreWords:#re.search(r"]$", word):
                            storedIgnoreWords[word] += 1
                        else:
                            storedIgnoreWords[word] = 1
                        charIgnoreWordCount[idx] = charIgnoreWordCount[idx] + storedIgnoreWords[word]
                # bracketSearch = re.search(r"\[(\w*\s\w*)]" , line.strip())
                # print(characterWords[idx].split())
                bracketSearch = len(re.findall(r'[\[\]]+', line.strip())) 
                if bracketSearch > 0:
                    charIgnoreWordCount[idx] = charIgnoreWordCount[idx] + bracketSearch
                
        line = file.readline() #read next line
    
    sorted(characterName, key=lambda c: c[0].upper())
    sort = sorted(zip(characterName, characterWords, charIgnoreWordCount),key=lambda c: c[0].upper()) #zip will first associate each characterName with its corresponding spoken lines, and it will then sorts characterName in alphabetical order 
    characterName, characterWords, charIgnoreWordCount = map(list, zip(*sort)) #map will split the newly zipped and sorted characterNames into its own list and will do the same for the spoken words

    return characterName, characterWords, charIgnoreWordCount        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help = "alls_wells_that_ends_well.txt")
    args = parser.parse_args()
    try:
        with open(args.filename) as file: 

            characterName, characterWords, charIgnoreWordCount = readFile(file)

            idx = 0 #reset index so you can print character's spoken words in sorted order

            #commonly spoken word
            for char in characterName:
                uniqueWords = []
                freq = []

                for word in sorted(characterWords[idx].split()): #takes all the lines in a text and sorts them
                    if word not in uniqueWords: #checks to see if the words in the line is in unique words
                        uniqueWords.append(word) #if not it adds it to the end words
                        freq.append(1) #and adds 1 to the end of freq
                    else:
                        index = uniqueWords.index(word) #if it is it will find where in words
                        freq[index] += 1

                frequency = sorted(zip(freq, uniqueWords), reverse = True)
                freq, uniqueWords = map(list, zip(*frequency)) #to extract freq and uniquewords separately
            
                hyphenCount = len(re.findall(r'\W+--', characterWords[idx].strip())) 
                print(characterName[idx] +" ("+ str(len(characterWords[idx].split()) + hyphenCount - charIgnoreWordCount[idx]) + ")") #print characterName name and it's total spoken words excluding the ignore words
                print(characterWords[idx]) #prints the characterName's spoken words including the ignore words
                print(characterName[idx] + " spoke the word '"+uniqueWords[0]+"' "+str(freq[0]) + " times.\n" )
                idx = idx+1 #move on to next characterName
                    
    except Exception as error: #tells why code crashed
        print("unable to open " + args.filename)
        print(error)

if __name__ == "__main__":
    main()
