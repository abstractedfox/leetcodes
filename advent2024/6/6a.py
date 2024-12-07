from helper import *

a=gi()
start=[]
m=[[-1,0],[0,1],[1,0],[0,-1]]
for x in rg(a):
    if "^" in a[x]:
        start=[x,a[x].index("^")]
def awa(a):
    d=m[0]
    pos=dcp(start)
    ct=1
    found=[]
    while True:
        npos=dcp(pos)
        npos[0]+=d[0]
        npos[1]+=d[1]
        while a[npos[0]][npos[1]]=="#":
            d=m[(m.index(d)+1) % 4] 

            npos=dcp(pos)
            npos[0]+=d[0]
            npos[1]+=d[1]
        pos=dcp(npos) 
        print(pos)
        if pos[0] < 0 or pos[0]>len(a)-1 or pos[1] > len(a[0]) or pos[1] < 0:
            break
        if pos not in found:
            found.append(pos)
            ct+=1
    print(ct)

awa(a)
