input = open("input.txt", "r").readlines()

a = ""
result = 0
for l in input:
    for c in l:
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            a += c
            break

    for c in range(len(l) - 1, -1, -1):
        if ord(l[c]) >= ord('0') and ord(l[c]) <= ord('9'):
            a += l[c]
            break

    if a != "":
        result += int(a)
    print(a)
    a = ""
   
print(result)
