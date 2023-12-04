import re

file = open ("input.txt", 'r')
input = file.readlines()

total = 0

for line in input:
    gameNumber = ""
    
    for char in line[4:]:
        if char.isdigit():
            gameNumber += char
        if char == ':':
            gameNumber = int(gameNumber)
            break
    
    print("game " + str(gameNumber))
        
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
            nextIndex -= 1
            lastInLine = True
            
            
        substring = line[index:nextIndex]
        #print("substring:" + substring)
        substringValue = ""
        for char in substring:
            if (ord(char) >= ord('0')) and (ord(char) <= ord('9')):
                substringValue += char
        substringValue = int(substringValue)
        
        if (substring.find("red") > -1) and substringValue > 12:
            break
        
        if (substring.find("green") > -1) and substringValue > 13:
            break
            
        if (substring.find("blue") > -1) and substringValue > 14:
            break
        
        if lastInLine:
            total += gameNumber
            
        index = nextIndex + 1
            
    print("total: " + str(total))
        
