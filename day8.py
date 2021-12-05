f = open("day8input.txt", "r")
input = f.read()

strings = input.split("\n")

def countCodeStrings(strings):
    total = 0
    for string in strings:
        total += len(string)
    return total

def countRepresentedCharacters(strings):
    total = 0
    for string in strings:
        i = 0
        while i < len(string):
            if string[i] == "\\" and string[i+1] == 'x':
                i+=3
            elif string[i] == "\\":
                i+=1
            elif string[i] == "\"":
                total -= 1
            i += 1
            total += 1
    return total

def countAdditonalToEncode(strings):
    total = 0
    for string in strings:
        i = 0
        
        # for quotes. Add 2 " per code
        total += 2
        while i < len(string):
            # for \x12 codes, add 1 \
            if string[i] == "\\" and string[i+1] == 'x':
                total += 1
                i+=3
            # for every \a escape code, add 2 \. \a -> \\\a
            elif string[i] == "\\":
                total += 2
                i+=1
            # for every ", encode to \"                
            elif string[i] == "\"":
                total += 1
            i += 1
    return total
        

print(countCodeStrings(strings) - countRepresentedCharacters(strings))

print(countAdditonalToEncode(strings))