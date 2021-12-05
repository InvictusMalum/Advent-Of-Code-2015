f = open("day5input.txt", "r")
input = f.read()

input = input.split("\n")

def containsThreeVowels(string):
    vowels = "aeiou"

    totalVowels = 0
    for letter in string:
        if letter in vowels:
            totalVowels += 1
    
    if totalVowels >= 3:
        return True
    return False

def containsDoubleLetter(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

naughtyWords = ["ab", "cd", "pq", "xy"]
def hasNaughtyWords(string):
    for word in naughtyWords:
        if word in string:
            return True
    return False

def isNiceStringP1(string):
    if containsThreeVowels(string) and containsDoubleLetter(string) and not(hasNaughtyWords(string)):
        return True
    return False

def countNiceStringsP1(strings):
    total = 0
    for string in strings:
        if isNiceStringP1(string):
            total += 1
    return total


def containsNonOverlapRepeats(string):
    for i in range(len(string)-3):
        if string[i]+string[i+1] in string[i+2:]:
            return True
    return False

def letterRepeatWithOneGap(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

def isNiceStringP2(string):
    if containsNonOverlapRepeats(string) and letterRepeatWithOneGap(string):
        return True
    return False

def countNiceStringsP2(strings):
    total = 0
    for string in strings:
        if isNiceStringP2(string):
            total += 1
    return total

print(countNiceStringsP1(input))
print(countNiceStringsP2(input))