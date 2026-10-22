# TUPLE DATATYPE
# --------------
''' It is a collection of homogeneous and hetrogeneous type of data .
--> Boundaries of tuple is parentheses () .
--> It is an immutable datatype .
--> It is an ordered datatype .
--> It allows duplicate elements .
--> It supports Indexing and Slicing .
--> The default value of tuple is empty parentheses() .'''

# examples:-
# ----------

t = tuple()
print(t)        #op:- ()

t = (1,2,3,4,5,6,6,7)
print(t)                # op:-   (1, 2, 3, 4, 5, 6, 6, 7)
print(type(t))          # op:-  <class 'tuple'>


t = (1,2.6,True,"rajesh",[1,2,3],("hello"),1+3j)
print(t ,type(t))
# op:- (1, 2.6, True, 'rajesh', [1, 2, 3], 'hello', (1+3j))     <class 'tuple'>


'''IMPORTANT:- WHENEVER WE ARE STORING A SINGLE VALUE INSIDE A TUPLE WE SHOULD MUST USE COMMA (,) 
ELSE IT WILL CONSIDER THE VALUE INTO ITS OWN DATATYPE .'''
# for examples:-

t = ("hii")
print(t)
print(type(t))    #op:- <class 'str'>
# op:-  hii    , why because we were not used there comma after the value so it treat as its own datatype that is string .

t = ("hiii",)
print(t)            #op:- ('hiii',)
print(type(t))      #op:- <class 'tuple'>


t = (1)
print(t , type(t))     #op:- 1 <class 'int'>


'''IMPORTANT:- WHENEVER WE ARE STORING MORE THAN ONE VALUE IN A SINGLE VARIABLE , PYTHON INTERPRETER WILL CONVERT THOSE VARIABLE
INTO TUPLE DATATYPE .'''
# for examples:-

t = 10,20,30,40,50
print(t)
# op:-  (10, 20, 30, 40, 50)

print(type(t))    #op:- <class 'tuple'>

a,b = 10,20
print(a)        #op:- 10
print(b)        #op:- 20

'''We will get an error if we pass more value with less variable .'''
# a,b = 10,20,30
# print(a)
# print(b)

'''look at the above code there we passed three value of two variable , so the value 10 will go the variable "a" 
and 20 will go to variable "b" but there is no such variable which can store the value 30 . , to overcome this we can use *variable_name....
'''
# for examples:-

a,b,*c = 10,20,30,40,50,60

print(a)    #op:- 10
print(b)    #op:- 20
print(c)    #op:- [30, 40, 50, 60]

# or

a,*b,c = 10,20,30,40,50,60

print(a)    #op:- 10
print(b)    #op:- [20, 30, 40, 50]
print(c)    #op:- 20


''' Even without parentheses, the comma can create a tuple:'''
# --------------------------------------------------------
t = 10,
print(type(t))  # <class 'tuple'>


# Using the tuple() constructor
t = tuple([10, 20, 30])
print(t)


'''You can convert other iterables into tuples:'''
# ---------------------------------------------
print(tuple("Python"))
# ('P', 'y', 't', 'h', 'o', 'n')

print(tuple([1, 2, 3]))
# (1, 2, 3)

print(tuple(range(5)))
# (0, 1, 2, 3, 4)


# indexing in tuple
# -----------------
''' It is a process of extract indivisual character from a collection is known as Indexing .
--> If you use an index that doesn't exist, Python raises an IndexError.

Syntax:- varibale_name([index])'''
t = (10, 20, 30, 40, 50)

print(t[0])   # 10
print(t[2])   # 30
print(t[-1])  # 50
print(t[-2])  # 40


# Slicing in tuples
# ------------------
''' It is a process of extracting more than one character from a collection is known as Slicing .
--> It accepts three arguments .
    1.start index , by default start from 0 .
    2.end index , by default till length of the collection .
    3.step value , by default +1 .

Syntax: tuple[start:stop:step]

- start: starting index, included.
- stop: ending index, excluded.
- step: interval between selected elements    '''

# examples:-

t = (10, 20, 30, 40, 50, 60)

print(t[1:4])   # (20, 30, 40)
print(t[:3])    # (10, 20, 30)
print(t[2:])    # (30, 40, 50, 60)
print(t[::2])   # (10, 30, 50)
print(t[::-1])  # (60, 50, 40, 30, 20, 10)
print(t[-3:-1]) # (40, 50)


''' This is the most important difference between tuples and lists.
 You cannot change an element  '''

# examples:-

# t = (10, 20, 30)
# t[0] = 100

# op:- TypeError: 'tuple' object does not support item assignment


'''You cannot append an element'''
# examples:-
# t = (10, 20, 30)
# t.append(40)

# op:- AttributeError: 'tuple' object has no attribute 'append'


'''You cannot remove an element'''
# examples:-
# t = (10, 20, 30)
# del t[1]

# op:-TypeError


'''However, you can delete the entire tuple variable:'''
# t = (10, 20, 30)
# del t

# print(t)  # NameError


'''Important advanced concept: a tuple can contain a mutable object'''
# examples:-

t = (10, [20, 30], 40)
t[1].append(50)

print(t)     #op:- (10, [20, 30, 50], 40)

'''
Why does this work?
The tuple itself remains unchanged: its second element still refers to the same list. But the list's contents can change because a list is mutable.

So, tuple immutability does not make every object inside the tuple immutable. '''


# Tuple operators
# ----------------

# A. Concatenation (+)
# --------------------
''' Combines two tuples into a new tuple.
--> The original tuples are not modified.'''

# examples:-
t1 = (10, 20)
t2 = (30, 40)

print(t1 + t2)    #op:- (10, 20, 30, 40)


# B. Repetition (*):-
# ------------------
'''It is the process of duplicating the data based on the integer value .'''
# examples:-
t = (1, 2)
print(t * 3)     #op:- (1, 2, 1, 2, 1, 2)


# C. Membership (in, not in):-
# ---------------------------
'''This operator are used to check either the value is present or not .
--> The return type is Boolean value (True / False)  .'''

# examples:-
t = (10, 20, 30)

print(20 in t)      # True
print(50 in t)      # False
print(50 not in t)  # True


# D. Comparison operators:-
# -------------------------
'''Tuples are compared element by element, from left to right .'''
# examples:-
print((1, 2, 3) == (1, 2, 3))  # True
print((1, 2) < (1, 3))         # True
print((2, 1) < (3, 0))         # True

# For example, (1, 2) < (1, 3) is true because the first elements are equal, and 2 < 3.


# 8. Built-in tuple methods:-
# -------------------------
'''Tuples have only two built-in methods.'''

# A. count():-
# -----------
'''It Returns how many times a value appears. '''

# examples:-
t = (10, 20, 10, 30, 10)

print(t.count(10))  # 3
print(t.count(20))  # 1
print(t.count(50))  # 0


# B. index():-
# -----------
''' It Returns the index of the first occurred specified element from the left side .
--> It raises ValueError if the specified element is not present .'''
# examples:-
t = (10, 20, 30, 20, 40)

print(t.index(20))  # 1
print(t.index(40))  # 4
# print(t.index(80))  # op:- ValueError: tuple.index(x): x not in tuple

'''You can also specify a starting position:'''
t = (10, 20, 30, 20, 40)

print(t.index(20, 2))  # 3


'''
What about sort(), append() and reverse()?
Tuples don't have these methods because they are immutable.

Method	        Available on tuple?
count()	                Yes
index()	                Yes
append()	            No
extend()	            No
insert()	            No
remove()	            No
pop()	                No
sort()	                No
reverse()	            No     '''


'''You can use sorted() to get a sorted list from a tuple:'''
t = (40, 10, 30, 20)
result = sorted(t)

print(result)  # [10, 20, 30, 40]

# Notice that sorted() returns a list, not a tuple.


'''To get a sorted tuple:'''
result = tuple(sorted(t))
print(result)  # (10, 20, 30, 40)


# 9. Tuple packing and unpacking
# ------------------------------
# A. Tuple packing:-
# ------------------
'''Putting multiple values into a single tuple.'''
# examples:-
t = 10, 20, 30

print(t)  # (10, 20, 30)


# B. Tuple unpacking:-
# ---------------------
'''Assigning individual tuple values to separate variables .'''
# examples:-
t = (10, 20, 30)
a, b, c = t

print(a)  # 10
print(b)  # 20
print(c)  # 30

# The number of variables must normally match the number of elements.


# C. Extended unpacking with *:-
# ------------------------------
'''The starred variable collects the remaining elements into a list.'''
# examples:-
t = (10, 20, 30, 40, 50)

a, *b, c = t

print(a)  # 10
print(b)  # [20, 30, 40]
print(c)  # 50

# Notice that b is a list, even though the original data was a tuple.


# D. Swapping variables:-
# ---------------------
'''Python allows swapping values without a temporary variable.'''
# examples:-
a = 10
b = 20
a, b = b, a

print(a)  # 20
print(b)  # 10

# This uses tuple packing and unpacking.


# 10. Looping through a tuple:-
# ----------------------------
'''Using a for loop'''
t = (10, 20, 30, 40)

for value in t:
    print(value)
'''
10
20
30
40'''


# Using a while loop
# -------------------
t = (10, 20, 30)
i = 0

while i < len(t):
    print(t[i])
    i += 1


# Using enumerate():-
# ------------------
'''When you need both the index and the value:'''
# examples:-
t = ("Python", "Java", "SQL")

for index, value in enumerate(t):
    print(index, value)

'''
0 Python
1 Java
2 SQL'''

# 11. Useful built-in functions:-
# ------------------------------
t = (10, 20, 30, 40, 50)

print(len(t))       # 5
print(min(t))       # 10
print(max(t))       # 50
print(sum(t))       # 150
print(any(t))       # True
print(all(t))       # True
print(sorted(t))    # [10, 20, 30, 40, 50]


'''
Some important points:
----------------------
- len() returns the number of elements.
- min() and max() return the smallest and largest values.
- sum() adds numeric elements.
- any() returns True if at least one element is truthy.
- all() returns True if every element is truthy.
- sorted() returns a new sorted list.  '''


# 12. Converting a tuple into a list and vice versa
'''Sometimes you need to modify tuple data. You can convert it to a list first.'''
t = (10, 20, 30)
lst = list(t)
lst.append(40)

t = tuple(lst)
print(t)
# op:- (10, 20, 30, 40)

'''
The steps are:
1. Convert the tuple to a list.
2. Modify the list.
3. Convert the list back into a tuple. '''

# 13. Nested tuples:-
# -------------------
'''A tuple can contain other tuples.'''
t = ((10, 20), (30, 40), (50, 60))

print(t[0])     # (10, 20)
print(t[0][1])  # 20
print(t[2][0])  # 50

# This is useful for representing structured data such as coordinates or rows and columns.

coordinates = ((10, 20), (30, 40))

for x, y in coordinates:
    print("X:", x, "Y:", y)


'''
X: 10 Y: 20
X: 30 Y: 40  '''



# ------------------------Thank You ------------------------------