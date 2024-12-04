input = open("input.txt", "r").readlines()
t = 0

nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for l in input:
    print("line", l)
    f=  ""
    last= ""
    i = 0
    for c in l:
        for num in nums:
            try:
                if l[i:i + len(num)] == num:
                    if f == "":
                        f = nums.index(num)
                    last = nums.index(num)
                    print(num, nums.index(num))
            except:
                continue

        if ord(c) >= ord("0") and ord(c) <= ord("9"):
            if f == "":
                f = c
            last = c
        i += 1
    f = str(f)
    last = str(last)
    if f == "":
        break
    print(f + last)
    t += int(f + last)

print(t)
