
times = [34, 90, 89, 86]
distances = [204, 1713, 1210, 1780]

#for each millisecond subtracted, distance increases by 1 millimeter per millisecond

def getDistance(index, millisecondsHeld):
    return millisecondsHeld * (times[index] - millisecondsHeld)

winningValues = []
output = 1
for i in range(len(times)):
    half = int(int(times[i]) / int(2))
    hits = 0
    while getDistance(i, half) > distances[i] and half > -1:
        hits += 1
        half -= 1
        
    half = int(int(times[i]) / int(2) + 1)
    while half < times[i] and getDistance(i, half) > distances[i]:
        hits += 1
        half += 1
        
    output *= hits
        
print(output)
    
