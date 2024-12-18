from helper import *
a=gi()
for i in rg(a):
    n=ordb(a[i],[toi,jn,signed])
    a[i]=[n[0:2], n[2:4]]
   
def addcoords(a, b,overflowx, overflowy):
    return [(a[0]+b[0]) % overflowx, (a[1]+b[1]) % overflowy]
steps=100
ttl=0
boundx=101
boundy=103

origa=dcp(a)
ct=0
samesies=[]
lut={}
outfile = open("outfile.txt","w")
jawns=[]
while True:
    for i in range(0, steps):
        for r in range(0, len(a)):
            key=str(a[r][0][0])+","+str(a[r][0][1])+","+str(a[r][1][0])+","+str(a[r][1][1])
            if key not in lut:
                lut[key]=addcoords(a[r][0],a[r][1], boundx, boundy)
            a[r][0] = lut[key] 
            #a[r][0] = addcoords(a[r][0],a[r][1], boundx, boundy)
    ct+=1

    if a==origa:
        break
    field=[[] for x in range(0,103)]
    for f in field:
        for x in range(0, 101):
            f.append(".")    
    
    segmentct=32 
    segs=[[0 for x in range(0, segmentct)] for x in range(0, segmentct)]    
    quads=[0,0,0,0]
    for r in a:
        if r[0][0] == 0:
            xcoord = 0
        else:
            xcoord=int(segmentct//(101/(r[0][0])))
        if r[0][1] == 0:
            ycoord=0
        else:
            ycoord=int(segmentct//(103/(r[0][1])))

        segs[ycoord][xcoord]+=1
        field[r[0][1]][r[0][0]] = "*"

        continue

    direction=0
    changes=[]
    score=0
    for seg in range(1,len(segs)):
        change=sum(segs[seg])-sum(segs[seg-1])
        direction+=change
        changes.append(change)
        if len(changes) > 1 and changes[-1] > changes[-2]:
            score+=1
    if score==19:
        print(ct, "\a")
        for seg in segs:
            print(seg, sum(seg))
        for x in field:
            print(jn2str(x))
    jawns.append([ct, score])
    continue

#print(quads)
#print(quads[0]*quads[1]*quads[2]*quads[3])

for x in sorted(jawns, key = lambda j:j[1]):
    print(x)
