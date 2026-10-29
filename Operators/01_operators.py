# OPERATOR IN PYTHON
# -------------------
''' An operator is a symbol or keyword used to perform an operation on variables and values .
--> There are several types of operators in python .
    1. ARITHMATIC OPERATORS (+, -, *, /, //, **, %) .
    2. RELATIONAL AND COMPARISION OPERATORS (>, <, >=, <=, ==, !=)
    3. LOGICAL OPERATORS (AND, OR, NOT)
    4. MEMBERSHIP OPERSTORS (IN, NOT IN)
    5. ASSIGNMENT OPERATORS (+=, -=, *=, /=, //=, **=, ^=, %=, &=, |=, >>=, <<= )
    6. IDENTITY OPERATORS (IS , IS NOT)
    7. BITWISE OPERATORS (AND(&), OR(|), NOT(~), XOR(^), LEFT SHIFT(<<), RIGHT SHIFT(>>))   '''


# 1. ARITHMATIC OPERATORS (+, -, *, /, //, **, %) .
# -------------------------------------------------
''' Arithmetic operators are operators used to perform mathematical calculations such as addition, subtraction, multiplication, and division.

Types of Arithmetic Operators
------------------------------
Python has 7 main arithmetic operators.
No.	            Operator	        Name
--------------------------------------------
1	            +	               Addition
2	            -	               Subtraction
3	            *	               Multiplication
4	            /	               Division
5	            %	               Modulus
6	            //	               Floor Division
7	            **	               Exponentiation
'''

# 1. Addition Operator (+)
# --------------------------
''' The addition operator is used to add two or more values.'''
# examples:-
a = 10
b = 20

print(a + b)    #op:-  30

'''
Explanation:
- a = 10
- b = 20
- a + b means 10 + 20.
- The result is 30.      '''

'''Important point:- The + operator can also concatenate (join) strings. '''
# example:-
first_name = "Rajesh"
last_name = "Gouda"

print(first_name + " " + last_name)    #op:- Rajesh Gouda

# ex-2
print([1, 2, 3] + [4, 5, 6])



# 2. Subtraction Operator (-):-
# -----------------------------
''' The subtraction operator is used to subtract one value from another.'''
# examples:-
a = 50
b = 20

print(a - b)   #op:- 30

# In set()  (-) means difference
# ex:-
print({1, 2, 3} - {3, 4, 5, 6})


# 3. Multiplication Operator (*):-
# --------------------------------
''' The multiplication operator is used to multiply two or more values.'''
# examples:-
a = 10
b = 5

print(a * b)   #op:- 50

# also we can use it replication for example ....
print("hii" * 3)
print([1,2,3] * 3)

'''Remember: In Python, use * for multiplication, not ×.'''



# 4. Division Operator (/):-
# -------------------------
''' The division operator is used to divide one value by another. It returns a floating-point result.'''
# examples:-
a = 10
b = 2

print(a / b)     #op:- 5.0

'''Notice that Python returns 5.0, not 5, because / returns a floating-point result.'''

# ex-2
print(10 / 3)
# op:- 3.3333333333333335

'''Important: Dividing by zero raises a ZeroDivisionError.

print(10/0)
This code produces an error because division by zero is not allowed.  '''


# 5. Modulus Operator (%):-
# ------------------------
''' The modulus operator returns the remainder after dividing one number by another.'''
# examples:-
a = 10
b = 3

print(a % b)      #op:- 1

'''Explanation:

When we divide 10 by 3:
- Quotient = 3
- Remainder = 1
Therefore, 10 % 3 returns 1.  '''

'''Real-life programming example: Even or odd  '''
num = 7
if num % 2 == 0:    
    print("Even")
else:    
    print("Odd")

# op:-odd

'''Why?
- Even numbers leave a remainder of 0 when divided by 2.
- Odd numbers leave a remainder of 1 when divided by 2.   '''


# 6. Floor Division Operator (//):-
''' The floor division operator divides one number by another and rounds the result down to the nearest whole integer when both operands are integers.'''
# examples:-
a = 10
b = 3

print(a // b)

'''Explanation:
10 / 3 = 3.3333...

But:  10 // 3 = 3     '''

# Important difference between / and //
print(10 / 3)
print(10 // 3)

# Output:
# 3.3333333333333335
# 3


'''Important: Floor division rounds down, not simply towards zero.'''
# For example:-
print(-10 // 3)

# Output: -4

''' Because -4 is the greatest integer less than or equal to -3.3333....'''


# 7. Exponentiation Operator (**):-
# --------------------------------
'''Definition: The exponentiation operator raises a number to the power of another number .'''
# examples:-
a = 2
b = 3

print(a ** b)      #op:-   8

'''
Explanation:
2 ** 3 means: 2 × 2 × 2 = 8  '''

# More examples:
print(2 ** 2)
print(3 ** 3)
print(5 ** 2)

# Output:
4
27
25

'''Remember: In Python, ** means power, while ^ is a bitwise XOR operator.'''



# 2. RELATIONAL AND COMPARISION OPERATORS (>, <, >=, <=, ==, !=)
# --------------------------------------------------------------
'''  Relational or Comparison Operators are operators used to compare two values. They return a Boolean result: True or False.

2. Types of Comparison Operators
---------------------------------
Python has six main comparison operators.

Operator	           Name	                                Example	Output
----------         ------------                          ------------------
    >	            Greater than	                        10 > 5	True
    <	            Less than	                            5 < 10	True
    >=	            Greater than or equal to	            10 >= 10  True
    <=	            Less than or equal to	                5 <= 5	True
    ==	            Equal to	                            10 == 10  True
    !=	            Not equal to	                        10 != 5	True

'''

# 1. Greater Than (>):-
# ---------------------
''' Checks whether the left value is greater than the right value.'''
a = 10
b = 5
print(a > b)
print(b > a)

'''
Output:
True
False'''

'''Explanation:
- 10 > 5 → True
- 5 > 10 → False'''


# 2. Less Than (<):-
# ------------------
''' Checks whether the left value is smaller than the right value.'''
# examples:-
a = 10
b = 5
print(b < a)
print(a < b)

'''
Output:
True
False'''


# 3. Greater Than or Equal To (>=):-
# ----------------------------------
''' Checks whether the left value is greater than or equal to the right value.'''
a = 10
print(a >= 5)
print(a >= 10)
print(a >= 15)
'''
Output:
True
True
False'''

'''  Remember: >= means greater than OR equal to.'''


# 4. Less Than or Equal To (<=):-
# -------------------------------
'''Checks whether the left value is smaller than or equal to the right value.'''
a = 10
print(a <= 5)
print(a <= 10)
print(a <= 15)

'''Output:
False
True
True'''


# 5. Equal To (==):-
# -------------------
''' Checks whether two values are equal.'''
a = 10
b = 10
c = 20
print(a == b)
print(a == c)

'''Output:
True
False'''

'''Important difference:
------------------------
- = → Assigns a value to a variable.
- == → Compares two values.
age = 23
print(age == 23) 
Output: True'''


# 6. Not Equal To (!=):-
# ----------------------
''' Checks whether two values are different.'''
a = 10
b = 20
print(a != b)
print(a != 10)

'''Output:
True
False'''


# 3. Real-World Example: Checking Eligibility
# Suppose a person must be at least 18 years old to be eligible.
age = 23
print(age >= 18)

'''Output: True'''


# We can use the comparison operator with an if statement:
age = 16
if age >= 18:    
    print("Eligible")
else:    
   print("Not eligible")

# Output: Not eligible


'''4. Important Points to Remember
------------------------------------
- Comparison operators return True or False.
- > means greater than.
- < means less than.
- >= and <= include equality.
- == checks equality.
- != checks inequality.
- Comparison operators are commonly used in if, elif, while, and filtering conditions.'''



'''
1. Relational vs Comparison vs Logical Operators
-------------------------------------------------
Operator type	               What does it do?	                                Examples
-------------               -----------------------------                   -------------------
Relational operators	    Compare two values using a relationship	            >, <, >=, <=
Comparison operators	    Compare values for equality or inequality, too	    >, <, >=, <=, ==, !=
Logical operators	        Combine conditions or reverse a condition	        and, or, not
'''



# 3 .Logical Operators (AND , OR, NOT):-
# -------------------------------------
'''Logical operators are used to combine multiple conditions or reverse a condition's result. They return a Boolean value (True or False) in ordinary Boolean expressions.'''

'''2. Types of Logical Operators
--------------------------------
Python has 3 logical operators.

Operator	                        Meaning	                                  Example
--------                    ---------------------------                  -----------------
  and	                     Both conditions must be true	           True and True → True
  or	                  At least one condition must be true	       True or False → True
  not	                      Reverses the Boolean result	              not True → False      '''


# 1. AND Operator (and):-
# ------------------------
'''The and operator returns True when both conditions are true. Otherwise, it returns False. '''

'''Truth table

Condition 1 	Condition 2	            Result
-----------     -------------          -------
True	            True	            True
True	            False	            False
False	            True	            False
False	            False	            False       '''

# Example:-
age = 23
print(age >= 18 and age <= 30)

'''Output:  True'''


'''Explanation:
- age >= 18 → True
- age <= 30 → True
- True and True → True  '''


'''Real-world example
Suppose a student must score at least 35 in both subjects to pass.'''
maths = 60 
science = 25
if maths >= 35 and science >= 35:    
    print("Pass")
else:    
    print("Fail")

# Output:  Fail

# Why? The student passed Maths but failed Science. Both conditions must be true.


# 2. OR Operator (or):-
# ---------------------
''' The or operator returns True if at least one condition is true. It returns False only when both conditions are false.
'''
'''Truth table

Condition 1	    Condition 2	    Result
-----------     -----------     --------
True	        True	        True
True	        False	        True
False	        True	        True
False	        False	        False       '''

# Example:-
day = "Sunday"
print(day == "Sunday" or day == "Saturday")

# Output: True


'''Explanation:
- day == "Sunday" → True
- day == "Saturday" → False
- True or False → True       '''


'''Real-world example
A person can enter using either a valid ID card or a valid entry pass.'''
has_id = False
has_pass = True
if has_id or has_pass:    
    print("Entry allowed")
else:    
    print("Entry denied")

# Output: Entry allowed

# Only one condition needs to be true.


# 3. NOT Operator (not):-
''' The not operator reverses a Boolean value: True becomes False, and False becomes True.'''

'''Truth table

Condition	 Result
---------   --------
True	     False
False	     True
'''
# Example 1:-
is_raining = False
print(not is_raining)

# Output: True

# Because is_raining is False, not is_raining becomes True.


# Example 2:-
age = 16
print(not (age >= 18))

# Output: True

'''Explanation:
1. age >= 18 → False
2. not False → True
'''


'''4. Difference between and, or, and not
Operator	   When is the result True?
--------      ----------------------------------
and	           When both conditions are true
or	           When at least one condition is true
not	           When the original Boolean value is false'''

# 5. Combined example:-
age = 23
has_id = True
if age >= 18 and has_id:    
    print("Entry allowed")
else:    
    print("Entry denied")

# Output: Entry allowed


'''Here:
- age >= 18 is a comparison expression.
- and combines the two conditions.
- Since both conditions are true, the result is True. '''

'''Remember: Comparison operators compare values, while logical operators combine or reverse conditions. Python's and and or can also return operands rather than literal Boolean values in some expressions, but in the conditional examples above, they determine whether the conditions are satisfied.'''



# Membership Operators(IN, NOT IN):-
# ----------------------------------
'''Membership operators are used to check whether a value exists or does not exist in a sequence or collection, such as a string, list, tuple, set, or dictionary.'''

'''Python has two membership operators:
Operator	                Meaning
---------               -----------------
  in	               Checks whether a value exists
 not in	           Checks whether a value does not exist'''

# 1. in Operator:-
# -----------------
''' The in operator returns True if the specified value is found in a sequence or collection. Otherwise, it returns False.'''
# Example 1: Using a list
fruits = ["apple", "banana", "mango"]
print("apple" in fruits)
print("grapes" in fruits)

'''
Output:
True
False'''

'''Explanation:
- "apple" in fruits → True, because apple exists in the list.
- "grapes" in fruits → False, because grapes does not exist in the list.  '''


# Example 2: Using a string
name = "Python Programming" 
print("Python" in name)
print("Java" in name)

'''
Output:
True
False'''

'''Here, in checks whether the specified substring exists in the string. String membership is case-sensitive.  '''
# For example:
print("python" in "Python")

# Output:  False
# Because lowercase p and uppercase P are different.


# 2. not in Operator:-
# -------------------
'''The not in operator returns True if the specified value is not found in a sequence or collection. Otherwise, it returns False.
'''
# Example 1: Using a list
fruits = ["apple", "banana", "mango"]
print("grapes" not in fruits)
print("apple" not in fruits)

'''
Output:
True
False'''

'''Explanation:
- "grapes" not in fruits → True, because grapes is absent.
- "apple" not in fruits → False, because apple is present.'''


# Example 2: Using a string:-
# ---------------------------
message = "Welcome to Python"
print("Java" not in message)
print("Python" not in message)

'''
Output:
True
False'''

# 3. Real-World Example
# Suppose you are building a login system and want to check whether a username exists in the registered users list.
users = ["rajesh", "amit", "rahul"]
username = "rajesh"
if username in users:    
    print("User exists")
else:   
    print("User not found")

# Output: User exists

# Now check a username that is not registered:
users = ["rajesh", "amit", "rahul"]
username = "ravi"
if username not in users:    
    print("Please register first")

# Output: Please register first


# 4. Membership Operators with Different Data Types
'''Data type	           Example	                        Output
-------------           -----------------               ---------------
    List	           "a" in ["a", "b"]	                True
    Tuple	            10 in (10, 20, 30)	                True
    Set	                5 in {1, 3, 5}	                    True
    String	            "Py" in "Python"	                True
    Dictionary	        "name" in {"name": "Rajesh"}	    True        '''

'''Important: When using in with a dictionary, Python checks its keys, not its values.'''
student = {"name": "Rajesh", "age": 23}
print("name" in student)
print("Rajesh" in student)

'''
Output:
True
False'''

# "Rajesh" is a value, not a key.

# 5. Difference Between in and not in
'''in	                                       not in
----------------------------         ---------------------------
Checks whether a value exists	   Checks whether a value is absent
Returns True if found	               Returns True if not found
Example: 5 in [1, 5, 9]	              Example: 5 not in [1, 5, 9]
Output: True	                               Output: False              '''



# ASSIGNMENT OPERATORS (+=, -=, *=, /=, //=, **=, ^=, %=, &=, |=, >>=, <<= ):-
# ----------------------------------------------------------------------------
'''Assignment operators are used to assign values to variables or update the values of existing variables. '''
# Examples:-
x = 10
print(x)

# Output: 10
# Here, = is the assignment operator. It assigns the value 10 to the variable x.


'''
2. Types of Assignment Operators
----------------------------------
Python has several assignment operators.

Operator	                Name	                    Example	              Equivalent expression
---------             --------------------             ---------              -----------------------
    =	              Simple assignment	                x = 10	                 Assigns 10 to x
    +=	              Addition assignment	            x += 5	                    x = x + 5
    -=	              Subtraction assignment	        x -= 5	                    x = x - 5
    *=	              Multiplication assignment	        x *= 5	                    x = x * 5
    /=	              Division assignment	            x /= 5	                    x = x / 5
    %=	              Modulus assignment	            x %= 5	                    x = x % 5
    //=	              Floor division assignment	        x //= 5	                    x = x // 5
    **=	              Exponentiation assignment	        x **= 2	                    x = x ** 2
    &=	              Bitwise AND assignment	        x &= 5	                    x = x & 5
    |=	              Bitwise OR assignment	            x |= 5	                    x = x | 5
    ^=	              Bitwise XOR assignment	        x ^= 5	                    x = x ^ 5
    <<=	              Left shift assignment	            x <<= 1	                    x = x << 1
    >>=	              Right shift assignment	        x >>= 1	                    x = x >> 1              '''


# Python also supports @=, :=, and other assignment-related syntax in specific contexts. 

# Let's understand the main operators one by one.

# 1. Simple Assignment Operator (=):-
# ------------------------------------
'''The = operator assigns a value to a variable.'''
# Example:-
name = "Rajesh"
age = 23
print(name)
print(age)

'''
Output:
Rajesh
23'''

'''Here:
- name = "Rajesh" assigns a string to name.
- age = 23 assigns an integer to age.
Remember: = assigns a value; == compares two values.'''


# 2. Addition Assignment Operator (+=):-
# --------------------------------------
'''The += operator adds a value to the existing variable value and assigns the result back to that variable. '''
# examples:-
x = 10
x += 5
print(x)

# Output: 15

'''
Explanation
The statement: x += 5
is equivalent to: x = x + 5  
Calculation: x = 10 + 5 = 15

Therefore, the new value of x is 15.'''




# Real-life example
# Suppose your bank balance is ₹1,000 and you deposit ₹500.
balance = 1000
balance += 500
print(balance)

# Output: 1500


# 3. Subtraction Assignment Operator (-=):-
# ------------------------------------------
'''The -= operator subtracts a value from the existing variable value and assigns the result back to the variable. '''
# examples:-
x = 20
x -= 5
print(x)

# Output:15

'''Explanation
x -= 5
is equivalent to:x = x - 5
Calculation:20 - 5 = 15       '''


# 4. Multiplication Assignment Operator (*=):-
# --------------------------------------------
'''The *= operator multiplies the existing variable value by another value and assigns the result back to the variable. '''
# examples:-
x = 10
x *= 3
print(x)

Output:30

'''Explanation
x *= 3
is equivalent to:x = x * 3
Calculation:10 × 3 = 30     '''


# 5. Division Assignment Operator (/=):-
# --------------------------------------
'''The /= operator divides the existing variable value by another value and assigns the result back to the variable. '''
# examples:-
x = 20
x /= 4
print(x)

# Output:5.0

'''Explanation
x /= 4
is equivalent to:x = x / 4
Calculation:20 / 4 = 5.0    '''
# Important: /= normally produces a floating-point result when applied to numbers.


# 6. Modulus Assignment Operator (%=):-
# --------------------------------------
'''The %= operator calculates the remainder after division and assigns that remainder back to the variable. '''
# examples:-
x = 17
x %= 5
print(x)

# Output:2

'''Explanation
x %= 5
is equivalent to: x = x % 5
Calculation: 17 ÷ 5 leaves a remainder of 2.
Therefore, x = 2.   '''


# 7. Floor Division Assignment Operator (//=):-
# ---------------------------------------------
'''The //= operator performs floor division and assigns the result back to the variable. '''
# Examples:-
x = 17
x //= 5
print(x)

# Output:3

'''Explanation
x //= 5
is equivalent to: x = x // 5
Calculation: 17 // 5 = 3     '''



# 8. Exponentiation Assignment Operator (**=):-
# ----------------------------------------------
'''The **= operator raises the existing variable value to a specified power and assigns the result back to the variable. '''
# examples:-
x = 2
x **= 3
print(x)

# Output: 8

'''Explanation
x **= 3
is equivalent to: x = x ** 3
Calculation: 2 × 2 × 2 = 8'''


# 3. Difference Between = and Compound Assignment Operators
# Look at this example:
x = 10
x = 5
print(x)

# Output: 5
# Here, x = 5 replaces the previous value with 5.

# Now look at this example:
x = 10
x += 5
print(x)

# Output: 15
# Here, x += 5 adds 5 to the existing value of x.

'''
Remember:
- = assigns a value.
- +=, -=, *=, and similar operators update a variable using an operation.'''


'''
4. Quick Revision Table
Operator	 Example	    Initial value	 Final value
=	         x = 10         	—	            10
+=	         x += 5	            10	            15
-=	         x -= 5	            10	            5
*=	         x *= 5	            10	            50
/=	         x /= 5	            10	            2.0
%=	         x %= 3	            10	            1
//=	         x //= 3	        10	            3
**=	         x **= 2	        10	            100                '''




# 6. IDENTITY OPERATORS (IS , IS NOT):-
# --------------------------------------
'''Identity operators are used to check whether two variables refer to the same object in memory. '''
'''
Python has two identity operators:
-----------------------------------
    Operator	                `Meaning
       is	                Checks whether two variables refer to the same object.
     is not	                Checks whether two variables refer to different objects.  '''

'''Important: Identity operators are different from comparison operators. == compares values, whereas is checks object identity. '''


# Identity Operator: is
# ---------------------
'''The is operator returns True if two variables refer to the same object in memory. Otherwise, it returns False. '''

# Example 1: Both variables refer to the same object
a = [10, 20, 30]
b = a
print(a is b)

# Output: True


'''
Explanation

Look at these statements:
a = [10, 20, 30]
b = a

1. We create a list and assign it to a.
2. We assign a to b.
3. Both variables refer to the same list object.
4. Therefore, a is b returns True.

here if we modify anything one of them it will affect each other
'''

# Example 2: Two different objects
a = [10, 20, 30]
b = [10, 20, 30]
print(a is b)

# Output: False

'''
Explanation

Although both lists contain the same values, Python creates two separate list objects.
- a refers to the first list.
- b refers to the second list.
- They have equal values but different identities.
Therefore, a is b returns False

here if we modify anything one of them it will not affect each other .
'''

# 3. Identity Operator: is not
# -----------------------------
'''The is not operator returns True if two variables refer to different objects. Otherwise, it returns False. '''

# Example 1: Different objects
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)

# Output:True
'''Explanation:

Both lists contain the same values, but they are separate objects.
Therefore, a is not b returns True.  
'''

# Example 2: Same object
a = [1, 2, 3]
b = a
print(a is not b)

# Output: False
'''
Explanation:
Both variables refer to the same list object. Therefore, a is not b returns False. '''

# 4. Difference Between == and is
# -------------------------------
'''This is the most important concept to understand.

Comparison operator:-(==)
-------------------------
Compares whether values are equal
Two different lists can return True	
Example: a == b	

Identity operator (is):-
-----------------------
Checks whether both variables refer to the same object
Two different lists return False
Example: a is b

'''


# Example:-
a = [10, 20, 30]
b = [10, 20, 30]
print(a == b)
print(a is b)

'''
Output:
True
False    
'''

'''
Why?
First statement:
print(a == b)
Both lists contain the same values, so the result is True.

Second statement:
print(a is b)
The lists are separate objects, so the result is False.

'''

# Remember: Equal values do not necessarily mean the same object.

# 5. Real-World Programming 
# Example: Checking None
'''In Python, None represents the absence of a value. '''

'''Identity operators are commonly used to check whether a variable is None. '''
# Example:-
result = None
if result is None:    
    print("No result available")
else:    
    print("Result available")

# Output:  No result available

'''Explanation
The condition result is None checks whether result refers to the special None object.
Since result is None, the condition is True.
'''

# Best practice: Use is None or is not None when checking for None.
result = 100
if result is not None:    
    print("Result is available")

# Output: Result is available

'''
6. Quick Revision

Expression	                    Meaning
-----------              -------------------
a is b	            Do a and b refer to the same object?
a is not b	        Do a and b refer to different objects?
a == b	            Do a and b have equal values?
a != b	            Do a and b have unequal values?

'''

'''Identity Operators: Identity operators in Python (is and is not) are used to check whether two variables refer to the same object in memory.
'''


# 7. BITWISE OPERATORS (AND(&), OR(|), NOT(~), XOR(^), LEFT SHIFT(<<), RIGHT SHIFT(>>)) :-
# -----------------------------------------------------------------------------------------
'''Bitwise operators are operators that perform operations on the individual bits (binary digits) of integers.

Computers represent numbers using binary digits: 0 and 1.
Bitwise operators work directly with the binary bits of numbers.  '''

''' 
 Decimal Number           Binary Representation 
------------------        ----------------------
        1                      `0001` 
        2                      `0010` 
        3                      `0011` 
        4                      `0100` 
        5                      `0101` 
        6                      `0110` 
        7                      `0111` 
        8                      `1000` 
        
'''

'''
Types of Bitwise Operators:-
----------------------------
Python has six commonly used bitwise operators:

Operator	Name	            Meaning
-------     ------          ----------------
    &	    Bitwise         AND	Both bits must be 1
    |	    Bitwise         OR	At least one bit must be 1
    ~	    Bitwise         NOT	Inverts the bits
    ^	    Bitwise         XOR	Bits must be different
    <<	    Left Shift	    Shifts bits to the left
    >>	    Right Shift	    Shifts bits to the right

'''


# 2. Bitwise AND (&):-
# --------------------
'''The bitwise AND operator compares the corresponding bits of two numbers. '''
'''
The result is 1 only when both bits are 1. Otherwise, the result is 0.

AND Truth Table
----------------
First Bit	Second Bit	Result
    0	        0	      0
    0	        1	      0
    1	        0	      0
    1	        1	      1
    
'''


# Example 1: 
a = 5
b = 3
print(a & b)

# Output: 1

'''How does it work?
First, convert both numbers into binary.
5 = 0101
3 = 0011

Now compare their bits: 0101 AND 0011  = 0001

The result is 0001, which is decimal 1.
Therefore: print(5 & 3)

Output: 1

AND returns 1 when both corresponding bits are 1
'''

# 3. Bitwise OR (|):-
# -------------------
'''The bitwise OR operator compares the corresponding bits of two numbers.'''
'''
The result is 1 when at least one of the bits is 1. It returns 0 only when both bits are 0.

OR Truth Table
------------------
First Bit	Second Bit	Result
    0	        0	      0
    0	        1	      1
    1	        0	      1
    1	        1	      1
    
'''
# Example:-
a = 5
b = 3
print(a | b)

# Output: 7

'''
How does it work?

Binary representations:
5 = 0101
3 = 0011

Apply OR: 0101 OR  0011  = 0111

0111 in binary equals 7 in decimal.
Therefore, the output is 7.

OR returns 1 if at least one corresponding bit is 1.'''

# AND vs OR
print(5 & 3)  # 1
print(5 | 3)  # 7


'''Remember:
- & → Both bits must be 1.
- | → At least one bit must be 1.
Important: | is the bitwise OR operator, while or is the logical OR operator. They are different. '''


# 4. Bitwise NOT (~):-
# --------------------
'''The bitwise NOT operator reverses the bits of an integer.
- 0 becomes 1.
- 1 becomes 0.
In Python, integers use a signed representation with effectively unlimited precision. As a result, bitwise NOT follows this rule:
[ boxed{sim x = -(x+1)}]'''

# Example 1:-
a = 5
print(~a)

# Output: -6

'''Why does it return -6 instead of -5?

Using Python's rule:
~5 = -(5 + 1)
   = -6
'''
# Example 2:-
print(~0)
print(~1)
print(~2)
print(~5)
'''
Output:
-1
-2
-3
-6  '''

'''Important Concept
For a positive integer:
~x = -(x + 1)

For example:
print(~10)
Output: -11

NOT reverses the bits. In Python, ~5 gives -6 because ~x equals -(x + 1).'''


# 5. Bitwise XOR (^):-
# ----------------------
'''XOR stands for Exclusive OR.
It returns 1 when the two corresponding bits are different. If they are the same, it returns 0.

XOR Truth Table
-----------------
First Bit	Second Bit	Result
    0	        0	      0
    0	        1	      1
    1	        0	      1
    1	        1	      0
'''

# Example:-
a = 5
b = 3
print(a ^ b)

# Output: 6

'''How does it work?
Convert the numbers into binary:
5 = 0101
3 = 0011

Apply XOR: 0101 XOR 0011 = 0110

The binary number 0110 equals decimal 6.
Therefore, the output is 6.'''


# Another Example:-
print(5 ^ 5)
print(5 ^ 0)

'''
Output:
0
5
'''

'''Why?
- 5 ^ 5 → Both numbers have identical bits, so the result is 0.
- 5 ^ 0 → XOR with zero leaves the original number unchanged.
XOR returns 1 when the corresponding bits are different.
'''
# Remember: ^ is bitwise XOR in Python, not the power operator. For powers, use **.
print(2 ** 3)  # 8
print(2 ^ 3)   # 1


# 6. Left Shift (<<):-
# --------------------
'''The left shift operator shifts the bits of a number to the left by a specified number of positions.

For non-negative integers, shifting left by n positions is equivalent to multiplying by \(2^n\).
Syntax: number << positions '''


# Example 1:-
a = 5
print(a << 1)

# Output: 10

'''
How does it work?
The binary representation of 5 is: 5 = 0101

Shift the bits one position to the left: 0101 << 1 = 1010

1010 in binary equals 10 in decimal.

Therefore: print(5 << 1)

Output: 10 '''

# Example 2:-
print(5 << 1)
print(5 << 2)
print(5 << 3)

'''
Output:
10
20
40'''

'''
Explanation:
Expression	Calculation	 Result
  5 << 1	   5 × 2¹	   10
  5 << 2	   5 × 2²	   20
  5 << 3	   5 × 2³	   40  
   
Left shift moves the bits to the left. For non-negative integers, each left shift multiplies the number by 2. '''


# 7. Right Shift (>>):-
# ---------------------
'''The right shift operator shifts the bits of a number to the right by a specified number of positions.

For non-negative integers, shifting right by n positions is equivalent to taking the floor of division by \(2^n\).
Syntax : number >> positions
'''

# Example 1
a = 10
print(a >> 1)

# Output: 5

'''
How does it work?
The binary representation of 10 is: 10 = 1010

Shift the bits one position to the right: 1010 >> 1 = 0101

0101 in binary equals 5 in decimal.

Therefore, the output is 5.
'''

# Example 2:-
print(20 >> 1)
print(20 >> 2)
print(20 >> 3)

'''
Output:
10
5
2'''

'''Explanation:
Expression	 Calculation	  Result
20 >> 1	       20 // 2¹	        10
20 >> 2	       20 // 2²	        5
20 >> 3	       20 // 2³	        2     

Right shift moves the bits to the right. For non-negative integers, shifting right by one position divides the number by 2, rounding down.
'''
'''Notice that 20 >> 3 gives 2, not 2.5, because right shifting a non-negative integer effectively takes the floor of division. '''
 
# 8. All Six Operators at a Glance
# Consider these two variables:
# -----------------------------
a = 5
b = 3
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a << 1)
print(a >> 1)

'''
Output:
1
7
-6
6
10
2'''








