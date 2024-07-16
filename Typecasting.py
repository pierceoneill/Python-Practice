"""
Type Casting: Forceful conversion of one data type into another
"""

a=1
b=2.5
c="3"
print(a)
print(b)
print(c)

d=int(c)        # convert into int
print(d)
e=a+d           # performs addition
print(e)

f=int(b)        # convert float value into int → 2 instead of 2.5
print(f)

g=float(a)      # convert int into float
print(g)

h=str(a)
i=c+h           # performs concatination
print(i)

print("A = "+str(a))