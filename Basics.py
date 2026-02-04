## Input##
name = input("enter your Name: ")
print("Hellov", name, "welcome")

# multiple input#
x, y = input("Enter the values: ").split()
print("X is: ",x)
print("y is: ",y)

color = input("what is color: ")
print(color)

## change the type of imput#

n = int(input("how many: "))
print(n)

n = float(input("Enter float num: "))
print("n is: ",n)

n = str(input("enter the number: "))
print(n)

## find data type of input#
a = "Hello world"
b = 10
c = 10.56
d = ("abc","fjj","hud")
e = ["gdh", "shdh", "dj"]
f = {"hdk":1, "abc":3, "bdj":6}

print("a is:",type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# variables#
# Multiple assignment

x= y = z = 10
print(x, y, z)

# Assigning different values

x, y , z = 1, 2.4, 'Python'
print (x, y, z)
print(type(z))

#type casting
a = 5
print(float(a))

b = 2.5
print(int(b))

c = 32
print(str(c))

# swapping
a, b = 10,5
a, b = b, a
print(a, b)

#length
a = 'example'
print(len(a))

