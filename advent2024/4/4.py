from helper import *

a=Array()
'''
a.inp=["MMMSXXMASM",
"MSAMXMSMSA",
"AMXSXMAAMM",
"MSAMASMSMX",
"XMASAMXAMM",
"XXAMMXXAMA",
"SMSMSASXSS",
"SAXAMASAAA",
"MAMMMXMMMM",
"MXMXAXMASX"]
'''
ttl=0
for l in a:
    c=re.findall("XMAS",l)
    ttl+=len(c)
    c=re.findall("SAMX",l)
    ttl+=len(c)
vert=[]
for c in rg(a[0]):
    vert.append(a.gcol(c, mkstr=True))
for l in vert:
    c=re.findall("XMAS",l)
    ttl+=len(c)
    c=re.findall("SAMX",l)
    ttl+=len(c)
def diag(l,r,c,direc):
    d=1*direc
    if d==-1:
        return l[r][c+3]+l[r+1][c+2]+l[r+2][c+1]+l[r+3][c]
    return l[r][c]+l[r+1][c+1]+l[r+2][c+2]+l[r+3][c+3]

for r in range(0,len(a)-3):
    for c in range(0,len(a[0])-3): 
        if diag(a.inp,r,c,1) == "XMAS" or diag(a.inp,r,c,1) == "SAMX": 
            ttl+=1
        if diag(a.inp,r,c,-1) == "XMAS" or diag(a.inp,r,c,-1) == "SAMX":
            ttl+=1
print(ttl)

def diag(l,r,c,direc):
    d=1*direc
    if d==-1:
        return l[r][c+2]+l[r+1][c+1]+l[r+2][c]
    return l[r][c]+l[r+1][c+1]+l[r+2][c+2]

ttl=0
for l in range(0,len(a)-2):
    for c in range(0,len(a[0])-2):
        if (diag(a.inp,l,c,1)=="MAS" or diag(a.inp,l,c,1)=="SAM") and (diag(a.inp,l,c,-1)=="MAS" or diag(a.inp,l,c,-1)=="SAM"):
            
            ttl+=1

print(ttl)
