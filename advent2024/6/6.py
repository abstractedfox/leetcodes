from helper import *

#ok some leaving off notes for me because this is well past the point of 4am code
#we're ending up in a situation where inserting a character into the source array causes unexpected behavior with the security guard walk

a=gi()
a=["....#.....",
".........#",
"..........",
"..#.......",
".......#..",
"..........",
".#..^.....",
"........#.",
"#.........",
"......#..."]
a=gi()


d=[-1,0]

pos=[0,0]
for r in rg(a):
    if "^" in a[r]:
        pos=[r,a[r].index("^")]
        break
initpos=[x for x in pos]
ct=0
found=[]
firststeps=0
while True:
    try:
        newpos=[x for x in pos]
        newpos[0]+=d[0]
        newpos[1]+=d[1]
        if a[newpos[0]][newpos[1]] == "#":
            if firststeps==0:
                firststeps=ct+1
                #in case we have to exclude the entire first path from pt2
            m=[[-1,0],[0,1],[1,0],[0,-1]]
            d=m[(m.index(d)+1)%4]
            newpos=[x for x in pos]
            newpos[0]+=d[0]
            newpos[1]+=d[1]
        if newpos[0] < 0:
            ct+=1
            break
        pos=[x for x in newpos]
        if pos not in found:
            ct+=1
            found.append([x for x in pos])
    except:
        break

m=[[-1,0],[0,1],[1,0],[0,-1]]
print(ct)
lastresult=0
def run(a):
    out=False
    found=[]
    foundmap=[]
    ct=0
    d=[-1,0]
    
    pos=[x for x in initpos]
    newpos=[0,0]
    
    hitblock=False 
    while True:
        try:
            newpos=[x for x in pos]
            
            newpos[0]+=d[0]
            newpos[1]+=d[1]
            while a[newpos[0]][newpos[1]] != ".":
                if a[newpos[0]][newpos[1]] == "!":
                    #print("we hit da block!")
                    hitblock=True
                d=m[(m.index(d)+1)%4]
                newpos=[x for x in pos]

                newpos[0]+=d[0]
                newpos[1]+=d[1]
            if newpos[0] < 0 or newpos[1]>=len(a[0]) or newpos[1] <0:
                ct+=1
                out=True
                break
            pos=[x for x in newpos]
            if pos not in found:
                ct+=1
                found.append([x for x in pos])
                foundmap.append([ct])
            else:
                #is it an issue if this gets hit for 2nd+ times hitting a block where it was initially recorded the first time?
                foundmap[found.index(pos)].append(ct)
                x=foundmap[found.index(pos)]
                if len(x) > 3: #having this set to 3 instead of 2 changes the output!!!!! (2 gets more, lower precision??)
                    if x[-1]-x[-2] == x[-2]-x[-3] and x[-2]-x[-3]==x[-3]-x[-4]:
                        if not hitblock:
                            print("FFFFUUUUUUCCCKKKKKKKK loop confirmed")
                        return True
        except IndexError:
            lastresult=ct
            if not hitblock:
                return "FFFFUUUUUUCCCKKKKKKKK"
            return False 
    if not hitblock:
        return "FFFFUUUUUUCCCKKKKKKKK"
    return False

blah = run(a)


ttl=0
if True:
    for l in rg(found):
        '''
        if found[l] in found[0:firststeps]:
            print("skip")
            continue
        '''
        #b=[x for x in a]
        #b[found[l][0]]=repl(b[found[l][0]],"!",found[l][1])
        h=a[found[l][0]]
        a[found[l][0]]=repl(a[found[l][0]],"!",found[l][1])
        result=run(a)
        a[found[l][0]]=h
        if result == True:
            ttl+=1
            print(ttl) 
        if result =="FFFFUUUUUUCCCKKKKKKKK":
            print("something's fucked!")
            print(found[l])
            #print(b[found[l][0]])
    exit()

if False:
    from multiprocessing import Pool, Lock
    pool=Pool(processes=6)
    lock=Lock()
    for l in range(0,len(found),6):
        jawns=[]
        def awa():
            if found[l] in found[0:firststeps]:
                print("skip")
                return
            b=[x for x in a]
            b[found[l][0]]=repl(b[found[l][0]],"#",found[l][1])
            if run(b):
                ttl+=1
                print(ttl) 
        

    exit()
for l in rg(a):
    for c in rg(a[0]):
        b=[x for x in a]
        for x in rg(b):
            b[x]=[y for y in b[x]]
        b[l][c]="#"
        if run(b):
            ttl+=1
            print(ttl) 
print(ttl)




