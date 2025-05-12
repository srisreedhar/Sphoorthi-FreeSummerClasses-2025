Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

x = []

type(x)
<class 'list'>

list
<class 'list'>

list()
[]


num=[1,2,3,4,5,6,7]
num
[1, 2, 3, 4, 5, 6, 7]

names = ['einstein','tesla','faraday','ramanujan']
names
['einstein', 'tesla', 'faraday', 'ramanujan']

len(num)
7
len(names)
4


names[0]
'einstein'

names[-1]
'ramanujan'



dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']



y='einstein'

y
'einstein'

y.strip()
'einstein'
y.rsplit()
['einstein']
y.rsplit()
['einstein']



'    einstein'.lstrip()
'einstein'


'einstein     '.rstrip()
'einstein'



"Am I audible ?"
'Am I audible ?'


" I will re join', please stay connected to the session "
" I will re join', please stay connected to the session "




len(y)
8

len(y)+1
9







# mutable
# add/remove values


a = []
len(a)
0

# adding new values to a list
# ListName.append()


a.append('apple')

a
['apple']

a.append('banana')
a
['apple', 'banana']

a.append('cherry')
a
['apple', 'banana', 'cherry']


a.append('water melon')
a
['apple', 'banana', 'cherry', 'water melon']

a.append('pineapple')
a
['apple', 'banana', 'cherry', 'water melon', 'pineapple']


veg=['brinjal','okra','bottleguard','kothmir']

veg
['brinjal', 'okra', 'bottleguard', 'kothmir']


a.append(veg)

a
['apple', 'banana', 'cherry', 'water melon', 'pineapple', ['brinjal', 'okra', 'bottleguard', 'kothmir']]

len(a)
6

a[-1]
['brinjal', 'okra', 'bottleguard', 'kothmir']


a
['apple', 'banana', 'cherry', 'water melon', 'pineapple', ['brinjal', 'okra', 'bottleguard', 'kothmir']]




a[0]
'apple'
a[0].upper()
'APPLE'


a[1].upper()
'BANANA'


a[3].upper()
'WATER MELON'


a[4].upper()
'PINEAPPLE'



a[5].upper()
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    a[5].upper()
AttributeError: 'list' object has no attribute 'upper'



a[5]
['brinjal', 'okra', 'bottleguard', 'kothmir']


['brinjal', 'okra', 'bottleguard', 'kothmir'].upper()
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    ['brinjal', 'okra', 'bottleguard', 'kothmir'].upper()
AttributeError: 'list' object has no attribute 'upper'





# removing values from a list
# ListName.remove(Value)


a
['apple', 'banana', 'cherry', 'water melon', 'pineapple', ['brinjal', 'okra', 'bottleguard', 'kothmir']]


a.remove(['brinjal', 'okra', 'bottleguard', 'kothmir'])
a
['apple', 'banana', 'cherry', 'water melon', 'pineapple']
['apple', 'banana', 'cherry', 'water melon', 'pineapple']
['apple', 'banana', 'cherry', 'water melon', 'pineapple']





a
['apple', 'banana', 'cherry', 'water melon', 'pineapple']

a.remove('gulabjam')
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    a.remove('gulabjam')
ValueError: list.remove(x): x not in list




a.pop()
'pineapple'
a
['apple', 'banana', 'cherry', 'water melon']

a.pop()
'water melon'
a
['apple', 'banana', 'cherry']


a.pop(0)
'apple'

a
['banana', 'cherry']




veg
['brinjal', 'okra', 'bottleguard', 'kothmir']

veg.remove('okra')
veg
['brinjal', 'bottleguard', 'kothmir']
veg.pop()
'kothmir'



veg=['brinjal','okra','bottleguard','kothmir']
veg
['brinjal', 'okra', 'bottleguard', 'kothmir']


fruits=['apple','berries','banana','cherries','mango']
veg
['brinjal', 'okra', 'bottleguard', 'kothmir']

fruits.append(veg)

fruits
['apple', 'berries', 'banana', 'cherries', 'mango', ['brinjal', 'okra', 'bottleguard', 'kothmir']]

fruits.pop()
['brinjal', 'okra', 'bottleguard', 'kothmir']

fruits
['apple', 'berries', 'banana', 'cherries', 'mango']


# listname.extend(another_list)

fruits.extend(veg)
fruits
['apple', 'berries', 'banana', 'cherries', 'mango', 'brinjal', 'okra', 'bottleguard', 'kothmir']







t = ()

t
()
type(t)
<class 'tuple'>
s=[]
type(s)
<class 'list'>


t.append(1)
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    t.append(1)
AttributeError: 'tuple' object has no attribute 'append'


t
()

t=('userid','password')
t
('userid', 'password')
t[0]
'userid'
t[0]t[1]
SyntaxError: invalid syntax
t[1]
'password'

a
['banana', 'cherry']
dd
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    dd
NameError: name 'dd' is not defined. Did you mean: 'id'?


1+'2'
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    1+'2'
TypeError: unsupported operand type(s) for +: 'int' and 'str'




a
['banana', 'cherry']


veg
['brinjal', 'okra', 'bottleguard', 'kothmir']


# convert all the values in the veg list into upper case and add them to a seperate list

veg_upper = []

veg[0]
'brinjal'
veg[0].upper()
'BRINJAL'


veg_upper.append(veg[0].upper())

veg_upper()
Traceback (most recent call last):
  File "<pyshell#251>", line 1, in <module>
    veg_upper()
TypeError: 'list' object is not callable
veg_upper
['BRINJAL']

temp = veg[0].upper()
temp
'BRINJAL'


veg_upper.append(temp)
veg_upper()
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    veg_upper()
TypeError: 'list' object is not callable
veg_upper
['BRINJAL', 'BRINJAL']
veg_upper.pop()
'BRINJAL'

veg_upper
['BRINJAL']

veg[1].upper()
'OKRA'
veg_upper.append(veg[1].upper())
veg_upper
['BRINJAL', 'OKRA']


veg[2].upper()
'BOTTLEGUARD'
veg_upper.append(veg[2].upper())
veg_upper
['BRINJAL', 'OKRA', 'BOTTLEGUARD']



veg[3].upper()
'KOTHMIR'
veg_upper.append(veg[3].upper())
veg_upper
['BRINJAL', 'OKRA', 'BOTTLEGUARD', 'KOTHMIR']




# Looping
# For Loop


veg
['brinjal', 'okra', 'bottleguard', 'kothmir']



for each_item in veg:
    print(each_item)

    
brinjal
okra
bottleguard
kothmir




for each_item in veg:
    print(veg)

    
['brinjal', 'okra', 'bottleguard', 'kothmir']
['brinjal', 'okra', 'bottleguard', 'kothmir']
['brinjal', 'okra', 'bottleguard', 'kothmir']
['brinjal', 'okra', 'bottleguard', 'kothmir']



for each_item in veg:
    print(each_item)
    print(veg)

    
brinjal
['brinjal', 'okra', 'bottleguard', 'kothmir']
okra
['brinjal', 'okra', 'bottleguard', 'kothmir']
bottleguard
['brinjal', 'okra', 'bottleguard', 'kothmir']
kothmir
['brinjal', 'okra', 'bottleguard', 'kothmir']




for chiranjeevi in veg:
    print(chiranjeevi)

    
brinjal
okra
bottleguard
kothmir



veg
['brinjal', 'okra', 'bottleguard', 'kothmir']

# find the length of each value in the list veg

#len(value)


for i in veg:
    length(i)

    
Traceback (most recent call last):
  File "<pyshell#324>", line 2, in <module>
    length(i)
NameError: name 'length' is not defined
for i in veg:
    len(i)

    
7
4
11
7



for name in veg:
    print(name.upper(),name.lower(),name.capitalize())

    
BRINJAL brinjal Brinjal
OKRA okra Okra
BOTTLEGUARD bottleguard Bottleguard
KOTHMIR kothmir Kothmir




# add 100 to every value in a list of 10 numbers

numbers = [1,2,3,4,5,6,7,8,9,10]

numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    num+100

    
101
102
103
104
105
106
107
108
109
110


veg
['brinjal', 'okra', 'bottleguard', 'kothmir']
# convert all the values in the list - veg to upper case and add them to a seperate list




new_veg=[]

for item in veg:
    t=item.upper()
    new_veg.append(t)

    
new_veg
['BRINJAL', 'OKRA', 'BOTTLEGUARD', 'KOTHMIR']


new_veg.clear()
new_veg
[]


c = [1,2,3,4,5]

c
[1, 2, 3, 4, 5]


c.clear()
c
[]
>>> 
>>> c = [1,2,3,4,5]
>>> c
[1, 2, 3, 4, 5]
>>> 
>>> 
>>> c= []
>>> c
[]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for item in veg:
...     new_veg.append(item.upper())
... 
...     
>>> new_veg
['BRINJAL', 'OKRA', 'BOTTLEGUARD', 'KOTHMIR']
>>> 
>>> 
>>> 
