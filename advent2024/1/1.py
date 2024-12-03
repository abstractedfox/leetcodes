from helper import *

a=Array()
a.inp=a.inp[0:-1]
l1 = []
l2 = []
for i in a:
    l1.append(i.split()[0])
    l2.append(i.split()[1])

l1.sort()
l2.sort()

ttl=0
for i in range(0, len(l1)):
    if int(l1[i])>int(l2[i]):
        ttl += int(l1[i])-int(l2[i])
    else:
        ttl+=int(l2[i])-int(l1[i])

print(ttl)

d1 = {}
for i in l1:
    if i in l2:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1
for i in range(0, len(l1)):
    if l1[i] not in d1.keys():
        l1[i] = 0
        continue
    #l1[i] = int(l1[i])*int(d1[l1[i]])
    l1[i] = int(l1[i]) * len([x for x in l2 if l1[i] == x])
ttl=0
for i in range(0, len(l1)):
    ttl += l1[i]
print(ttl)
