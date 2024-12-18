from helper import *
a=gi()

a=gi("tinput.txt")
mach=[]
for x in range(0,len(a),4):
    mach.append([])
    mach[-1].append(ordb(a[x],[toi,jn]))
    mach[-1].append(ordb(a[x+1],[toi,jn]))
    mach[-1].append(ordb(a[x+2],[toi,jn]))
combinations=[]
ttl=0
for m in mach:
    works=[]
    for i in range(0,101):
        for j in range(0,101):
            #print(mach[0][0]*i+mach[1][0]*j, mach[2][0], mach[0][1]*i+mach[1][1]*j, mach[2][1])

            if m[0][0]*i+m[1][0]*j==m[2][0] and m[0][1]*i+m[1][1]*j==m[2][1]:
                works.append([i,j])
    works=sorted(works, key=lambda a:a[0]*3 + a[1])
    combinations.append(works)
    if len(works) > 0:
        ttl+=works[0][0]*3 + works[0][1]
print(ttl)

#part 2: learn how to do math first
