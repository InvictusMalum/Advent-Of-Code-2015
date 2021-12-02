f = open("day3input.txt", "r")
input = f.read()


def move(x,y,moveCode):
    if moveCode == "^":
        y += 1
    elif moveCode == ">":
        x += 1
    elif moveCode == "v":
        y -= 1
    elif moveCode == "<":
        x -= 1
    return x,y

def countHousesMovedTo(instructionString):
    x = 0
    y = 0

    positions = {(0,0):1}
    for moveCode in instructionString:
        x,y = move(x,y, moveCode)
        positions[(x,y)] = 1
    
    return len(positions)

def countHousesWithRobo(instructionString):
    santaX = 0
    santaY = 0

    roboX = 0
    roboY = 0

    positions = {(0,0):1}
    i = 0
    for moveCode in instructionString:
        if i%2 == 0:
            santaX,santaY = move(santaX,santaY, moveCode)
            positions[(santaX,santaY)] = 1
        else:
            roboX,roboY = move(roboX,roboY, moveCode)
            positions[(roboX,roboY)] = 1
        i+=1
    return len(positions)

print(countHousesMovedTo(input))
print(countHousesWithRobo(input))