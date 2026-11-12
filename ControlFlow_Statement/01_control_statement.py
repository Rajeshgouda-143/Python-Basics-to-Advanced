# CONTROL STATEMENT :-
# --------------------
''' Control statements are used to control the flow of execution of a program .
--> Normally, Python executes statements from top to bottom. Control statements allow us to make decisions, repeat tasks, or change the normal flow of execution.
--> It is classified into two types .
    1. Conditional Statements 
    2.Looping Statements '''

'''
Decision-Making Statements
---------------------------
Decision-making statements execute code depending on whether a condition is true or false.'''

# 1. Conditional Statements:-
# -----------------------------
''' This statement are used to specify what has to be done if the condition is satisfied and what has to be done if the condition is not satisfied .
--> It is classified into four types .
    1. if statement
    2. if-else statement
    3. if-elif-else statement
    4. nested if statement'''

# if statement:-
# ---------------
''' The if statement executes a block of code only when its condition is True.

Syntax:- if condition:
            true statement block'''

# examples:-
'''Q1. WAP TO CHECK GIVEN NUMBER IS A POSITIVE NUMBER .'''
# no = int(input("Enter the no: "))
# if no > 0:
#     print(f'The {no} is a positive number')

# op:- The 2 is a positive number


'''Q2. WAP TO CHECK YOU ARE ADULT OR NOT .'''
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult.")

# op:- You are an adult.
'''
Explanation
- age = 20 stores the value 20.
- age >= 18 checks whether the age is at least 18.
- The condition is True.
- Therefore, Python executes the print() statement.'''


# What if the condition is false?
# age = 15
# if age >= 18:    
#     print("You are an adult.")

# print("Program finished.")

'''Output: Program finished.
The message inside the if block is skipped because the condition is false.'''


'''Q3. WAP TO CHECK THE NUMBER IS EVEN .'''
# no = int(input("Enter the number: "))
# if no%2==0:
#     print(f"{no} is even")

# op:- 20 is even

'''Q4. WAP TO CHECK GIVEN NUMBER IS DIVISIBLE BY 2 AND 3 .'''
# no = int(input("Enter your number: "))
# if no%2==0 and no%3 == 0:
#     print(f"The {no} is divisible by 2 and 3")

# op:- The 6 is divisible by 2 and 3


'''Q5. WAP TO CHECK FIRST NUMBER IS GREATER THAN THE SECOND NUMBER .'''
# no1 = int(input("enter the no1: "))
# no2 = int(input("enter the no2: "))

# if no1 > no2:
#     print(f"The {no1} is greater than {no2}")

# op:- The 2 is greater than 1


'''Q6. WAP TO CHECK WEATHER GIVEN CHARACTER IS A ALPHABET  .'''
# char = input("Enter a character: ")
# if char.isalpha():
#     print("The character is a alphabet .")

# op:- The character is a alphabet .


'''Q7. WAP TO CHECK THE GIVEN CHARACTER IS A UPPERCASE CHARACTER .'''
# char = input("enter a char: ")
# if char.isupper():
#     print("The given character is a uppercase")


'''Q8. WAP TO CHECK THE GIVEN YEAR IS A CENTURY YEAR .'''
# year = int(input("enter the year: "))
# if year%100 == 0:
#     print("The given year is a century year.")


'''Q9. WAP TO CHECK IF THE GIVEN NUMBER IS ZERO .'''
# no = int(input("Enter a number:"))
# if no == 0:
#     print("The given number is a zero.")


'''10. WAP TO CHECK THE FIRST NUMBER IS DIVIDED BY SECOND NUMBER .'''
# no1 = int(input('Enter a no1: '))
# no2 = int(input('Enter a no2: '))

# if no1%no2==0:
#     print(f"The {no1} divisible by {no2}")


'''Q11. WAP TO CHECK THE CHARACTER ENTERED BY THE USER IS A VOWEL .'''
# char = input("Enter a char: ")
# if char.lower() in "aeiou":
#     print(f"The {char} is a vowel")


'''Q12. WAP TO CONVERT FIRST LETER OF THE WORD INTO UPPERCASE IF IT IS STARTING WITH VOWEL '''
# word = input("Enter a word: ")
# if word[0].lower() in "aeiou":
#     print(f"{word[0].upper()}")     #OP:- A

# or

# word = input("Enter a word: ")

# if word[0].lower() in "aeiou":
#     word = word[0].upper() + word[1:]

# print(word)   #OP:- Apple


'''Q13. WAP TO CHECK A NUMBER ENTERED BY THE USER IS A MULITPLE OF 5 .'''
# no = int(input("Enter a number: "))
# if no%5==0:
#     print("The no is a multiple of 5")


'''q14. WAP TO CHECK THE GIVEN STRING IS A PALINDROME .'''
# s = input("Enter the string: ")
# if s == s[::-1]:
#     print("The string is a palindrome")

# or

# without TypeCasting
# s = input("Enter a string: ")
# res=""
# for i in s:
#     res=i+res
# if s == res:
#     print("palindrome")
# else:
#     print("Not a palindrome")



# if-else statement
# ------------------
''' The if-else statement selects one of two blocks based on a condition.
--> If the condition is True, the if block executes.
--> If the condition is False, the else block executes.

Syntax:- if condition:   
             Executes if True
         else:  
             Executes if False     '''


# Example:-1
# number = 7
# if number % 2 == 0:    
#     print("Even number")
# else:    
#     print("Odd number")


'''Output:Odd number

Explanation
The modulus operator % returns the remainder.
7 % 2 == 0
This condition is false because 7 % 2 equals 1.
Therefore, Python executes the else block.

'''

# Real-world example: Login:-2
# password = "python123"
# if password == "python123":    
#     print("Login successful")
# else:   
#     print("Incorrect password")

# Output: Login successful


'''Q.3 WAP TO CHECK WEATHER THE GIVEN NUMBER IS A EVEN NUMBER OR ODD NUMBER .'''
# no = int(input("Enter a number: "))
# if no%2==0:
#     print("EVEN")
# else:
#     print("ODD")


'''Q.4 WAP TO CONVERT THE GIVEN CHARACTER INTO UPPERCASE IF IT IS A LOWERCASE CHARACTER ELSE CONVERT INTO LOWER .'''
# char = input("Enter a char: ")
# print(char.swapcase())

# # or

# char = input("Enter a char: ")
# if char.islower():
#     print(char.upper())
# else:
#     print(char.lower())

# or

# if "A"<=char and char<="Z":
# # or
# if "A"<=char<="Z":
#     print(char(ord(char) + 32))
# else:
#     print(char(ord(char) -32 ))



# TWO IMPORTANT CONCEPTS (ord(), chr())
# ---------------------------------------
# 1.ord():-
# ---------
''' It is used to return the ASCII value based on the character .

Syntax:- ord(character)'''

# Example 1: Uppercase Letter
# --------------------------
# print(ord('A'))

# Output:65
# Explanation: The Unicode code point of 'A' is 65.


# Example 2: Lowercase Letter
# ---------------------------
# print(ord('a'))
# print(ord('b'))
# print(ord('z'))
# '''
# Output:
# 97
# 98
# 122'''


# Example 3: Digits
# -----------------
# print(ord('0'))
# print(ord('1'))
# print(ord('9'))
'''
Output:
48
49
57

Important: '5' is a character, not the integer 5.'''

# print(ord('5'))  # Valid: 53
# print(ord(5))    # TypeError


# 2. What is chr() in Python ?
# -----------------------------
'''The chr() function returns the character represented by a given Unicode code point.

Syntax: chr(number)'''


# Example 1: Convert Number to Character
# ---------------------------------------
# print(chr(65))

# Output: A

# Example 2: More Characters
# ----------------------------
# print(chr(66))
# print(chr(97))
# print(chr(48))

'''
Output:
B
a
0

Explanation:
- chr(66) → 'B'
- chr(97) → 'a'
- chr(48) → '0 '''


'''Remember:
- ord() converts a character into its code point.
- chr() converts a code point into its character.
'''

'''
4. Using ord() and chr() Together
You can use both functions to convert a character into its code point and then back into a character.'''
# char = 'A'
# number = ord(char)
# result = chr(number)
# print(number)
# print(result)

'''Output:
65
A
The process is: 'A' → ord('A') → 65 → chr(65) → 'A'''


# 5. Practical Example: Get the Next Character
# Suppose you want to get the next character after 'A'.
# char = 'A'
# next_char = chr(ord(char) + 1)
# print(next_char)

# Output: B

'''
How does it work?
1. ord('A') returns 65.
2. 65 + 1 becomes 66.
3. chr(66) returns 'B'.'''

# You can also try:
# print(chr(ord('a') + 1))
# print(chr(ord('C') + 1))

'''Output:
b
D

Note: This method follows Unicode code points; it does not automatically wrap from 'Z' back to 'A'.'''


# 6. Important Examples for Practice
# print(ord('A'))
# print(ord('Z'))
# print(ord('a'))
# print(ord('z'))
# print(chr(65))
# print(chr(90))
# print(chr(97))
# print(chr(122))


'''Output:
65
90
97
122
A
Z
a
z

Quick Reference
Character	ord() Result
'A'	65
'B'	66
'Z'	90
'a'	97
'b'	98
'z'	122
'0'	48
'1'	49'''


'''Q5. WAP TO CHECK WEATHER GIVEN STRING CONTAINS EVEN LENGTH OR ODD LENGTH .'''
# s = input("Enter the string: ")
# if len(s)%2==0:
#     print("The string contains even length")
# else:
#     print("The string contains odd length")


'''Q6. WAP TO CHECK IF A NAME START WITH CAPITAL LETER , IF IS IS STARTING WITH CAPITAL LETER REVERSE AND PRINT ELSE PRINT HALF OF THE NAME .'''

# s = input("Enter the string: ")
# for i in s:
#     if i[0].isupper():
#         res = i[0] + s[1:]
#         print(res[::-1])
# else:
#     res = s[:len(s)//2] 
#     print(res)

# or

# s = input("enter the string: ")
# if s.istitle():
#     print(s[::-1])
# else:
#     print(s[:len(s)//2])

# or

# s = input("enter the string:")
# if s[0].isupper():
#     print(s[::-1])
# else:
#     print(s[:len(s)//2])/


'''Q.6 WAP TO CHECK IF THE SUM OF TWO NUMBERS IS EVEN OR ODD .'''
# no1 = int(input("enter the no1:"))
# no2 = int(input("enter the no:"))
# sum_of_no = no1 + no2
# if sum_of_no %2 == 0:
#     print(f"The sum of {no1} + {no2} = {no1 + no2} is even")
# else:
#     print("The sum of number is odd")


'''Q.7 WAP TO CHECK IF THE LAST DIGIT OF A NUMBER IS EVEN OR ODD  '''
# no = int(input("ente the no: "))
# res = str(no)
# if int(res[-1])%2:
#     print(f"The no {res[-1]} is even")
# else:
#     print(f"The no {res[-1]} is odd")

# or

# no = input("enter the no:")
# last_digit = no[-1]

# if int(last_digit) % 2==0:
#     print("The no is even")
# else:
#     print("The no is odd")

# no = int(input("enter the no:"))
# while no > 0:
#     rem = no % 10
#     if rem % 2 ==0:
#         print(f"The no {rem} is even")
#         break
#     else:
#         print(f"The no {rem} is odd")
#     no = no//10
   

'''Q.8 WAP TO CHECK IF TWO NUMBERS HAVE THE SAME LAST DIGITS .'''
# no1 = input("Enter the no1:")
# no2 = input("Enter the no2:")

# if no1[-1] == no2[-1]:
#     print("Both the no have the same last digit")
# else:
#     print("Both doesn''t have the same last two digit")


''' WAP TO CHECK WHETHER THE GIVEN NUMBER IS A MULTIPLE OF 2 , IF IT IS MULTIPLE OF 2 MAKE IT SQUARE ELSE MAKE IT CUBE .'''
# no = int(input("enter the no: "))
# if no % 2 == 0:
#     print(no**2)
# else:
#     print(no**3)


''' WAP TO CHECK IF THE ENTERED AGE IS GREATER THAN OR EQUAL TO 18, PRINT YOU ARE ELIGIBLE TO VOTE , ELSE NOT ELIGIBLE '''
# age = int(input("enter the age: "))
# if age >= 18:
#     print("Eligible for vote ")
# else:
#     print("Not eligible for vote")


''' WAP TO DISPLAY "HEY" IF THE USER ENTERED NUMBER IS POSITIVE ELSE PRINT "BYE" '''
# no = int(input("enter the no: "))
# if no > 0:
#     print("Hey")
# else:
#     print("Bye")


'''WAP TO PRINT THE GIVEN CHARACTER UPPER IF IT IS LOWER AND VICE VERSA '''
# char = input("enter the character: ")
# if char.islower():
#     print(char.upper())
# else:
#     print(char.lower())

# OR 

# char = input("enter the char: ")
# print(char.swapcase())


# 3. if-elif-else Statement:-
# ---------------------------
'''The if-elif-else statement is used to check multiple conditions. Python executes the first block whose condition is True.

Syntax:
if condition1:   
      statement1
elif condition2:    
    statement2
elif condition3:    
    statement3
else:    
    statement4
    
'''



'''elif means else if.
Example 1: Find the Grade
--------------------------
marks = 85
if marks >= 90:    
    print("Grade A")
elif marks >= 75:    
    print("Grade B")
elif marks >= 50:    
    print("Grade C")
else:    
    print("Fail")


Output:
Grade B


How does it work?
Python checks the conditions one by one:
Condition	Result
marks >= 90	False
marks >= 75	True
marks >= 50	Not checked
else	Not executed

Once Python finds a true condition, it executes that block and skips the remaining branches.

'''


# Q.2 example:-
# no = int(input("enter the no: "))

# if no > 0:
#     print("Positive Number")
# elif no < 0:
#     print("Negative Number")
# else:
#     print("Neutral")


''' Q.3 WAP TO 
PRINT "FIZZBUZZ" IF THE GIVEN NUMBER IS DIVISIBLE BY BOTH 5 AND 3 ELSE
PRINT "FIZZ" IF THE GIVEN NUMBER IS DIVISIBLE ONLY 5  ELSE
PRINT "BUZZ" IF THE GIVEN NUMBER IS DIVISIBLE BY ONLY 3 .'''

# no = int(input("enter the no: "))
# if no % 5 == 0 and no % 3 == 0:
#     print("FIZZBUZZ")
# elif no % 5 == 0:
#     print("FIZZ")
# elif no % 3 == 0:
#     print("BUZZ")

'''IMPORTANT:- Here if we use else block , then if we pass anything instead of 3 and 5 then it will return "BUZZ .'''



# 4. Nested if:-
# ---------------
'''When we write an if statement inside another if statement, it is called a Nested if statement.
In simple words, an if inside another if is called nested if.

Syntax:-

if condition1:
    if condition2:
        statement1
    else:
        statement2
else:
    statement3
'''

'''
How does it work?
1. First, Python checks condition1.
2. If it is True, Python enters the outer if block.
3. Then it checks condition2.
4. If it is True, the inner if block executes.
5. Otherwise, the inner else block executes.
6. If the outer condition is False, the outer else block executes.  '''


# Example 1: Check Age and ID
age = 22
has_id = True
if age >= 18:    
    if has_id:        
        print("You are eligible for entry")    
    else:        
        print("Please bring your ID")
else:    
    print("You are not eligible for entry")



# Output: You are eligible for entry

'''Explanation
- age >= 18 → True
- Python enters the outer if.
- has_id → True
- Python enters the inner if.
- It prints "You are eligible for entry". '''


'''Q1.  WAP TO CHECK THE USER IS EXIST OR NOT .'''
# user_name = input("Enter the usernam: ")
# user_password = input("Enter the password: ")

# if user_name == "Rajesh":
#     if user_password == "Raj@9337":
#         print("Login successfully")
#     else:
#         print("Incorect Password")
# else:
#     print("Incorect Username")


# OR

user_password = {"Srabani":"Papli@123","Pradeep":"Pra@1234","Rajesh":"Rajesh@143"}
user_name = input("Enter the username: ")

if user_name in user_password:
    password = input("Enter the password:")

    if password == user_password[user_name]:
        print("Login Succefully")
    else:
        print("Invalid Password")
else:
    print("User doesn't exits ")

    































