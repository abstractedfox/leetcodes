import re

file = open ("input.txt", 'r')
input = file.read()

length = len(input)
lineLength = input.find("\n") + 1
total = 0
    
def numberGrab(index):
    counter = index
    while input[counter].isnumeric():
        counter -= 1
    counter += 1
    
    output = ""
    while input[counter].isnumeric():
        output += str(input[counter])
        counter += 1
        
    if output == "":
        output = 1
        
    return int(output)

def checksOut(index):
    return input[index].isnumeric()

for i in range(length):
    if input[i] == '*':
        ratio = 1
        numCounter = 0
        if i - lineLength > 0:
            #if i - linelength is a ., we can treat the other two places as separate numbers if they are numbers, but if it's a number, anything we can find on i - linelength will be one number
            
            if checksOut(i - lineLength):
                ratio *= numberGrab(i - lineLength)
                numCounter += 1
                
            else:
                if i - lineLength != 0 and checksOut(i - lineLength - 1):
                    ratio *= numberGrab(i - lineLength - 1)
                    numCounter += 1
                if checksOut(i - lineLength + 1):
                    numCounter += 1
                    ratio *= numberGrab(i - lineLength + 1)
                
        if i != 0 and checksOut(i - 1):
            numCounter += 1
            ratio *= numberGrab(i - 1)
        
        if i + 1 < length and checksOut(i + 1):
            numCounter += 1
            ratio *= numberGrab(i + 1)
            
        if i + lineLength < length:
            if checksOut(i + lineLength):
                ratio *= numberGrab(i + lineLength)
                numCounter += 1
            else:
                if i + lineLength + 1 < length and checksOut(i + lineLength + 1):
                    numCounter += 1
                    ratio *= numberGrab(i + lineLength + 1)
                if checksOut(i + lineLength - 1): 
                    numCounter += 1
                    ratio *= numberGrab(i + lineLength - 1)
                
        if numCounter == 2:
            total += ratio
        
print("result2: " + str(total))
