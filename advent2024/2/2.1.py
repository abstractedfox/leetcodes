from helper import *
a=Array()

a.inp=[ordb(x, [toi,spt]) for x in a]

sf=0
for i in rg(a):
    def check(line):
        sn = line[0]-line[1] > -1
        for j in range(0,len(line)-1):
            val=line[j]-line[j+1]  
            if ((val > 0) != sn):
                return False
            if (abs(val) >3 or abs(val)<1):
                return False
        return True
    if check(a[i]):
        sf += 1
    else:
        for j in rg(a[i]):
            new=a.inp[i][0:j]+a.inp[i][j+1:]
            if check(new):
                sf+=1
                break

print(sf)
