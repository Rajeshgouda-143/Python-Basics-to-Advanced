
'''Input and Output statements'''

# Input():-
# ----------
''' It is an inbuilt function which is used to get the input from a user .
--> It store the input data in the form of string .
--> It accepts one argument called promt.

Syntax:- input([promt])'''
# examples:-
name = input("Enter your name: ")
age = input("Enter your name: ")
print(name)
''' here the age by default store the string , so we have to convert it into particular datatype .'''
print(int(age) + 10)
print(int(age) - 5)
print(int(age) * 2)

''' or we can directly take as an input like ....'''
# example:-
name = input("enter your name: ")
age = int(input("enter your age: "))
print(name)
print(age + 10)
print(age - 5)
print(age * 2)



# print():-
''' It is used to display the results .
--> It accepts three arguments 
    1. Elements
    2.Separator
    3.End

Syntax:- print(ele1,ele2,....,[sep=],[end=])'''

# sep=
''' It is used to separate the element present in a single print statement .
--> In python by default separator is Space .'''
# examples:-
print("hello","good")
print("hello","good",sep="-")
print("hello","every","one",sep="$")


# end=
''' It is used to separate the two print statement .
--> By default end() will be "new line" .'''
# examples:-
print("hello")
print("every")
print("one")
'''
Output:-
hello
every
one     '''

# or
print("hello",end=" ")
print("every",end=" ")
print("one")

# Output:- hello every one

# or

print("hello","every","one",sep="-",end=" ")
print("good",end=" ")
print("bye")

# Output:- hello-every-one good bye


