Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


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




#### copy method

first
{}

second
{'z': 900}

second_dup = second.copy()

second_dup
{'z': 900}


#### iteratable items

sample={
'sandles':1220,
'idly rava':100,
'jeans':1111,
'fruit':'apple',
'cooldrink':'butter milk'
}

sample
{'sandles': 1220, 'idly rava': 100, 'jeans': 1111, 'fruit': 'apple', 'cooldrink': 'butter milk'}


sample.items()
dict_items([('sandles', 1220), ('idly rava', 100), ('jeans', 1111), ('fruit', 'apple'), ('cooldrink', 'butter milk')])



for key,value in sample.items():
    print("key is ",key,"value is ",value)

    
key is  sandles value is  1220
key is  idly rava value is  100
key is  jeans value is  1111
key is  fruit value is  apple
key is  cooldrink value is  butter milk


# converting a dict item to list

sample.keys()
dict_keys(['sandles', 'idly rava', 'jeans', 'fruit', 'cooldrink'])

list(sample.keys())
['sandles', 'idly rava', 'jeans', 'fruit', 'cooldrink']

sample.values()
dict_values([1220, 100, 1111, 'apple', 'butter milk'])

list(Sample.values())
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    list(Sample.values())
NameError: name 'Sample' is not defined. Did you mean: 'sample'?
list(sample.values())
[1220, 100, 1111, 'apple', 'butter milk']
>>> 
>>> 
>>> # set default
>>> 
>>> sample.setdefault('jeans','pepe')
1111
>>> 
>>> sample
{'sandles': 1220, 'idly rava': 100, 'jeans': 1111, 'fruit': 'apple', 'cooldrink': 'butter milk'}
>>> 
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
>>> # setdefaut returns the value of a key and its value if the key is present in the dictionary, if the key is not present then setdefault creates a key-value pair
>>> # if the key is already present in the ditioanry then it wont disturb the existing key value pair
