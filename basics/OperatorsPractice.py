#Calculate the area and perimeter of a rectangle using length and width as inputs.

l = float(input('length: '))
w = float(input('width: '))
P = 2 * (l + w)
a = l * w
print('area: ', a)
print('permeter: ', P)

# Find the square and cube of a number using the exponent operator (**).

a = int(input("enter number: "))
square = a**2
cube =  a**3
print('square: ',square)
print('cube is: ',cube)

# Swap two numbers using arithmetic operators (no third variable).

a = int (input('enter number: '))
b = int(input('enter number: '))

print('before swapping: ',a ,b )
a = a + b
b = a - b
a = a - b

print('after swapping: ',a , b)

# Take two numbers and display the quotient and remainder.
a = float(input("enter a: "))
b = float(input("enter b: "))
print('quotient:',a/b)
print('reminder: ',a%b)

# Start with x = 10. Increment x by 5, then decrement by 3, and print the final value using += and -=.
x = 10
x += 5
x -= 3
print(x)

# Use *=, /=, and %= on a variable and print output after each step.

a = int(input('enter a: '))
a *= 2
print(a)
a /= 4
print(a)
a %= 6
print(a)

# Take input from user, multiply it by 2 using assignment operator and print result.

a = int(input("enter value: "))
a *= 2
print(a)

# Demonstrate compound assignment in a loop: increment a variable by 2 until it reaches 20.

x = 0

while x <= 20:
    print(x)
    x += 2

# Compare two numbers and print whether the first is greater, smaller, or equal to the second.

a = int(input('Enter first number'))
b = int(input('Enter second number'))

if a > b:
   print('a is greater: ')
elif a < b:
   print('a is smaller: ')
else:
    print('equal')


# Check if a number is between 10 and 50 using comparison operators.

a =  float(input("enter number: "))
if a >=10 and a <= 50 :
    print("range is okay")
else:
    print('out of range')

# Take a password length and verify if it is strong (length >= 8).

a = str(input('Enter password: '))
if len(a) >= 8:
    print('pass is strong')
else:
    print('change pass')

# Check if two strings are equal using ==.

a = str(input("enter string a: "))
b = str(input("enter string b: "))
if len(a) == len(b):
    print('equal')
else:
    print('not equal')

# Write a login program: check if both username and password match using and.

username = "vaistaya"
password = "12345"

a = input("enter user name: ")
b = input("Enter pass: ")

if a == username and b == password:
    print('Credentials correct')
else:
    print('incorrect credentials')

# Check if a number is divisible by 3 or 5 using or operator.

num = float(input('enter num: '))
if num % 3 or num % 5 == 0:
    print("num is divisible")
else:
    ('num is not devisible')

# Check if a number is not negative using not operator

num = float(input('enter num: '))
if not (num < 0):
    print("The number is NOT negative.")
else:
    print("The number is negative.")

# Print the binary representation of two numbers using bin() and apply &, |, and ^ operators.

a = int(input('enter a: '))
b = int(input('Enter b: '))
print(bin(a))
print(bin(a))

print('a & b', a & b, 'binary',bin(a & b))
print('a | b', a | b, 'binary',bin(a | b))
print('a ^ b', a ^ b, 'binary',bin(a ^ b))

# 	Left shift a number by 2 bits and right shift it by 2 bits, print both results

a = 4
left = a << 2
print('left shit: ',left)

right = a >> 2
print('right shit: ',right)


# Use bitwise NOT (~) and ^ (XOR) on two numbers 

a = int(input('enter a: '))
b = int(input('Enter b: '))

not_a =  ~ a 
not_b =  ~ b
print('not: ',not_a)
print('not: ',not_b)

xor = a ^ b
print('XOR: ',xor)

# Count number of set bits in a number using bitwise operations.

num = int(input('Enter num: '))
count =0

while num > 0:
    count += num & 1
    num = num >> 1
print(count)


# Check if a character is present in a string using in.

a = str(input('Enter string: '))
char = input("enter char to check: ")
if char in a:
    print('present')
else:
    print('not present')

Check if an element is not in a list using not in.

# list1 = ['a',4,'h',7,8,'g','h']
list1 = input('enter list: ')
char = input('enter char: ')

if char not in list1:
    print('not preseent')

else:
    print('present in list')

# Use is and == to compare two lists: a = [1, 2, 3], b = [1, 2, 3].

a = [1, 2, 3]
b = [1, 2, 3]

print(a==b)
print(a and b)

#	Write a program that checks if a user-given number exists in a predefined list

list1 = ['a','4','h','7','8','g','h']
char =  input('Enter char: ')
if char in list1:
    print("char present")
else:
    print('not preseent')

# Take marks from the user and use ternary operator to print "Pass" or "Fail".

marks = float(input('Enter Marks: '))
result = "pass" if  marks >= 80 else "fail"
print(result)

# Find the largest of three numbers using logical and comparison operators.

a = input('Enter a: ')
b = input('Enter b: ')
c = input('Enter c: ')

if a > b and a > c:
    print('a is greater')
else:
     print('a is not the greatest')

# Write a calculator program that uses all arithmetic operators based on user input.

num1 = float(input('Enter num1: '))
num2 = float(input('Enter num2: '))

operator = input(('Enter operator(+,-,/,%): '))

if operator == '+':
    print('addition: ',num1 + num2)
elif operator == '-':
    print('subtraction: ',num1 - num2)
elif operator == '*':
    print('multiplication: ',num1 * num2)
elif operator == '/':
    print('division: ', num1 / num2)
else:
    print('input incorrect')








