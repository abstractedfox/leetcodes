
file = open("input.txt", 'r')
input = file.readlines()

directions = input[0]
maplines = input[2:len(input)]
steps = 0


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

#this time, we'll say that on each call we make one single step and return where we ended up
def stepThroughMap(currentLine, direction):
    if direction == "L":
        return findLineByName(getLineValues(currentLine, "L"))
    else:
        return findLineByName(getLineValues(currentLine, "R"))

#i = a ghost, [i] = its current line in maplines
concurrentghostlines = []    
for line in maplines:
    if line[2] == "A":
        concurrentghostlines.append(line)

#i = a position in directions[], [i] = a dictionary of lines in maplines where the value of a given mapline = the number of steps from that line to the next 'Z' index for that line at that position in directions
indexOfZSteps = [{}] * len(directions)

#i = a position in directions[], [i] = a dictionary where the key = a line in maplines and the value = the destination of the next index of a 'z' from that line for that position in directions[]
indexOfZPositions = [{}] * len(directions)

#i = a ghost, [i] = the number of steps since it last saw a 'Z'
ghostStepsSinceLastZ = [0] * len(concurrentghostlines)

#indexOfEverything = [{}] * len(directions)
indexOfEverything = []
for count in range(len(directions)):
    indexOfEverything.append({})

endsInZ = False
indexcounty = 0
usedy = 0

indexOfDirections = {"L": {}, "R": {}}

directionsLength = len(directions)
ghostsLength = len(concurrentghostlines)
while endsInZ != True:
    for d in range(directionsLength):
        if directions[d] == "\n":
            break;
        endsInZ = True
        for i in range(ghostsLength):
            direction = directions[d]
            if concurrentghostlines[i] in indexOfDirections[direction]:
                newIndex = indexOfDirections[direction][concurrentghostlines[i]]
                concurrentghostlines[i] = newIndex
                
            else:
                print("indexed!" + str(indexcounty))
                indexcounty += 1
                #indexOfEverything[d][concurrentghostlines[i]] = stepThroughMap(concurrentghostlines[i], directions[d])
                newEntry = stepThroughMap(concurrentghostlines[i], direction)
                indexOfDirections[direction][concurrentghostlines[i]] = newEntry

                concurrentghostlines[i] = indexOfDirections[direction][concurrentghostlines[i]]

            steps += 1
            #ghostStepsSinceLastZ[i] += 1
            #print("checking " + concurrentghostlines[i][0:3] + "  " + str(concurrentghostlines[i][2] == "Z"))
            if concurrentghostlines[i][2] != "Z":
                endsInZ = False
        if endsInZ:
            break

print(concurrentghostlines)
#print("indexed " + str(indexcounty) + " things!")
print(steps)


#ok, alternative idea because this probably works but is taking 5ever: just count the steps between each instance of 'z' for each given starting position. create a loop where each 'ghost' has a step count which is incremented by 1 on each pass, and continue until all ghosts = a value in their index of z's
#and furthermore we could probably code That faster by indexing the 'z' indexes as we go as some function of a given location and place in the directions list, ie line x at directions position y = this number of steps to the next 'z' index
