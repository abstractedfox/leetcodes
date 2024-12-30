from helper import *
a=gi()
#a=gi("tinput.txt")
#a junction will be any ./S/E which is bordered by at least two other .'s, but not where the only two .'s are on the same vertical or horizontal line
jct=[]
jctmap=[]
index=[]
start=None

copy=dcp(a)

import sys
sys.setrecursionlimit(10000)
def addpos(pos1,pos2):
    return [pos1[0]+pos2[0],pos1[1]+pos2[1]]
for r in rg(a):
    for c in rg(a[r]):
        if a[r][c]=="E":
            jct.append([r,c])
            jctmap.append([])
            index.append([])
            continue  
        if a[r][c] == "."   or a[r][c]=="S":
            dirs = [addpos([r,c], d) for d in dmap]
            dots=len([a[x[0]][x[1]] for x in dirs if a[x[0]][x[1]] == "."]) 
            if dots == 2:
                if a[dirs[0][0]][dirs[0][1]] == a[dirs[2][0]][dirs[2][1]] and a[dirs[0][0]][dirs[0][1]] == ".":
                    continue
                if a[dirs[1][0]][dirs[1][1]] == a[dirs[3][0]][dirs[3][1]] and a[dirs[1][0]][dirs[1][1]] == ".":
                    continue
            if dots >= 2:
                jct.append([r,c])
                jctmap.append([])
                index.append([])
for node in range(0, len(jct)):
    for d in dmap:
        pos=addpos(d,jct[node])
        i=1
        while a[pos[0]][pos[1]] != "#":
            if pos in jct:
                #jctmap[jct.index(node)].append(a[pos[0][pos[1]]
                jctmap[jct.index(jct[node])].append({"pos": pos, "i": i})
                if a[pos[0]][pos[1]] == "E":
                    jctmap[jct.index(jct[node])][-1]["E"] = "E"
                if a[pos[0]][pos[1]] == "S":
                    start=jct[node]
                #break
            pos=addpos(d,pos)
            i+=1

def score(path):
    ttl=0
    if path[0]["pos"][0] != path[1]["pos"][0]:
        ttl+=1000
    for x in path:
        ttl+=x["i"]
    ttl+=1000*len(path)-2
    return ttl

found=[]

def walk(startpos, history, v=False):
    if v:
        print(startpos)
    copy[startpos[0]]=repl(copy[startpos[0]],"*",startpos[1])
    if v:
        copy[startpos[0]]=repl(copy[startpos[0]],"&",startpos[1])
        
    #print("HEYYYYYYY===============")
    if startpos[0] == 99 and startpos[1]== 23:
        print("WE INT HE THING")
    if startpos[0] == 99 and startpos[1]== 25:
        print("WE almost INT HE THING")
        print("positions relating to ", startpos, jctmap[jct.index(startpos)])
    if v:
        for l in copy:
            print(l)
    best=None
    #ahh wait i think the issue we've been having is that we assumed it would take care of itself in situations where there are no paths to E (ie in a loop) because it would see the other nodes in 'history' and continue. this does stop it from going back over the node it just came from but doesn't stop it from infinite looping. i think what happened is that it would eventually unwind enough from bumping into 'history' enough that it would end up back in a fresh enough state to re-loop into a section it had just gone over (ie i assume they put in some nested loops just for people whose algorithm always looks in the same order of directions))
    #in tandem with this, i think we assumed naively that every node would have a path to x that didn't require backtracking
    if len([x for x in jctmap[jct.index(startpos)] if x["pos"] in history]) == len(jctmap[jct.index(startpos)]):
        return None
    for connection in jctmap[jct.index(startpos)]:
        if startpos[0] == 99 and startpos[1]== 25:
            print("connect!!",connection)
        #print(jctmap[jct.index(startpos)])
        if "E" in connection:
            print("e")
            nhistory=dcp(history)
            nhistory.append(connection)
            return nhistory
        if connection["pos"] in [x["pos"] for x in history]:
            continue
        test=None
        if index[jct.index(startpos)] != []:
            if startpos[0] == 99 and startpos[1]== 25:
                print("i guess we're indexed")
            nhistory=dcp(history)
            nhistory+=index[jct.index(startpos)]
            test = nhistory
        else:
            nhistory=dcp(history)
            nhistory.append(connection)
            if startpos[0] == 99 and startpos[1]== 25:
                print("about to call again for ", connection["pos"])
                test=walk(connection["pos"], nhistory, v=True)
            else:
                test=walk(connection["pos"], nhistory, v=v)
            if startpos[0] == 99 and startpos[1]== 25:
                print("back from call!!")
        if startpos[0] == 99 and startpos[1]== 25:
            print("on",connection, "test?", test is not None)
        #print(test, best)
        if test is not None and (best is None or score(test)<score(best)):
            best=test
    if best is not None:
        print("indexing!",best)
        index[jct.index(startpos)] = best[(len(history)):]
    
    if startpos[0] == 99 and startpos[1]== 25:
        print("somehow we're returning")
    
    return best

best=walk(start, [])
print("done")
print(best)
print("len", len(best))
print(score(best))
