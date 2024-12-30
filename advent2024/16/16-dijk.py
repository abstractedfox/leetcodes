from helper import *
a=gi()
grid=grid(a)

nodes=[] 
nodemap=[] #[[connected node], steps]
dijkmap=[]
start=None
end=None
for r in range(1, grid.r):
    for c in range(1, grid.c):
        if grid[r,c]=="#":
            continue
        pos=[r,c]
        dirs=direction(pos)
        dotct = [x for x in dotct if grid[x] == "."]
        if len(dotct) > 1:
            if len(dotct) == 2:
                if dirs.u == dirs.d and grid[dirs.u] == ".":
                    continue
                if dirs.l == dirs.r and grid[dirs.l] == ".":
                    continue
        nodes.append(pos)
        if grid(pos) == "S":
            start=pos
        if grid(pos) == "E":
            end=pos
        nodemap.append([])
        dijkmap.append([])
for n in nodes:
    for d in dmap:
        pos=n
        i=-1
        while grid[pos] == ".":
            i+=1
            pos = addpos(pos, d)
            if pos in nodes:
                nodemap[pos].append([pos, i])

unvisited=nodes

