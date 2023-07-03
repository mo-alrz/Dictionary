# Create a dictionary from the list with same key:value pairs, such as: {"key": "key"}.

lst = ["NY", "FL", "CA", "VT"]
dict = {i: i for i in lst}
print(dict)

# First, create a range from 100 to 160 with steps of 10.
# Second, using dict comprehension, create a dictionary where each number in the range is the key and each item divided
# by 10 is the value.

rng = range(100, 161, 10)
dict = {i: int(i / 10) for i in rng}

print(dict)

# Using dict comprehension and a conditional argument create a dictionary from the current dictionary where only the
# key:value pairs with value above 2000 are taken to the new dictionary.

dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2={k:v for k,v in dict1.items() if v > 2000}
print(dict2)

# Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict = {k:v for k,v in zip(keys,values)}
print(dict)

# Merge two Python dictionaries with same length and no common keys or values into one
dict1 = {'Ten': 10, 'Twenty': 20}
dict2 = {'Thirty': 30, 'Fourty': 40}
dict3 = {**dict1, **dict2}
print(dict3)

# Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
new_dict = {i:defaults for i in employees}
print(new_dict)

# Fahrenheit to celsius
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
celsius = {k:5/9*(int(v)- 32) for k,v in fahrenheit.items()}
print(celsius)

