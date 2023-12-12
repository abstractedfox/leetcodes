file = open("input.txt", 'r')
input = file.readlines()
quantity = [1] * len(input)

total = 0

for i in range(len(input)):
    winningNumbers = input[i][(input[i].find(':') + 1) : (input[i].find('|'))]
    haveNumbers = input[i][input[i].find('|') + 1:len(input[i])]
    
    winningNumbers = winningNumbers.split()
    haveNumbers = haveNumbers.split()
    
    for countOfThisCard in range(quantity[i]):
        matches = 0
        for num in winningNumbers:
            if (num in haveNumbers):
                matches += 1
                if i + matches < len(input):
                    quantity[i + matches] += 1

total = 0
for i in quantity:
    total += i
    
print(total)
