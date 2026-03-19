## Numeric Data type

a = 10
print(type(a))

b = 12.00
print(type(b))

c = 2 + 3j
print(type(c))

## Sequence datatype
# string
s = 'welcome onboard'
print(type(s))

# access through index
print(s[0])
print(s[3])
print(s[4])

# List Data type

a = ['abc', 4,'hj','q',5]
print(type(a))

## access through index
print(a[0])
print(a[-1])

a[1] = 'cd'
print(a)

## enter element at end
a.append(4)
print(a)

## extend the list

a.extend(['hbfh',6,'hg'])
print(a)

##insert at specific index

a.insert(1,100)
print(a)

## remove by value

a.remove(100)
print(a)

## remove by index

a.pop(0)
print(a)

## del keyword
del a[2]
print(a)

##slicing chnage multiple elements

a[0:3] =[34,67,'rt']
print(a)

### Tuple Data Type- Immutable

a = ('dgd','dh',2,87,'jfh')
print(a)

## index accessing
print(a[0])
print(a[-1])

# tuple unpacking

t = (100,00,588,45)
a,*b,d = t
print(a)
print(b)
print(d)

## Boolean DataType

a =  True
print(type(a))

b =  False
print(type(b))

## Set data type

s = set('helloWorld')
print(s)
print(type(s))

s1 = set(['hsh','hjds','ty',65])

for i in s1:
    print(i, end=" ")

print('ty' in s1)

## oprations on set

s2 = {'jhds',56,'jh','du',58,90}
print('s2: ',s2)

## add
s2.add('ty') 
print(s2)

## update
s2.update([5,6])
print(s2)

## 
s2.remove(56)
print(s2)


## union

a = {1, 2}
b = {2, 3}
print(a.union(b))

## intersection

print(a.intersection(b))

## difference

print(b.difference(a))

# symmetric_difference

print(a.symmetric_difference(b))

## Dict Data type(data can be duplicate but not key, data is mutable keys are immutable)

d = {1: 'hello', 2: 'For', 3: 'if'}
print(d)
print(d[1])
print(d[1],d[2])

