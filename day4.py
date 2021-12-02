f = open("day4input.txt", "r")
input = f.read()

import hashlib

def MD5HashOf(string):
    return str(hashlib.md5(string.encode()))

def StartWith5Zeroes(string):
    if len(string) > 5 and string[0:5] == "00000":
        return True
    return False

def findValidCode(letters):
    number = 0
    while True:
        number += 1
        if StartWith5Zeroes(MD5HashOf(letters+str(number))):
            return number

print(findValidCode(input))