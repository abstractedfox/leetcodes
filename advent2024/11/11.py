from helper import *
a=gi()
a=[int(x) for x in a[0].split()]
quick=False
memo={}
def awa(inp, d, ttl):
    key=str(inp)+","+str(d)
    if key not in memo:
        memo[key]=walk(inp,d,ttl)
        return memo[key]
    else:
        return memo[key]
def walk(inp,d,ttl):
    key=str(inp)+","+str(d)
    if key in memo:
        return memo[key]
    if d==0:
        return ttl
    if inp==0:
        memo[key]=walk(1,d-1,ttl)
        return memo[key]
    elif len(str(inp))%2==0:
        c=str(inp)
        memo[key]=walk(int(c[0:int(len(c)/2)]),d-1,1) + walk(int(c[int(len(c)/2):]), d-1,ttl)
        return memo[key]
    
    memo[key]= walk(inp*2024,d-1,ttl)
    return memo[key]

if __name__ == "__main__":
    import concurrent.futures
    from datetime import datetime,timedelta
    futures=[]
    ttl=0
    st=datetime.now()
    depth=75
    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
        for x in a:
            futures.append(executor.submit(awa,x,depth,1))
        while len(futures) > 0:
            for future in futures:
                if future.done():
                    ttl+=future.result()
                    print("progress",ttl)
                    del futures[futures.index(future)]
    print(ttl, datetime.now()-st)
    print("\a")
    exit()

