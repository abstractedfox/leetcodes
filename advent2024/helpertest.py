import helper
a = [[1, 2, 3, 4, 5], ['a','b','c','d','e'],[10,11,12,13,14]]

print(helper.gcols(a))

b = ["1 2 3 4 5", "11 12 13 14 15", "111 112 113 114 115"]
for i in range(0, len(b)):
    b[i] = b[i].split()

c = ["abcde", "fghij", "klmno"]

a = helper.Array(override_input = c)
print("3rd column", a.gcol(3))

a.scol("awa", 3)
print("2nd column after awa", a.gcol(2))
print(a.inp)

#entire arr is now['abcae', 'fghwj', 'klmao']

a.scel("a",0,1)
print(a[0] == "aacae")
a.scel("hhhh",0,1)
print(a[0] == "ahhhh")

a.scel(":3",1,2, insert = True)
print(a[1]=="fg:3hwj")

test = "hello"
dicty=helper.gendict(helper.strtoarr(test), ct = True)
print(dicty["h"] == 1 and dicty["e"] == 1 and dicty["l"] == 2 and dicty["o"] == 1)
