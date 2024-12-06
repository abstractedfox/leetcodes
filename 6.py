from helper import *

a=gi()

d=[-1,0]

pos=[0,0]
for r in rg(a):
    if "^" in r[a]:
        pos=[r,r[a].index("^")]
        break
ct=0
while True:
    try:
        newpos=pos
        newpos[0]+=d[0]
        newpos[1]+=d[1]
        if a[newpos[0]][newpos[1]] == "#":
            m=[[-1,0],[0,1],[1,0],[0,-1]]
            d=m[(m.index(d)+1)%4]
        pos=newpos
        ct+=1
    except:
        break

print(ct)



