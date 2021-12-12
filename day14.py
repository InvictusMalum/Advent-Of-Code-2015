from typing import get_args


f = open("day14input.txt", "r")
input = f.read()
descriptions = input.split("\n")

class Reindeer():
    def __init__(self, n, s, mT, rT):
        self.name = n
        self.speedPerSecond = s
        self.maintainTime = mT
        self.restTime = rT
        
        self.distanceTraveled = 0
        
        self.points = 0

    def distanceInTime(self, time):
        # Number of times the reindeer gets through maintained speed and rest times
        completedCycles = time//(self.maintainTime + self.restTime)
        extraTime = time%(self.maintainTime + self.restTime)
        return completedCycles*self.speedPerSecond*self.maintainTime+min(extraTime,self.maintainTime)*self.speedPerSecond
    
def createReindeer(descriptions):
    reindeer = []
    for description in descriptions:
        d = description.split(" ")
        reindeer.append(Reindeer(d[0], int(d[3]), int(d[6]), int(d[13])))
    return reindeer

def setReindeerDistInSeconds(reindeer, seconds):
    for object in reindeer:
        object.distanceTraveled = object.distanceInTime(seconds)

def getDistance(object):
    assert isinstance(object, Reindeer), "Object must be of type Reindeer"
    return object.distanceTraveled

def getPoints(object):
    assert isinstance(object, Reindeer), "Object must be of type Reindeer"
    return object.points

time = 2503

# Part 1
reindeer = createReindeer(descriptions)
setReindeerDistInSeconds(reindeer, time)
reindeer.sort(key=getDistance, reverse=True)
print(reindeer[0].name + " travels " + str(reindeer[0].distanceTraveled) + " and wins the race!")

# Part 2
for second in range(1, time+1):
    setReindeerDistInSeconds(reindeer, second)
    reindeer.sort(key=getDistance, reverse=True)
    reindeer[0].points += 1
    for i in range(1,len(reindeer)):
        if reindeer[i].distanceTraveled == reindeer[0].distanceTraveled:
            reindeer[i].points += 1
    print(reindeer[0].name + " travels " + str(reindeer[0].distanceTraveled) + " in " + str(second) + " seconds and is in the lead!")

reindeer.sort(key=getPoints, reverse=True)
print(reindeer[0].name + " gained " + str(reindeer[0].points) + " points and has the most points!")