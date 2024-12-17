#let's try a better version:
#if we work backwards from E, then we can check each node for "the best path to E" and build an index of this as it goes
#this should get faster the longer it runs since it will encounter more and more nodes that are already indexed

from helper import *
a=gi()

#a junction will be any ./S/E which is bordered by at least two other .'s, but not where the only two .'s are on the same vertical or horizontal line
jct=[]
jctmap=[]
def addpos(pos1,pos2):
    return [pos1[0]+pos2[0],pos1[1]+pos2[1]]
for r in rg(a):
    for c in rg(a[r]):
        if c == ".":
            dirs = [addpos([r,c], d) for d in dmap]
            dots=len([a[x[0]][x[1]] for x in dirs if a[x[0]][x[1]] == "."]) 
            if dots >= 2:
                if a[dirs[0][0]][dirs[0][1]] == a[dirs[2][0]][dirs[2][1]] and a[dirs[0][0]][dirs[0][1]] == ".":
                    continue
                if a[dirs[1][0]][dirs[1][1]] == a[dirs[3][0]][dirs[3][1]] and a[dirs[1][0]][dirs[1][1]] == ".":
                    continue
                jct.append([r,c])
                jctmap.append([])
       #finish this later 
