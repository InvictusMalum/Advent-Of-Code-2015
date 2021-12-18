f = open("day15input.txt", "r")
input = f.read()

descriptions = input.split("\n")

class Ingredient():
    ingredients = []
    properties = 5
    def __init__(self, name, cap, d, f, t, cal):
        self.name = name
        self.properties = [cap, d, f, t, cal]
        
        Ingredient.ingredients.append(self)



class Recipe():
    recipes = []
    def __init__(self, q):
        self.quantities = q
        self.score = 0
        
        Recipe.recipes.append(self)
    
    def calculateScore(self):
        self.score = 1
        for property in range(Ingredient.properties):
            propertyTotal = 0
            for i in range(len(self.quantities)):
                propertyTotal += self.quantities[i]*Ingredient.ingredients[i].properties[property]
            if propertyTotal > 0:
                self.score *= propertyTotal
            else:
                self.score = 0
    
    def getScore(self):
        return self.score
    
    @staticmethod
    def createAllRecipes():
        for q in getAllCombinations(len(Ingredient.ingredients)):
            Recipe(q)
    
    @staticmethod
    def scoreAllRecipes():
        for recipe in Recipe.recipes:
            recipe.calculateScore()



def getAllCombinations(number, total = 100):
    '''Get all combinations that add up to the total'''
    out = []
    if number == 1:
        return [[total]]
    for i in range(total+1):
        for other in getAllCombinations(number-1, total - i):
            out.append([i] + other)
    return out

# Parse and process data
for description in descriptions:
    d = description.split(" ")
    for i in range(len(d)):
        if ',' in d[i]:
            d[i] = d[i].split(',')[0]
    Ingredient(d[0][:len(d[0])-1], int(d[2]), int(d[4]), int(d[6]), int(d[8]), int(d[10]))
    
Recipe.createAllRecipes()
Recipe.scoreAllRecipes()
Recipe.recipes.sort(key = Recipe.getScore, reverse = True)
print(Recipe.recipes[0].score)