
file = open("input.txt", 'r')
input = file.readlines()

directions = input[0]
maplines = input[3:len(input)]

def getLineValues(line, leftOrRight):
    if leftOrRight == "name":
        return line[0:3]
    if leftOrRight == "L":
        return line[line.find("(") + 1:line.find(",")]
    if leftOrRight == "R":
        return line[line.find(",") + 2:line.find(")")]
    
def findLineByName(name):
    for line in maplines:
        if getLineValues(line, "name") == name:
            return line

def stepThroughMap(startingLine):
    steps = 0
    currentLine = startingLine
    for direction in directions:
        if direction == "\n":
            continue
        if getLineValues(currentLine, "name") == "ZZZ":
            return steps
        if direction == "L":
            currentLine = findLineByName(getLineValues(currentLine, "L"))
        else:
            currentLine = findLineByName(getLineValues(currentLine, "R"))
        steps += 1
    steps += stepThroughMap(currentLine)
    return steps

print(stepThroughMap(findLineByName("AAA")))
