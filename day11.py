f = open("day11input.txt", "r")
input = f.read()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def incrementCode(code):
    code = list(code)
    for j in range(-1, -len(code)-1, -1):
        code[j] = alphabet[(alphabet.index(code[j])+1)%26]
        if code[j] != 'a':
            break
    return "".join(code)

def isValidCode(code):
    foundThreeString = False
    # Check increasing string - (abc, bcd, etc)
    for i in range(len(code)-2):
        if alphabet.index(code[i])+1 == alphabet.index(code[i+1]) and alphabet.index(code[i])+2 == alphabet.index(code[i+2]):
            foundThreeString = True
    
    invalidLetters = 'iol'
    for letter in invalidLetters:
        if letter in code:
            return False
        
    # Check 2 different pairs
    for i in range(len(code)-3):
        if alphabet.index(code[i]) == alphabet.index(code[i+1]):
            for j in range(i+2, len(code)-1):
                if alphabet.index(code[j]) == alphabet.index(code[j+1]):
                    return foundThreeString
            break
    
    return False

# Part 1
while True:
    if isValidCode(input):
        print(input)
        break
    input = incrementCode(input)

input = incrementCode(input)

# Part 2
while True:
    if isValidCode(input):
        print(input)
        break
    input = incrementCode(input)