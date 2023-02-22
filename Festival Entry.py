# Create a security_check function that returns a list of festival goers who can enter the festival (only the names)

# If guns are found, remove them and put them on the watchlist (only the names), they can not enter the festival
# If alcohol is found confiscate it (set it to zero and add it to security_alcohol_loot) and let them enter the festival

watchlist = []
allowed_people = []
security_alcohol_loot = 0
queue = [
    {'name': 'Amanda', 'alcohol': 10, 'guns': 1},
    {'name': 'Mark', 'alcohol': 0, 'guns': 0},
    {'name': 'Dolores', 'alcohol': 0, 'guns': 1},
    {'name': 'Wade', 'alcohol': 1, 'guns': 1},
    {'name': 'Anna', 'alcohol': 10, 'guns': 0},
    {'name': 'Rob', 'alcohol': 2, 'guns': 0},
    {'name': 'Joerg', 'alcohol': 20, 'guns': 0}]


def guns(my_list):

    for i in my_list:
        if i['guns'] > 0:
            watchlist.append(i['name'])

        else:
            allowed_people.append(i['name'])

    return f'Allowed people : {allowed_people}\nWatchlist : {watchlist}'


def alcohol_loot(my_list):

    global security_alcohol_loot
    for i in my_list:
        if i['alcohol'] > 0:
            security_alcohol_loot += i['alcohol']
            i['alcohol'] = 0
    return f'Alcohols looted from guests : {security_alcohol_loot}'


print(guns(queue))
print(alcohol_loot(queue))
print(queue)
