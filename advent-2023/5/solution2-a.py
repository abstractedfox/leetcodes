#better-optimized solution, whenever i get to actually implementing it

file = open("input.txt", 'r')
input = file.read()

#note that each map describes a range of values, so for each value we want to convert using a given map, we're first assessing where it fits in that map
#find range in map A for value A > get value B from map A > repeat in map B for value B etc

maps = []
maplines = []
bufferSize = 1000000
realseeds = [None] * bufferSize

mapRangeBreaks = [None][None] * 7

#Return the conversion of a value against a map
def getConversion(mapIndex, value):
    for line in maplines[mapIndex]:
        if value >= line[1] and value < line[1] + line[2]:
            if mapIndex < 6:
                return getConversion(mapIndex + 1, line[0] + (value - line[1]))
            return line[0] + (value - line[1])
    
    if mapIndex < 6:
        return getConversion(mapIndex + 1, value)
    return value

def getLowestLocationOfSeeds():
    runningValue = 0
    min = getConversion(0, realseeds[0])
        
    for seed in realseeds:
        runningValue = getConversion(0, seed)
        
        if runningValue < min:
            min = runningValue
    return min

seeds = input[input.find(" ") + 1:input.find("\n\n")]
seeds = seeds.split()
valuesToFindMinOf = []
asdfcount = 0

#pre-process maps
inputchopped = input
while inputchopped.find("map:") > -1:
    inputchopped = inputchopped[inputchopped.find("map:") + 5 : len(inputchopped)]
    thisMap = inputchopped[0:inputchopped.find("\n\n")]
    maps.append(thisMap)

for mapIndex in range(len(maps)):
    aMapSplit = maps[mapIndex].split("\n")
    parsedMap = []
    for line in aMapSplit:
        #order is 'destination start', 'source start', 'length'
        dest = line[0:line.find(" ")]
        source = line[line.find(" ") + 1:len(line)]
        length = source[source.find(" "):len(source)]
        source = source[0:source.find(" ")]
        dest = int(dest)
        source = int(source)
        length = int(length)
        parsedMap.append([dest, source, length])
    maplines.append(parsedMap)
    #maplines[mapIndex] = parsedMap
    
for i in range(5, 0, -1):
    for line in maplines[i]:
        

#do all the seeds
for i in range(0, len(seeds), 2):
    print("new seed!")
    count = 0
    for j in range(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])):
        #realseeds.append(j)
        realseeds[count] = j
        count += 1
        #print(len(realseeds))
        if (count == bufferSize):
            count = 0
            if len(valuesToFindMinOf) > 0:
                print("current min " + str(valuesToFindMinOf[0]) + " " + str(asdfcount))
                asdfcount += 1
            valuesToFindMinOf.append(getLowestLocationOfSeeds())
            valuesToFindMinOf = [min(valuesToFindMinOf)]

realseeds = realseeds[0:count - 1]
valuesToFindMinOf.append(getLowestLocationOfSeeds())
valuesToFindMinOf = [min(valuesToFindMinOf)]
print("output: " + str(min(valuesToFindMinOf)))


