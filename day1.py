f = open("day1input.txt", "r")
input = f.read()

def readInstructions(input):
    """Read an instruction code. Start on floor zero. '(' sends up a floor. ')' sends down a floor."""
    floor = 0
    for i in input:
        if i=="(":
            floor += 1
        elif i ==")":
            floor -= 1
    return floor

def findFirstBasement(input):
    """Return the instruction count of the first code that sends to a negative floor level. (Start at index of 1)"""
    floor = 0
    for i in range(len(input)):
        if input[i] == "(":
            floor += 1
        elif input[i] == ")":
            floor -= 1
        if floor < 0:
            return i+1
    return -1

print("He will end on floor: " + str(readInstructions(input)))
print("He will first enter the basement on move: " + str(findFirstBasement(input)))