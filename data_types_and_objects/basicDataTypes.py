# Basic Data types
""" 
Numeric: Integer, float and complex data types
Integer : 45,100,-90
Float   : 2.5, 100.98
Complex : 3.0 + 1.3i

Boolean: Ture or False
 """
print("test print")

bool(False)
print(bool(False))
val1 =0
print(bool(val1))
val2 = 11
print(bool(val2))
va3 = -2.3
print(bool(va3))

""" 
Sequences:
  Strings
  Range
  Lists
 """

str1 = "Hello how are you"
str2 = "Hello how are you"
str = """Multi
line string"""
print(str1)
print(str2)
print(str)

f = 'data'
s = 'structure'
print(f+s)
print('Data'+'Structure')

st = 'data.'
print(st*3)
print(4*st)

# Range
print(list(range(10)))
print(range(10))
print(list(range(10)))
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(20,10,-1)))

# Lists

a = ['food','bus','apple','queen']
print(a)
mylist = [10, "hello", 'world',10.23]
print(mylist)
print(mylist[3])

# memberships, identity and logical operations
# Membership operators

# in and not in

mylist1 = [100,20,30,40,50]
mylist2 = [10,50,60,90]

if mylist1[1] in mylist2:
  print('Elements are overlapping')
else:
  print("elements are not overlapping")

val =104
mylist = [100,210,430,670,108]
if val not in mylist:
  print("value is not present in mylist")
else:
  print('Value is present in mylist')

# Identity operators
firstList = []
secondList = []
if firstList == secondList:
  print('Both are equal')
else:
  print('Both are not equal')

if firstList is secondList:
  print("Both are variables are pointing to same object")
else:
  print("Both variables are not poitning to same object")

firstList = []
secondList = []
if firstList is not secondList:
  print("Both firstList and secondList variables are the same object")
else:
  print('Both firstList and secondList variables are not the same object')


# Logical Operators
# AND, OR and NOT

a = 32
b = 132
if a>0 and b>0:
  print("Both a and b are greater than zero")
else:
  print("At least one variable is less than 0")

a = 32 
b=-32
if a> 0 or b>0:
  print("At least one variable is greater than zero")
else:
  print("Both variables are less than 0")

a =32
if not a:
  print("Boolean value of a is False")
else:
  print("Boolean value of a is True")
