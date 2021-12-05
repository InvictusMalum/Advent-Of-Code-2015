from os import sep


f = open("day7input.txt", "r")
input = f.read()

commands = input.split("\n")

def separateCommand(command):
    list = command.split(" -> ")
    func = list[0].split(" ")
    target = list[1]
    
    return func, target

def valueOf(term, values):
    try:
        return int(term)
    except:
        if term not in values:
            return None
        return values[term]

def createPathDict(commands):
    paths = {}
    for i in range(len(commands)):
        func, target = separateCommand(commands[i])
        paths[target] = func
    
    return paths

def runThroughPaths(paths, startingValues = {}):
    values = startingValues
    overridden = []
    for value in values:
        overridden.append(value)
    for target in paths:
        for target in paths:
            # NUMBER or CODE
            if len(paths[target]) == 1:
                if target not in overridden:
                    value = valueOf(paths[target][0], values)
                    if value != None:
                        values[target] = value
            # NOT
            elif len(paths[target]) == 2:
                if "NOT" in paths[target]:
                    value = valueOf(paths[target][1], values)
                    if value != None:
                        values[target] = ~value
            # AND or LSHIFT or RSHIFT or OR
            elif len(paths[target]) == 3:
                if "AND" in paths[target]:
                    value1 = valueOf(paths[target][0], values)
                    value2 = valueOf(paths[target][2], values)
                    if value1 != None and value2 != None:
                        values[target] = value1 & value2
                    
                elif "LSHIFT" in paths[target]:
                    value1 = valueOf(paths[target][0], values)
                    value2 = valueOf(paths[target][2], values)
                    if value1 != None and value2 != None:
                        values[target] = value1 << value2
                    
                elif "RSHIFT" in paths[target]:
                    value1 = valueOf(paths[target][0], values)
                    value2 = valueOf(paths[target][2], values)
                    if value1 != None and value2 != None:
                        values[target] = value1 >> value2
                    
                elif "OR" in paths[target]:
                    value1 = valueOf(paths[target][0], values)
                    value2 = valueOf(paths[target][2], values)
                    if value1 != None and value2 != None:
                        values[target] = value1 | value2
    return values


aValue = runThroughPaths(createPathDict(commands))['a']
print(aValue)

part2Value = aValue = runThroughPaths(createPathDict(commands), {'b': aValue})['a']
print(part2Value)
        