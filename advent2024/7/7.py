from helper import *


a=["190: 10 19",
"3267: 81 40 27",
"83: 17 5",
"156: 15 6",
"7290: 6 8 6 15",
"161011: 16 10 13",
"192: 17 8 14",
"21037: 9 7 18 13",
"292: 11 6 16 20"]

a=gi()
if False:
    a=["10: 5 5",
    "20: 10 10",
    "30: 5 5 5",
    "40: 4 0",
    "50: 5 5 2",
    "150: 5 3 0",
    "150: 10 5 2 50",#450
    "1250: 25 5 8 200 10 10 10 10 10", #1700
    "1300: 5 2 5 2 10 10 10 0", #3000,
    "100: 100" #3100
    ]

if False:
    a=["30: 1 0 2 5 5",
    "30: 5 5 0 3",
    "30: 3 1 0",
    "30: 30",
    "30: 2 2 2 2 2 3",
    ]

if False:
    a=["25: 5 5",
    "1234567: 12 345 67",
    "1128: 3 12 3 4 8"]

a=do(a, lambda a:ordb(a, [toi,jn]))
o=0
for r in a:
    break
    for i in range(1,pow(2,len(r)-1)):
        ttl=r[1]
        well=[i]
        for j in range(2,len(r)):
            #print(i)
            if i&1 == 1:
                ttl*=r[j]
                well.append("*")
                well.append(r[j])
            else:
                ttl+=r[j]
                well.append("+")
                well.append(r[j])
            if i > 0:
                i=i>>1
        if ttl == r[0]:
            #print(r[0],well, ttl, o)
            o+=ttl
            break
print(o)


#leaving off! "i remembered i have a math final on monday" edition
#combinations of operators are fine, i verified the correct number of unique sets comes out 
#it's not double-counting rows where more than one combination can be correct


o=0
for r in a:
    #for i in range(1,pow(3,len(r)-1)):
    #for i in range(0,pow(3,len(r))+1):
    for i in range(0,pow(3,len(r))):
        ttl=r[1]
        well=[i]
        for j in range(2,len(r)):
            #print(i)
            if i%3 == 0:
                ttl*=r[j]
                #well.append("*")
                #well.append(r[j])
            elif i%3 ==1:
                ttl+=r[j]
                #well.append("+")
                
                #well.append(r[j])
            else:
                #well.append("||")
                ttl = int(str(ttl)+str(r[j]))
            if i > 0:
                i=i>>2
        
        #print(well)
        #if well[1:] not in unique:
            #unique.append(well[1:])

        if ttl == r[0]:
            print(r[0],well, ttl, o)
            o+=ttl
            break
    #print("unique!",len(unique))
print(o)
print("\a")

exit()
