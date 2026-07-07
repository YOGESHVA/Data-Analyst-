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
# Day 8 – Conditional Statements in Python

## 📚 Topics Covered

### 1. Python Statements

Python statements are categorized into three main types:

* **Conditional Statements** – `if`, `elif`, `else`
* **Control Statements** – `break`, `continue`, `pass`
* **Looping Statements** – `for`, `while`

Today, I focused on **Conditional Statements**.

---

## 2. `if` Statement

The `if` statement executes a block of code only when the given condition is `True`.

Example:

* Checking whether a number is even or odd.

```python
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## 3. Nested `if` Statement

A nested `if` is an `if` statement inside another `if` statement.

Example:

* Validating an ATM PIN by checking:

  * PIN length
  * Correct PIN value

This helped me understand how multiple conditions can be checked step by step.

---

## 4. `elif` Statement

The `elif` statement is used to evaluate multiple conditions.

Example:

* Grade calculation based on marks.

```python
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B+")
else:
    print("Fail")
```

---

## 5. Practice Programs

### ✔ Even or Odd Number

Used `if...else` to determine whether a number is even or odd.

### ✔ ATM PIN Validation

Created a simple ATM PIN verification program using nested `if`.

### ✔ Student Grade Calculator

Used multiple `elif` conditions to assign grades.

### ✔ Vowel or Consonant

Checked whether a user-entered character is a vowel or consonant.

### ✔ Maximum of Four Numbers

Compared four numbers using conditional statements to find the largest value.

---

## 🎯 Key Takeaway

Conditional statements allow programs to make decisions based on different situations. Understanding `if`, `elif`, `else`, and nested `if` is essential for building interactive applications and solving real-world programming problems.

---

✅ Day 8 completed successfully as part of my **#100DaysOfDataAnalyst** journey.

# Day 9 – Loops and Control Statements in Python

## 📚 Topics Covered

### 1. Loops in Python

Loops are used to execute a block of code repeatedly without writing the same code multiple times.

Python provides two types of loops:

* **for loop**
* **while loop**

---

## 2. For Loop

The `for` loop is used to iterate over a sequence such as:

* Strings
* Lists
* Tuples
* Dictionaries
* Ranges

### Examples Practiced

* Iterating through a string character by character.
* Iterating through a list and printing even numbers.
* Iterating through a tuple.
* Iterating through dictionary keys using `keys()`.

---

## 3. `else` with `for` Loop

The `else` block executes after the loop finishes normally.

If the loop is terminated using `break`, the `else` block will not execute.

---

## 4. Control Statements

### `break`

* Immediately exits the loop.

### `continue`

* Skips the current iteration and moves to the next one.

### `pass`

* Acts as a placeholder when no action is required.

---

## 5. `range()` Function

The `range()` function generates a sequence of numbers.

Syntax:

```python
range(start, stop, step)
```

Examples practiced:

* Printing numbers from 1 to 10.
* Printing even numbers using `range()`.

---

## 6. While Loop

The `while` loop executes as long as the given condition is `True`.

Example:

* Printing numbers using a counter variable.
* Understanding the importance of updating the loop variable to avoid infinite loops.

---

## 7. `assert` Statement

The `assert` statement checks whether a condition is `True`.

If the condition is `False`, Python raises an `AssertionError`.

Example:

* Validating that a user's age is at least 18.

---

## Practice Programs

✔ Printing characters from a string.

✔ Printing even numbers using a `for` loop.

✔ Iterating through tuples and dictionaries.

✔ Using `break`, `continue`, and `pass`.

✔ Generating number sequences using `range()`.

✔ Printing numbers using a `while` loop.

✔ Understanding `assert` for condition validation.

---

## 🎯 Key Takeaway

Loops are essential for automating repetitive tasks, while control statements like `break`, `continue`, and `pass` provide greater flexibility in managing program flow. Mastering loops is a fundamental step toward solving programming problems efficiently.

---

✅ Day 9 completed successfully as part of my **#100DaysOfDataAnalyst** journey.
# Day 10 – Prime Numbers, Armstrong Numbers, and Pattern Programs

## 📚 Topics Covered

### 1. Prime Number

A prime number is a number that has exactly two factors: **1** and itself.

### Concepts Learned

* Finding whether a number is prime.
* Counting the number of factors using loops.
* Using nested loops to generate all prime numbers within a given range.

Example:

* Check if a number is prime.
* Print all prime numbers from **1 to 20**.

---

## 2. Nested Loops

Practiced nested `for` loops to solve different programming problems.

### Pattern Programs

#### Star Pattern

```text
*
* *
* * *
* * * *
* * * * *
```

#### Repeating Number Pattern

```text
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

#### Sequential Number Pattern

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

#### Continuous Number Pattern

```text
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

#### Reverse Pattern

```text
1 2 3 4
1 2 3
1 2
1
```

---

## 3. Armstrong Number

An Armstrong number is a number that is equal to the sum of its digits raised to the power of the total number of digits.

Example:

153

* 1³ + 5³ + 3³ = 153

Concepts practiced:

* Converting numbers to strings.
* Finding the length of a number.
* Using loops to calculate the sum of powers.
* Verifying whether a number is an Armstrong number.

---

## 4. Pyramid Star Pattern

Created a centered pyramid using nested loops.

Example:

```text
    *
   ***
  *****
 *******
*********
```

---

## 🎯 Key Takeaway

Today's practice strengthened my understanding of nested loops, conditional logic, and mathematical programming. Solving prime number, Armstrong number, and pattern problems improved my problem-solving skills and helped me understand how loops can be used to solve real-world programming challenges.

---

✅ Day 10 completed successfully as part of my **#100DaysOfDataAnalyst** journey.
# Day 11 – Python Problem Solving

## 📚 Topics Covered

Today, I practiced solving common Python programming problems to strengthen my understanding of loops, conditional statements, and logical thinking.

---

## 1. Palindrome

A palindrome is a word or number that reads the same forwards and backwards.

### Methods Practiced

* Reversing a string using a `for` loop.
* Reversing a string using Python slicing (`[::-1]`).

Examples:

* `madam`
* `level`
* `radar`

---

## 2. Fibonacci Series

The Fibonacci sequence is a series in which each number is the sum of the previous two numbers.

Example:

```text
0 1 1 2 3 5 8 13 21 ...
```

Concepts Learned:

* Variable swapping.
* Looping through a sequence.
* Generating Fibonacci numbers up to a given limit.

---

## 3. Simple Calculator

Built a menu-driven calculator using conditional statements.

Operations included:

* Addition
* Subtraction
* Multiplication
* Exponentiation
* Division

This helped me understand how to create interactive programs using user input.

---

## 4. Multiplication Table

Generated the multiplication table of a user-entered number using a `for` loop.

Example:

```text
5 × 1 = 5
5 × 2 = 10
...
5 × 10 = 50
```

---

## 5. Perfect Number

A perfect number is a positive integer that is equal to the sum of its proper factors (excluding itself).

Example:

```text
6

Factors: 1, 2, 3

1 + 2 + 3 = 6
```

Concepts Learned:

* Finding factors using loops.
* Summing factors.
* Comparing the result with the original number.

---

## 🎯 Key Takeaway

Today's practice focused on improving logical thinking and problem-solving skills. By solving classic programming problems such as palindrome checking, Fibonacci series generation, calculator implementation, multiplication tables, and perfect number verification, I strengthened my understanding of loops, conditions, and algorithm design.

---

✅ Day 11 completed successfully as part of my **#100DaysOfDataAnalyst** journey.
# Day 12 – Functions in Python

## 📚 Topics Covered

Today, I learned about **Functions** in Python and how they help organize, reuse, and simplify code.

---

## 1. What is a Function?

A function is a reusable block of code that performs a specific task.

### Benefits of Functions

* Improves code reusability.
* Reduces duplicate code.
* Makes programs easier to read and maintain.
* Breaks large problems into smaller, manageable parts.

---

## 2. Types of Functions

### Built-in Functions

Python provides many built-in functions, such as:

* `print()`
* `type()`
* `max()`
* `min()`
* `sum()`

### User-Defined Functions

Functions created by the programmer using the `def` keyword.

Example:

```python
def add(a, b):
    print(a + b)

add(3, 4)
```

---

## 3. Types of Function Arguments

### Required (Positional) Arguments

Arguments must be passed in the correct order and with the required count.

Example:

```python
add(3, 6)
```

---

### Keyword Arguments

Arguments are passed using parameter names.

Example:

```python
add(a=4, b=5)
```

---

### Default Arguments

Parameters are assigned default values that are used if no argument is provided.

Example:

```python
def greet(name="Guest"):
    print(name)
```

---

### Variable-Length Arguments

Used when the number of arguments is unknown.

#### `*args`

* Accepts multiple positional arguments.
* Stores them as a tuple.

Example:

```python
def add(*numbers):
    print(numbers)
```

#### `**kwargs`

* Accepts multiple keyword arguments.
* Stores them as a dictionary.

Example:

```python
def details(**info):
    print(info["Age"])
```

---

## 4. Variable Scope

### Global Variable

A variable declared outside a function can be accessed throughout the program.

### Local Variable

A variable declared inside a function can only be accessed within that function.

### Global Keyword

The `global` keyword allows a function to modify a global variable.

Example:

```python
num = 9

def fun():
    global num
    num = 77
```

---

## 🎯 Key Takeaway

Functions make programs modular, reusable, and easier to maintain. Understanding different types of arguments and variable scope is essential for writing clean, efficient, and scalable Python code.

---

✅ Day 12 completed successfully as part of my **#100DaysOfDataAnalyst** journey.
# Day 13 – Return Statement and Recursive Functions in Python

## 📚 Topics Covered

Today, I learned about the **`return` keyword**, explored Python's **built-in functions**, and understood the basics of **recursive functions**.

---

## 1. Return Statement

The `return` keyword is used to send a value back from a function to the place where it was called.

### Why use `return`?

* Returns the result of a function.
* Ends the execution of the function immediately.
* Allows the returned value to be stored in a variable or used in another expression.

Example:

```python
def myfunc(n):
    return 5 + n

result = myfunc(10)
print(result)
```

Output:

```text
15
```

---

## 2. Python Built-in Functions

Python provides many built-in functions that simplify programming tasks.

Example:

```python
import builtins

built_function = [
    name for name in dir(builtins)
    if callable(getattr(builtins, name))
]

print(built_function)
```

This program lists all callable built-in functions available in Python.

Some commonly used built-in functions include:

* `print()`
* `input()`
* `len()`
* `type()`
* `sum()`
* `max()`
* `min()`
* `abs()`
* `sorted()`
* `range()`

---

## 3. Recursive Functions

A recursive function is a function that calls itself until a stopping condition (base case) is reached.

### Basic Structure

```python
def function_name(parameter):
    if base_case:
        return value
    else:
        return function_name(updated_parameter)
```

### Why Recursion?

Recursion is commonly used to solve problems that can be broken down into smaller versions of the same problem, such as:

* Factorial calculation
* Fibonacci series
* Tree traversal
* Searching and sorting algorithms

---

## 🎯 Key Takeaway

The `return` statement makes functions more useful by allowing them to produce reusable results. Exploring Python's built-in functions helped me understand the language's powerful features, while recursion introduced a new way of solving repetitive problems using self-calling functions.

---

✅ Day 13 completed successfully as part of my **#100DaysOfDataAnalyst** journey.










