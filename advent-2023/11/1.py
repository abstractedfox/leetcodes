#works for 'test' input, does not work for real input

a = open("input.txt").readlines()
#a = open("test.txt").readlines()
#a = open("dumb").readlines()

i = 0
h=[x for x in range(0,len(a[0])-1 )]
while i < len(a):
    if a[i][-1]=='\n':
        a[i] = a[i][0:-1]
    if len(a[-1]) <2:
        a=a[0:-1]
    for c in range(0, len(a[i])):
        if a[i][c]!='.' and c in h:
            h.remove(c)
    if len([x for x in a[i] if x == "."]) == len(a[i]):
        a.insert(i + 1, a[i])
        i+=1
    i+=1
print(h)
for r in h:
    for l in range(0, len(a)):
        a[l]=a[l][0:r]+'.'+a[l][r:]
    for x in h:
        h[h.index(x)] += 1

pairs=[]
ttl=0

for l in range(0, len(a)):
    sameline=[]
    for j in range(0, len(a[l])):
        if a[l][j] == "#":
            sameline.append(j)
            for k in range(l+1, len(a)):
                for x in range(0, len(a[k])):
                    if a[k][x] == "#":
                        ttl += (k-l)+abs(x-j)
    for i in sameline:
        if sameline.index(i) > 0:
            ttl+=i-sameline[sameline.index(i)-1]
    sameline = []
print(ttl)
