from helper import *
a=gi()
#a[0]="0 1 10 99 999"
a=[int(x) for x in a[0].split()]

def walk(inp,d,ttl):
    if d==0:
        return ttl
    if inp==0:
        return walk(1,d-1,ttl)
    elif len(str(inp))%2==0:
        c=str(inp)
        return walk(int(c[0:int(len(c)/2)]),d-1,1) + walk(int(c[int(len(c)/2):]), d-1,ttl)
        #return walk(int(c[0:int(len(c)/2)] + c[int(len(c)/2)]), d-1,ttl+2)
    return walk(inp*2024,d-1,ttl)

ttl=0
for x in a:
    ttl+=walk(x,75,1)
    print(ttl)
print(ttl)
exit()

for i in range(0, 25):
#for i in range(0, 1):
    print("inc")
    #for n in range(0,len(a)):
    n=0
    while n < len(a):
        if a[n]==0:
            a[i]=1
        elif len(str(a[n]))%2==0:
            b=str(a[n])
            c=b[0:int(len(b)/2)]
            d=b[int(len(str(b))/2):]
            a[n]=int(c)
            a.insert(n+1,int(d))
        else:
            a[n]*=2024
        n+=1
        #print(len(a))
print(len(a),"\a")
