#  STRING FORMATING 
# -----------------
''' String formating we can be achieve in three ways .
    1. with the help of "%" operator
    2. with the help of format() 
    3. with the help of "f" String . '''

# 1. with the help of "%" operator
'''
%s--> for String
%d--> for integer
%f--> for float'''
# examples:-
name = input("Enter your name: ")
age = int(input("enter your age: "))
print("hey %s your age is %d"%(name,age))

# op:- hey rajesh your age is 23

'''But one drawback is here , that is if we change the value , means in the place of string if we pass integer value or in the place of integer if we pass string then it will raises an error .
# examples:-

name = input("Enter your name: ")
age = int(input("enter your age: "))
print("hey %s your age is %d"%(age,name))

# op:-  TypeError: %d format: a real number is required, not str   '''


# 2. with the help of format():-
# ------------------------------
''' for format() we use curly braces {} .'''
# examples:-
# examples:-
name = input("Enter your name: ")
age = int(input("enter your age: "))
print("hey {} your age is {}".format(name,age))

# op:- hey rajesh your age is 23

''' But here one drawback , that is when we change the value it won't affect or won't raises any error .'''
# for example:-
name = input("Enter your name: ")
age = int(input("enter your age: "))
print("hey {} your age is {}".format(age,name))

# op:- hey 23 your age is rajesh    // look at the output


# 3. With the help of "f" string:- (important)
# --------------------------------------------
'''We use it to update or code redeability inside the curly braces .
--> Most of the time we use it .'''
# examples:-
name = input("Enter your name: ")
age = int(input("enter your age: "))
print(f"Hey {name} your age is {age}")

# op:- Hey rajesh your age is 23




