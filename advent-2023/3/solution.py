import re

file = open ("input.txt", 'r')
input = file.read()

lineLength = input.find("\n") + 1
length = len(input)
#regex = r"\D*[^\.]"
regex = r"\*|#|\$|&|=|\/|\+|-|%|@"
total = 0

knownPartIndexes = [] #For part 2

#check if one character has any symbols in an adjacent index
def adjacentSymbol(index):
    if index - 1 > 0 and re.search(regex, input[index - 1:index]) is not None:
        return True
        
    if (index > lineLength):
        prevLineStart = index - lineLength - 1
        prevLineEnd = prevLineStart + 2
        while prevLineStart < 0:
            prevLineStart += 1
        if re.search(regex, input[prevLineStart:prevLineEnd + 1]) is not None:
            return True
    
    if index + 1 < length and input[index + 1:index + 2] != '\n':
        if re.search(regex, input[index + 1:index + 2]) is not None:
            return True
            
    if index + lineLength - 1 < length:
        nextLineStart = index + lineLength - 1
        nextLineEnd = index + lineLength + 2
        while nextLineEnd > length:
            nextLineEnd -= 1
        
        if re.search(regex, input[nextLineStart:nextLineEnd]) is not None:
            return True
                
    return False
    
def getPartIndexes():
    return knownPartIndexes

iterator = iter(range(length))
for i in iterator:
    foundPart = False
    newVal = ""
    indexes = []
    while input[i].isnumeric():
        newVal += str(input[i])
        if foundPart == False and adjacentSymbol(i) == True:
            foundPart = True
        indexes.append(i)
        i += 1
        next(iterator, None)
    if (foundPart):
        total += int(newVal)
        knownPartIndexes += indexes

print("result:" + str(total))
