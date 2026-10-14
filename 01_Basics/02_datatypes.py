
# What is Identifier:-
# --------------------

''' Identifier are user defined name which is given to an object, class, variables, and function() etc.
'''
# Rules of identifier:-
# ---------------------
# Rule 1:- Identifier should starts with either alphabets or under_scores ("_") , for examples

name = "Rajesh"
_age = 23
print(name)   # op:- "Rajesh"
print(_age)   # op:- 23

# but what if we declare the variable like this...

''' 
$age = 200
print($age)   #op:-  SyntaxError: invalid syntax  '''

''' 
1a = "rajesh"
print(1a)   # op:-  SyntaxError: invalid decimal literal  '''


# Rule 2:- Identifier can have numbers but it should not start with numbers. for examples,

pass123 = "rajesh@123"
print(pass123)     # op:- rajesh@123

''' 
1a = "rajesh"
print(1a)   # op:-  SyntaxError: invalid decimal literal  '''


# Rule 3:- No other special characters are allowed accepts "_" under_score, including space.
# examples:-

your_name = "Srabani"
print(your_name)     # Srabani

''' 
your@name = "Dinga"
print(your@name)  

op:- SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
'''

'''
your~name = "Dingi"
print(your~name)

op:- SyntaxError: invalid syntax
'''

''' 
your name = "Manga"
print(your name)

op:- SyntaxError: invalid syntax
'''

'''
"yourname" = "rajesh"
print("yourname")

op:-  SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?  '''

# Rule 4:- Keywords can't be used as an identifier name.
# examples:-

'''
True = 10
print(True)  

op:-  SyntaxError: cannot assign to True  '''

'''
as = 10
print(as)  

op:- SyntaxError: invalid syntax  '''

#  But why we can't use keyword as an identifier name 

''' answer: Keywords are reserved words in Python that have predefined meanings and specific purposes in the language. Therefore, we cannot use them as identifiers (such as variable names, function names, or class names) because doing so would conflict with Python's syntax and the meaning assigned to those words.

In simple word keywords are already have some special properties. '''


# Rule 5:-
'''identifier can have unlimited length but according to the convension or guidelines the maximum no.of
character is "79", but in "IT" industry we will use upto "32" characters. '''


# What is pep-8 (Python enhancement proposal-8)
# ---------------------------------------------
'''it is a documentation or guidelines which tells us how to write and execute python programs.'''


# isidentifier():-
# ----------------
'''It is a inbuilt function which is return true if the given string follows all the identifier rules else return false.

syntax:- string.isidentifier()
'''
# example:-

print("age".isidentifier())  #OP:- True
print("ag@e".isidentifier())  #op:-  False

name = "rajesh@gouda"
print(name.isidentifier())   #op:- False


# What is keyword:-
# -----------------
'''Keywords are the predefined or reserved words which are used to perform some specific task.
--> Keywords are used to define the syntax and structure of python programs.
--> In python we have "35" keywords in the current version

--> We can access the keywords in two ways,

    1.with the help of -> help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

print(help('keywords'))

False               class               global              pass
None                continue            if                  raise
True                def                 import              return
and                 del                 in                  try
as                  elif                is                  while
assert              else                lambda              with
async               except              match               yield
await               finally             nonlocal            
break               for                 not                 
case                from                or                  
    
2.second way:- 
import keyword
print(keyword.kwlist)

op:- 
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''

'''Important:- (False, True, None) are the special keywords which start with uppercase character.'''


# What is Variable:-
# -------------------
'''Variable is a named memory location which is used to store the data and it can be modified "n" no.of times during execution

examples:-
a = 10
a = 20
print(a) 

here: a is the variable name and 10 is the value

Now the output is 2o because it has been modified now from 10 to 20.
'''

# ID():-
# ------
'''It is an inbuild function which is used to returns the object address of a variable.'''
# example:-
name = "rajesh"
print(id(name))   # op:- 1434936300896

# suppose we have reference to the same variable like..
a = 10
b = a
print(id(a))  #op:-  140712844453272
print(id(b))  #op:-  140712844453272
'''
1. a = 10 — Python creates or reuses an integer object representing 10, and a refers to it.
2. b = a — Python does not create another integer object here. Instead, b refers to the same object as a.
3. Therefore, both variables have the same id().

Both variables refer to the same object.
'''

#  what if we give like this ...
a = 1000
b = 1000
print(id(a))   #op:-  2789475463664
print(id(b))   #op:-  2789475463664

print(a == b)  #op:- True
print(a is b)  #op:- True

'''But How?:-
When Python executes these assignments, it can reuse the same integer object for both variables. For example, a compiler may recognize that the same constant 1000 appears twice and reuse the corresponding object.

However, Python does not guarantee that separately written integer literals such as 1000 will always have the same identity. The result can vary depending on the Python implementation and execution context.
'''

name = "rajesh"
fullname = "rajesh" 
print(id(name))       # op:- 1838275450208
print(id(fullname))   # op:- 1838275450208

print(name == fullname)  # op:- True
print(name is fullname)  # op:- True



#  Datatype:-
# ------------
'''Datatypes are used to specify what type of and what kind of data should be stored inside a variable
--> Datatypes are classified into two types
    1.Indivisual/single value datatype
    2.Collection/container datatype '''

# 1. Indivisual Datatype:-
# ------------------------
'''This datatype are used to store the data in a single memory block.
--> All the indivisual datatypes are immutable, means we can't add , update and modify the values.
--> We can't use lenght() function for the indivisual datatypes.

--> It is classified into 4types
    1.INT
    2.FLOAT
    3.BOOLEAN
    4.COMPLEX'''

# 1.INTEGER (int):-
# ----------------
'''This datatype are used to store the number without any decimal value
--> Default value of integer is 0'''
# examples:-
a = 100
print(a)   # 100
print(type(a))  # op:- <class 'int'>

b = int()
print(b)   #op:- 0

# type() :- it is used to check what type of data we were storing inside the variable.

# or we can give the value like this ..
c = int(2030)
print(c)       # op:- 2030
print(type(c))  # op:- <class 'int'>

d = int("20027")
print(d)            # op:-  20027
print(type(d))      # op:- <class 'int'>

# here the int convert string of "20027" into integer . but if there is anyother value instead of number it reised error.
# for example:-

'''
e = int("abc1234")
print(e)             #op:-  ValueError: invalid literal for int() with base 10: 'abc1234'
print(type(e))

'''


# 2.FLOAT (flaot):-
# -----------------
'''This datatype is used to store the number along with decimal value.
-->Default value of float is 0.0'''

# example:-
a = 12.0
print(a)      # op:- 12.0
print(type(a))  #op:- <class 'float'>

# or we can use the float explicit  for example

b = float(123.0)
print(b)
print(type(b))

#op:- 123.0
#op:- <class 'float'>

c = float(127)
print(c)        #op:- 127.0   
#  by default it will make the simple number into a flaot value add 0 add the end.


# default value of flaot is  0.0
f = float()
print(f)     # op:-  0.0

d = float("123")
print(d)
print(type(d))

'''
op:-
    123.0
    <class 'float'>'''


# 3.BOOLEAN (bool):-
# -----------------
'''This datatype are used to store either true or false
--> Default value of boolean is false
--> the value of "True" is 1 and the value of "False" is 0 '''
# example:-

a = True
print(a)
print(type(a))

# default value of boolean is "False"
b = bool()
print(b)   #op:- False

print(True)

# here we can see...

c = bool(0.0)
print(c)     #False

d = bool(1)
print(d)     #True

'''IMPORTANT:- 
--> All the default values wiill be False
--> All the non-default values will be True'''

# for example:-

s = bool("")
print(s)    # False

n = bool(0)
print(n)        # False


# 4.COMPLEX (complex):-
# --------------------
'''It is a collection of real and imaginary numbers.
--> it will be represent in the form of "a+bj" 
--> the internal value of "j" is roor over -1 
--> the default value of complex is "0j" '''

# examples:-

p = 2 + 3j
print(p)               #op:- (2+3j)
print(type(p))         #op:- <class 'complex'>

#  or we can use it explicit

c = complex(5 + 10j)
print(c) 
print(type(c))

# op :- (5+10j)
# op:-  <class 'complex'>

d = complex("5+10j")
print(d)
print(type(d))

''' 
op:-
(5+10j)
<class 'complex'>'''

# or we can take the value like this
e = complex(real=8,imag=9)
print(e)   

#op:- (8+9j)

#  if we change the value also it doesn't matter

f = complex(imag=9,real=5)
print(f)     

# op:- (5+9j)


# 2.Collectional / container datatype:-
# ------------------------------------
'''This datatype are used to stored the data in a sequence of memory
--> We can use length() for the collection datatype'''
# We have 5 types of collectional datatype:-

# 1. String()  --> str()
# 2. List()    --> list()
# 3. Tuple()   --> tuple()
# 4. Set()     --> set()
# 5. Dictionary{}  --> dict{}















 














    



