#this solution is incomplete

import common

file = open("input.txt", 'r')
input = file.read()

start = input.find("S")
lineLength = input.find("\n") + 1

loopNodes = []

xAxisOrientation = []

#For a cardinal direction and element, return the value of the next index we will land on
def nextDirection(incomingDirection, element):
    if element == "F":
        if incomingDirection == "north":
            return "east"
        else:
            return "south"
        
    if element == "J":
        if incomingDirection == "south":
            return "west"
        return "north"
        
    if element == "L":
        if incomingDirection == "west":
            return "north"
        return "east"
        
    if element == "7":
        if incomingDirection == "north":
            return "west"
        return "south"
            
    if element == "-":
        return incomingDirection
            
    if element == "|":
        return incomingDirection


currentPosition = start
steps = 0

input = list(input)
input[start] = "|"
input = "".join(input)

directionMoving = "north"

while True:
    up = common.resolveDirectionalIndex(input, currentPosition, 0, -1)
    right = common.resolveDirectionalIndex(input, currentPosition, 1, 0)
    down = common.resolveDirectionalIndex(input, currentPosition, 0, 1)
    left = common.resolveDirectionalIndex(input, currentPosition, -1, 0)
    
    loopNodes.append(currentPosition)
    
    if directionMoving == "north":
        currentPosition = up
        xAxisOrientation.append(-1)
        
    if directionMoving == "east":
        currentPosition = right
        xAxisOrientation.append(1)
        
    if directionMoving == "south":
        currentPosition = down
        xAxisOrientation.append(1)
    
    if directionMoving == "west":
        currentPosition = left
        xAxisOrientation.append(-1)
        
    directionMoving = nextDirection(directionMoving, input[currentPosition])
    
    steps += 1
    
    if currentPosition == start:
        break
        
#for the 'find enclosed elements' part, let's say that any element that is bordered by elements belonging to the loop on the left and right, and which hits boundaries created by the loop on the top and bottom (accounting for the 'between the pipes' rule) is considered enclosed

for i in range(len(input)):
    goLeft = i
    success = False
    if i > 0 and input[i - 1] != '\n':
        while goLeft >= 0 and input[goLeft] != '\n':
            if goLeft in loopNodes:
                success = True
                break
            goLeft -= 1
        if !success:
            continue
        
    goRight = i
    if i < len(input) and input[i + 1] != '\n':
        while goRight < len(input) and input[goRight] != '\n':
            if goRight in loopNodes:
                success = True
                break
            goRight += 1
        if !success:
            continue

    goUp = i
    if i > lineLength:
        boundaries = 0
        goUp -= lineLength
        foundLeft = False
        foundRight = False
        while goUp >= 0 and hits < 2:
            #Check for boundaries on both sides of the index going up
            if goUp in loopNodes:
                if input[goUp] == "7" or input[goUp] == "F":
                    hits += 1
                if input[goUp] == "-":
                    hits += 2
            goUp -= lineLength
        if !success:
            continue
            
        
                
