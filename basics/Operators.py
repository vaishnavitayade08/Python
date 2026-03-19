##Arithmatic Operators
a = 10
b = 20

print("addition: ", a+b)
print("Subtraction: ", a-b)
print("Division: ",a/b)
print("Modulus: ",a%b)
print("exponential: ",a**b)
print("multiplication: ",a*b)

##Compariosn Operators

a = 20
b = 30

print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)
print(a==b)

## Logical operators
a = True
b = False

print(a and b)
print(a or b)
print(not b)
print(not a)

## Bitwise operators

a = 10
b= 20
print(a&b)
print(a|b)
print(~a)
print(a ^ b)
print(a >> b)
print(a << b )

## Identity Operator
a = 10
b = 20
c = a
print(a is not b)
print(a is c)

##Membership Operators
x = 24
y = 20

list = [10, 34, 20, 40, 50]

if (x not in list):
    print("x not present")
else:
    print("x is present")

if(y in list):
    print("y present")
else:
    print("y is not present")

## Assignment Operators

a = 10
b = a
print(b)
b += a
print(b)
b =+ a
print(b)
b =- a
print(b)
b *= a
print(b)
b >>= a
print(b)

## Ternary Operator
a, b = 10,20
min = a if a > b else b
print(min)


######### Hackerrank questions########

a = int(input())
b = int(input())
print(int(a/b))
print(float(a/b))

################

n = int(input())
for i in range(n):
    print(i*i)





