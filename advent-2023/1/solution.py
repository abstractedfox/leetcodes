#note: based on the example, it appears that 'first and last digit' is not mutually exclusive, so if there is one digit it counts as both

result = 0
file = open("input.txt", 'r')
input = file.readlines()

for line in input:
    first = ''
    last = ''
    for char in line:
        if (ord(char) >= ord('1')) & (ord(char) <= ord('9')):
            if first == '':
                first = char
                last = char
            else:
                last = char
    if first != '':
        result += (int(first + last))
    
print(result)
