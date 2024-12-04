from helper import *
import re

a=Array()

#a.inp=["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
r=0
for line in a:
    b=re.findall(r"mul\(.\d*,.\d*\)", line)
    for n in b:
        n=ordb(n,[toi,jn])
        r+=n[0]*n[1]
    print(r)
print(r)
