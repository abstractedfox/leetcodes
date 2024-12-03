#note to future kira: we're keeping this one so you can remember what was bad about it
from helper import *
a=Array()

a.inp=[ordb(x, [toi,spt]) for x in a]

sf=0
for i in rg(a):
    b=[x for x in a[i]]

    b.sort()
    c=[x for x in a[i]]
    c.sort(reverse=True)

    bad=0
    #remove the first value from b and a[i] that is different from the same index in a[i]
    for j in rg(a[i]):
        if a[i][j]!=b[j]:
            a.inp[i]=a.inp[i][0:j]+a.inp[i][j+1:]
            b=b[0:j]+b[j+1:]
            bad+=1
            break

    #if b == a[i] or c ==a[i]:
        #if len([a[i][x] for x in range(0,len(a[i])-1) if abs(a[i][x]-a[i][x+1]) <= 3 and abs(a[i][x]-a[i][x+1]) >= 1])+1 == len(a[i]):
            #sf += 1 
    if not (b == a[i] or c == a[i]):
        continue
    
    for j in range(1, len(a[i])):
        try:
            if not (abs(a[i][j]-a[i][j-1]) <= 3 and abs(a[i][j]-a[i][j-1]) >= 1) or a[i][j] == a[i][j-1]:
                bad +=1
        except:
            break
    if bad < 2:
        print(a[i])
        sf +=1


print(sf)
