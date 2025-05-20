Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={
...     "list_data" : [1,2,3,4,5,6,7,8,9],
...     "tuple_data" : (1,2,3,4,5,6),
...     'int_data' : 1111,
...     "string": "Sphoorthi",
...     "anthr_dict" : { 'a':1,
...                       "b":2
...                       },
...     "keys" : "values"
... }
>>> 
>>> 
>>> d
{'list_data': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'tuple_data': (1, 2, 3, 4, 5, 6), 'int_data': 1111, 'string': 'Sphoorthi', 'anthr_dict': {'a': 1, 'b': 2}, 'keys': 'values'}
>>> 
>>> 
>>> 
e= { 'a':111,
     'a':222,
     'b':333
     }

e
{'a': 222, 'b': 333}



e= { 'a':111,
     'a':222,
     'a':333
     }

e
{'a': 333}

e= { 'a':111,
     'a':222,
     'a':333,
     'a':444
     }

e
{'a': 444}

e= { 'a':111,
     'a':222,
     'a':333,
     'a':444
     }
e= { 'a':444,
     'a':222,
     'a':333,
     'a':111
     }

e
{'a': 111}



x = 5
x
5

x=6
x
6

x=7
x
7

d
{'list_data': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'tuple_data': (1, 2, 3, 4, 5, 6), 'int_data': 1111, 'string': 'Sphoorthi', 'anthr_dict': {'a': 1, 'b': 2}, 'keys': 'values'}

d[ 'string']
'Sphoorthi'

d['list_data']
[1, 2, 3, 4, 5, 6, 7, 8, 9]


d['keys']
'values'





d
{'list_data': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'tuple_data': (1, 2, 3, 4, 5, 6), 'int_data': 1111, 'string': 'Sphoorthi', 'anthr_dict': {'a': 1, 'b': 2}, 'keys': 'values'}


d['anthr_dict']
{'a': 1, 'b': 2}


d['NewKey']="This isa new value for the new key"

d
{'list_data': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'tuple_data': (1, 2, 3, 4, 5, 6), 'int_data': 1111, 'string': 'Sphoorthi', 'anthr_dict': {'a': 1, 'b': 2}, 'keys': 'values', 'NewKey': 'This isa new value for the new key'}


d.keys()
dict_keys(['list_data', 'tuple_data', 'int_data', 'string', 'anthr_dict', 'keys', 'NewKey'])




d.values()
dict_values([[1, 2, 3, 4, 5, 6, 7, 8, 9], (1, 2, 3, 4, 5, 6), 1111, 'Sphoorthi', {'a': 1, 'b': 2}, 'values', 'This isa new value for the new key'])


{ "item" : "almonds", "price" : 12, "quantity" : 2 }
{'item': 'almonds', 'price': 12, 'quantity': 2}



{
"employees":[
    {"firstName":"John", "lastName":"Doe"},
    {"firstName":"Anna", "lastName":"Smith"},
    {"firstName":"Peter", "lastName":"Jones"}
]
}


{'employees': [{'firstName': 'John', 'lastName': 'Doe'}, {'firstName': 'Anna', 'lastName': 'Smith'}, {'firstName': 'Peter', 'lastName': 'Jones'}]}







temp={
      "dt": 1747549800,
      "sunrise": 1747526879,
      "sunset": 1747573706,
      "temp": {
        "day": 36.44,
        "min": 28.99,
        "max": 39.16,
        "night": 32.19,
        "eve": 36.02,
        "morn": 28.99
      }



      }

temp
{'dt': 1747549800, 'sunrise': 1747526879, 'sunset': 1747573706, 'temp': {'day': 36.44, 'min': 28.99, 'max': 39.16, 'night': 32.19, 'eve': 36.02, 'morn': 28.99}}


temp['sunrise']
1747526879


values  = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(values)
[1, 2, 3, 4, 5, 6, 7, 8, 9]

print(*values)
1 2 3 4 5 6 7 8 9

print(**temp)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    print(**temp)
TypeError: 'dt' is an invalid keyword argument for print()

print(*temp)
dt sunrise sunset temp


print(values,sep="'")
[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(values,sep='-')
[1, 2, 3, 4, 5, 6, 7, 8, 9]

print(values,end='\n')
[1, 2, 3, 4, 5, 6, 7, 8, 9]



import pprint
pprint.pprint(temp)
{'dt': 1747549800,
 'sunrise': 1747526879,
 'sunset': 1747573706,
 'temp': {'day': 36.44,
          'eve': 36.02,
          'max': 39.16,
          'min': 28.99,
          'morn': 28.99,
          'night': 32.19}}





















details =   {
  'company':'maggi',
  'contact':"roalnd",
  'country':'austria'
  }


details
{'company': 'maggi', 'contact': 'roalnd', 'country': 'austria'}

details['company']
'maggi'


details['projects'] ="Business Intelligence"

details
{'company': 'maggi', 'contact': 'roalnd', 'country': 'austria', 'projects': 'Business Intelligence'}



details['projects']
'Business Intelligence'



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

details.get('projects',"Check the Key Name properly")
'Business Intelligence'





details
{'company': 'maggi', 'contact': 'roalnd', 'country': 'austria', 'projects': 'Business Intelligence'}


details.pop('contact')
'roalnd'


details
{'company': 'maggi', 'country': 'austria', 'projects': 'Business Intelligence'}


details
{'company': 'maggi', 'country': 'austria', 'projects': 'Business Intelligence'}


details['another dictionary'] = {}

details
{'company': 'maggi', 'country': 'austria', 'projects': 'Business Intelligence', 'another dictionary': {}}
details['another dictionary'] = {'a':1,'b':2}


details
{'company': 'maggi', 'country': 'austria', 'projects': 'Business Intelligence', 'another dictionary': {'a': 1, 'b': 2}}


details.get('another dictionary')
{'a': 1, 'b': 2}
