from collections import deque,defaultdict
from helper import *
a=gi()
#a=gi("tinput.txt")
#a=["aaaaa"]
b=[]
for x in a:
    b.append([y for y in x])
a=b
def incpos(pos,diff):
    return [pos[0]+diff[0],pos[1]+diff[1]]
def walk(pos,found,fence):
    ttl=1
    if pos in found:
        return 0
    found.append(pos)
    for m in dmap:
        npos=incpos(pos,m)
        if bounds(a,npos) and a[npos[0]][npos[1]] == a[pos[0]][pos[1]]:
            ttl+=walk(npos,found,fence)
        elif npos not in fence:
            fence.append(npos)
    return ttl

d={}
found=[]
i=0
for r in range(0,len(a)):
    for c in range(0,len(a[r])):
        if i not in d:
            d[i]=[]
        #if [r, c] not in [d[x] for x in d]: #this doesnt work!!!!! is this possible tow rite
        if [r, c] not in found:
            awa=[]
            walk([r, c],awa,[])
            found+=awa
            d[i]+=awa
            i+=1
            continue
            
            nxt=deque()
            nxt.append([r, c])
            while len(nxt)>0:
                d[i].append(nxt[0])
                for m in dmap:
                    npos=incpos(m,[r, c])
                    if bounds(a,npos) and a[npos[0]][npos[1]] == a[r][c] and npos not in d[i]:
                        nxt.append(npos)
                nxt.popleft()
o=0
for x in d:
    perim=0
    for pos in d[x]:
        poss=4
        for m in dmap:
            if incpos(pos,m) in d[x]:
                poss-=1
        perim+=poss
    o+=perim*len(d[x])
print(o)
