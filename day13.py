f = open("day13input.txt", "r")
input = f.read()

input = input.split("\n")

def createHappinessDictAndGetPeople(input):
    dict = {}
    people = []
    for instruction in input:
        instruction = instruction.split(" ")
        
        if instruction[0] not in people:
            people.append(instruction[0])
        
        if instruction[3] == 'gain':
            dict[(instruction[0], instruction[10].split(".")[0])] = int(instruction[3])
        else:
            dict[(instruction[0], instruction[10].split(".")[0])] = (int(instruction[3])*-1)
            
    return dict, people

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

def happinessValue(dict, people, combination):
    happiness = 0
    for i in range(len(combination)):
        happiness += dict[(people[combination[i-1]], people[combination[(i+1)%len(combination)]])]
    return happiness

def getMaxHappinessComb(dict, people):
    happinesses = []
    for combination in getCombinations(len(people)):
        happinesses.append(happinessValue(dict, people, combination))
    return max(happinesses) 

dict, people = createHappinessDictAndGetPeople(input)
print(getMaxHappinessComb(dict, people))
    