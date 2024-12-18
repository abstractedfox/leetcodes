#this is definitely shaped like something that would work
#consider working backwards from E instead because we could index the most efficient paths and have really easy lookahead by the time we're getting close to the beginning

from helper import *
a=gi()
a=gi("tinput.txt")

jct=[]
jctmap=[]
start=[]
def concatcoord(pos):
    return str(pos[0])+"|"+str(pos[1])

ct=0
pos=[]
for r in rg(a):
    for c in rg(a[r]):
        if a[r][c] == "E":
            pos=[r,c]
for r in rg(a):
    for c in rg(a[r]):
        #if a[r][c]==".":
        if a[r][c]=="." or a[r][c] == "S" or a[r][c]=="E":
            dirs=[addpos([r,c], x) for x in dmap]
            if len([x for x in dirs if a[x[0]][x[1]]=="."]) == 2:
                if a[dirs[0][0]][dirs[0][1]] == a[dirs[2][0]][dirs[2][1]] and a[dirs[0][0]][dirs[0][1]] == ".":
                    continue
                if a[dirs[1][0]][dirs[1][1]] == a[dirs[3][0]][dirs[3][1]] and a[dirs[1][0]][dirs[1][1]] == ".":
                    continue
            if len([x for x in dirs if a[x[0]][x[1]]=="."]) >= 2:
                #jct.append(concatcoord([r,c]))
                jct.append([r,c])
                jctmap.append([])
print(len(jct), "nodes found")
for x in jct:
    for d in dmap:
        pos = addpos(x,d)
        poschar=a[pos[0]][pos[1]] 
        steps=0
        while poschar != "#":
            steps+=1
            entry=[]
            if pos in jct:
                entry.append(pos)
                entry.append(steps)
            
            if poschar == "S":
                entry.append("S")
        
            if poschar == "E":
                entry.append("E")
            if entry != []:
                jctmap[jct.index(x)].append(entry)
                if "S" in entry:
                    start=x
            pos = addpos(pos,d)
            poschar=a[pos[0]][pos[1]] 
def getscore(path):
    score=0
    for n in path:
        score+=1000
        score+=n[1]
    return score
bests_path=[]
scoremap={}

def reaches_e(node, path):
    best_path=[]
    for n in jctmap[jct.index(node)]:
        if "E" in n:
            print("E")
            path.append(n)
            return path
        if n not in path:
            npath=dcp(path)
            npath.append(n)
            test=reaches_e(n[0], npath)
            if test == []:
                continue
            if best_path==[] or getscore(best_path) > getscore(test):
                best_path=test
                if test not in bests_path:
                    bests_path.append(test)
                    print("new best score", getscore(best_path))
                else:
                    print("dupe path!!")
    return best_path

path=reaches_e(start, [])
print(score(path))
