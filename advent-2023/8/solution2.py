
file = open("input.txt", 'r')
input = file.readlines()

directions = input[0]
maplines = input[2:len(input)]
steps = 0

directionsIndex = [{}] * len(directions)

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

#i = a ghost, [i] = the number of steps since it last saw a 'Z'
ghostStepsSinceLastZ = [0] * len(concurrentghostlines)

#i = a ghost, [i] = the contents of the last 'Z' line it saw
ghostLastZ = [None] * len(concurrentghostlines)

endsInZ = False
while endsInZ != True:
    for direction in directions:
        if direction == "\n":
            break;
        endsInZ = True
        for i in range(len(concurrentghostlines)):
            concurrentghostlines[i] = stepThroughMap(concurrentghostlines[i], direction)
            ghostStepsSinceLastZ[i] += 1
            if concurrentghostlines[i][2] == "Z":
                ghostStepsSinecLastZ[i] = 0
                #note for next time i return to this: this is where we need to zero the steps since last Z count, set ghostlastz, and either check or update the Z value index
            else:
                endsInZ = False

print(steps)


#ok, alternative idea because this probably works but is taking 5ever: just count the steps between each instance of 'z' for each given starting position. create a loop where each 'ghost' has a step count which is incremented by 1 on each pass, and continue until all ghosts = a value in their index of z's
#and furthermore we could probably code That faster by indexing the 'z' indexes as we go as some function of a given location and place in the directions list, ie line x at directions position y = this number of steps to the next 'z' index
