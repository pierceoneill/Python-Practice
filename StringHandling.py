# String Handling

a = "Hello, World"
print(a)

print(len(a))   # print the lenght of String, returns no. og characters in string
print(a[1])     # returnes the character of given index no.
print(a[2:5])   # returns the substring with start no anbd end index no.

print(a.split(","))     # Separate the string with given delimter
b = "As per survey its 62 percentage better with live instructor"
print(b.split(" "))

c = "   Hello World     "
print(c)
print(c.strip())    # removes prefix and postfix whitespaces

print(a.replace("o","u"))   # replaces the old char with new char

print(a.lower())    # Convert string into small letters
print(a.upper())    # Convert the string into capital letters