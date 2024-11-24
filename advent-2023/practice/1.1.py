input = open("input.txt", "r").readlines()

t = 0
for l in input:
    print(l)
    f=  ""
    last= ""
    for c in l:
        if ord(c) >= ord("0") and ord(c) <= ord("9"):
            if f == "":
                f = c
            last = c
    if f == "":
        break
    t += int(f + last)

print(t)
