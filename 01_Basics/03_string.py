# STRING DATATYPE (str())
# -------------------------
'''String is a collection of characters, alphabets, numbers, special character, alpha numeric values.
--> Boundaries of string is single quatos '', or double quatos"", or triple single quatos''' ''', or triple double quatos""" """.
--> String is a immutable datatype.
--> String allows duplicate characters
--> String is a ordered datatype
--> String supports indexing and slicing
--> Default value of string is empty single quatos ''.  '''

# examples:-

s = "hello"
print(s)     # op:- hello
print(type(s))     # op:- <class 'str'>

s = str("hello")
print(s)
print(type(s))

'''
op:-
hello
<class 'str'> '''

# default value is '', example
s = str()
print(s)

# s = "hello
# print(s)   #op:- SyntaxError: unterminated string literal (detected at line 30)

s = '''
hello
every 
one '''
print(s)

#  see the output is coming like this...
'''
op:-
hello
every 
one 
'''

# but whenever we are trying to do this same thing in a single quatos or doouble quatos the output will be different.... for example

s = 'hello' \
'every' \
'one'

print(s)

# op:- helloeveryone

# important:- whenever we are using single quatos , we have to remember there will be no other single quatos appears, it will raised error for example

# s = 'mr's'
# print(s)     #op:- SyntaxError: unterminated string literal (detected at line 59)


# "/n":- slash "/n" we used for creating a new line , for example..


# Indexing:-
# ----------
'''It is a process of extracting indivisual character from a collection is known as Indexing.
--> It raises index error if the specified index is not present.
--> It accepts both positive and negative index , positive index starts from "0" and negative index starts from "-1".

--> Syntax:- string/variable_name[index]'''

# examples:-

s = "Programming"
print(s[1])      #op:- r

print(s[5])      #op:- a

print(s[-1])    #op:- g

# what is the index is out of range, for example
'''
print(s[100])   

op:- IndexError: string index out of range  '''

# and we can findout the length

print(len(s))    #op:- 11
print(len(s) - 3)   #op:- 8
print(len("hi") + 4)   #op:- 6

print(s[-11+1])     #op:- r    it means s[-10] 
print(s[9-15])      #op:- a    it means s[-6]


#  interesting thing , what will be the output of this code ..

s= ' '
print(s)    
print(len(s))    #op:- 1
print(s[0])      #op:- not empty one value is there

# that was not an empty string there were one gap, so string count the gap as a string value. thats way the length of the string is 1.

#  we can also ..
print("hello"[4])



# Slicing:-
# ---------
'''It is the process of extracting more than one character from a collection is known as Slicing. 
--> It accepts three arguments:-
    1.Start index
    2.End index
    3.Step value
    
--> By default the start index will be zero (0)
--> End index will be the length of the string
--> The step value will be +1 

--> Syntax:- String/variable_name[SI:EI:SV]'''

# examples:-

s = "Pragramming"
print(s[::])        #op:- Pragramming

# here the output is as it is , because we didn't provided any step value or end index or start index.

print(s[::+1])  #op:- Pragramming      it means starts from 0 to till end , and step value +1 , that is bydefault so it won't affect.

print(s[:7:+1])  #op:- Pragram         it means starts from 0 to till 7 .

print(s[4::+2])    #op:- rmig          it means satrts from 4 to till end , step value is +2

print(s[5:10:])    #op:-  ammin        it means starts from 5 to till 10

print(s[::-1])     #op:-gnimmargarP    it means reverse the string, from left to right -1 means

print(s[:-6:])     #op:- Pragr         it means starts from 1 to 6

print(s[3:8:-1])



print(s[-3:-7:])   #op:- output is nothing means empty string ''

print(s[-3:-7:-1])   #op:- imma     means it start from -3 to -7 from left to right

# why?
'''
answer:-
In Python, print(s[-3:-7:]) returns an empty string because the default step is +1, but your start index is greater than your stop index.
Let's understand it with an example.

s = "Python"
print(s[-3:-7:])

Output: ''

1. Understand the negative indexes
For s = "Python":
P
-6

y
-5

t
-4

h
-3

o
-2

n
-1

Negative indexes: -6, -5, -4, -3, -2, -1

--> s[-3] → 'h'
--> s[-7] → Out of range for this string.

2. Why does slicing return nothing?
The syntax is:
s[start:stop:step]

Your code:
s[-3:-7:]

is equivalent to:
s[-3:-7:+1]

Because the step is positive (+1), Python moves from left to right.
But you are asking Python to start at index -3 and move toward index -7, which is in the opposite direction. Therefore, Python finds no characters to return.

3. How can you get the characters in reverse?
Use a negative step (-1):
s = "Python"print(s[-3:-7:-1])

Output:
htyP

Here's why:
- Start at -3 → 'h'
- Move backward → 't'
- Then → 'y'
- Then → 'P'

- Stop before reaching index -7 (the stop index is excluded).
Remember this rule:

Step	Direction	Example
+1	Left to right	s[1:5:1]
-1	Right to left	s[-3:-7:-1]

The key point is that the step direction must match the direction from the start index toward the stop index.
'''

# METHODS OF STRING:-
# ------------------

# 1.UPPER():-
# -----------
'''It is an inbuild function which is used to convert the given character and string into uppercase .
--> It won't accepts any argument .
--> The return type of upper() is string .
'''

# examples:-

name = "Srabani"
print(name.upper())   #SRABANI

# or
upp = name.upper()
print(upp)           #SRABANI

# or

s1 = "hello123"
print(s1.upper())     #op:- HELLO123

# or

s2 = "Hello@#$%BYE364"
print(s2.upper())       #op:- HELLO@#$%BYE364

# or

print("d".upper())      #op:- D
print("DIMPLE".upper())     #op:- DIMPLE


# or if we pass any argument inside the upper() it will raised error for example
'''
s3 = "hello"
print(s3.upper("h"))

op:- TypeError: str.upper() takes no arguments (1 given)  '''

#  we can use it with indexing and slicing. for example

# Indexing
greet = "Good Morning"
print(s[3].upper())     #op:- G

# Slicing
print(s[::2].upper())   #op:- PARMIG       it means starts from 0 to till end with the step value +2.

print(s[::2][::2].upper())   #op:- PRI   it means starts from 0 to till end with step value +2 , and repeat it one more time



# 2.LOWER():-
# -----------
''' It is an inbuild function which is used to convert the given character or string into lowercase.
--> It won't accepts any arguments .
--> The return type of lower() is a string

Syntax:-  string.lower()'''

#  for examples:-

lang = "malayalam"
print(lang.lower())     #op:- malayalam

# or

p_lang = "PROGRAMMING"
print(p_lang.lower())       #op:- programming

# or

myName = "RaJEsH"
print(myName.lower())      #op:- rajesh

# or
print(myName[5].lower())        #op:- h

# print(myName[9].lower)      op:- IndexError: string index out of range

print(myName[:5:].lower())     #op:- rajes

print("RAJESH%*^#$^&387847".lower())        #op:- rajesh%*^#$^&387847



# 3.SWAPCASE():-
# --------------
'''It is an inbuild function which is used to convert all the uppercase character into lowercase and all the lowercase character into uppercase .
--> It won't accepts any arguments .
--> The retunr type of swapcase() is a string

Syntax:- String.swapcase()'''

# examples:-

name = "Rajesh Gouda"
print(name.swapcase())      #op:- rAJESH gOUDA

last_name = "GOUDA"
print(last_name.swapcase())     #op:- gouda

first_name = "rajesh"
print(first_name.swapcase())       #op:- RAJESH

# It won't accepts any arguments, so if we try to pass it will raised an error.
'''
print(first_name.swapcase("j"))   
op:- TypeError: str.swapcase() takes no arguments (1 given)  '''


# 4.CAPITALIZE():-
# ---------------
''' It is an inbuild functionwhich is used to coverts first letter of a string into uppercase and remaing all the letters into lowercase .
--> It won't accepts any arguments .
--> The return type of capitalize() is a string .

Syntax:- String.capitalize()'''

# examples:-

name = "Bijaya Srabani Gouda"
print(name.capitalize())          #op:- Bijaya srabani gouda

# what if the string is like this..

grt = "@hello"
print(grt.capitalize())      #op:- @hello

'''here look at the above code , the output is as it is , why because the string starts with "@" so there is no upper and lower character for special character , it will affect only first chracter .'''

nst = "1hello"
print(nst.capitalize())        #op:- 1hello

print("sr".capitalize())        #op:- Sr

# it won't accepts any arguments, if we pass then it will raised an error
'''
code = "Python"
print(code.capitalize("p"))

op:- TypeError: str.capitalize() takes no arguments (1 given)  '''



# 5.TITLE():
# ---------
''' It is an inbuild function which is used to convert the first letter of every word of the string into uppercase and remain all letter into lowercase .
--> It won't accepts any argument .
--> The return type of title() is a string .

Syntax:- String.title()'''

# examples:-

name = "bijaya srabani Gouda"
print(name.title())

# or

s = "@hello"
print(s.title())      #op:- @Hello

# or

s1 = "12##$%^&*hello"
print(s1.title())          #op:- 12##$%^&*Hello

# or

s2 = "Hello every one"
print(s2.title())           #op:- Hello Every One

# or

s3 = "@rajesh $kumar &^gouda"
print(s3.title())                  #op:- @Rajesh $Kumar &^Gouda

# or
print("^*rajesh@3".title())         #op:- ^*Rajesh@3

'''Look at the above all codes it doesn't metter , where is the alphabet started, it will find the first alphabet and make it into uppercase and rest of the letters are lowercase .'''

# if we pass any arguments it will raised an error.
'''
myLang = "Odia"
print(myLang.title("o"))      

op:- TypeError: str.title() takes no arguments (1 given)  '''


# DIFFERENCE BETWEEN CAPITALIZE AND TITLE IS
# Capitalize:- it will convert the first alphabet into uppercase, if instead of alphabet anyother character at the first index it won't work.
#title():- it will convert the first letter of every word into uppercase , if instead of alphabet anyother character at first index i will find the alphabet then make it into uppercase and remains all are in lowrrcase.


# 6.INDEX():-
# ---------
''' It is an inbuild function which is used to return the position of a first occured specified element from the left side .
--> It accepts three arguments .
    1.Element
    2.Start index
    3.End index
--> It raises value error if the specified element is not present .
--> The return type of index is integer .

Syntax:- String.index(Element,[SI],[EI])'''
# the "element"  is mandatory , but the start and end index is not mandatory.

# examples:-

s = "programming"
print(s.index("g"))     #op:- 3

print(s.index("r",2))  #op:- 4

print(s.index("m",1,7))     #op:- 6

'''
 look at this code
print(s.index("m",1,6))    

#op:- ValueError: substring not found    because from 1 to 6 there is no "m"  '''

''' 
# if the character is not present it will raised an error .
print(s.index("z"))

op:- ValueError: substring not found   '''



# 7.rindex():-
# ------------
''' It is an inbuild function which is used to returns position of a first occured specified element from the right side .
--> It accepts three arguments .
    1. Element
    2. Start index
    3. End index
--> The return type of "rindex" is integer .
--> It raises value error if the specified element is not preset .

Syntax:- String.rindex(element,[SI],[EI])'''
# the element is mandatory, but the Start index and End index is optional .

# examples:-

s = "programming"
print(s.rindex("g"))     #op:- 10

print(s.rindex("r",2))  #op:- 4

print(s.rindex("m",1,7))

'''' if the specified element is not present it raises error
print(s.rindex("s"))  

op:- ValueError: substring not found  '''



# 8.find():-
# ---------
''' It is used to returns the position of first occured specified element from the left side .
--> It accepts three arguments .
    1.Element
    2.start index
    3.end index
--> It returns "-1" if the specified element is not present .
--> The return type of find() is an integer

Syntax:- String.find(element,[SI],[Ei])'''
# element is mandatory but start and end index is optional .

# examples:-
''' it accepts atleasr 1 argument
s = "Srabani"
print(s.find())   

op:- TypeError: find expected at least 1 argument, got 0   '''

'''
One argument must be string

s = "srabani"
print(s.find(3,4))  

op:- TypeError: find() argument 1 must be str, not int'''

s = "Srabani"
print(s.find("s"))    #op:- -1   beacause the samll "s"  is not present . it won't raised any error it return "-1"

s = "Srabani"
print(s.find("S"))        #op:- 0

s = "Srabani"
print(s.find("r",0,9))      #op:- 1



# 9.rfind():-
# -----------
''' It is used to return the position of first occured specified element from the right side .
--> It accepts three arguments .
    1.element
    2.start index
    3.end index
--> It return "-1" if the specified element is not present .
--> The return type of rfind() is an integer .

Syntax:- String.rfind(element,[si],[ei])'''
# One String value is mandatory , but the start and end index is optional

# examples:-

s = "Morning"
print(s.rfind("o"))     #op:- 1

print(s.rfind("n"))    #op:- 5

print(s.rfind("w"))    #op:- -1   beacause the "w" is not present in the specified string.



# 10.count():-
# -----------
''' It is an inbuild function which is used to returns no.of times the specified element is present in a collection .
--> It accepts three arguments .
    1.Element
    2.start index
    3.end index
--> It return zero if the specified element  is not present
--> The return type of count() is an integer

Syntax:- String.count(element,[si],[ei])'''

# examples:-
'''we should must pass one argument 

s = "malayalam"
print(s.count())      

op:- TypeError: count expected at least 1 argument, got 0   '''

s = "malayalam"
print(s.count("z"))    #op:- 0     beacause the specified element is not present it will return zero, instead of error.

print(s.count("m"))     #op:- 2   because two times the "m" is present

print(s.count("la"))    #op:- 2     beacause two times the consecutive "la" presents



# 11.split():-
# -----------
''' It is an inbuild function which is used to split the given string based on the separator and maximum splits , and return the values inside a list .
--> It will return a list .
--> By default separator is space .

Syntax:- String.split([separator],[max_split])'''

# examples:-

# bydefault separator is space .
s = "Hello Every one"
print(s.split())  

# op:- ['Hello', 'Every', 'one']       # beacause after every space it will split

print(s.split(" ",1))    

# op:- ['Hello', 'Every one']      beacause separator is space and the max_split is "1" so after one split it will stop spliting.

s = "malayalam"
print(s.split("a"))

# op:- ['m', 'l', 'y', 'l', 'm']       # Beacause after every "a" it will split

s = "Bijaya-Srabani-Gouda"
print(s.split())    

# op:-['Bijaya-Srabani-Gouda']     here the output is as it is, beacause split by default split the space not other , so we have to give the separator icon. for example here we have "-",

print(s.split("-"))       #op:- ['Bijaya', 'Srabani', 'Gouda']       now see the output .


# 12.rsplit():-
# -------------
''' It is an inbuild function which is used to split the given string based on the separator and maximum splits from the right side, and return the values inside a list .
--> It will return a list .
--> By default separator is space .

Syntax:- String.rsplit([separator],[max_split]) '''

# examples:-
s = "Hello Every one"
print(s.rsplit())        #op:- ['Hello', 'Every', 'one']

print(s.rsplit(" ",1))   #op:- ['Hello Every', 'one']



# 13.strip():-
# ------------
''' It is an inbuild function which is used to remove the given string from both leading and tailing part .
--> By default it will remove spaces .
--> The return type of strip() is a string .
--> If we won't pass any value it will return as it is the string .

Synatx:- String.strip([element])'''

# examples:-

s = "***hello***"
print(s.strip("*"))        #op:- hello

# if wont' pass any value it return the string as it is . example
print(s.strip())     #op:- **hello***

s = "***he**ll**o***"
print(s.strip("*"))       #op:- he**ll**o      why beacause it will remove only the leading and tailing part not the middle part .

# if we pass element which is not exist , it will return the string as it is.
s = "***h*e*ll*o****"
print(s.strip("@"))        #op:- ***h*e*ll*o****

# important:-

s = "@#@#@#hello#@#@@"
print(s.strip("@#"))        #op:- hello    beacause whatever the elements we were pass , there are had those "@#"

# another one:

s = "@#@#$@#@#hello@#@#@"
print(s.strip("@#"))         #op:- $@#@#hello     beacause in between @ and # the "$" is comming .

s = "     helloo   "
print(s.strip())            #op:- helloo       it will remove all the spaces and return the string .


# 14.lstrip():-
# -------------
''' It is used to remove the specified elements only from the leading part .
--> By default it will remove spaces .
--> The return type of lstrip() is a string .
--> If won't pass any argument it will return the string as it is .
--> if we pass the argument which is not exist it will return as it is the string .

Syntax:- String.lstrip([element])'''

# example:-

s = "*****hello******"
print(s.lstrip("*"))            #op:- hello******

s = '    hello    '
print(s.lstrip())               #op:- "hello     "


# 15.rstrip():-
# -------------
''' It is used to remove the specified elements only from the tailing part .
--> By default it will remove spaces .
--> The return type of rstrip() is a string .
--> If won't pass any argument it will return the string as it is .
--> if we pass the argument which is not exist it will return as it is the string .

Syntax:- String.rstrip([element])'''

# example:-

s = "*****hello******"
print(s.rstrip("*"))            #op:- *****hello

s = '    hello    '
print(s.rstrip())               #op:- "    hello"


# 16.replace():-
# -------------
'''It is a inbuild function which is used to replace the old substring or old element with the new substring or new element .
--> It accept three arguments .
    1.Old element
    2.New element
    3.Count
--> The return type of replace() is String 
--> Here it takes at least 2 positional arguments (1 given) , and count is optional.
--> If the element is not present it will return the string as it is .

syntax:- String.replace(old_element,New_element,[count])'''

# examples:-

'''Here it raised TypeError: replace() takes at least 2 positional arguments (1 given)
s = "malayalam"
s.replace("a")
print(s)          '''

s = "malayalam"
res = s.replace("a","e")
print(res)
# op:- meleyelem

res = s.replace("Q","o")
print(res)
# op:- malayalam       why? because the specified element is not present .

res = s.replace("la","p")
print(res)
# op:- mapyapm


# interesting
res = s.replace("a"," ")
print(res)
# op:- m l y l m        why because there were a space between the string it is count as a character .



# 17. join():-
# ------------
'''It is a inbuild function which is used to join the given string in between the elements present in a collection .
--> The return type of join is a "String" .
Syntax:- String.join(collection)'''

# examples:-

s = "Hello"
res = "-".join(s)
print(res) 
# op:- H-e-l-l-o

res = "dinga ".join(s)
print(res)
# op:- Hdinga edinga ldinga ldinga o

lst = ["Hey","every","one"]
res = " ".join(lst)
print(res)
# op:- Hey every one


# 18. startswith():-
# ------------------
'''It is an inbuild function which is used to check the string is starting with specified element or not .
--> The return type of startswith() is a Boolean .
--> It accepts three arguments .
    1.element
    2.start index
    3.end index
--> here "element" pass is mandatory but start and end index is optional .

Syntax:- String.startswith(element,[si],[ei])'''

# examples:-

s = "programming"
print(s.startswith("o"))   
# op:- False

print(s.startswith("p"))
# op:- True

print(s.startswith(""))
# op:-True

# print(s.startswith())
# op:- TypeError: startswith expected at least 1 argument, got 0

print(s.startswith("r",4,8))
# op:-True

print(s.startswith('m',5,7))
# op:- False

print(s.startswith("m",6))
# op:- True


# 19. endswith():-
# ------------------
'''It is an inbuild function which is used to check the string is starting with specified element or not .
--> The return type of startswith() is a Boolean .
--> It accepts three arguments .
    1.element
    2.start index
    3.end index
--> here "element" pass is mandatory but start and end index is optional .

Syntax:- String.endswith(element,[si],[ei])'''

# examples:-

s = "programming"
print(s.startswith("g"))   
# op:- False

print(s.endswith("p"))
# op:- True

print(s.endswith(""))
# op:-True

# print(s.endswith())
# op:- TypeError: startswith expected at least 1 argument, got 0

print(s.endswith("r",4,8))
# op:-True

print(s.endswith('m',5,7))
# op:- False

print(s.endswith("m",1,7))
# op:- True



# 20. isupper():-
# --------------
'''It returns True if the given string contains only the uppercase character .
--> The return type of isupper() is Boolean .
--> It won't accepts any argument .

Syntax:- String.isupper()'''

# examples:-

s = "APPLE"
print(s.isupper())
# op:- True

s = "HeLLO"
print(s.isupper())
# op:- False

s = "HEY123&*%"
print(s.isupper())
# op:- True

# s = 123
# print(s.isupper())
# op:- AttributeError: 'int' object has no attribute 'isupper'

s = "123"
print(s.isupper())
# op:- False

s = "#$%^&*@#$"
print(s.isupper())
# op:- False



# 21. islower():-
# --------------
'''It returns True if the given string contains only the lowercase character .
--> The return type of islower() is Boolean .
--> It won't accepts any argument .

Syntax:- String.islower()'''

# examples:-

s = "apple"
print(s.islower())
# op:- True

s = "HellO"
print(s.islower())
# op:- False

s = "hey123&*%"
print(s.islower())
# op:- True

# s = 123
# print(s.islower())
# op:- AttributeError: 'int' object has no attribute 'isupper'

s = "123"
print(s.islower())
# op:- False

s = "#$%^&*@#$"
print(s.islower())
# op:- False



# 22. isalpha():-
# ---------------
''' It returns True if the given string contains only alphabet .
--> It won't accepts any argument .
--> The return type if isalpha() is Boolean .

Syntax:- String.isalpha()'''

# examples:-

s = "hello"
print(s.isalpha())
# op:-True

s = "HELLO"
print(s.isalpha())
# op:- True

s = "hello123"
print(s.isalpha())
# op:- False

print("a".isalpha())  
# op:- True

s = "#$%Rajesh"
print(s.isalpha())
# op:- False

s = "#$%^&"
print(s.isalpha())
# op:- False


# 23. isdigit():-
# ----------------
''' It returns True if the given string contains only integer value .
--> It won't accepts any argument .
--> Return type of isdigit() is boolean .

Syntax:- String.isdigit()'''

# examples:-

s = "12345"
print(s.isdigit())
# op:- True

s = "1234Rajesh"
print(s.isdigit())
# op:-False

# s = 1234
# print(s.isdigit())
# op:- AttributeError: 'int' object has no attribute 'isdigit'

s = "#$%^12883"
print(s.isdigit())
# op:- False


# 24. isalnum():-
# ----------------
''' It returns True if the given string contains only alphabets or only digits or combination of alphabets and digits .
--> It won't accepts any argument .
--> Return type of isalnum() is Boolean .

Syntax:- String.isalnum()'''

# examples:-

s = "Hello1234"
print(s.isalnum())
# op:- True

s = 'Hello#^&2y37'
print(s.isalnum())
# op:- False

s = "1234"
print(s.isalnum())
# op:- True

s = 'Hello'
print(s.isalnum())
# op:- True



# 25. isspace():-
# ---------------
''' It returns True if the given string contains only space .
--> It won't accepts any arguments .
--> The return type of isspace() is Boolean .

Syntax:- String.isspace()'''

# examples:-

s = '  '
print(s.isspace())
# op:- True

s = " R "
print(s.isspace())
# op:- False

s = "  1"
print(s.isspace())
# op:- False

s = " @    "
print(s.isspace())
# op:- False


# 26.istitle():-
# ---------------
''' It returns True if the first alphabet of every word starts with uppercase and rest of in lowercase in the given string .
--> It won't accepts any arguments .
--> return type of istitle() is Boolean .

Syntax:- String.istitle()'''

# examples:-

s = "Hello Every One"
print(s.istitle())
# op:- True

s = "HELLO EVERY ONE"
print(s.istitle())
# op:- False

s = "Helo134 Kumar"
print(s.istitle())
# op:- True

s = "hello every one"
print(s.istitle())
# op:- False

s = "123Rajesh kumar"
print(s.istitle())
# op:-  False

s = "1234Rajesh Kumar"
print(s.istitle())
# op:- True

s = "@#$%^Rajesh"
print(s.istitle())
# op:- True


# ---------------Thank You ---------------------






 




 




























