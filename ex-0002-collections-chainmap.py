"""
This is an exercise to get familiar with Collections Chainmap class.
"""

from collections import ChainMap


fruits = {'apples':50, 'oranges':60, 'pears':20}
vegetables = {'tomatoes':10, 'potatoes':20, 'onions':30}
dairy = {'milk':10, 'cheddar':40, 'parmesan': 50}

inventory = ChainMap(fruits, vegetables, dairy)
""" inventory is a ChainMap object """
print(type(inventory))
print(inventory['apples'])
""" throws an exception if no key found"""
try:
    print(inventory['cabbage'])
except:
    print("no key found")
print(fruits)
print(vegetables)
print(dairy)

inventory.update({'test': 999})

print(inventory)
print(fruits)


