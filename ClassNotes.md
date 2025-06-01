# Class Notes 


03May2025


For code sharing - GitHub Link
For Class Notes  - Google Docs
Syllabus  - Google Doc

 - by  09May2025



Python :

- installation - IDLE, Shell, [ Jupyter, Spyder, Pycharm/VC Code
- Tools
- Variables - assignment operator; variable names; 
- Print functions
- Basic programs



Variables - variables are container like structures that Hold data in it, we can call them as identifiers/aliases of values.

how to create/define variables ?


LHS = RHS
variableName = Value
any_name_without_spaces = int, float, str, filename, name of a song, URL ..... Matrix of values, 
							image, expression ( that outputs a result) 3+9+4+8+1 , function that returns a value

Program - input - output


#### Input types

       - numbers
       
               - real numbers : 1,2,3,4,5.... 1111    : - int 

               - decimal numbers : 1.23. 0.001, 3.333, 1.111   : - float

               - Boolean  : True, False : bool
         
         strings/ str
		       - alphabets : a,b,c,d,e,f,g ...

		       - words : apple, banana, good, ... 

		       - paragraphs : collection of words

		       - special chars : symbols - #$%^&*() space


       - always strings will have quotations - '' , " "

       'sree' , "sree" 

strings - all the strings/characters/alphabets/sentences/paragraphs should be defined with quotations around it.
 these quotes can be single quotes or double quotes , " ", ' ', '''  ''' , """  """


'apples','pineapples','free classes are very informative'


Proper way of define/creating variables -- 



### Variable Names


1) Variable names should always be in lower cases *
2) Variable names should always be unique
3) you can use underscores as a char within variable name
            first_name, last_name

4) 
```python
first_name = "sri"
firstname____name = "somename"

_first = "aa"
second_ = "bb"

____ = "a"
```


*** 5) We use Upper case variable Name for Global Declarations
*** 6) functions/function names shold be defined in Camel case  camelCase



Commenting - #
anything after # is treating as a comment is ignored by Python and is not executed.

Operators -

Addition  +
Subtraction -
Assignment operator =
Equality checking operator ==  
multiplication *
Power **

*** divide/divisible by   / 

```
2) 14 (7 - Quotient
   14
   ___
   0 - remainder
   
2 - ?
7 - ?
0 - ?


2) 3 (1
   2
   ___
   1

```



# find the average of 6 subject marks

- we need 6 subject marks
- first find the total of 6 subject marks
  second, divide that total by number of subjects

 - print the answer



# defining 6 subject marks
 maths = 80
 telugu = 90
 hindi = 40
 social = 70
 science = 80
 english = 36

# find the total of 6 subjects

total = maths + telugu + hindi + social + science + english

# divide the total with 6 

avg = total/6


```python
### Program Structure


 - Data Part
 - Logic Part
 - Results/Presentation Part

######   - Data Part  ###########

# defining 6 subject marks
 maths = 80
 telugu = 90
 hindi = 40
 social = 70
 science = 80
 english = 36

######   Logic Part  ###########

# find the total of 6 subjects

total = maths + telugu + hindi + social + science + english

# divide the total with 6 




######   Results Part  ###########


avg = total/6

```


### Collecting Inputs from the user directly


input(somevalue) - function collects user inputs,
			It reads all the keystrokes of the keyboard and returns them as is
			input() will only collect andwill not store any values.
			define a variable and assign an input function to it so that the value collected by input() is stored in respective variable.

			input() will always collects everything as strings


function - collection of multiple commands put together as a single word
     will accept values as inputs 
     the inputs we pass into a function are known as parameters/Arguments
     somevalue - parameter/argument/arg

prompt - the parameter/arg we pass into the input function 
input("enter your name    :") here, enter your name    :" is the prompt


```python
Version - 2

# define 3 subject marks

maths = input("Enter your maths marks     :")
Enter your maths marks     :30

science = input("Enter your science marks     :")
Enter your science marks     :50

telugu = input("Enter your telugu marks     :")
Enter your telugu marks     :80


maths
'30'
science
'50'
telugu
'80'

total = maths + science + telugu

total
'305080'
# joining/concatenation , not addition

```


type() - the type() tells us what datatype it is.
		 It takes a value as an input and tells us if the input is an integer or a float or a string

		 type(Value)


### DataType conversions / TypeCasting

 - Converting a datatype from one type to another type
 	eq : converting an integer into a string

 06May2025


 Type casting / Data type conversions
 Dynamic/Run time Data type conversions

 Run Programs



 Strings 




### Type casting / Data type conversions


to convert into a string - str()
to convert into an integer - int()
to convert into a decimal - float()


int(value) -> integer value

The above functions will only return a new value,
they will not change the parent value / existing value
inorder to change the existing values, we need to override the variables with latest values


### Chaining of functions

int(input())



maths_n = int(maths)
science_n = int(science)
social_n = int(social)
hindi_n = int(hindi)
telugu_n = int(telugu)
english_n = int(english)


Print Function - print displays or prints the convent on the screen, this is a presentation function that displays values/text on the screen or as output

print() is the keyword

```python
print(value) - this only prints the value

print("some help text",value) - this print the text first and then the value
print("his name is ",name) >>> "his name is einstein"

print("his name is",name,"he is ", age,"years old","his favourite food is",food,1111)


Print formatting , multi-line printing

name = "einstein"
age = 72
food = 'idly'

print(name)
einstein

print(age)
72

print(name,age)
einstein 72
print(name,'is',age)
einstein is 72


print("His name is",name,"he is ",age,"years old","his fav food is",food)
His name is einstein he is  72 years old his fav food is idly
```

### Strings

anything which has quotes around it - string/str
strings are collections ( multiple values as a single value)
string are immutable
strings will have positional addresses/location - indices ( index )
string have length

strings are considered as Text and will have case functions

uppercase 
lowercase
titlecase


we can extract single value from the entire string based on their positions


len() - is the function that takes a value and outputs the length of it/total characters persent in it
The output type is integer


text cases

These methods/functions will not replace the old strings with new formatted strings
these will only return the modified values, the actual values are undisturbed.


  - upper case : converting a string to upper case.

                 String.upper()



  - lower case : convert a string to lower case.

                String.lower()


  - title case : convert a string to a title case

               String.title()


- .capitalize() : this method capitalizes 
               String.capitalize()




function(variable) - function
variable.function() - methods ( designed for specific datatype only)


dir() - a builtin function that takes a dattype and gives all posible functions of that datatype.


sublimetext editor





07May2025 ::  

Strings 
Candidate Interview
Data Structures


name = "sphoorthi"

- length
- indices/index


### Indexing
        - extract the values from a specific position in a collection using indexing


Indexing can ben done from Right to left with the addresses starting from 0 to n and from left to right the address starting from -1 to -n

the last index value would be len(string)-1


we extract values from the collection using below syntax

VariableName[IndexNumber]

name[0] , name[1], name[2],name[3] ...



### Print formatting

Placeholders 
for strings - %s
for integers - %d



08May2025


- String methods ( validations)
- conditionals
- data structures


- How to execute a program from a command line ?

- save the program in a folder
- open that folder in command line
- locate the program you've saved
- type below syntax and hit enter

python program_name.py



Identifying - Features




### conditionals

we use if as a conditions - executing in the programming

"what if ?"

1) simple if condition 

we use the keyword, if with a condition and execute the code based on that condition

```python
if <condition>:
    code to be execute
    code line
    code line
    code lines
    to be executed only when the condition is TRUE
```

condition - True / False


condition's output is true, then the code block within if is executed, if the output is false then not

```python
if raining:
   carry umbrella
```

2) simple if-else condition

 in cases where the if fails or the condition in IF is False then the alternative should be executed, the Else block is the alternative


```python
if <Condition>:
	Execute this block only when 
    the condition in if block is TRUE
else:
     execute this block when the 
     condition in the IF block is False


eg :

# it_is_raining = True/False

if it_is_raining:
    take a cab and go to office
else:
    Go on bike

```

else will not have any condition and will be only executed in the scenarios when the condition in if is false



- if a number is divisible by 5
- tiffin center


09 May 2025

Nested IF conditions
Conditions Chaining using Logical Operators

Data Structures





find if a number is greater than x or lesser than x or equal to x
x & number can be any integers


greater than x

lesser than x

equal to x


if-elif

There will be only one if block and there can be any number of elif blocks
elif - (else if)a combination of both else & if which takes a condition unlike else block

```python
if <condition>:
    Code to be executed when the condition is True

elif <condition>:
    Code to be executed when the condition is True

elif <condition>:
    Code to be executed when the condition is True

elif <condition>:
    Code to be executed when the condition is True

elif <condition>:
    Code to be executed when the condition is True

elif <condition>:
    Code to be executed when the condition is True

elif <condition>:
    Code to be executed when the condition is True

else :
      Code to be executed when all the above conditions are not met

```






"Hi StudentName ( in capitals),

Your sub1 marks are :
Your sub2 marks are :
Your sub3 marks are :
-
-
-
-

Your Average is : 
The grade assigned to you in : Grade

Thank you"






govt scheme -

age should be more than 60, yearly income should be less than 1 lakh rupees, family size should be less than 4, no other alternative income sources, no lands, no properties
then they're eligible for free govt scheme


### Logic gating / conditional chaining
### [Class Notes - And-OR-Operators-ClassWorkout.py ](https://github.com/srisreedhar/Sphoorthi-FreeSummerClasses-2025/blob/main/And-OR-Operators-ClassWorkout.py)

we chain all the conditions using AND & OR


AND operator - in the chain of multiple conditions, only when the case all the conditions are TRUE then the 
                final outcome will be TRUE

OR Operator - in the chain of multiple conditions, if atleast one condition is TRUE then the entire chain 
                will be  TRUE


Eg : - 
False or False or False or False or False or False or True
True


if (65>6) and (66>51) and (55>1) and (64 >3) and (72 > 1) and (5 <42):
    print("Executed becasue the final reulst is TRUE")

    
Executed becasue the final reulst is TRUE



if (65>6) and (66>51) and (55>1) and (64 >3) and (72 > 1) and (5 <4):
    print("Executed becasue the final reulst is TRUE")





scalars  - single values, data types

vectors - collection of scalars, multiple values, multiple data types




### Data Structures 

- is a container like stucture that holds data in an orderly manner as per the datastructure being used.



- List 

- Tuple

- Dictionary

- Set (function)


10May2025

### LIST


- List

        - Arrays
        - mutable data structures ( we can modify the size of the list, add/remove values)
        - we create a list using  [] ; assign [] to any variable
        - list, list() are the keyword and functions of list
        - indexing, length are applicable
        - Lists are Homogenous Data Structures ( all same data types in the list)
        - each and every value in list are comma seperated and the value can be anything between commas

        [1,2,3,4,5,6,7], ['a','b','c','d','e']  -> homogenous lists
        [1,2.5,'apple',False] -> Heterogenous List X


names = ['einstein','tesla','faraday','ramanujan']



# adding values to a list
ListName.append()
- all the values which are being added are appened from the end/tail of the list.
  [] <-

names.append("NewName")




# removing values from a list
ListName.remove(Value)

.remove(Value) takes an argument, a value which needs to be removed from the list. the values needs to be exist in the list.


# removing values based on their index number
.pop() removes values rom the end if no argument is passed. pop deletes values from the end/tail
ListName.pop(IndexNumber) - pop takes an index number and removes value of that index number


# unpacking another list and adding only values of another list
# listname.extend(another_list)
this will unpack the another list and only adds values to current list



# extending a list with the values of another list / merge

ListName.extend(Value)




- if we do not pass any index number, it by default removes the last element from a list
- It always returns the value which is being popped out/removed



# To clear or Empty the entire list / delete all elements in the List

Listname.clear()



###  Tuple
        - are immutable data structures
        - they're the opposite of lists
        - we create a tuple using () 
        - tuple,tuple() are the keywords
        - len & indexing are applicable





Dictionary
    - weather data
    - apis

['11', '11', '11', '11', '11', '11']



Loops
Functions
- packages

Data Analysis

SQL



Errors:

AttributeError: 'list' object has no attribute 'upper'
ValueError: list.remove(x): x not in list
NameError: name 'dd' is not defined
TypeError: unsupported operand type(s) for +: 'int' and 'str'




### Loops

For Loop - repeating the same piece of code / code block or set of commands on every item in a 
            collection


syntax

for each_item in collection:
    write code on each_item only


for - keyword that we use to initiate for loop


each_item - Temp Variable / Loop Variable
             this stores every value in a collection till it is processed
             when the loop is initiated,
                - the first value in the collection is assigned to loop variable
                        each_item = firt_value
                - then the code is applied on that
                - once completed, it moves to the second element in the collection
                - the second element is aassigned to the loop variable 
                - this cycle continues till the end of the collection or all the values are processed.

                - you always have to write code on each_item itself as this is the variable that iterates.

                - the loop/iteration happens for lenght of collection times, 
                   i.e., if the collection has 10 values, the loop will run 10 iterations or the code block is executed 10 times for each value in the collection








```python
['brinjal', 'okra', 'bottleguard', 'kothmir']



for item in ['brinjal', 'okra', 'bottleguard', 'kothmir']:
    x = item.upper()
    print(x)


item='brinjal', 
x = item.upper()
print(x)

>>> BRINJAL


item='okra', 
x = item.upper()
print(x)

>>> OKRA


item='bottleguard',
x = item.upper()
print(x)

>>> BOTTLEGUARD


 item='kothmir'
 x = item.upper()
print(x)
>>> KOTHMIR


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






1)
for each in 123456:
 print(each)

2)
for each in "123456":
 print(each)


13May2025

- github account

create an account on github.com 


```


[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 
25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]



stringName.split(delimitter)

                    - splits a string into multiple parts based on the (argument) delimitter
                    - by default it considers space as a delimitter
                    - the output will be a list
                    - this will not impact the actual defination


### unpacking variables from a collection:

veg
['brinjal', 'okra', 'bottleguard', 'kothmir']


a,b,c,d = veg
a
'brinjal'
b
'okra'
c
'bottleguard'
d
'kothmir'



### Membership checking operator - in

if we want to check if a value is a part or a member of or exists in  a collection, then we use membership operator

"value_you_want_to_check" in collection

5 in [1,2,3,4,5,6,7,8,9]

when executed this returns a boolean value,
if the value is present, it returns True or False if it doesnt



's' in 'sphoorthi'



:) :D :x 



X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

fn,ln = name.split()


14May2025


### Counters in Loops



numbers = [1,1,1,1,1,1,1,1,2,2,2,3,3,3,3,4,4,4,4,5,5,5,6,7,8,9]


when there's a collection and we have to count the number of occurances or repititions of a particular item/value in that collection, then we need to count those number of occurances.

to implement counting mechanism we create a variable outside of forloop and increment/increase the variable everytime we come across that value

we call this variable as counter / counter variable.

counter = 0
for something in collection:


in the above example we defined a counter varaible and set its value to 0, the counter variables will have
the initial values as 0, based on the occurances of a value in collection the 0 will be incremented



### Indexing - extracting sub-groups from a string


: - continuation operator

to extract a single value , String[IndexNumber]

to extract a sub-group or collection of values / multiple values from a string

String[StartIndexNumber : StopIndexNumber]
String[0:10] - will extract values from 0 - 9(10-1)

Indexing always returns the (StopIndexNumber-1) values



age(Stock/Raw columns)     age<30 ( derived variables/columns/values / features KPI)

10                          True
20                          True
31                          False
35                          False


- Dictionary 
- Functions
- Packages & imports


### Files - 



### Packages / Libraries / Modules


- collection of commands / programs which are packed as a single module/package
- we can call them into our program and use their functionalities, we dont have to create the functions again


- you create a program with 10 functionalities and you use them for some tasks
- if any of your friend is performing the same taks, they need to create code for the same functionalities
- instead, if you share your functions/file with them they can import/call the functions into their program
and use them





### methods to import Packages / Libraries / Modules

library - msoffice
                - word
                - ppt
                - onenote
                - paint
                - excel


import - we use import keyword to import a package into our current program
```python
import <packageName>

import msoffice

```
once the package is imported, we can call its functionalites using . operator

if we want to use word then we can call it from msoffice

```python
ImportedPackageName.function(arg)

msoffice.word()
msoffice.ppt()

```


Python has a lot of builtin libraries which we call as Standard Libaries whih offers multiple functionalities

- os module/library
- lets us interact with the operating system
- we can operate on files/folders/paths/ print the contents of a folder

- if we want to find how many functions are avaialble in a package that you have imported
run dir() on it


import os


-getcwd() : get current working directory()
-chdir()  : change to a different directory
-mkdir()   : create a folder/directory
listdir()  : list all the content in a directory


# Dictionary

```python
{
'science' : 90,
'social' : 10,
'hindi' : 30,
'telugu' : 99,
'english' : 70,
'maths' : 99
}
```

- labels
  value identifiers
  - hash maps
  - associative arrays

 - Key & Value stores
    - keys are labels/identifiers of the data
    - values can be anything, int, str, list, tuple, dictionary 
    - a single value in dictionary is a kv pair (key value pair)
    - keys are unique and they should be unique
    - values can be duplicated

    - keys should be strings

```python

{
    "list_data" : [1,2,3,4,5,6,7,8,9],
    "tuple_data" : (1,2,3,4,5,6),
    'int_data' : 1111,
    "string": "Sphoorthi",
    "anthr_dict" : { 'a':1,
                      "b":2
                      },
    "keys" : "values"
}


e= { 'a':111,
     'a':222,
     'b':333
     }

e
{'a': 222, 'b': 333}

```

- if there are duplicate key names or same key names with different values
then python considers the latest defination and ignores previous value




Extracting values fron a Dictionary
```python
DictionaryName[KeyName]

d['string']
'Sphoorthi'
```
### add new key value pairs to a dictionary

 - if you want to add a new value to an existing dictionary, you always have to add a pair to it
 - we define a key and a value at the same time.
 - 
```python
 DictionaryName[NewKey] = 'NewValue'
```

 ### print all the keys
```python
 DictionaryName.keys()
```
 ### print all the values
```python
 DictionaryName.values()
```



 # API - Application Programming Interface

 - the data sharing protocol
 - Serialized Data

```python
 [
 {
  'company':'nike',
  'contact':"maria anders",
  'country':'Germany'
  },
 {
  'company':'adidas',
  'contact':"fransicico",
  'country':'mexico'
  },
  {
  'company':'maggi',
  'contact':"roalnd",
  'country':'austria'
  }
  ]

```

 API is an interface between the End users and the DataBase whch guards data with security protocols and shared only what is demanded based on authorization

```json
{
'sandles':1220,
'idly rava':100,
'jeans':1111
}
```

-> cart ( aws dynamodb )

Example : https://api.github.com/users/srisreedhar
https://api.github.com/users





# Associated arrays / Dictionary
### [Class Notes - ClassWorkout-Dictionaries.py ](https://github.com/srisreedhar/Sphoorthi-FreeSummerClasses-2025/blob/main/ClassWorkout-Dictionaries.py)

    - values -> associated with a Label
    - duplicates
    - values are reffered using that label
    - values are retrieved using that label
    - these labels are known as Keys
    - keys are unique in a dictionary
    - value can be anything

    - a single value is a Key-value pair in a dictionary 
      ( single - single pair, single country, single group, single constellation)

    - values will only exist with Keys in dictionary
    so, if you're creating a value in a dictionary, you need to create a key first and then associate values with it

    - Dictionaries are unordered data structures, the data is not organized inside the dictionary

    - we can retrieve calues based on the Keys
    - Keys should always be Strings

    - Dictionaries are mutable datastructures
    - create a new dictionary using {}
    - dict, dict() 





` JSON, Mongodb, Dynamodb, APIs`



### adding  a new key value pair

 - if you want to add a new value to an existing dictionary, you always have to add a pair to it
 - we define a key and a value at the same time.
  -- creating an association with the Key and Value

```python
 DictionaryName[NewKey] = 'NewValue'

 class5['NewStudent'] = 'NewStudent Name'

 Restaurent['Veg Menu'] = 'Sambar'
```


```python

### printing/ extracting / accessing values from a dictionary

details =   {
  'company':'maggi',
  'contact':"roalnd",
  'country':'austria'
  }

  # extract/access maggi

  1)  DictionaryName['KeyName']

  2) DictionaryName.get('KeyName')

  details.get('projects')
'Business Intelligence'


details['project']
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    details['project']
KeyError: 'project'



details.get('project')


details.get('project',"Check the Key Name properly")
'Check the Key Name properly'




# Print all the keys 
DictionaryName.keys() -> prints all the keys as a dict object


# Print all the values 
DictionaryName.values() -> prints all the values as a dict object

```

### remove values from a Dicitonary

```python
DictionaryName.pop(KeyName) 
```

pop takes keyname as argument/arg and removes that KV pair, it returns the value of the Keyname/arg

```python
details.pop('contact')
'roalnd'
```


- Nested Dictionaries



list = []

tuples = ()

Dictioanries = {}




# Files :
         - locate the file ( go to the folder where the file is located)
         - Open the file
         - read the file content || write something to the file || read and write something to the file
         - close the file


### Types of Files :

         - Text files, CSV files -> open with a notepad
         - Excel Files, PDF files -> respective softwares ( MS Excel , Acrobat Reader ..)
                   ( - binary files )



### File Operation Functions

open() - this function opens the file
         - this function takes 2 arguments, FilePath/FileName & AccessMode

         open("FileName","AccessMode")

        _ this function when executed will return a file_object, the file object needs to be saved and should be read to read the content of the file

        - we save the file_object in a variable and use that variable for all the later workflows

        - if we did not specify any modes when opening the file, by default it considers read-only mode ( r )


.read() - we use .read() method on the file_object to read its content. We need to apply this on file_Object


.close()  - once the operations are complete with the files, we close the opened file with .close() method
            we apply .close() on the file_object that we opned using open()


```python
f = open("FileName")
content=f.read()
print(content)
f.close()
```




### File Access modes

read only-  "r"

write -  "w"

append -  "a"

read & write - "r+"

read & write binary  - "rb+"



```python

f = open("FileName", 'r')
content=f.read()
print(content)
f.close()

```


### Write operations on Files


.write("content") - we use write method to write content to the file.
                  - we apply this method on file_object

                  - if the file is opened in write mode, then all the existing content would be deleted 

                  - so, if you want to add content to existing content in the file, then use 'a' (append) mode


```python

f = open("FileName", 'w')
f.write("have a great day ahead")
f.close()

```

# Packages / Libraries / Modules


- collection of commands / programs / values which are packed as a single module/package / python file
- we can call them into our program and use their functionalities, we dont have to create the functions or defining values again


- you create a program with 10 functionalities/values and you use them for some tasks
- if any of your friend is performing the same taks, they need to create code for the same functionalities
- instead, if you share your functions/file with them they can import/call the functions into their program
and use them


### methods to import Packages / Libraries / Modules


library - msoffice
                - word
                - ppt
                - onenote
                - paint
                - excel


import - we use import keyword to import a package/file/library into our current program

```python
import <packageName/LibraryName/FileName/ProgramName>

import msoffice

```
once the package is imported, we can call its functionalites using . operator

if we want to use word then we can call it from msoffice, 

```python
ImportedPackageName.function(arg)
ImportedFileName.Value

msoffice.word()
msoffice.ppt()

from /values.py file - 
values.numbers
values.marks
```

### [Class Notes - values.py ](https://github.com/srisreedhar/Sphoorthi-FreeSummerClasses-2025/blob/main/values.py)
### [Class Notes - importing from values.py ](https://github.com/srisreedhar/Sphoorthi-FreeSummerClasses-2025/blob/main/import-testing.py)
we call this as NameSpacing



kcr   TRS.kcr
ktr   TRS.ktr
pvr    congrass.pvr

js   bjp.js
css  bjp.css



## Selective Imports
### Second form of Importing, what is needed

Instead of importing everything into a program, 
using below syntaxes we only import what is required

```python
from PackageName import FunctionName
from PackageName import value


from PackageName import value1,value2,value3..
```


# if we want to give our own namespaces/names to the packages that we are importing into our program
```
from values import aadhar_num as an
```

Python has a lot of builtin libraries which we call as Standard Libaries whih offers multiple functionalities

- os module/library
- lets us interact with the operating system
- we can operate on files/folders/paths/ print the contents of a folder

- if we want to find how many functions are avaialble in a package that you have imported
run dir() on it

List of all Standard Libraries : https://docs.python.org/3/py-modindex.html

```
import os


-getcwd() : get current working directory()
-chdir()  : change to a different directory
-mkdir()   : create a folder/directory
listdir()  : list all the content in a directory

```

## How to install External Libraries ? / 3rd Party Libraries

we use a Package Manager to manage all the packages (PIP)

Managing ? -
            Installing
            updating
            deleting

pip is the package manager using which we can manage packages
always refer to respective package webpage or PYPI page for package information

```python
pip install PackageName
```

# Connecting to internet 
# we use requests library to connect to internet and perform tass which needs connectivity


### handling requests - responses

```python
import requests
```
- we need to send the request to open a resource using get method.

```python
requests.get(url)
```
.get() method- this method will take a url and returns a response object

we need to store this response object in a variable so that we apply all the other methods on that response obj


resp = requests.get(url) - we use resp varaible for all the later operations


resp.text - this method will read the response object and extracts the test from it

resp.content - this methods returns the data in the form of byte stream



```python

import requests
resp = requests.get(URL)
data = resp.text


import requests as r
resp = r.get(URL)
data = resp.text


```

### install Jupyter notebook
    -- https://jupyter.org/
    -- https://jupyter.org/install#jupyter-notebook
        --- pip install notebook

Dataset : [Animal - Sleep time](https://raw.githubusercontent.com/srisreedhar/DataSets/refs/heads/master/animal_sleeptime_ggplot2.csv)

# Function

    a small programs which are saved with an alias/identifier
    few lines of code / code block which has a name and when the name is called the code block is executed.
    we can call the functionality multiple times using the alias 



### How to create a Function ?

we use def keyword to define/create a function, every function returns a value, for which we use return keyword

```python
def functionName(arg1,arg2,arg3):
    write code on arg1, arg2 ..
    write code using args
    we get result
    return result

```

#### create a function that takes 2 numbers and returns the sum of the 2 numbers

```python
def sumof2(num1,num2):
    total = num1+num2
    return total

```

Code Reusability

# Dictionary Methods


#### Print all the keys 
```
DictionaryName.keys() -> prints all the keys as a dict object
```

#### Print all the values 
```
DictionaryName.values() -> prints all the values as a dict object
```

#### remove values from a Dicitonary
```
DictionaryName.pop(KeyName) 
```
pop takes keyname as argument/arg and removes that KV pair, it returns the value of the Keyname/arg
```
details.pop('contact')
'roalnd'
```


#### printing/ extracting / accessing values from a dictionary
```python
details =   {
  'company':'maggi',
  'contact':"roalnd",
  'country':'austria'
  }
```
```python
  # extract/access maggi

  1)  DictionaryName['KeyName']

  2) DictionaryName.get('KeyName')

>>> details.get('projects')
'Business Intelligence'
```
```python
 
If we give the wrong key name -->  KeyError
>>> details['project']
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    details['project']
KeyError: 'project'

>>> details.get('project')

We can supply a default value which runs when its a KeyError
>>> details.get('project',"Check the Key Name properly")
'Check the Key Name properly'

```




#### Update

appends all the KV pairs from one dictionary into another
```python
first = {'a':100}
second={'z':900}

first
{'a': 100}
second
{'z': 900}

first.update(second)
first
{'a': 100, 'z': 900}


#### clear
#### to empty a dictioanry

first
{'a': 100, 'z': 900}
first.clear()
first
{}

```

```python
{
'sandles':1220,
'idly rava':100,
'jeans':1111,
'fruit':'apple',
'cooldrink':'butter milk'
}
```

#### Looping in dictioanry

When we apply for-loop on a dict, it loops over the keys.
to loop over on both keys & values at the same time, we use .items() method and apply loop on 
dictionary.items()
```python
for each_key,each_value in sample.items():
    print(each_key," --",each_value)
```

we need to create 2 loop variables / Temp variables . one for keys and one for values
        
        each_key -- handles all the keys,
        each_value -- handles all the values


IF you're trying to loop over a dictioanry, 
    first, confirm if you want to loop over just keys or values and use .keys() or .values() accordingly

    Lastly, if you want to simultaneously apply loop on both keys and values,
         then use .items()

        - cases when there is a collection of dictionaries, with the same key arrangement, use items



 #### Dictionary.set default('Key','value')
 ```python
 sample.setdefault('jeans','pepe')
1111
 
 sample
{'sandles': 1220, 'idly rava': 100, 'jeans': 1111, 'fruit': 'apple', 'cooldrink': 'butter milk'}
 
>>> sample
{'sandles': 1220, 'idly rava': 100, 'jeans': 1111, 'fruit': 'apple', 'cooldrink': 'butter milk'}
>>> 
>>> sample.setdefault("new key","new value")
'new value'
>>> 
>>> sample
{'sandles': 1220, 'idly rava': 100, 'jeans': 1111, 'fruit': 'apple', 'cooldrink': 'butter milk', 'new key': 'new value'}
>>> 
>>>
```
setdefaut returns the value of a key and its value if the key is present in the dictionary,
if the key is not present then setdefault creates a key-value pair
if the key is already present in the ditioanry then it wont disturb the existing key value pair


### CSV Module

csv - comma seperated values : file format   
    - all the values are coma seperated   
    - all the values are in string format   


csv module - standard library

-Opening a csv file    
-Reading a csv    
    - reading it as a dictionary    
-writing a csv    


**with - context manager**
       used for file operations
       using with we can open-operate-close a file
       using with will create a code block and helps us organize all our file related operations
       in the same block.
       file closes and everything will be taken care by with


    with open(FILENAME,'ACCESS MODE') as file_alias:
         operations on file_alias


In Python, the File Handling process
 ```python
 filehandler = open(filename,accessmode)
 data = filehandler.read()
 filehandler.close()

  with open(FILENAME,'ACCESS MODE') as filehandler:
         operations on filehandler
```
Using CSV Module

```python
import csv

with open(filename,accessMode) as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)
```

 **csv.reader(csvfile)**     
 
> a csv file reader method imported from CSV module     
> this creates a csv file object which will have all the file data    
> all the remaining operations are to be done on this csv object    

for row in csv_reader: we use for-loop to loop over every ROW in the csvfile and performa any operation <br> <br>

**DictReader** : This method allows us to read the data as a dictionary



