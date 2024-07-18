"""
What is List?
A list is a data structure in Python that is mutable, or changeable, ordered sequence of elements.

Lists are just like dynamic sized arrays, similar to vector in C++ and Arraylist in Java.

Lists need not be homogenous always which makes its a most powerful tool in Python. This means a 
single list may contain DataTypes like Integers, Strings, as well as Objects. In other words a list 
can contain different types of elements.
"""

# Define a list

list1 = ["A", "B", "C", "D", "E"]

# Print the list
print(list1)

# Access the elements of list
print(list1[3])

# Total no. of elements in a list
print(len(list1))

# Replace an element from list
list1[3] = "F"
print(list1)

# Find the index no. of an element
x = list1.index("C")
print(x)

# Find the index no. of an element
list1.append("G")
print(list1)

# Insert an element on a specific index no.
list1.insert(2,"H")
print(list1)

# Loop with the list
for x in list1:         # for(int i=0; i<10; i++)
    print(x)

# check if the element exists or not
if "A" in list1:
    print("Yes, A is present")