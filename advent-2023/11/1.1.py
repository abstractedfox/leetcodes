#do one that's less golfed
lines = open("input.txt").readlines()

#expand universe
for row in range(0, len(lines)):
    if lines[row][-1] == "\n":
        lines[row]=lines[row][0:-1]
    if len([x for x in lines[row] if x == '#'] == 0):
        lines.insert(row + 1, lines[row])
