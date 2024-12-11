from helper import *
a=gi()
#a[0]="0 1 10 99 999"
a=[int(x) for x in a[0].split()]
quick=True
def walk(inp,d,ttl):
    if d==0:
        return ttl
    if inp==0:
        return walk(1,d-1,ttl)
    elif len(str(inp))%2==0:
        if quick:
            #probably cuts down on some calls if i can figure out what's wrong with it :3
            e=1
            strinp=str(inp)
            while len(strinp)%pow(2,e+1)==0 and d-e>0:
                e+=1
            val=0
            size=int(len(str(inp))/pow(2,e))
            for x in range(0,int(len(strinp)/size)):
                try:
                    #print(len(str(inp)),"size",size,"exponent",e,"current depth", d,"new depth",d-e)
                    print("from input",inp,"calling for",int( str(inp)[size*x:(size*x)+size]), "size",size, "e",e)
                    val+=walk(int( str(inp)[size*x:(size*x)+size]),d-e,1)
                except:
                    print("inp",inp, "size", size,"e", e, str(inp)[size*x:(size*x)+size])
                    exit()
            return ttl+val
        else:
            #orig
            c=str(inp)
            return walk(int(c[0:int(len(c)/2)]),d-1,1) + walk(int(c[int(len(c)/2):]), d-1,ttl)
            #return walk(int(c[0:int(len(c)/2)] + c[int(len(c)/2)]), d-1,ttl+2)
    return walk(inp*2024,d-1,ttl)
if __name__ == "__main__":
    import concurrent.futures
    futures=[]
    ttl=0
    from datetime import datetime,timedelta
    st=datetime.now()
    depth=25
    #with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
        for x in a:
            if quick:
                futures.append(executor.submit(walk,x,depth,1))
            else:
                futures.append(executor.submit(walk,x,depth,1))
        while len(futures) > 0:
            for future in futures:
                if future.done():
                    ttl+=future.result()
                    print("progress",ttl)
                    del futures[futures.index(future)]
    print(ttl, datetime.now()-st)
    print("\a")
    exit()

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
