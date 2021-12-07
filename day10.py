f = open("day10input.txt", "r")
input = f.read()

input = int(input)

def fakeLookAndSay(number):
    out = ''
    
    digitCounts = {}
    number = str(number)
    for char in number:
        if char not in digitCounts:
            digitCounts[char] = 1
        else:
            digitCounts[char] += 1
    
    for digit in digitCounts:
        out += str(digitCounts[digit]) + digit
    
    return out

def lookAndSay(number):
    out = ''
    number = str(number) + '-'
    
    count = 1
    for i in range(len(number)-1):
        if number[i] == number[i+1]:
            count += 1
        else:
            out += str(count)+number[i]
            count = 1
    
    return out

applyNumber = 50
for i in range(applyNumber):
    input = lookAndSay(input)

print(len(input))
    