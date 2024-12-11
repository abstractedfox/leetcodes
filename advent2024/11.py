from helper import *
a=gi()
#a[0]="0 1 10 99 999"
#a[0]="125 17"
a=[int(x) for x in a[0].split()]

for i in range(0, 75):
#for i in range(0, 1):
    print("i=",i)
    #for n in range(0,len(a)):
    n=0
    while n < len(a):
        if a[n]==0:
            a[n]=1
        elif len(str(a[n]))%2==0:
            b=str(a[n])
            c=b[0:int(len(b)/2)]
            d=b[int(len(str(b))/2):]
            a[n]=int(c)
            a.insert(n+1,int(d))
            n+=1 
        else:
            a[n]*=2024
        n+=1
print(len(a),"\a")
