
file = open("input.txt", 'r')
input = file.readlines()

#cardValueOrder = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
cardValueOrder = "J23456789TJQKA"


def getHandType(hand):
    joker = False
    values = {}
    for char in hand:
        if char == "J":
            joker = True
        if (char in values) == False:
            values[char] = 0
            for char2 in hand:
                if char2 == char:
                    values[char] += 1
                    
    if joker:
        #let's note that it isn't as simple as just equating J to whatever the second largest quantity of cards is; even the example shows "QJJQ2" where it would be preferable for J to become 2
        #a working approach could simply be to say that for each card that is not J, test an example of that hand where J is replaced with that card, and return whatever is best
        hands = []
        handvalues = []
        for value in values:
            if value == "J":
                continue
            split = list(hand)
            for i in range(len(split)):
                if split[i] == "J":
                    split[i] = value
            hands.append("".join(split))
        for newhand in hands:
            handvalues.append(getHandType(newhand))
        if len(handvalues) == 0:
            return 6 #full house
        return max(handvalues)
            
                    
    length = len(values)
    valuesArr = []
    for value in values:
        valuesArr.append(values[value])
        
        
    if length == 1:
        return 6 #five of a kind
        
    if length == 2:
        if valuesArr[0] == 4 or valuesArr[0] == 1:
            return 5 #four of a kind
        if valuesArr[0] == 2 or valuesArr[0] == 3:
            return 4 #full house
                    
    if length == 3:
        if valuesArr[0] == 3 or valuesArr[1] == 3 or valuesArr[2] == 3:
            return 3 #three of a kind
                
        return 2 #two pair
        
    if length == 4:
        return 1 #one pair
        
    return 0 #high card


#returns 1 if hand1 is stronger or 2 if hand2 is stronger, or 0 if they're equal
def compareHands(hand1, hand2):
    hand1Type = getHandType(hand1)
    hand2Type = getHandType(hand2)
    
    if hand1Type > hand2Type:
        return 1
    if hand2Type > hand1Type:
        return 2
        
    for i in range(len(hand1)):
        if cardValueOrder.find(hand1[i]) > cardValueOrder.find(hand2[i]):
            return 1
        if cardValueOrder.find(hand1[i]) < cardValueOrder.find(hand2[i]):
            return 2
    return 0


for i in range(len(input) - 1):
    parsed1 = input[i][0:5]
    parsed2 = input[i + 1][0:5]
    #compare = compareHands(parsed1, parsed2)
    
    while compareHands(parsed1, parsed2) == 2:
        hold = input[i]
        input[i] = input[i + 1]
        input[i + 1] = hold
        i -= 1
        if i == -1:
            break
        parsed1 = input[i][0:5]
        parsed2 = input[i + 1][0:5]
   
length = len(input)
total = 0

for i in range(length):
    total += int(input[i][input[i].find(" "):len(input[i])]) * (length - i)
    
print(total)
