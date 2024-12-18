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
for i in range(0, steps):
    for r in range(0, len(a)):
        a[r][0] = addcoords(a[r][0],a[r][1], boundx, boundy)
quads=[0,0,0,0]
for r in a:
    left=None
    if r[0][0] > 50:
        left=False
    elif r[0][0] < 50:
        left=True
    if left is None:
        continue
    if r[0][1] < 51:
        if left:
            quads[0]+=1
        else:
            quads[1]+=1
    elif r[0][1] > 51:
        if left:
            quads[2]+=1
        else:
            quads[3]+=1
    else:
        continue
print(quads)
print(quads[0]*quads[1]*quads[2]*quads[3])
