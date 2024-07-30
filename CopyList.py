"""
How to copy a List?
You cannot copy list1 list simply by typing list2 = list1, because: list2 will only be list2 reference you list2, and changes made to list2 will automatically also be made in list2.

There are ways to make list copy. list methods:
1. copy() method
2. list() constructor
"""

# Define a list
list1 = ["A", "B", "C", "D", "E"]
print(list1)

# using copy()
list2 = list1.copy()
print(list2)

# using list() constructor
list3 = list(list1)
print(list3)