import re

file = open ("input.txt", 'r')
input = file.readlines()

total = 0

for line in input:
    gameNumber = ""
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    
    for char in line[4:]:
        if char.isdigit():
            gameNumber += char
        if char == ':':
            gameNumber = int(gameNumber)
            break
    
        
    index = line.find(":")
    lastInLine = False
    while lastInLine == False:
        lastInLine = False
        nextIndexComma = line[index:].find(",")
        nextIndexSemi = line[index:].find(";")
        nextIndex = -1
        if nextIndexComma < nextIndexSemi:
            if nextIndexComma != -1:
                nextIndex = index + nextIndexComma
            else:
                nextIndex = index + nextIndexSemi
        else:
            if nextIndexSemi != -1:
                nextIndex = index + nextIndexSemi
            else:
                nextIndex = index + nextIndexComma
        if (nextIndexComma == -1) and (nextIndexSemi == -1):
            nextIndex = len(line)
            #nextIndex -= 1
            lastInLine = True
            
            
        substring = line[index:nextIndex]
        substringValue = ""
        for char in substring:
            if (ord(char) >= ord('0')) and (ord(char) <= ord('9')):
                substringValue += char
        substringValue = int(substringValue)
        
        
        if substring.find("red") > -1:
            if maxRed < substringValue or maxRed == 0:
                maxRed = substringValue
        
        if substring.find("green") > -1:
            if maxGreen < substringValue or maxGreen == 0:
                maxGreen = substringValue
            
        if substring.find("blue") > -1:
            if maxBlue < substringValue or maxBlue == 0:
                maxBlue = substringValue
        
        if lastInLine:
            #total += gameNumber
            power = 1
            if maxRed > 0:
                power *= maxRed
            if maxGreen > 0:
                power *= maxGreen
            if maxBlue > 0:
                power *= maxBlue
            print(str(maxRed) + " " + str(maxGreen) + " " + str(maxBlue))
            total += power
            
        index = nextIndex + 1
            
    print("total: " + str(total))
        
