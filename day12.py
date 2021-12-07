f = open("day12input.txt", "r")
input = f.read()

def addAllNumbers(JSON_String):
    total = 0
    i = 0
    while i < len(JSON_String):
        if JSON_String[i] in '-0123456789':
            j = 1
            while JSON_String[i+j] in '0123456789':
                j+=1
            total += int(JSON_String[i:i+j])
            i += j
        i += 1
    return total

def separateInto(start, string):
    list = start
    i = 0
    if start == [] and '[' not in string and ']' not in string and '{' not in string and '}' not in string:
        return [s for s in string.split(",")]
    elif start == {}:
        elements = [s for s in string.split(",")]
        for element in elements:
            if ']' in element:
                list[element.split("\"")[0]] = separateInto([], element.split(":")[1][1:len(element.split(":")[1])-1])
            else:
                list[element.split("\"")[0]] = element.split(":")[1].split("\"")[0]
    else:
        while i < len(string):
            if string[i] == '{':
                leftCount = 1
                rightCount = 0
                
                j = 1
                while not(string[i+j] == '}' and leftCount == rightCount+1):
                    if string[i+j] == '}':
                        rightCount += 1
                    elif string[i+j] == '{':
                        leftCount += 1
                    j += 1
                list.append(separateInto({}, string[i+1:i+j]))
                i += j
            if string[i] == '[':
                leftCount = 1
                rightCount = 0
                
                j = 1
                while not(string[i+j] == ']' and leftCount == rightCount+1):
                    if string[i+j] == ']':
                        rightCount += 1
                    elif string[i+j] == '[':
                        leftCount += 1
                    j += 1
                list.append(separateInto([], string[i+1:i+j]))
                i += j
            i += 1
        return list

def getAllObjects(string):
    objects = []
    
    i = 0
    while i < len(string):
        if string[i] == '{':
            leftCount = 1
            rightCount = 0
            
            j = 1
            while not(string[i+j] == '}' and leftCount == rightCount+1):
                if string[i+j] == '}':
                    rightCount += 1
                elif string[i+j] == '{':
                    leftCount += 1
                j += 1
            objects.append(string[i:i+j+1])
            i += j
        i += 1
        
    return objects

def totalInObjectWithRed(objects):
    total = 0
    for object in objects:
        if "red" in object:
            total += addAllNumbers(object)
    return total
        
print(addAllNumbers(input))
print(separateInto([], input))