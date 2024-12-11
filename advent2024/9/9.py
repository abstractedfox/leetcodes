from helper import*
aa=gi()
#aa=["2333133121414131402"]
a=[int(x) for x in aa[0]]
blocks=[]
fid=0
for c in range(0,len(a)):
    if c%2==1:
        for i in range(0,a[c]):
            blocks.append("E")
    else:
        for i in range(0,a[c]):
            blocks.append(fid)
        fid+=1
o=0
#print(blocks)
for c in range(0,len(blocks)):
    break
    if blocks[c]=="E":
        for c2 in range(len(blocks)-1, c,-1):
            if c2<c:
                break
            if blocks[c2]!="E":
                blocks[c]=blocks[c2]
                blocks[c2]="E"
                break
    if blocks[c]!="E":
        o+=blocks[c]*c
    #print(blocks, o)
print(o)
print("\a")
aa=gi()
#aa=["2333133121414131402"]
a=[int(x) for x in aa[0]]
blocks=[]
fid=0
lblock=0
for c in range(0,len(a)):
    if c%2==1:
        for i in range(0,a[c]):
            blocks.append("E")
    else:
        for i in range(0,a[c]):
            blocks.append(fid)
            lblock=c
        fid+=1
o=0

aptr=lblock
for c in range(len(blocks)-1, -1, -1):
    if blocks[c]!="E":
        l=a[aptr]
        l=len([x for x in blocks if x==blocks[c]])
        if blocks[c:c+l] != [blocks[c] for x in range(0,l)]:
            continue
        aptr-=2
        #for d in range(c-1, -1, -1):
        for d in range(0,c):
            if len([x for x in blocks[d:d+l] if x == "E"]) == l:
                #print("moving",blocks[c:c+l],blocks[d:d+l],l)
                blocks[d:d+l]=blocks[c:c+l]
                blocks[c:c+l]=["E" for x in range(0, l)]
                #print(blocks)
                break
for c in range(0,len(blocks)):
    if blocks[c]!="E":
        o+=blocks[c]*c
    
print(o)
print("\a")
