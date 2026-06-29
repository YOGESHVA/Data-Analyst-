# Day 1 – Introduction to Python Fundamentals

Today I learned the basic concepts of Python programming and understood how Python works.

## Topics Covered

### 1. Programming Paradigms

* Procedural Programming

  * Step-by-step execution.
  * Code is organized into functions or procedures.
  * Example: C language.

* Object-Oriented Programming (OOP)

  * Based on objects and classes.
  * Helps organize and manage code efficiently.

### 2. Objects and Memory Management

* Used `id()` function to understand memory locations.
* Learned that objects are created and stored in memory.
* Used `type()` to identify data types.

### 3. Features of Python

* Dynamically Typed Language.
* Interpreted Language.
* High-Level Language.
* Cross-platform support.
* Large library ecosystem.

### 4. Python History

* Python was created by Guido van Rossum.
* First released in 1991.

### 5. Tokens in Python

* Keywords
* Identifiers
* Literals
* Operators
* Punctuators

### 6. Variables and Naming Rules

* Valid and invalid variable names.
* Rules for creating variables.

### 7. Comments

* Single-line comments (`#`)
* Multi-line comments (`''' '''` and `""" """`)

### 8. Boolean Values

* Understanding True and False.
* Comparison operators.

## Conclusion

Day 1 focused on understanding Python fundamentals, programming concepts, variables, tokens, comments, and basic data types.

# Day 2 – Python Operators

Today I learned different types of operators in Python and how they are used in real-world programming.

## Topics Covered

### 1. Arithmetic Operators

* Addition (+)
* Subtraction (-)
* Multiplication (*)
* Division (/)
* Floor Division (//)
* Modulus (%)
* Exponent (**)

### 2. Assignment Operators

* =
* +=
* -=
* *=
* %=
* //=

These operators help update variable values efficiently.

### 3. Comparison Operators

* ==
* !=
* >
* <
* > =
* <=

Used for comparing values and making decisions in programs.

### 4. Logical Operators

* and
* or
* not

Used to combine multiple conditions.

### 5. Identity Operators

* is
* is not

Learned the difference between:

* `==` → compares values.
* `is` → compares memory locations (objects).

### 6. Membership Operators

* in
* not in

Used to check whether a value exists inside a sequence such as a list.

### 7. Bitwise Operators

* &
* |
* ^
* ~
* <<
* > >

Learned how binary operations work and how left shift and right shift operators perform multiplication and division operations.

## Key Learnings

* Operators are essential for calculations and decision-making.
* Identity operators compare objects rather than values.
* Bitwise operators work directly with binary numbers.
* Logical operators help create complex conditions.

# Day 3 – Python Data Types and String Operations

## 📚 Topics Covered

### 1. Data Types in Python

Data types define the type of data that can be stored in a variable.

#### Numeric Data Types

* Integer (`int`)
* Float (`float`)

Example:

```python
num = 8
num_2 = 7.89
```

### 2. Floor Division (`//`)

The floor division operator returns the quotient as the nearest whole number.

Example:

```python
num = 6.89
print(num // 2)
```

### 3. Strings in Python

A string is a sequence of characters enclosed in single quotes (`' '`) or double quotes (`" "`).

Features:

* Strings are immutable (cannot be modified directly).
* Strings support concatenation using the `+` operator.

Example:

```python
so = "Python"
any_ = " is a Language"
print(so + any_)
```

### 4. String Indexing

Indexing allows us to access individual characters in a string.

* Positive indexing starts from `0`.
* Negative indexing starts from `-1`.

Example:

```python
so = "Python is a Language"
print(so[3])
print(so[-1])
```

### 5. String Methods

#### replace()

Replaces old text with new text.

```python
so.replace("python", "Java")
```

#### join()

Joins characters or strings using a separator.

```python
"-".join(so)
```

#### split()

Splits a string into a list.

```python
so.split()
```

#### count()

Counts the occurrences of a substring.

```python
so.count("a")
```

### 6. Built-in String Functions

* `len()` – Returns the length of the string.
* `max()` – Returns the maximum character.
* `min()` – Returns the minimum character.

Example:

```python
len(so)
max(so)
min(so)
```

## 🎯 Key Takeaway

Understanding data types and string operations is essential because strings play a major role in data cleaning, text processing, and real-world data analysis tasks. Learning string methods and built-in functions helps write efficient and readable Python code.

---

✅ Day 3 completed successfully as part of my #100DaysOfDataAnalyst journey.

# Day 4 – Python Lists and Tuples

## 📚 Topics Covered

### 1. Lists in Python

A list is a collection of different data types enclosed in square brackets `[]` and separated by commas.

Example:

```python
all_type = [1, 'Python', [1, 2]]
```

### Key Features of Lists:

* Ordered collection.
* Can store multiple data types.
* Mutable (values can be modified).
* Supports indexing and slicing.

---

## List Methods

### append()

Adds a single element to the end of the list.

```python
numbers = [1, 2, 3, 4]
numbers.append(5)
```

### extend()

Adds multiple elements to the list.

```python
numbers.extend([10, 20])
```

### pop()

Removes an element based on its index position.

```python
numbers.pop(2)
```

### remove()

Removes the specified value from the list.

```python
numbers.remove(4)
```

### Indexing

Accessing elements using index positions, including nested lists.

```python
any = [1, 2, 'Python', [45, 78, 'Java', [1, 23], 90]]
print(any[3][3][1])
```

---

## Mutable vs Immutable

### Mutable Data Types

* List
* Dictionary
* Set

Their values can be modified after creation.

### Immutable Data Types

* String
* Tuple

Their values cannot be changed after creation.

---

## 2. Tuples in Python

A tuple is a collection of different data types enclosed in parentheses `()`.

Example:

```python
how = (1, 2, 3, 4, "Python", [4, 5, 'yogi'], (90, 60))
```

### Features of Tuples:

* Ordered collection.
* Immutable.
* Faster than lists.
* Allows duplicate values.

---

## Tuple Methods

### index()

Returns the index position of an element.

```python
how.index("Python")
```

### count()

Counts the number of occurrences of a value.

```python
how.count(3)
```

### len()

Returns the total number of elements.

```python
len(how)
```

---

## 🎯 Key Takeaway

Lists are useful when data needs to be modified, while tuples are ideal for storing fixed data that should remain unchanged. Understanding these collection data types is essential for data manipulation and analysis in Python.

---

✅ Day 4 completed successfully as part of my #100DaysOfDataAnalyst journey.
# Day 5 – Python Dictionaries and Sets

## 📚 Topics Covered

### 1. Dictionaries in Python

A dictionary is a collection of key-value pairs separated by a colon (`:`). Each key must be unique and should use immutable data types.

Example:

```python
details = {
    "Name": "Teja",
    "Age": 56,
    "Gender": "Male"
}
```

### Features of Dictionaries:

* Stores data as key-value pairs.
* Keys are unique.
* Mutable data structure.
* Fast data retrieval using keys.

---

## Dictionary Methods

### `keys()`

Returns all the keys in the dictionary.

```python
details.keys()
```

### `values()`

Returns all the values in the dictionary.

```python
details.values()
```

### `items()`

Returns key-value pairs as tuples.

```python
details.items()
```

### `clear()`

Removes all elements from the dictionary.

```python
details.clear()
```

### `update()`

Adds or updates key-value pairs.

```python
details.update({"mob": "234566"})
```

---

## 2. Sets in Python

A set is a collection of unique elements enclosed in curly braces `{}`.

Example:

```python
numbers = {1, 2, 3, 4}
```

### Features of Sets:

* Stores unique values.
* Automatically removes duplicate elements.
* Mutable data structure.
* Unordered collection.

---

## Set Operations

### `union()`

Combines elements from both sets.

```python
set1.union(set2)
set1 | set2
```

### `intersection()`

Returns common elements between sets.

```python
set1.intersection(set2)
```

### `symmetric_difference()`

Returns elements that are present in either set but not in both.

```python
set1.symmetric_difference(set2)
set1 ^ set2
```

---

## Set Methods

### `add()`

Adds a new element to the set.

```python
numbers.add(7)
```

### `pop()`

Removes and returns a random element from the set.

```python
numbers.pop()
```

### `discard()`

Removes a specified element without raising an error if the element is not present.

```python
numbers.discard(2)
```

---

## 🎯 Key Takeaways

* Dictionaries organize data using key-value pairs.
* Keys must be unique and immutable.
* Sets automatically remove duplicate values.
* Set operations such as union and intersection are useful for data analysis.
* Dictionaries and sets are widely used in Python programming and real-world data processing.

---

✅ Day 5 completed successfully as part of my **#100DaysOfDataAnalyst** journey.
# Day 6 – Python Type Conversion

## 📚 Topics Covered

### What is Type Conversion?

Type conversion is the process of converting one data type into another data type.

Python provides several built-in functions for type conversion.

---

## Numeric Type Conversion

### Float to String

```python
num = 8.9
text = str(num)
```

### Float to Integer

```python
num = 8.9
value = int(num)
```

The decimal part is removed during integer conversion.

---

## String Conversion

### String to Integer

```python
value = "38"
num = int(value)
```

Only numeric strings can be converted into integers.

### String to Float

```python
value = "67.8"
num = float(value)
```

### String to List

```python
text = "12345"
result = list(text)
```

### String to Tuple

```python
text = "12345"
result = tuple(text)
```

---

## List Conversion

### List to String

```python
letters = ['p', 'y', 't', 'h', 'o', 'n']
text = "".join(letters)
```

### List to Tuple

```python
letters = ['p', 'y', 't', 'h', 'o', 'n']
result = tuple(letters)
```

### List to Dictionary

```python
data = [('a', 1), ('b', 2)]
result = dict(data)
```

---

## Tuple Conversion

### Tuple to List

```python
numbers = (1, 2, 3, 4)
result = list(numbers)
```

### Tuple to String

```python
letters = ('y', 'o', 'g', 'e', 's', 'h')
name = "".join(letters)
```

---

## Built-in Functions Learned

* `str()`
* `int()`
* `float()`
* `list()`
* `tuple()`
* `dict()`

---

## 🎯 Key Takeaway

Type conversion helps transform data from one type to another, making data processing easier and more flexible. Understanding type casting is important for data cleaning, user input handling, and data analysis tasks.

---

✅ Day 6 completed successfully as part of my **#100DaysOfDataAnalyst** journey.







