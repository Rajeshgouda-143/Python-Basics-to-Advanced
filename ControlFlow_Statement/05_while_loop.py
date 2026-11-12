# While Loop
# ------------
''' It is used to execute some setup instructions for "n" number of times until the condition is not satisfied .
--> For the while loop declaration of looping Variable is mandatory .
--> For the while loop updation is mandatory .

Syntax:- Variable_name = Value  //Variable declaration
         While condition:
                Statement
                updation(increament / decreament)
'''

# example:-
'''WAP TO PRINT "HELLO PYTHON" 5 TIMES .'''
# i = 1
# while i <=5:
#     print("Hello Python")
#     i+=1

'''op:-
Hello Python
Hello Python
Hello Python
Hello Python
Hello Python
'''

'''Q.2 WAP TO PRINT 1 TO 5 NUMBERS .'''
# i = 1
# while i <= 5:
#     print(i)
#     i+=1

'''op:-
1
2
3
4
5
'''

'''Q.3 WAP TO PRINT 5 TO 1 NUMBER .'''
# i = 5
# while i > 0:
#     print(i)
#     i-=1

'''op:-
5
4
3
2
1
'''

'''Q.4 WAP TO PRINT EVEN NUMBERS FROM 1 TO 10 .'''
# way-1
# i = 2
# while i <= 10:
#     print(i)
#     i+=2

'''op:-
2
4
6
8
10
'''
# way-2
# i = 1
# while i < 11:
#     if i%2 == 0:
#         print(i)
#     i+=1

'''op:-
2
4
6
8
10
'''

# way-3
# i = 1
# while i <= 10:
#     if i%2 == 0:
#         print(i)
#     i+=1

'''op:-
2
4
6
8
10
'''

'''Q.5 WAP TO PRINT ODD NUMBERS FROM 1 TO 10'''
# way-1
# i = 1
# while i <= 10:
#     print(i)
#     i+=2

'''op:-
1
3
5
7
9
'''
# way-2
# i = 1
# while i < 11:
#     if i%2 != 0:
#         print(i)
#     i+=1

'''op:-
1
3
5
7
9
'''

# way-3
# i = 1
# while i <= 10:
#     if i%2 != 0:
#         print(i)
#     i+=1

'''op:-
1
3
5
7
9
'''

'''Q.6 WAP TO CHECK THE FACTORIAL NUMBER OF 5 .'''
# no = 5
# fact = 1
# while no > 0:
#     fact = fact * no
#     no=no-1
# print(fact)

'''op:- 120'''

'''Q.7 WAP TO CHECK '''
no1 = int(input("enter the no1:"))
no2 = int(input("enter the no2:"))
i = 1

while i <= no2:
    print(f'{no1} * {i} = {no1*i}')
    i+=1

'''op:-
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
'''





