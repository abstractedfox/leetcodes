file = open("input.txt", 'r')
input = file.read()

#note that each map describes a range of values, so for each value we want to convert using a given map, we're first assessing where it fits in that map
#find range in map A for value A > get value B from map A > repeat in map B for value B etc

#Return the conversion of a value against a map
def getConversion(aMap, value):
    value = int(value)
    aMap = aMap.split("\n")
    for line in aMap:
        #order is 'destination start', 'source start', 'length'
        dest = line[0:line.find(" ")]
        source = line[line.find(" ") + 1:len(line)]
        length = source[source.find(" "):len(source)]
        source = source[0:source.find(" ")]
        dest = int(dest)
        source = int(source)
        length = int(length)

        #print(str(dest) + " " + str(source) + " " + str(length))
        if value >= source and value < source + length:
            return dest + (value - source)
    return value


seeds = input[input.find(" ") + 1:input.find("\n\n")]
seeds = seeds.split()
runningValue = 0
outputs = []
for seed in seeds:
    inputchopped = input
    runningValue = seed
    while inputchopped.find("map:") > -1:
        inputchopped = inputchopped[inputchopped.find("map:") + 5 : len(inputchopped)]
        thisMap = inputchopped[0:inputchopped.find("\n\n")]

        runningValue = getConversion(thisMap, runningValue)
    outputs.append(runningValue)

print(min(outputs))
