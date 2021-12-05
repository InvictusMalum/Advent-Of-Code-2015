f = open("day6input.txt", "r")
input = f.read()

commands = input.split("\n")

def cornerStringToInts(cornerString):
    rowCol = cornerString.split(",")
    row = int(rowCol[0])
    col = int(rowCol[1])
    return row, col

def applyFunctionToRange(startCorner, endCorner, grid, function):
    row0, col0 = cornerStringToInts(startCorner)
    row1, col1 = cornerStringToInts(endCorner)
    
    for row in range(row0, row1+1):
        for col in range(col0, col1+1):
            grid[row][col] = function(grid[row][col])
            
def processCommand(command, grid, toggleFunction, onFunction, offFunction):
    command = command.split(" ")
    
    if command[0] == "toggle":
        startCorner = command[1]
        endCorner = command[3]
        applyFunctionToRange(startCorner, endCorner, grid, toggleFunction)
    elif command[0] == "turn" and command[1] == "on":
        startCorner = command[2]
        endCorner = command[4]
        applyFunctionToRange(startCorner, endCorner, grid, onFunction)
    elif command[0] == "turn" and command[1] == "off":
        startCorner = command[2]
        endCorner = command[4]
        applyFunctionToRange(startCorner, endCorner, grid, offFunction)

def on(number):
    return 1

def off(number):
    return 0

def toggle(number):
    return (number+1)%2


def onP2(number):
    return number+1

def offP2(number):
    return max(0,number-1)

def toggleP2(number):
    return number+2


def processAllCommandsP1(commands, toggleFunction, onFunction, offFunction):
    grid = [[0 for i in range(1000)] for i in range(1000)]
    for command in commands:
        processCommand(command, grid, toggleFunction, onFunction, offFunction)
    
    total = 0
    for row in grid:
        for light in row:
            total += light
    return total


def processAllCommandsP2(commands, toggleFunction, onFunction, offFunction):
    grid = [[0 for i in range(1000)] for i in range(1000)]
    for command in commands:
        processCommand(command, grid, toggleFunction, onFunction, offFunction)
    
    total = 0
    for row in grid:
        for light in row:
            total += light
    return total

print(processAllCommandsP1(commands, toggle, on, off))
print(processAllCommandsP1(commands, toggleP2, onP2, offP2))