# Represent the following products with their prices:
item = ['Milk', 'Rice', 'Eggs', 'Cheese',
        'Chicken Breasts', 'Apples', 'Tomato', 'Potato', 'Onion']
price = [1.07, 1.59, 3.14, 12.60, 9.40, 2.31, 2.58, 1.75, 1.10]

tuples = zip(item, price)
products = {}
for k, v in tuples:
    products[k] = v

# Represent Bob's shopping list:
bob = ['Milk', 'Rice', 'Eggs', 'Cheese',
       'Chicken Breasts', 'Apples', 'Tomato', 'Potato']
amount = [3, 2, 2, 1, 4, 1, 2, 1]
tuples_2 = zip(bob, amount)
bobs_items = {}
for k, v in tuples_2:
    bobs_items[k] = v

# Represent Alice's shopping list:
alice = ['Rice', 'Eggs', 'Chicken Breasts', 'Apples', 'Tomato']
amount_2 = [1, 5, 2, 1, 10]
tuples_3 = zip(alice, amount_2)
alices_items = {}
for k, v in tuples_3:
    alices_items[k] = v

# How much does Bob pay?
bob_spent = {key: products[key] * bobs_items[key] for key in products if key in bobs_items}
total_bob_spent = 0
for k, v in bob_spent.items():
    total_bob_spent += v
print(total_bob_spent)

# How much does Alice pay?
alice_spent = {key: products[key] * alices_items[key] for key in products if key in alices_items}
total_alice_spent = 0
for k, v in alice_spent.items():
    total_alice_spent += v
print(total_alice_spent)


# Who buys more Rice?
# Who buys more Potato?
# Who buys more Ham?
# Who buys more Apples?
def who_buys_more(key):
    if key not in bobs_items and key not in alices_items:
        print(f'No one buys {key}')

    if key in alices_items and key not in bobs_items:
        print(f'Alice buys more {key}')

    if key in bobs_items and key not in alices_items:
        print(f'Bob buys more {key}')

    if key in bobs_items and key in alices_items:
        if bobs_items[key] > alices_items[key]:
            print(f'Bob buys more {key}')
        elif bobs_items[key] < alices_items[key]:
            print(f'Alice buys more {key}')
        else:
            print(f'They bought equal amount of {key}')


who_buys_more('Rice')
who_buys_more('Potato')
who_buys_more('Ham')
who_buys_more('Apples')

# Who buys more of different products?
if len(bobs_items) > len(alices_items):
    print(f'Bob bought {len(bobs_items)} types of products')

# Who buys more items? (more pieces)
pieces_bob = 0
for k, v in bobs_items.items():
    pieces_bob += v

pieces_alice = 0
for k, v in alices_items.items():
    pieces_alice += v

if pieces_bob > pieces_alice:
    print(f'Bob bought {pieces_bob} items')
else:
    print(f'Alice bought {pieces_alice} items')