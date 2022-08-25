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