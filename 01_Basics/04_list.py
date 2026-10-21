# LIST

''' List is a collection of homogeneous and hetrogeneous type of data .
--> Boundaries of list is square bracket [] .
--> List is a mutable datatype .
--> List is a ordered datatype .
--> It supports both Indexing and Slicing .
--> It allows duplicate elements .
--> Default value of list is empty square bracket .
--> The index start from zero .'''

# Homogeneous means:-
''' Same datatype of value present inside the list .'''
# example:-  lst = [1,2,3,4,5,6,7]

# Hetrogeneous means:- 
''' Different types of datatypes present inside the list .'''
# example:-  lst = [1,2.4,"hello",[1,2,3],true,2+3j]

# the list elements are separates by comma [,]

lst = list()
print(lst)      # op:- []

# To Update the value
'''Syntax:-  variable_name[index]=value'''
# example:- 
lst = [1,2,3,4,"hello",[1,23,4]]
lst[4] = "Bye"
print(lst)  

# op:- [1, 2, 3, 4, 'Bye', [1, 23, 4]]

lst[5][1] = "hello"
print(lst)

# op:- [1, 2, 3, 4, 'Bye', [1, 'hello', 4]]


# Indexing:-
# ----------
''' It is the process of extracting indivisual character from a collection is known as indexing .
--> It raises Index error if the specified index is not present .

Syntax:- variable_name[index]'''
# examples:-

lst = ["apple","orange","mango","grape"]
print(lst[3])
# op:- grape

print(lst[2][2])      #op:- n

''' if the specified index is not present it raises IndexError

print(lst[10]) 
op:- IndexError: list index out of range '''


# Slicing:-
# ---------
''' The process of extracting more than one character from a collection is known as slicing .
--> It accepts three arguments .
    1.start index
    2.end index
    3.step value
    
--> where start index by default starts with 0 
--> end index length of the list len()
--> step value by default +1 

Syntax:- variable_name[[si]:[ei]:[sv]]'''

# examples:- 
lst = ["apple","orange","mango","grape"]
print(lst[::])
# op:- ['apple', 'orange', 'mango', 'grape']

print(lst[::2])
# op:- ['apple', 'mango']

print(lst[0][::2])     #op:- ape

print(lst[10::])        #op:- []

# another example:-
lst = ["facebook",["whatsap"],"twitter",[["instagram"]]]
print(lst[3])
# op:-[['instagram']]

lst[2] = "messanger"
print(lst)
# op:- ['facebook', ['whatsap'], 'messanger', [['instagram']]]

print(lst[3][0])       #op:- ['instagram']

# Q. get the "gram" from instagram 
print(lst[3][0][0][5::])
# op:- gram


# another example:-
lst = ["a","b",["apple",[["mango"],"grapes"]]]

# Q. get apple 
print(lst[2][0])     #op:- apple

# Q. get mango
print(lst[2][1][0][0])    #op:- mango

# Q. update mango to orange
lst[2][1][0][0] = "orange"
print(lst)
# op:- ['a', 'b', ['apple', [['orange'], 'grapes']]]

# Q. get "gae" from grapes 
print(lst[2][1][1][::2])       #op:- gae


# METHODS IN LIST 
# ---------------
# TO ADD THE ELEMENTS
# -------------------

# 1. append():-
# -------------
''' It is an inbuild function which is used to add the element at last into a list .
--> It accepts only one argument and that can be both indivisual or collection datatype .
--> It will add the collection datatypes without unpacking .

Syntax:- variable_name.append(element)
'''
# examples:-
lst = [1,2,3,4,5]
lst.append(6)
print(lst)
# op:- [1, 2, 3, 4, 5, 6]

lst.append("hello")
print(lst)
# op:- [1, 2, 3, 4, 5, 6, 'hello']

'''
lst.append("Hey","Bye")
op:- TypeError: list.append() takes exactly one argument (2 given)  '''

lst.append(["Hey","Bye"])
print(lst)
# op:- [1, 2, 3, 4, 5, 6, 'hello', ['Hey', 'Bye']]

'''Without unpacking it will add the collection values .'''



# 2. extend():-
''' It is an inbuild function which is used to add the element atlast into a list .
--> It accepts only one arguments and that should be only collection datatype .
--> we can't pass indivisual datatypes .
--> It will add the elements by performing unpacking , and it will happens only once .

Syntax:- variable_name.extend(iterable/collection)'''

# examples:-

lst = [1,2,3,4]
lst.extend("hello")
print(lst)
# op:- [1, 2, 3, 4, 'h', 'e', 'l', 'l', 'o']

lst.extend(["good"])
print(lst)
# op:- [1, 2, 3, 4, 'h', 'e', 'l', 'l', 'o', 'good']

lst = ["a","b","c"]
lst.extend(["c","d","e"])
print(lst)
# op:- ['a', 'b', 'c', 'c', 'd', 'e']

lst = [1,2,3,4]
lst.extend([5,6,7,8])
print(lst)
# op:- [1, 2, 3, 4, 5, 6, 7, 8]

''' Conclusion:- Whenever we want single value we use append() and Whenever we want multiple value we use extend()'''


# 3. insert():-
# ------------
''' It is an inbuild function which is used to add the element at a specific position .
--> It accepts two arguments 
    1.index
    2.element
--> if the specified index is not present it will add the element at last .
--> It accepts both indivisual and collection datatype .

Syntax:- variable_name.insert(index,element)'''

# examples:-

lst = [1,2,4,5]
lst.insert(2,3)
print(lst)
# op:- [1, 2, 3, 4, 5]

'''if the specified index not present it will add the index at last into the list .'''
lst.insert(10,9)
print(lst)
# op:-[1, 2, 3, 4, 5, 9]


# TO REMOVE THE ELEMENTS 
# -----------------------
# 1. remove():-
# -------------
''' It is an inbuild function which is used to remove the first occured specified element from the left side .
--> It raises ValueError if the specified element is not present .

Syntax:- variable_name.remove(element)'''

# examples:-

lst = [1,2,3,4,5,3,4,5,6,7]
lst.remove(5)
print(lst)
# op:- [1, 2, 3, 4, 3, 4, 5, 6, 7]

'''error
lst.remove(55)
print(lst)
op:- ValueError: list.remove(x): x not in list    '''


# 2. pop():-
# ---------
''' It is an inbuild function which is used to remove the element based on the index .
--> By default it will remove the last element (-1) .
--> It returns the element which got removed .
--> It raises IndexError if the specified index is not present and also whenever the list is empty .

Syntax:- variable_name.remove([index])'''

# examples:-
lst = [11,22,"apple","manago"]
print(lst.pop())
# op:- manago

print(lst.pop(1))
# op:- 22

'''error 

print(lst.pop(10))
op:- IndexError: pop index out of range'''

lst.pop()
lst.pop()
print(lst)  #op:- []


'''error because list is empty now
lst.pop()
print()
op:- IndexError: pop from empty list  '''


# 3. clear():-
# ------------
''' It is an inbuild function which is used to remove all the elements from the list at the same time .
--> It won't accept any arguments .
-->The default value of list will be present [] .

Syntax:- variable_name.clear()'''

# examples:-

lst = [1,2,3,4,5,"hellol","bye"]
lst.clear()
print(lst) 
# op:- []

'''Error
lst.clear(9)
print(lst)
# op:- TypeError: list.clear() takes no arguments (1 given)
'''


# index():-
# ---------
''' It is an inbuild function which is used to return the position of a first occured specified element from the left side .
--> It accepts three arguments 
    1.Element
    2.start index
    3.end index
--> It raises value error if the specified element is not present .

Syntax:- variable_name.index(element,[si],[ei])'''

# examples:-

lst = [1,2,3,4,1,2,["apple"]]
print(lst.index(2))
# op:- 1

'''error
ValueError: list.index(x): x not in list
lst.index(5)
print(lst) 
'''

lst = ["apple","mango","grapes","orange"]
print(lst.index("grapes",0,4))
# op:- 2


# count():-
# ---------
''' It is an inbuild function which is used to returns the no.of times the specified element present .
--> It returns 0 if the specified element is not present .
--> It accepts only one argument .

Syntax:- variable_name.count(element)'''

# examples:-

lst = [1,2,3,4,1,2,3,2,2,5,2,6,7]
print(lst.count(2))
# op:-  5

print(lst.count(10))    #op:- 0    because the specified element is not present 

'''error
print(lst.count(2,4))
# op:- TypeError: list.count() takes exactly one argument (2 given)  '''


# reverse():-
# -----------
''' It is used to reverse the given list .
--> It won't accepts any arguments .

Syntax:- variable_name.reverse()'''

# examples:-

lst = [1,2,3,4,5]
print(lst.reverse())     #op:- None

lst.reverse()
print(lst)      #op:- [1, 2, 3, 4, 5]

res = lst.reverse()
print(res)


'''
The reverse() method reverses the original list in place. It changes the existing list instead of creating and returning a new list.'''

# examples:-

lst = [1, 2, 3, 4, 5]
res = lst.reverse()

print(lst)  # [5, 4, 3, 2, 1]
print(res)  # None

# or

lst = [1, 2, 3]
result = lst.append(4)

print(lst)     # [1, 2, 3, 4]
print(result)  # None

# or we can reverse the value by using slicing
# example:-
# ----------
lst = [1,2,3,4,5,6]
print(lst[::-1])
# op:- [6, 5, 4, 3, 2, 1]

''' If we use reverse the original value get changed .'''


# sort():-
# -------
''' It is an inbuild function which is used to arrange the elements either ascending or descending order .
--> By default it will arrange an elements in ascending order , becasue by default the reverse is "False" .
--> To arrange the elements in descending order we have declare the reverse as "True" .

Syntax:- variable_name.sort([reverse=True/False])'''

# examples:-
lst = [1,20,90,40,28,90,45]
print(lst.sort())
# op:- None

lst.sort()
print(lst)  
# op:- [1, 20, 28, 40, 45, 90, 90]

'''because it will update the original list .'''

# to make it descending
lst.sort(reverse=True)
print(lst)
# op:- [90, 90, 45, 40, 28, 20, 1]


# Interesting part 

lst = ["mango","apple","orange","fecebook"]
lst.sort()
print(lst)
# op:- ['apple', 'fecebook', 'mango', 'orange']

'''IMPORTANT:- it will not arranged by the alphabetic order , it will posible because of ascii value .
A-Z --> 65-90
a-z --> 97-122
"0"-"9" --> 48-57'''

lst = ["Mango","apple","orange","facebook","app"]
lst.sort()
print(lst)
# op:- ['Mango', 'app', 'apple', 'facebook', 'orange']

'''look at the above code Mango is comes first , because ascii value of capital "M" is less than as compare to where the small a-z start 97-122  '''

'''IMPORTANT:- it won't perform the operation if inside the list there are different types of datatype , it will accepts same datatype values .'''
# for examples:-

'''
lst = ["apple",1,2,"banana"]
lst.sort()
print(lst)
op:- TypeError: '<' not supported between instances of 'int' and 'str'   '''

# it can be like this 
lst = ["apple","1","2","banana"]
lst.sort()
print(lst)
# op:- ['1', '2', 'apple', 'banana']

'''becasue first ascii value "0"-"9" start from 48-57 that's why it start from numbers .'''

lst = [[3,2],[1,4],[3,7],[2,9]]
lst.sort()
print(lst)
# op:- [[1, 4], [2, 9], [3, 2], [3, 7]]

'''why because it will always check the first value .'''

lst.sort(reverse=True)
print(lst)
# op:- [[3, 7], [3, 2], [2, 9], [1, 4]]


# what is concatenation(+)
# ------------------------
''' It is a process of combining two or more same type of collection datatypes .
--> To perform concatenation we use addition operator (+) .'''
# examples:-

print("hello" + "bye")
# op:- hellobye

print("hello  " + "bye")
# op:-hello  bye

print([1,2,3,4] + [5,6,7,8])
# op:- [1, 2, 3, 4, 5, 6, 7, 8]

'''if we use different different datatype it will raises an error
# for examples:-
print("hello"+[1,2,3,4,5])
# op:-TypeError: can only concatenate str (not "list") to str   '''


# if try it in integer value then the result will be something different
# examples:-
print(10 + 20)   #op:- 30


# Replication:-
# -------------
''' It is the process of duplicating the data based on integer value .'''
# examples:-
print([1,2,3,4] * 2)
# op:- [1, 2, 3, 4, 1, 2, 3, 4]

print("hii" * 3)
# op:-hiihiihii

# if we do it with an intger value then the result will be different
# examples:-
print(2 * 4)        #op:- 8



# ---------------thank you-------------------------
























