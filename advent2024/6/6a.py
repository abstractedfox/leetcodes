from helper import *

a=gi()
start=[]
m=[[-1,0],[0,1],[1,0],[0,-1]]
for x in rg(a):
    if "^" in a[x]:
        start=[x,a[x].index("^")]
def awa(a,found=[], rfound=False):
    if rfound:
        found=[]
    foundct=[]
    d=m[0]
    pos=dcp(start)
    ct=1
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
        if pos[0] < 0 or pos[0]>len(a)-1 or pos[1] > len(a[0]) or pos[1] < 0:
            break
        if pos not in found:
            found.append(pos)
            ct+=1
            foundct.append([ct])
            print("HELO")
        else:
            foundct[found.index(pos)].append(ct)
            print(foundct[found.index(pos)], len(foundct[found.index(pos)]), found.index(pos), len(foundct))
            if len(foundct[found.index(pos)])>3:
                print("return")
                return True
    return(ct)
found=[]
print(awa(a,found))
loop=0
for x in found:
    cp=dcp(a)
    cp[x[0]]=repl(a[x[0]],"X",x[1])
    if awa(cp,rfound=True) == True:
        loop+=1
        print(loop)
