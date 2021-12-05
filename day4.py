f = open("day4input.txt", "r")
input = f.read()

import hashlib

def MD5HashOf(string):
    return str(hashlib.md5(string.encode()).hexdigest())

def StartWithXZeroes(string, xZeroes):
    zeroes = "0"*xZeroes
    if len(string) > xZeroes and string[0:xZeroes] == zeroes:
        return True
    return False

def findValidCode(letters, xZeroes):
    number = 0
    while True:
        number += 1
        if StartWithXZeroes(MD5HashOf(letters+str(number)), xZeroes):
            return number

print(findValidCode(input, 5))
print(findValidCode(input, 6))