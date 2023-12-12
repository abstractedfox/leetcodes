import common

file = open("input.txt", 'r')
input = file.read()

start = input.find("S")

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
    
    if directionMoving == "north":
        currentPosition = up
        
    if directionMoving == "east":
        currentPosition = right
        
    if directionMoving == "south":
        currentPosition = down
    
    if directionMoving == "west":
        currentPosition = left
        
    directionMoving = nextDirection(directionMoving, input[currentPosition])
    
    steps += 1
    
    if currentPosition == start:
        break
        
print(steps / 2)
