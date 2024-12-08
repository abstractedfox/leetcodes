from helper import *
a=gi()
ab=dcp(a)
d={}
ttl=0
for l in rg(a):
    for c in rg(a[l]):
        if a[l][c] != ".":
            if a[l][c] not in d:
                d[a[l][c]]=[[l, c]]
            else:
                d[a[l][c]].append([l,c])
for x in d:
    if len(d[x]) < 2:
        continue
    x=d[x]
    for i in range(0, len(x)):
        for j in range(0, len(x)):
            diff=[x[i][0]-x[j][0],x[i][1]-x[j][1]]
            checks=[x[i][0]-diff[0],x[i][1]-diff[1]]
            checka=[x[i][0]+diff[0],x[i][1]+diff[1]]
        
            bounds=lambda z:(z[0] >= 0 and z[0] < len(a) and z[1] >= 0 and z[1] < len(a[0]))
            if bounds(checks) and checks not in x:
                print(checks[0],"asdf",x)
                ab[checks[0]]=repl(ab[checks[0]],"#",checks[1])
            if bounds(checka) and checka not in x:
                ab[checka[0]]=repl(ab[checka[0]],"#",checka[1])
            

for x in ab:
    print(x)
    ttl+=len(re.findall(r"\#",x))
print(ttl)
ttl=0
for x in d:
    if len(d[x]) < 2:
        continue
    x=d[x]
    for i in range(0, len(x)):
        for j in range(0, len(x)):
            if i==j:
                continue
            diff=[x[i][0]-x[j][0],x[i][1]-x[j][1]]
            checks=[x[i][0]-diff[0],x[i][1]-diff[1]]
            checka=[x[i][0]+diff[0],x[i][1]+diff[1]]
        
            bounds=lambda z:(z[0] >= 0 and z[0] < len(a) and z[1] >= 0 and z[1] < len(a[0]))
            while bounds(checks):
                ab[checks[0]]=repl(ab[checks[0]],"#",checks[1])
                checks=[checks[0]-diff[0],checks[1]-diff[1]]
            while bounds(checka):
                ab[checka[0]]=repl(ab[checka[0]],"#",checka[1])
                checka=[checka[0]+diff[0],checka[1]+diff[1]]

for x in ab:
    #print(x)
    ttl+=len(re.findall(r"\#",x))
print(ttl)
