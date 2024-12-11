from helper import *
a=gi()
#a=gi("ttinput.txt")

for x in range(0,len(a)):
    a[x]=ordb(a[x],[toi])
z=[]
for x in range(0,len(a)):
    for j in range(0,len(a[0])):
        if a[x][j]==0:
            z.append([x,j])

m=[[-1,0],[0,1],[1,0],[0,-1]]
cts=[]
def walk(a,s,d=False):
    score=0
    mm=[]
    def addpairs(p1,p2):
        return [p1[0]+p2[0], p1[1]+p2[1]]
    if a[s[0]][s[1]] == 9:
        if [s[0],s[1]] not in cts:
            cts.append([s[0],s[1]])
        return 1 
    for x in m:
        mm.append(addpairs(s,x))
    for x in mm:
        try:
            if len([y for y in x if y<0])>0:
                continue
            if a[x[0]][x[1]] - a[s[0]][s[1]] == 1:

                score+=walk(a,x,d) 
        except:
            continue
    return score 
ttl=0
rtg=0
for x in z:
    out=0
    out=walk(a,x,d= False)
    ttl+=len(cts)
    rtg+=out
    cts=[]
print(ttl,rtg)
