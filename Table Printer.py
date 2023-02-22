# Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# OPTIONAL:
# The first columns should be automatically as wide as the longest key

ingredients = [
    {"name": "vodka", "in_stock": 1, "needs_cooling": True},
    {"name": "coffee_liqueur", "in_stock": 0, "needs_cooling": True},
    {"name": "fresh_cream", "in_stock": 1, "needs_cooling": True},
    {"name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": True},
    {"name": "mint_leaves", "in_stock": 0, "needs_cooling": False},
    {"name": "sugar", "in_stock": 0, "needs_cooling": False},
    {"name": "lime juice", "in_stock": 0, "needs_cooling": True},
    {"name": "soda", "in_stock": 0, "needs_cooling": True}
]

a = ''
keys = []

for i in ingredients:
    for k, v in i.items():
        if k == 'name':
            keys.append(len(v))

max_key = max(keys)

print(f'+{max_key*"-"}+{len("Needs cooling")*"-"}+{len("In Stock")*"-"}+')
print(f'|Ingredient{(max_key - len("ingredient"))*" "}|Needs Cooling|In Stock|')
print(f'+{max_key*"-"}+{len("Needs cooling")*"-"}+{len("In Stock")*"-"}+')

for i in ingredients:
    for k, v in i.items():
        if i['needs_cooling']:
            i['needs_cooling'] = 'Yes'
        else:
            i['needs_cooling'] = 'No'
        print(f'|{str(v)}{(max_key - len(v)) * " "}|{i["needs_cooling"]}'
              f'{(len("Needs cooling") - len(i["needs_cooling"])) * " "}|'
              f'{str(i["in_stock"])}{(len("In stock") - len(str(i["in_stock"]))) * " "}|')
        break

print(f'+{max_key*"-"}+{len("Needs cooling")*"-"}+{len("In Stock")*"-"}+')