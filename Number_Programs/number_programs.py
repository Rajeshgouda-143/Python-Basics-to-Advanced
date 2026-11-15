'''THIS ALL NUMBER PROGRAMS ARE IMPORTANT FOR THE INTERVIEW .'''

# 1. Duck Number:-
# ---------------
''' A Duck Number in Python is a number that contains at least one 0 (zero), but the zero must not be at the beginning of the number.
Examples
--------
Number	       Result	          Reason
-------      ----------         ----------
1023	    Duck Number	        Contains 0
506	        Duck Number	        Contains 0
12045	    Duck Number	        Contains 0
1234	  Not a Duck Number	    No zero
0123	  Not a Duck Number	    Leading zero    '''

# num = int(input("Enter a number: "))
# temp = num
# count = 0

# while temp > 0:
#     rem = temp % 10
#     if rem == 0:
#         count += 1
#     temp = temp // 10

# if count > 0:
#     print("Duck Number")
# else:
#     print("Not a Duck Number")

# OR

'''By using typecasting'''

# num = input("Enter a number: ")

# if num[0] == '0':
#     print("Not a Duck Number")

# elif '0' in num:
#     print("Duck Number")

# else:
#     print("Not a Duck Number")


'''IMPORTANT:-
Suppose the user enters:

num = int(input("Enter a number: "))

And gives input: 0123

Python converts the input into an integer:
num = 123

Why? Because integers do not preserve leading zeros.
So, the previous program will treat 0123 as 123 and print '''


# 2. Perfect Square:-
# -------------------
''' A Perfect Square is a number that can be expressed as the product of an integer multiplied by itself.

For example:
 4 = 2 * 2
 9 = 3 * 3
 16 = 4 * 4
 25 = 5 * 5
 36 = 6 * 6
 '''
# example:-
# no = int(input("enter the no:"))
# i = 1

# while i * i <= no:
#     if i * i == no:
#         print("Perfect Number")
#         break
#     i+=1
# else:
#     print('Not a Perfect Number')

# OR

# no = int(input("enter the no: "))
# temp = no ** 0.5

# if temp * temp == no:
#     print(f'The {int(temp)} is a Perfect Number')
# else:
#     print("Not a Perfect Number")


# BY USING isinstance():-
# -----------------------
''' In Python, isinstance() is a built-in function used to check whether a variable belongs to a particular data type (class).
Syntax:- isinstance(object, classinfo)

object → The variable you want to check.
classinfo → The data type or class you want to compare it with.  '''
# example:-
# a = 10
# print(isinstance(a, int))    

# op:- True

''' Checking multiple data types
You can also check multiple types using a tuple.'''
# a = 10.5
# print(isinstance(a, (int, float)))

'''Output: True
It returns True if the object belongs to at least one of the specified types.'''

# to check perfect number by using isinstance() 
# example:-
# no = int(input("enter the no: "))
# temp = no ** 0.5

# if isinstance(temp , (int,float)):
#     print("Perfect Number")
# else:
#     print("Not a Perfect Number")



# 3. Reverse A Number:- (IMPORTANT)
# ---------------------
'''WAP TO REVERSE A GIVEN NUMBER .'''

'''by using typecasting
example:-'''
# no = int(input("enter the no: "))
# s = str(no)
# print(s[::-1])

'''without typecasting
 example:-'''
# no = int(input("enter the no: "))
# rev = 0
# while no > 0:
#     rem = no % 10
#     rev = rev * 10 + rem
#     no = no//10
# print(rev)



# 4. Palindrome Number:-(important)
# ----------------------
''' A Palindrome Number is a number that remains the same when it is reversed.
In simple words, the original number and reversed number must be equal.'''

'''by using typecasting
example:-'''
# no = int(input("enter the no: "))
# s = str(no)

# if s == s[::-1]:
#     print(f"The {s} is a Palindrome Number")
# else:
#     print("Not a Palindrome Number")

'''without typecasting
 example:-'''
# no = int(input("enter the no: "))
# temp = no
# rev = 0
# while no > 0:
#     rem = no % 10
#     rev = rev * 10 + rem
#     no = no//10
# if temp == rev:
#     print(f"The {temp} is a Palindrome Number")
# else:
#     print("Not a Palindrome Number")


'''Q. WAP TO FIND ALL THE DIGITS PRESENT IN A GIVEN NUMBER .'''
# example:-
# num = int(input("Enter a number: "))

# while num > 0:
#     rem = num % 10
#     print(rem)
#     num = num // 10



# 5. Spy Number:- (important)
# ----------------
'''A Spy Number is a number in which the sum of its digits is equal to the product of its digits.

In simple words:
1. Add all the digits.
2. Multiply all the digits.
3. If both results are equal, it is a Spy Number.  '''
# example:- 123 (spy number)
# no = int(input("enter the no: "))
# sum = 0
# pro = 1

# while no > 0:
#     rem = no % 10
#     sum = sum + rem
#     pro = pro * rem
#     no = no//10
# if sum == pro:
#     print("Spy Number")
# else:
#     print("Not a Spy Number")


# 6. Harshad / Niven Number:-(important)
# ---------------------------
''' A Harshad Number (also called Niven Number) is a number that is completely divisible by the sum of its digits.

In simple words:
1. Find the sum of all digits.
2. Divide the original number by that sum.
3. If the remainder is 0, it is a Harshad Number.'''
# example:- 18 (niven number)
# no= int(input("enter the no: "))
# temp = no
# sum = 0

# while no > 0:
#     rem = no % 10
#     sum = sum + rem
#     no = no // 10
# if temp % sum == 0:
#     print("Harshad Number")
# else:
#     print("Not a Harshad Number")



# 7. Armstrong Number:-(*** Important )
# ---------------------
''' An Armstrong Number is a number in which the sum of each digit raised to the power of the total number of digits is equal to the original number.

suppose = input is 153
1. The total number is = 3 
2. raised the power 3 in each number and add them = 1 + 125 + 27 => 153
3. compare the original number with the result , 153 == 153 .'''
# code:-
# no = int(input("enter the no: "))
# temp = no
# sum = 0
# length = len(str(no))

# while no > 0:
#     rem = no % 10
#     sum = sum + rem ** length
#     no = no//10
# if temp == sum:
#     print("Armstrong Number")
# else:
#     print("Not a Armstrong Number")


# 8. Neon Number:- (** Important)
# ------------------
''' A Neon Number is a number in which the sum of the digits of its square is equal to the original number.

In simple words:
1. Calculate the square of the given number.
2. Extract all digits from the square.
3. Calculate the sum of those digits.
4. Compare the sum with the original number.'''
# code:-
# no = int(input("enter the no: "))
# sq = no ** 2
# sum = 0

# while sq > 0:
#     rem = sq % 10
#     sum = sum + rem
#     sq = sq//10
# if no == sum:
#     print("Neon Number")
# else:
#     print("Not a Neon Number")


# 9. Disarium Number:- (** Important)
# ---------------------
''' A Disarium Number is a number in which the sum of its digits, raised to the power of their respective positions, is equal to the original number.

In simple words:
1. First digit is raised to power 1.
2. Second digit is raised to power 2.
3. Third digit is raised to power 3.
4. Continue until all digits are covered.
5. Add all the results and compare with the original number.

like -> input is 135  =>  1 + 9 + 125'''
# code:-
# no = int(input("enter the no: "))
# temp = no
# sum = 0

# while no > 0:
#     rem = no % 10
#     sum = sum + rem ** len(str(no))
#     no = no//10
# if temp == sum:
#     print("Disarium Number")
# else:
#     print("Not a Disarium Number")



# 10. Automorphic Number:-(** Important)
# ------------------------
''' An Automorphic Number is a number whose square ends with the same digits as the original number.

In simple words:
1. Take a number.
2. Calculate its square.
3. Check whether the square ends with the original number.
4. If it matches, it is an Automorphic Number.

like->  25 ** 2 = 625   look at here the 25 is end of the 625'''
# code:-
# no = int(input("enter the no: "))
# temp = no
# sq = no ** 2
# count = 0

# while no > 0:
#     count += 1
#     no = no // 10

# divisior = 10 ** count
# if sq % divisior == temp:
#     print("Automorphic Number")
# else:
#     print("Not a Automorphic Number")



# 11. Perfect Number:- (** Important)
# --------------------
''' A Perfect Number is a positive number that is equal to the sum of all its proper divisors (excluding the number itself).

In simple words:
1. Find all the factors of a given number, excluding the number itself.
2. Add those factors.
3. Compare their sum with the original number.
4. If both are equal, it is a Perfect Number.  

like -> let input is 6 so all the number till 6 is = 1, 2, 3, 4, 5, 6 now check which are the numbers divisible by 6 .those are (1, 2, 3 = 1 + 2 + 3 = 6)'''
# code:-
# no =int(input("enter the no: "))
# sum = 0
# i=1

# while i < no:
#     if no % i == 0:
#         sum = sum + i
#     i+=1

# if sum == no:
#     print("Perfect Number")
# else:
#     print("Not a Pefect Number")



# 12. Fibonacci Series:-(*** Important)
# ------------------------
''' A Fibonacci Series is a sequence of numbers in which each number is the sum of the previous two numbers.
The series starts with 0 and 1.

example:-  0 1 1 2 3 5 8 13 21 34......'''
# code:-  Simple code
# no1 = 0
# no2 = 1
# i = 1
# no = int(input("enter the no: "))
# print(no1 , no2 , end=" ")

# while i <= no - 2:
#     no3 = no1 + no2
#     print(no3, end=" ")
#     no1 = no2
#     no2 = no3
#     i+=1

# By using Recursion (*** Important)

# def fibonacci(no):
#     if no == 0:
#         return 0
#     elif no == 1:
#         return 1
#     else:
#         return fibonacci(no -1) + fibonacci(no - 2)
# no = int(input("enter the no: "))
# for i in range(no):
#     print(fibonacci(i),end=" ")



# 13. Happy Number:-
# ------------------
''' A number is called a Happy Number if the sum of the squares of its digits eventually becomes 1 after repeatedly performing the same operation.
If it never reaches 1 and enters a repeating cycle, it is an Unhappy Number.

Example: 19

Follow the sequence
19
1² + 9² = 82

82
8² + 2² = 68

68
6² + 8² = 100

100
Happy!
1² + 0² + 0² = 1

Since the final result is 1, 19 is a Happy Number.'''
# code:-
# num = int(input("Enter a number: "))
# temp = num

# while temp != 1 and temp != 4:
#     sum = 0
#     while temp > 0:
#         rem = temp % 10
#         sum = sum + rem ** 2
#         temp = temp // 10
#     temp = sum

# if temp == 1:
#     print("Happy Number")
# else:
#     print("Not a Happy Number")



# 14. Strong Number:-
# -------------------
''' A Strong Number is a number in which the sum of the factorials of its individual digits is equal to the original number.

In simple words:
1. Extract each digit from the number.
2. Find the factorial of each digit.
3. Add all the factorials.
4. Compare the sum with the original number. 

example:- 145'''
# code:-
# no = int(input("enter the no:"))
# temp = no
# sum = 0
# while no > 0:
#     rem = no % 10
#     fact = 1
#     while rem > 0:
#         fact = fact * rem
#         rem = rem - 1
#     sum = sum + fact
#     no = no//10
# if temp == sum:
#     print("Strong Number")
# else:
#     print("Not a Strong Number")



# 15. Xylem and Phloem Number:-
# -----------------------------
'''1. Xylem Number
A number is called a Xylem Number when the sum of its extreme digits (first and last digits) is equal to the sum of its middle digits.

Example: 34326
- Extreme digits: 3 + 6 = 9
- Middle digits: 4 + 3 + 2 = 9
Since both sums are equal, 34326 is a Xylem Number.
2. Phloem Number
A number is called a Phloem Number when the sum of its extreme digits is NOT equal to the sum of its middle digits.

Example: 12345
- Extreme digits: 1 + 5 = 6
- Middle digits: 2 + 3 + 4 = 9
Since both sums are different, 12345 is a Phloem Number.'''

# Python program using while loop
num = int(input("Enter a number: "))
temp = num
extreme_sum = 0
middle_sum = 0
last = temp % 10
extreme_sum = last
temp = temp // 10
while temp >= 10:    
    rem = temp % 10    
    middle_sum = middle_sum + rem    
    temp = temp // 10

extreme_sum = extreme_sum + temp
if extreme_sum == middle_sum:    
    print("Xylem Number")
else:    
    print("Phloem Number")


'''Dry run: 34326
Step	                        Value
Last digit	                      6
Middle digits	            2 + 3 + 4 = 9
First digit	                      3
Extreme sum	                  6 + 3 = 9
Middle sum	                      9                             '''












