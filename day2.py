f = open("day2input.txt", "r")
input = f.read()
input = input.split("\n")

def paperNeededForCode(code):
    """Code is in the form LxWxH, the sq footage = 2*L*W + 2*W*H + 2*L*H. Add a little extra, which is equal to the smallest of the three sides."""
    codeList = code.split("x")
    for i in range(len(codeList)):
        codeList[i] = int(codeList[i])
    side1 = codeList[0]*codeList[1]
    side2 = codeList[1]*codeList[2]
    side3 = codeList[0]*codeList[2]
    return 2*side1 + 2*side2 + 2*side3 + min([side1, side2, side3])

def sumSqFtOfCodes(codes):
    total = 0
    for code in codes:
        total += paperNeededForCode(code)
    return total

def ribbonNeededForCode(code):
    """Ribbon wraps around smallest perimeter, and add on the bow, equal to the cubic feet of the box. code is in form L*W*H"""
    codeList = code.split("x")
    for i in range(len(codeList)):
        codeList[i] = int(codeList[i])
    volume = codeList[0]*codeList[1]*codeList[2]
    codeList.remove(max(codeList))
    return 2*codeList[0] + 2*codeList[1] + volume

def sumRibbonsOfCodes(codes):
    total = 0
    for code in codes:
        total += ribbonNeededForCode(code)
    return total

print("Part1: Sum of sq footage of all boxes (+smallest side): " + str(sumSqFtOfCodes(input)))
print("Part2: Sum of ribbon of all boxes: " + str(sumRibbonsOfCodes(input)))