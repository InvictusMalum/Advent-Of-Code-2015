f = open("day9input.txt", "r")
input = f.read()

input = input.split("\n")

def createDict(directionLines):
    directionMap = {}
    locations = []
    for direction in directionLines:
        directionCode = direction.split(" to ")
        directionCode = [directionCode[0]] + directionCode[1].split(" = ")
        
        if directionCode[0] not in locations:
            locations.append(directionCode[0])
        if directionCode[1] not in locations:
            locations.append(directionCode[1])
        
        directionMap[(directionCode[0], directionCode[1])] = int(directionCode[2])
        directionMap[(directionCode[1], directionCode[0])] = int(directionCode[2])

    return directionMap, locations

def remove(list, nums):
    for num in nums:
        list.remove(num)
    return list

def getCombinations(totalLength, used = []):
    allCombs = []
    if totalLength-len(used) == 1:
        return [remove([i for i in range(totalLength)], used)]
    else:
        for i in remove([i for i in range(totalLength)], used):
            for j in getCombinations(totalLength, used + [i]):
                list = [i]+j
                allCombs.append(list)
        return allCombs

            
def pathLen(directionMap, locations, path):
    pathLen = 0
    for i in range(len(path)-1):
        pathLen += directionMap[(locations[path[i]], locations[path[i+1]])]
    return pathLen

def indexZero(list):
    return list[0]

def findPathsByDistance(directionMap, locations):
    paths = []
    combinations = getCombinations(len(locations))
    for i in range(len(combinations)):
        paths.append([pathLen(directionMap, locations, combinations[i]), combinations[i], [locations[combinations[i][j]] for j in range(len(combinations[0]))]])
    paths.sort(key=indexZero)
    return paths

    

directionMap, locations = createDict(input)

print(findPathsByDistance(directionMap, locations)[0])
print(findPathsByDistance(directionMap, locations)[-1])

