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
        
        directionMap[(directionCode[0], directionCode[1])] = int(directionCode[2])
        directionMap[(directionCode[1], directionCode[0])] = int(directionCode[2])

    return directionMap, locations

def remove(list, nums):
    for num in nums:
        list.remove(num)
    return list

def getAllCombinations(startLen, used):
    combinations = []
    for a in remove([0,1,2,3,4,5,6], []):
        for b in remove([0,1,2,3,4,5,6], [a]):
            for c in remove([0,1,2,3,4,5,6], [a,b]):
                for d in remove([0,1,2,3,4,5,6], [a,b,c]):
                    for e in remove([0,1,2,3,4,5,6], [a,b,c,d]):
                        for f in remove([0,1,2,3,4,5,6], [a,b,c,d,e]):
                            for g in remove([0,1,2,3,4,5,6], [a,b,c,d,e,f]):
                                combinations.append([a,b,c,d,e,f,g])
    print(len(combinations))
    return combinations
                
def pathLen(directionMap, locations, path):
    pathLen = 0
    for i in range(len(path)-1):
        pathLen += directionMap[(locations[path[i]], locations[path[i+1]])]
    return pathLen

def indexZero(list):
    return list[0]

def findShortestPath(directionMap, locations):
    paths = []
    combinations = getAllCombinations(len(locations), 0)
    for combination in combinations:
        print(combination)
    for i in range(len(combinations)):
        paths.append([pathLen(directionMap, locations, combinations[i]), combinations[i], [locations[combinations[i][j]] for j in range(len(combinations[0]))]])
    paths.sort(key=indexZero)
    return paths[0]
    

directionMap, locations = createDict(input)

print(findShortestPath(directionMap, locations))

