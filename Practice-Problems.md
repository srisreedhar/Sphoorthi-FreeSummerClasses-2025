# Python lists

---

### 1. **Create and Modify a List**
**Problem**: Write a Python program to create a list of 5 favorite fruits, then:
- Add a new fruit to the end of the list.
- Insert a fruit at the second position.
- Remove one fruit by its value.
- Print the final list.

**Apply these ->** : List creation, `append()`, `insert()`, `remove()`, basic list operations.

---

### 2. **Reverse a List**
**Problem**: Write a Python function that takes a list of numbers as input and returns the list in reverse order without using the built-in `reverse()` method or slicing (`[::-1]`).

**Hint**: Use a loop to create a new list by iterating from the end to the start.

**Apply these ->**: Loops, indexing, creating a new list.

---

### 3. **Find the Largest Number**
**Problem**: Write a program that takes a list of numbers (e.g., `[4, 2, 9, 7, 5]`) and finds the largest number in the list without using the `max()` function.

**Hint**: Initialize a variable with the first element and compare it with each element in the list.

**Apply these ->**: Iteration, comparison operators.

---

### 4. **Count Occurrences**
**Problem**: Write a function that takes a list and an element as input and returns how many times that element appears in the list. For example, for `["apple", "banana", "apple", "orange"]` and `"apple"`, return `2`.

**Apply these ->**: Loops, conditionals, counting elements.

---

### 5. **Remove Duplicates**
**Problem**: Write a program to remove duplicates from a list while preserving the order of the first occurrence of each element. For example, `[1, 3, 3, 4, 2, 1]` should become `[1, 3, 4, 2]`.

**Hint**: Use a loop and a new list, or consider using a set carefully to maintain order.

**Apply these ->**: Loops, sets (optional), list manipulation.

---

### 6. **List Slicing Practice**
**Problem**: Given a list of 10 numbers, write a program to:
- Extract the first 3 elements.
- Extract the last 4 elements.
- Extract every second element.
- Print all three results.

**Example Input**: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

**Apply these ->**: List slicing, indexing.

---

### 7. **Sort a List Without `sort()`**
**Problem**: Write a function to sort a list of numbers in ascending order without using the built-in `sort()` or `sorted()` functions. Use a simple algorithm like bubble sort.

**Hint**: Compare adjacent elements and swap them if they are in the wrong order, repeating until no swaps are needed.

**Apply these ->**: Nested loops, swapping elements, basic sorting logic.

---

### 8. **Merge Two Lists**
**Problem**: Write a function that takes two lists and merges them into a single list, alternating elements. For example, `[1, 2, 3]` and `["a", "b", "c"]` should become `[1, "a", 2, "b", 3, "c"]`. Handle cases where lists have different lengths.

**Hint**: Use a loop with indexing and check the length of both lists.

**Apply these ->**: Loops, conditionals, list concatenation.

---

### 9. **List Comprehension**
**Problem**: Write a program that uses list comprehension to:
- Create a list of squares of numbers from 1 to 10.
- Create a list of even numbers from an input list (e.g., `[1, 2, 3, 4, 5, 6]`).
- Create a list of strings from a list of numbers, appending "th" to each (e.g., `[1, 2, 3]` becomes `["1th", "2th", "3th"]`).

**Apply these ->**: List comprehension, string formatting.

---

### 10. **Rotate a List**
**Problem**: Write a function that rotates a list to the left by `n` positions. For example, for `[1, 2, 3, 4, 5]` and `n=2`, the result should be `[3, 4, 5, 1, 2]`. Handle cases where `n` is larger than the list length.

**Hint**: Use slicing or modulo arithmetic to handle rotations efficiently.

**Apply these ->**: Slicing, modulo operator, list manipulation.

---


# Python dictionaries

---

### 1. **Create and Update a Dictionary**
**Problem**: Write a Python program to create a dictionary of 3 favorite Movies with their titles as keys and authors as values. Then:
- Create an empty dictionary called Movies and then add all the movies one by one.
- Do not create the Entire dictionary on a single go.
- Add a new Movie to the dictionary.
- Create a seperate List for Actors, Producers, Directors, Songs
- Update the author of an existing Movie.
- Remove a Movie by its title.
- Print the final dictionary.

**Apply these ->**: Dictionary creation, adding key-value pairs, updating values, `pop()` or `del`.

---

### 2. **Count Characters in a String**
**Problem**: Write a function that takes a string as input and returns a dictionary where keys are characters and values are the number of times each character appears. For example, `"hello"` should return `{'h': 1, 'e': 1, 'l': 2, 'o': 1}`.

**Hint**: Word counts, Iterate through the string and update counts in the dictionary.

**Apply these ->**: Loops, dictionary updates, `get()` method (optional).

---

### 3. **Check for Key Existence**
**Problem**: Write a program that takes a dictionary and a key as input and checks if the key exists in the dictionary. If it does, print its value; otherwise, print "Key not found." and create the key with its value. Precisely, Check if a Key exists in  dictioanry, if it doesnt then create a key and assign its value.

**Hint**: Membership checking

**Example Input**: `{"apple": 1, "banana": 2, "orange": 3}`, key: `"banana"`

**Apply these ->**: Dictionary key access, `in` operator, conditionals.

---

### 4. **Merge Two Dictionaries**
**Problem**: Write a function that takes two dictionaries and merges them into a single dictionary. If a key exists in both dictionaries, keep the value from the second dictionary. For example, `{"a": 1, "b": 2}` and `{"b": 3, "c": 4}` should return `{"a": 1, "b": 3, "c": 4}`.

**Hint**: Use a loop or the `update()` method.

**Apply these ->**: Dictionary merging, `update()`, loops.

---

### 5. **Find the Key with Maximum Value**
**Problem**: Write a function that takes a dictionary with numeric values and returns the key associated with the maximum value. For example, `{"apple": 5, "banana": 2, "orange": 7}` should return `"orange"`.

**Hint**: Iterate through the dictionary and track the key with the highest value. Use `items()` method and try to iterate between keys and lists, see if you can use an if condition to find key based on value.

**Apply these ->**: for loop, if-else, `items()` method.

---

### 6. **Filter Dictionary by Value**
**Problem**: Write a function that takes a dictionary and a threshold value, and returns a new dictionary containing only key-value pairs where the value is greater than the threshold. For example, `{"a": 10, "b": 5, "c": 15}` with threshold `7` should return `{"a": 10, "c": 15}`.

**Apply these ->**: Dictionary iteration, conditionals, dictionary comprehension (optional).

---

### 7. **Nested Dictionary Access**
**Problem**: Write a program to create a nested dictionary representing 3 students, with each student having a name and a dictionary of subjects with grades (e.g., `{"math": 90, "science": 85}`). Prompt the user for a student name and subject, then print the corresponding grade or an error message if not found.

**Hint**: Create a Dicntionary with the Student name as Key, create a sub-dictionary for every student that has marks, grades, contact-details of the students.

**Example Structure**: 
```python
{"Sreedhar": {'marks':{
                        'maths':90,
                        "science": 85
                        },
                'grade':'Pass/Fail/Distinction',
                'contact-details':{
                        'phone':123456789,
                        'address':'Hyderabad',
                        'landmark':'DhyanaManoPrasthanam'
                                    }
            },
"Suresh": {'marks':{
                    'maths':90,
                    "science": 85
                    },
                'grade':'Pass/Fail/Distinction',
                'contact-details':{
                        'phone':123456789,
                        'address':'Hyderabad',
                        'landmark':'DhyanaManoPrasthanam'
                                    }
                            }
}
```

**Apply these ->**: Nested dictionaries, key access : get(), input()

---





# Python Functions

### 1. **Search-Find**
**Problem**: Write a function that takes a dictionary and a Key-name as arguments, returns the key-value pair as dictionary if exists or returns the error message 'Key doesnt not exist as shown below.

```python

sample = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}

#function : search(dictioanry,keyName)

Case(1) Input >>> search(sample,'b')
Output >>> {'b':2}

Case(2) Input >>> search(sample,'i')
Output >>> {'i':'KeyNotFound'}

```

**Hint**: see if you find a key in the Dictionary and create a dubdictionary based on key and value being searched.

**Apply these ->**: function, dict.get()


### 2. **word-counter**
**Problem**: Write a function that takes a Text and a String, returns a dictionary of the String and count of number of times the string has been repeated in the Text.

```python
sampleText = 'This is a beautiful day'

search_string = 'a'

>>> searchtext(sampleText,search_string)
{
    'a':3
}

```
