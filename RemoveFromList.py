"""
Remove Item
There are several methods to remove items frin list1 list:
1. remove () - Removes Specific Item
2. pop(indexNo) - Removes the specified index
3. pop() - Removes the last item if index is not specified.
4. del keyword with given index number deletes specific element
5. del keyword without index no. deletes whole list
6 clear() - empties the list, will not delete the list
"""

# Define a list
list1 = ["A", "B", "C", "D", "E"]
list2 = ["1", "2", "3", "4", "5"]

print(list1)

# using remove()
list1.remove("C")
print(list1)

# using pop() with index no.
list1.pop(1)
print(list1)

# using pop() without index no.
list1.pop(1)
print(list1)

print(list2)