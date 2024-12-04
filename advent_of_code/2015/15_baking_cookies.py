#  15th day of advent of code 2015
from utils.inputs import get_data_set
from itertools import combinations_with_replacement

data = get_data_set(2015,15)

# data = [
#     "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8\n",
#     "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3\n"
# ]

class Ingredient:
    def __init__(self, name, capacity, durability, flavour, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavour = int(flavour)
        self.texture = int(texture)
        self.calories = int(calories)
    def __repr__(self) -> str:
        return f"{self.name}(C:{self.capacity}, D:{self.durability}, F:{self.flavour}, T:{self.texture}, C:{self.calories})"

ingredients = []
for ingredient in data:
    name, capacity, durability, flavour, texture, calories = ingredient.replace(":", ",").split(",")
    ingredients.append(Ingredient(name, capacity[-2:], durability[-2:], flavour[-2:], texture[-2:], calories[-3:]))

print(ingredients)
res = []
for n1 in range(0,101):
    for n2 in range(0,101-n1):
        for n3 in range(0,101-n1-n2):
                n4 = 100 - n3 - n2 - n1
                if n4<0:
                     continue
                C = sum(n * ingredient.capacity for n, ingredient in zip([n1,n2,n3,n4], ingredients))
                D = sum(n * ingredient.durability for n, ingredient in zip([n1,n2,n3,n4], ingredients))
                F = sum(n * ingredient.flavour for n, ingredient in zip([n1,n2,n3,n4], ingredients))
                T = sum(n * ingredient.texture for n, ingredient in zip([n1,n2,n3,n4], ingredients))
                if C <= 0 or D <= 0 or F <= 0 or T <= 0:
                    continue
                res.append(C*D*F*T)
print(max(res))

res = []
for n1 in range(0,101):
    for n2 in range(0,101-n1):
        for n3 in range(0,101-n1-n2):
                n4 = 100 - n3 - n2 - n1
                if n4<0:
                     continue
                calories = sum(n * ingredient.calories for n, ingredient in zip([n1,n2,n3,n4], ingredients))
                if calories!=500:
                     continue
                C = sum(n * ingredient.capacity for n, ingredient in zip([n1,n2,n3,n4], ingredients))
                D = sum(n * ingredient.durability for n, ingredient in zip([n1,n2,n3,n4], ingredients))
                F = sum(n * ingredient.flavour for n, ingredient in zip([n1,n2,n3,n4], ingredients))
                T = sum(n * ingredient.texture for n, ingredient in zip([n1,n2,n3,n4], ingredients))
                if C <= 0 or D <= 0 or F <= 0 or T <= 0:
                    continue
                res.append(C*D*F*T)
print(max(res))