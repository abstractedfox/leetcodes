file = open("input.txt", 'r')
input = file.readlines()

total = 0

for line in input:
    winningNumbers = line[(line.find(':') + 1) : (line.find('|'))]
    haveNumbers = line[line.find('|') + 1:len(line)]
    
    winningNumbers = winningNumbers.split()
    haveNumbers = haveNumbers.split()
    
    points = 0
    for num in winningNumbers:
        if (num in haveNumbers):
            if points == 0:
                points += 1
            else:
                points *= 2
            
    total += points
    
print(total)
