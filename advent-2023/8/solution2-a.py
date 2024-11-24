file = open("input.txt", 'r')
input = file.readlines()

directions = input[0]
maplines = input[2:len(input)]
steps = 0

directions = directions[0:-1]

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
ghosts = []    
for line in maplines:
    if line[2] == "A":
        ghosts.append(line)
        
#ghosts = ghosts[0:3]
        
def oldSolution():
    #old dead solution below
    steps = 0
    endsInZ = False
    indexcounty = 0

    indexOfDirections = {"L": {}, "R": {}}

    directionsLength = len(directions)
    ghostsLength = len(ghosts)
    while endsInZ != True:
        for d in range(directionsLength):
            if directions[d] == "\n":
                break;
            endsInZ = True
            for i in range(ghostsLength):
                direction = directions[d]
                if ghosts[i] in indexOfDirections[direction]:
                    newIndex = indexOfDirections[direction][ghosts[i]]
                    ghosts[i] = newIndex
                    
                else:
                    print("indexed!" + str(indexcounty))
                    indexcounty += 1
                    newEntry = stepThroughMap(ghosts[i], direction)
                    indexOfDirections[direction][ghosts[i]] = newEntry

                    ghosts[i] = indexOfDirections[direction][ghosts[i]]

                steps += 1
                if ghosts[i][2] != "Z":
                    endsInZ = False
                    
                #if i == 0 and ghosts[i][2] == "Z":
                #    print(steps)
            if endsInZ:
                break

    print(ghosts)
    print(steps)

    exit()
    
#oldSolution()

#the entire path each ghost takes to end up back at its starting position
ghostZPositions = [[] for ghost in ghosts]

for i in range(len(ghosts)):
    positions = []
    
    loopOffset = None
    repeat = True
    offset = 0
    startingPos = ghosts[i]
    while repeat:
        for d in range(len(directions)):
            #print(str(len(positions)) + " " + str(i))
            ghosts[i] = stepThroughMap(ghosts[i], directions[d])
            
            if loopOffset is not None and (offset * len(directions)) + d == loopOffset * 2:
                repeat = False
                break
            
            #note: the loop entry index has to be both the same index and at the same pos in directions
            if ghosts[i] in positions and loopOffset == None and positions.index(ghosts[i]) % len(directions) == d:
                #print(str(positions.index(ghosts[i])) + " and " + str(offset * len(directions) + d))
                loopOffset = (len(directions) * offset)# + i
                #print("loop entry at " + str(loopOffset) + " " + ghosts[i])
                continue
            
            if loopOffset == None:
                positions.append(ghosts[i])
            
            if loopOffset is not None and ghosts[i][2] == "Z":
                ghostZPositions[i].append((d, offset, loopOffset))
        offset += 1
        
for jawn in ghostZPositions:
    print(jawn)
    
#finally, once we've plotted all our z positions, all we need to do is create a new set for each ghost and a new loop where on each step, we count through a full 'directions' list worth of z positions for each ghost, specifically tracking the number of steps it would take for that ghost to get to that position. if any position is present in all ghosts, return it
    
totalZ = 0
maxoffset = 0
counters = []
for item in ghostZPositions:
    for position in item:
        if maxoffset < position[2]:
            maxoffset = position[2]
        totalZ += 1
        
print("max loop start offset is " + str((maxoffset)))

directionsCounter = 0
directionsLength = len(directions)

#ok so wait a second, i think we're looking at this again dumbly.
#the 'all ghosts land on a Z' happens where:
#we can find the first value that consists of every ghostZPositions' 'offset' value incremented by itself to where they all equal the same value
#AFTER initializing each value to a multiple of its own 'offset' value where its own count of steps would exceed the highest 'loopOffset' value
            
for ghost in ghostZPositions:
    for z in ghost:
        counters.append(z[1])
        #print(str(counters[-1] * len(directions)))
        if z[2] != maxoffset:
            #give each z counter a starting value that is above the highest loop entry value we found earlier
            counters[-1] = counters[-1] * int(maxoffset / (counters[-1] * len(directions))) + counters[-1]

while True:
    test = counters[0]
    for element in counters:
        if element != test:
            counters[counters.index(min(counters))] += min(counters)
            continue
    print(test * len(directions) + ((test * len(directions)) % len(directions)))
    exit()
    

while True:
    #i = a ghost, i[] = the number of steps this ghost has taken to reach its 'z' indexes on this pass
    #actually, nevermind. a dumb list that just contains a count of steps for every 'z' index we've found in this pass
    ghostcounts = []
    
    #For each ghost, check if we can get to its 'z' positions on this iteration of 'directions', and if so, let's hold the number of steps to get to them
    for i in range(len(ghosts)):
        #to know if we're on a 'z': directionsCounter % offset (offset being the second index of the ghost Z positions)
        for z in range(len(ghostZPositions[i])):
            if directionsCounter % ghostZPositions[i][z][1] == 0:
                ghostcounts.append(ghostZPositions[i][z][0] + directionsLength * directionsCounter)
    
    #print(str(directionsCounter * len(directions)) + " " + str(len(ghostcounts)))
    if len(ghostcounts) == totalZ:
        success = True
        checkValue = ghostcounts[0]
        for steps in ghostcounts:
            if steps != checkValue:
                success = False
                break
        if success:
            print(checkValue)
            print(checkValue + maxoffset)
            exit()
            
    directionsCounter += 1
        
    
exit()


#ok, alternative idea because this probably works but is taking 5ever: just count the steps between each instance of 'z' for each given starting position. create a loop where each 'ghost' has a step count which is incremented by 1 on each pass, and continue until all ghosts = a value in their index of z's
#and furthermore we could probably code That faster by indexing the 'z' indexes as we go as some function of a given location and place in the directions list, ie line x at directions position y = this number of steps to the next 'z' index
