from helper import *
a=gi()
#a=gi("tinput.txt")

def gps(r, c):
    return (100*r)+c 

warehouse=[x for x in a[0:50]]
#warehouse=[y for y in a[0:11]]
for x in rg(warehouse):
    warehouse[x]=[y for y in warehouse[x]]
pt2=True
if pt2:
    for x in rg(warehouse):
        for y in range(0,len(warehouse[x]),2):
            poschar=warehouse[x][y]
            if poschar=="#":
                warehouse[x].insert(y,"#")
            if poschar=="O":
                warehouse[x][y]="["
                warehouse[x].insert(y,"]")
            if poschar==".":
                warehouse[x].insert(y,".")
            if poschar=="@":
                warehouse[x][y]="@"
                warehouse[x].insert(y,".")
moves=""
for x in a[51:]:
    if len(x)>1:
        moves+=x
def getrobotpos():
    robot=[0,0]
    for r in warehouse:
        for c in r:
            if c=="@":
                robot=[warehouse.index(r), r.index(c)]
                break
    return robot
def addpos(pos1,pos2):
    return [pos1[0] + pos2[0],pos1[1]+pos2[1]]

def go(pos, char,chg,warehouse):
    print(pos,char)
    poschar=warehouse[pos[0]][pos[1]] 
    nextpos=addpos(pos,chg)
    if poschar == "#":
        return False
    if poschar == ".":
        warehouse[pos[0]][pos[1]] = char
        return True

    if poschar=="[":
        if chg==[0,1]:
            warehouse[pos[0]][pos[1]] = "["
            return go(nextpos,"]",chg,warehouse) 
        l=go(nextpos,"[",chg,warehouse)
        r=go(addpos(nextpos,[0,1]), "]",chg,warehouse)
        if l and r:
            warehouse[pos[0]][pos[1]]=char
            warehouse[pos[0]][pos[1]+1]="."
            return True
        return False
    if poschar=="]":
        if chg==[0,-1]:
            warehouse[pos[0]][pos[1]] = "]"
            return go(nextpos, "[",chg,warehouse) 
        l=go(addpos(nextpos,[0,-1]),"]",chg,warehouse)
        r=go(nextpos, "]",chg,warehouse)
        if l and r:
            warehouse[pos[0]][pos[1]]=char
            warehouse[pos[0]][pos[1]-1]="."
            return True
        return False
    if poschar == "O":
        if go(addpos(pos, chg), "O", chg, warehouse):
            warehouse[pos[0]][pos[1]] = char
            return True
        return False       

for move in range(0, len(moves)):
    m={"^": dmap[0], ">": dmap[1], "v": dmap[2], "<": dmap[3]}
    robotpos=getrobotpos()
    d=m[moves[move]]
    newwarehouse=dcp(warehouse)
    print(moves[move])
    if go(addpos(robotpos,d),"@",d,newwarehouse):
        warehouse[robotpos[0]][robotpos[1]]="."
        warehouse=newwarehouse

ttl=0
for r in rg(warehouse):
    for c in rg(warehouse[r]):
        if warehouse[r][c]=="O":
            ttl+=gps(r,c)

print(ttl)
