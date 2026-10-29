
# TYPECASTING 

# 1. What is Type Casting:-
# ------------------------
'''Type casting is the process of converting a value from one data type to another data type.
For example, converting an integer (int) into a string (str) or a string into an integer.'''

# Example:-
a = 10
b = str(a)
print(a)       # 10
print(b)       # 10
print(type(a)) # <class 'int'>
print(type(b)) # <class 'str'>
'''
Although both values display as 10, their data types are different.
 a is an integer.
 b is a string.
Type casting means changing a value from one data type to another.'''


# 2. Types of Type Casting:-
# ---------------------------
'''Python type conversion is commonly divided into two categories.

1. Implicit Type Casting
Python automatically converts a value to another compatible type in certain operations.
Example: int to float.

2. Explicit Type Casting
The programmer manually converts a value using functions such as int(), float(), and str().'''

# 3. Implicit Type Casting:-
# --------------------------
'''Implicit type casting happens when Python automatically converts a value from one data type to another during an operation. '''
# Example 1: Integer to Float
a = 10
b = 2.5
result = a + b
print(result)
print(type(result))
'''Output:
12.5
<class 'float'>

Explanation
- a = 10 is an integer.
- b = 2.5 is a float.
- Python converts the integer to a float for the addition.
- The result is 12.5, a float.
'''

# Example 2: Another Implicit Conversion
a = 5
b = 2.0
print(a * b)
print(type(a * b))

'''Output:
10.0
<class 'float'>'''


# Remember: Implicit conversion does not happen for every combination of data types.
'''
For example:
a = 10
b = "20"
print(a + b)

Output: TypeError
Python cannot directly add an integer and a string. You must explicitly convert one of them.'''


# 4. Explicit Type Casting:-
# --------------------------
'''Explicit type casting happens when the programmer manually converts a value using a conversion function. '''
# For example:-
a = "100"
b = int(a)
print(b)
print(type(b))

'''
Output:
100
<class 'int'>

Here, int() converts the string "100" into the integer 100. '''


# 5. Important Type Casting Functions

# int():-
# -------
'''Convert to integer'''
print(int("25"))
print(int(8.9))

'''
Output:
25
8

int() removes the fractional part of a float; it does not round to the nearest integer.'''



# float():-
# ----------
'''Convert to float'''
print(float("12.5"))
print(float(10))

'''
Output:
12.5
10.0'''


# str():-
# --------
'''Convert to string'''
print(str(100))
print(str(5.5))
'''
Output:
100
5.5
Both results are strings.'''



# bool():-
# ---------
'''Convert to Boolean'''
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Hello"))
'''
Output:
True
False
False
True

Zero, empty strings, and other empty collections are false-like. Non-empty strings are true-like, even "False".'''



# list():-
# ---------
'''Convert an iterable to a list'''
print(list("abc"))
print(list((1, 2, 3)))

'''
Output:
['a', 'b', 'c']
[1, 2, 3]
'''

# tuple():-
# --------
'''Convert an iterable to a tuple'''
print(tuple([1, 2, 3]))
# Output:(1, 2, 3)





# set():-
# -------
'''Convert an iterable to a set'''
print(set([1, 2, 2, 3]))
'''Example output: {1, 2, 3}

A set removes duplicate values; its display order is not guaranteed.'''


# dict():-
# -------
'''Create a dictionary'''
pairs = [("name", "Ravi"), ("age", 20)]
print(dict(pairs))

'''Output: {'name': 'Ravi', 'age': 20}
The input must contain valid key-value pairs.'''




'''
6. Type Casting Between Common Data Types
-----------------------------------------
Conversion	                Example	            Result
String → Integer	        int("50")	        50
String → Float	            float("5.5")	    5.5
Integer → Float	            float(10)	        10.0
Integer → String	        str(25)	            "25"
Float → Integer	            int(7.9)	        7
List → Tuple	            tuple([1, 2])	    (1, 2)
Tuple → List	            list((1, 2))	    [1, 2]
List → Set	                set([1, 1, 2])	    {1, 2}

'''

# 7. Type Casting in User Input:-
# --------------------------------
'''This is one of the most important practical uses of type casting.
In Python, the input() function returns a string, even if the user enters a number.  '''
# Incorrect example
a = input("Enter first number: ")
b = input("Enter second number: ")
print(a + b)
'''Suppose the user enters 10 and 20.

Output: 1020
Why? Because Python concatenates two strings instead of adding two integers.  '''

# Correct example
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)
'''
Input:
Enter first number: 10
Enter second number: 20

Output:30'''


# 8. Common Type Casting Errors
'''Error 1: Converting an invalid string to an integer'''
# x = int("hello")
# print(x)
'''
Result: ValueError
Python cannot convert "hello" into an integer.'''


'''Error 2: Converting a decimal string directly to an integer
x = int("12.5")

Result: ValueError

Correct approach:
x = int(float("12.5"))
print(x)
# Output: 12 

This first converts the string to 12.5, then truncates it to 12.
'''

# Error 3: Mixing incompatible types
'''
print(10 + "20")

Result: TypeError

Correct approach:
print(10 + int("20"))

Output: 30'''



'''9. Type Casting vs Type Checking
These are different concepts.
Type Casting	                      Type Checking
Converts a value to another type	Identifies a value's type
Uses int(), str(), float(), etc.	Uses type() or isinstance()
Example: int("10")	                Example: type(10)'''

# Example:
x = "100"
print(type(x))
x = int(x)
print(type(x))
'''
Output:
<class 'str'>
<class 'int'>'''


#  SOME EXTRA EXAMPLES 

''' int():- 
we can convert a number into --> (string, float, boolean, complex)'''
# examples:-
no = 123
print(str(no))        #op:- 123
print(bool(no))       #op:- True
print(float(no))      #op:- 123.0
print(complex(no))    #op:- 123+oj
print(complex(no,no)) #op:- 123+123j

''' instead of these datatypes , if we try to convert the number into anyother datatype like LIST, Tuple, Set, Dictionary 
it will raises an error.
# examples:-
no = 123
print(list(no))
print(tuple(no))
print(set(no))
print(dict(no))

op:-  TypeError: 'int' object is not iterable

'''

# float:-
'''we can convert a float into --> (string, number, boolean, complex)'''
# examples:-
s = 24.20
print(str(s))        #op:- 24.2
print(int(s))        #op:- 24
print(bool(s))       #op:- True
print(complex(s))    #op:- 24.2+0j


''' instead of these datatypes , if we try to convert the float into anyother datatype like LIST, Tuple, Set, Dictionary 
it will raises an error.
# examples:-
s = 24.20
print(list(s))
print(tuple(s))
print(set(s))
print(dict(s))

op:-  TypeError: 'int' object is not iterable

'''

# boolean:-
'''we can convert a boolean into --> (string, number, float, complex)'''
# example:-
s = True
print(str(s))         #op:- True
print(int(s))         #op:- 1
print(float(s))       #op:- 1.0
print(complex(s))     #op:- (1+0j)

''' instead of these datatypes , if we try to convert the float into anyother datatype like LIST, Tuple, Set, Dictionary 
it will raises an error.
# examples:-
s = True
print(list(s))
print(tuple(s))
print(set(s))
print(dict(s))

op:-  TypeError: 'int' object is not iterable

'''

# complex:-
'''we can only convert a complex into --> (string, boolean)'''
# examples:-
s = 2 + 3j
print(str(s))       #op;- (2+3j)
print(bool(s))      #op:- True

''' instead of these two datatypes , if we try to convert the complex into anyother datatype like LIST, Tuple, Set, Dictionary, int, float
it will raises an error.
# examples:-
s = 2 + 3j
print(list(s))
print(tuple(s))
print(set(s))
print(dict(s))
print(int(s))
print(float(s))

op:-  TypeError: 'int' object is not iterable

'''

# LIST typecasting:-
# ------------------
''' It takes boolean, string, tuple, set, and also dictionary .
But for dictionary (we have to pass two values contains of list / tuple / set .)'''
# examples:-
lst = [['a',1],["b",2],["c",3]]
print(dict(lst))
# op:- {'a': 1, 'b': 2, 'c': 3}

lst = [("a",1),("b",2),('c',3)]
print(dict(lst))
# op:- {'a': 1, 'b': 2, 'c': 3}

lst = [{"a",1},{"b",2},{'c',3}]
print(dict(lst))
# op:- {1: 'a', 2: 'b', 'c': 3}

'''error

lst = [{"a":1},{"b":2},{"c":3}]
print(dict(lst))

lst = [['a',1],["b",2],["c",3, 4]]

lst = [("a",1),("b",2,3),('c',3)]
op:- ValueError: dictionary update sequence element #0 has length 1; 2 is required

'''

# TUPLE typecasting:-
# --------------------
''' It takes boolean, string, list, set, dictionary, 
But for dictionary (we have to pass two values contains of list / tuple / set .)'''


# SET typecasting:-
# -----------------
''' It takes boolean, string, list, dictionary
but for dictionary (we pass tuple of 2 values)'''


# DICTIONARY typecasting:-
# ------------------------
''' It go with boolean, string, list, tuple, set 
--> list, tuple, set by default stores all the keys .
--> if we want to store both value and key then we use values() or items() '''
# examples:-
d = {"a":1,"b":2,"c":3}
print(str(d))
# op:- {'a': 1, 'b': 2, 'c': 3}

print(list(d))   
#op:- ['a', 'b', 'c']

print(tuple(d))
# op:- ('a', 'b', 'c')

print(set(d))
# op:- {'b', 'c', 'a'}

print(d.values())
# op:- dict_values([1, 2, 3])

print(d.items())
# op:- dict_items([('a', 1), ('b', 2), ('c', 3)])


















