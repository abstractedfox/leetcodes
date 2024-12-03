from helper import *
import re

a=Array()

#a.inp=["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
condensed=""
for line in a:
    condensed+=line
a.inp=[condensed]

r=0
for line in a:
    while line.find("don't()") > -1:
        end=line.find("do()", line.find("don't()"))
        if end == -1:
            end=len(line)
        line=line[0:line.find("don't()")]+line[end:]
    b=re.findall(r"mul\(.\d*,.\d*\)", line)
    for n in b:
        jawn=n
        n=ordb(n,[toi,jn])
        r+=n[0]*n[1]
    print(r)
print(r)
