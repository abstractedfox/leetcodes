file = open("input.txt", 'r')
input = file.readlines()


def getNextValue(sequenced):
    #skipping the last line (all zeroes) manually add the next element to the second to last line
    sequenced[-2].append(sequenced[-2][0])    
    
    for i in range(len(sequenced) - 3, -1, -1):
        sequenced[i].append(sequenced[i][-1] + sequenced[i + 1][-1])
    
    return sequenced[0][-1]

total = 0

for line in input:
    line = line.split()
    line = [int(item) for item in line]
    rows = [line]
    
    while all(element == 0 for element in rows[len(rows) - 1]) == False:
        newRow = []
        for i in range(1, len(rows[-1])):
            newRow.append(rows[-1][i] - rows[-1][i - 1])
        rows.append(newRow)
    total += getNextValue(rows)

print(total)
