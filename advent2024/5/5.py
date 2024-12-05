from helper import *

a=Array()

a1=a[0:1176]
a2=a[1177:] 
'''
a1=["47|53",
"97|13",
"97|61",
"97|47",
"75|29",
"61|13",
"75|53",
"29|13",
"97|29",
"53|29",
"61|53",
"97|53",
"61|29",
"47|13",
"75|47",
"97|75",
"47|61",
"75|61",
"47|29",
"75|13",
"53|13"]
a2=["75,47,61,53,29",
"97,61,53,29,13",
"75,29,13",
"75,97,47,61,53",
"61,13,29",
"97,13,75,29,47"]
'''

for l in rg(a1):
    a1[l]=ordb(a1[l],[toi,jn])

ttl=0
bads=[]
for l in rg(a2):
    nums=ordb(a2[l],[toi,jn])
    good=True
    for vals in a1:
        if vals[0] in nums and vals[1] in nums:
            if nums.index(vals[0]) > nums.index(vals[1]):
                good=False
                bads.append(nums)
                break
    if good:
        ttl+=nums[int(len(nums)/2)]

print(ttl)
def isbad(nums):
    for vals in a1:
        if vals[0] in nums and vals[1] in nums:
            if nums.index(vals[0]) > nums.index(vals[1]):
                return False
    return True

def anyf(arr,func):
    for a in arr:
        if not func(a):
            return False
    return True
while not anyf(bads, isbad):
    for l in rg(bads):
        good=True
        for vals in a1:
            if vals[0] in bads[l] and vals[1] in bads[l]:
                if bads[l].index(vals[0]) > bads[l].index(vals[1]):
                    i1=bads[l].index(vals[0])
                    i2=bads[l].index(vals[1])
                    h=bads[l][i1]
                    bads[l][i1]=bads[l][i2]
                    bads[l][i2]=h
ttl=0

for b in bads:
    ttl+=b[int(len(b)/2)]

print(ttl)
           
