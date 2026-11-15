# For Loop 
# ----------
''' It is used to execute some setup instructions for "n" number of times .
--> For the for_loop declaration of looping variable is not required .
--> For the for_loop updation is not required .

or

A for loop is used when we want to execute a block of code repeatedly, usually by going through a sequence such as a list, string, tuple, 
or range().

Syntax:
for variable in range / collection:    
    statement 1
    statement 2
    ...........
    ..........

Here:
- for starts the loop.
- variable stores each value one by one.
- in takes values from the sequence.
- The indented code executes for each value.'''

'''
5. Difference between for loop and while loop
---------------------------------------------
                    For loop	                                                                    While loop
                    ---------   
Commonly used to iterate over a sequence or range	                                    Used while a condition remains true
Often used when the number of iterations is known	                               Useful when the stopping point depends on a condition
Advances through the sequence automatically	                                            You usually update the variable yourself

'''
# What is range():-
# -----------------
''' It is a Inbuild function which is used to returns the values based on the starting value , ending value , and step value .
--> start value of range is by default "0" 
--> end is the length of the collection .
--> step value is by default "+1" 

'''
# examples:-

'''Q1. WAP TO PRINT 1 TO 5 .'''
# for i in range(5):
#     print(i)

'''
op:-
1
2
3
4

 why It print upto 4 , because the last or ending value is not Included .'''

# for i in range(6):
#     print(i)

'''
op:-
1
2
3
4
5
'''

'''Q2. WAP TO PRINT 1 TO 10 NUMBERS .'''
# for i in range(1,11):
#     print(i)

# for i in range(11):
#     print(i)


'''Q3. WAP TO PRINT 5 TO 1 NUMBERS .'''
# for i in range(5,0,-1):
#     print(i)


'''Q4. WAP TO PRINT EVEN NUMBERS FROM 1 TO 10 .'''
# for i in range(1,11):
#     if i%2==0:
#         print(i)


# for i in range(2,11,+2):
#     print(i)


'''Q5. WAP TO PRINT ODD NUMBERS FROM 1 TO 10.'''
# for i in range(1,11):
#     if i%2!=0:
#         print(i)

# for i in range(1,11,+2):
#     print(i)


'''Q6. WAP TO TRAVERSE THROUGH A STRING .'''
s = "Python"
# for i in range(len(s)):
#     print(i)               #It will print the index value starting from 0 .(0,1,2,3,4,5)

#     print(s[i])            #It will print the value of the collection .


'''Note:- When we use range , when we want to work with both index and their elements .
--> When we use colection datatype , when we want only the elements .'''

'''Q7. WAP TO TRAVERSE THROUGH A LIST BY USING while , for (with range and collection)'''
lst = ["Apple","Mango","Grapes","Tamarind"]

# for i in lst:        #collection
#     print(i)

# for i in range(len(lst)):
#     print(i , end=" ")         #op:- 0 1 2 3 

# for i in range(len(lst)):
#     print(lst[i] , end=" ")     #op:- Apple Mango Grapes Tamarind 

'''By using while loop '''

# i = 0
# while i<len(lst):
#     print(i , end=" ")     #op:- 0 1 2 3 
#     i+=1

# i = 0
# while i<len(lst):
#     print(lst[i] , end=" ,")   #op:- Apple ,Mango ,Grapes ,Tamarind ,
#     i+=1


'''IMPORTANT NOTE:- we should use while_loop, for_loop, range(), collection, in String, List, and Tuple datatype .
--> But we can't use while_loop, for_loop, range() in set,dictionary but  we can use collection syntax for it .'''
# examples:-
'''Q8. WAP TO TRAVERSE THROUGH A SET .'''
# by using collection
# s = {"a","b","c","d"}
# for i in s:
#     print(i , end=" ")      #op:- b d c a 

'''whenever we will try to find the index it will raises TypeError , because it is not an ordered datatype'''
# s = {"a","b","c","d"}
# for i in s:
#     print(s[i])    

# op:-  TypeError: 'set' object is not subscriptable

# by using range()
# s = {"a","b","c","d"}
# for i in range(len(s)):
#     print(s[i])

# op:- TypeError: 'set' object is not subscriptable

# By using while loop
# s = {"a","b","c","d"}
# i=0
# while i<len(s):
#     print(i , end=" ")      #op:- 0 1 2 3 
#     i+=1

# s = {"a","b","c","d"}
# i=0
# while i<len(s):
#     print(s[i] , end=" ")      #op:- TypeError: 'set' object is not subscriptable
#     i+=1


'''Q9. WAP TO TRAVERSE THROUGH A DICTIONARY .'''
# d = {"a":1,"b":2,"c":3,"d":4}
# for i in d:
#     print(i , end=" ")          #op:- a b c d (keys)

# d = {"a":1,"b":2,"c":3,"d":4}
# for i in d:
#     print(d[i] , end=" ")          #op:- 1 2 3 4 (values)

'''By using range()'''
# d = {"a":1,"b":2,"c":3,"d":4}
# for i in range(len(d)):
#     print(d[i])                   #op:- KeyError: 0

# d = {"a":1,"b":2,"c":3,"d":4}
# for i in range(len(d)):
#     print(i, end=" ")                   #op:- 0 1 2 3 


d = {"a":1,"b":2,"c":3,"d":4}
# for i in d.values():
#     print(i)

# for i in d.keys():
#     print(i)

# for i in d.items():
#     print(i)

# for key,value in d.items():
#     print(key ,"=" , value)


'''Q.10 WAP TO CREATE A LIST FROM A STRING .'''
# s = "Python"
# lst = list(s)
# print(lst)      #op:- ['P', 'y', 't', 'h', 'o', 'n']

# # or
# lst = []
# for i in s:
#     lst.append(i)
# print(lst)          #op:- ['P', 'y', 't', 'h', 'o', 'n']

# or

# s = "Python"
# lst = s.split()
# print(lst)          #op:- ['Python']


'''by using while loop'''
# s = "Python"
# lst = []
# i = 0
# while i < len(s):
#     # lst.append(i)         #op:- [0, 1, 2, 3, 4, 5]
#     lst.append(s[i])        #op:- ['P', 'y', 't', 'h', 'o', 'n']
#     i+=1
# print(lst) 


'''Q11. WAP TO CREATE A LIST FROM A STRING AND ALL THE ELEMENTS BY CONVERTING INTO UPPERCASE .'''
# s = "Srabani"
# lst=[]
# for i in s:
#     lst.append(i.upper())
# print(lst)

# op:- ['S', 'R', 'A', 'B', 'A', 'N', 'I']

# s = "Srabani"
# lst=[]
# for i in range(len(s)):
#     lst.append(s[i].upper())
# print(lst)

# op:- ['S', 'R', 'A', 'B', 'A', 'N', 'I']


'''Q12. WAP TO CREATE A LIST FROM A STRING AND ADD ALL THE ELEMENTS WHICH ARE IN EVEN INDEX .'''
# s = "Pradeep"
# lst=[]
# for i in range(len(s)):
#     if i%2==0:
#         lst.append(s[i])
# print(lst)

# op:- ['P', 'a', 'e', 'p']

# or

# lst2=[]
# for i in range(0,len(s),2):
#     lst2.append(s[i])
# print(lst2)
# op:- ['P', 'a', 'e', 'p']

'''Q13. WAP TO CREATE A LIST FROM A STRING AND ADD ALL ELEMENTS BY CONVERTING UPPER INTO LOWER AND LOWER INTO UPPER .'''
# s = "MoRNinG"
# lst=[]
# for i in s:
#     lst.append(i.swapcase())
# print(lst)

# # op:- ['m', 'O', 'r', 'n', 'I', 'N', 'g']

# # or

# lst2=[]
# for i in s:
#     if i.isupper():
#         lst2.append(i.lower())
#     elif i.islower():
#         lst2.append(i.upper())
# print(lst2)

# op:- ['m', 'O', 'r', 'n', 'I', 'N', 'g']


'''Q14. WAP TO CREATE A DICTIONARY FROM A STRING WITH KEY AS ELEMENT AND VALUE AS ASCII VALUE OF THE ELEMENT .'''
# s = "rajesh"
# dic={}
# for i in s:
#     key = i
#     value = ord(i)
#     dic[key] = value
# print(dic)

# # op:- {'r': 114, 'a': 97, 'j': 106, 'e': 101, 's': 115, 'h': 104}

# s = "rajesh"
# dic={}
# for i in s:
#     dic[i] = ord(i)
# print(dic)

# # op:- {'r': 114, 'a': 97, 'j': 106, 'e': 101, 's': 115, 'h': 104}


'''Q15. WAP TO CREATE A LIST FROM A STRING IF THE ELEMENT IS PRESENT IN AN EVEN INDEX ADD ASCII VALUE OF THE ELEMENT ELSE ADD THE ELEMENT AS IT IS .'''
# s = "ritesh"
# lst=[]
# for i in range(len(s)):
#     if i%2==0:
#         lst.append(ord(s[i]))
#     else:
#         lst.append(s[i])
# print(lst)

# op:- [114, 'i', 116, 'e', 115, 'h']

'''Q16. WAP TO PRINT ALL THE ELEMENTS WHOSE INDEX IS EVEN AND ALSO LENGTH OF THE ELEMENT IS EVEN IN A LIST .'''
lst = ["apple","mango","orange","tamarind","grapes"]
# for i in range(len(lst)):
#     if i%2==0:
#         if len(lst[i])%2==0:
#             print(lst[i] , end=" ")
# # op:- orange grapes 

# # or

# for i in range(len(lst)):
#     if i%2==0 and len(lst[i])%2==0:
#         print(lst[i] , end=" ") 

# op:- orange grapes 


'''Q17. WAP TO CREATE A DICTIONARY FROM A LIST WHERE KEY WILL BE ELEMENT AND VALUE WILL BE REVERSED ELEMENT .'''
# lst = ["apple","mango","grapes","tamarind"]
# dic={}
# for i in lst:
#     dic[i] = i[::-1]
# print(dic)

# op:- {'apple': 'elppa', 'mango': 'ognam', 'grapes': 'separg', 'tamarind': 'dniramat'}

# lst = ["apple","mango","grapes","tamarind"]
# dic={}
# for i in lst:
#     key = i
#     value = i[::-1]
#     dic[key] = value
# print(dic)

# op:- {'apple': 'elppa', 'mango': 'ognam', 'grapes': 'separg', 'tamarind': 'dniramat'}

'''Q18. WAP TO PRINT THE LARGEST NUMBER PRESENT IN A GIVEN LIST .'''
# lst = [11,55,66,33,22,21,65,78,33,22]
# large_number = lst[0]
# for i in lst:
#     if i > large_number:
#         large_number = i
# print(large_number)          #op:- 78

# # or

# lst = [11,55,66,33,22,21,65,78,33,22]
# lst.sort()
# print(lst[-1])

# # or

# lst = [11,55,66,33,22,21,65,78,33,22]
# lst.sort(reverse=True)
# print(lst[0])

# # or

# lst = [11,55,66,33,22,21,65,78,33,22]
# print(max(lst))


'''Q19. WAP TO FIND THE LEAST NUMBER PRESENT IN A GIVEN LIST .'''
# lst = [55,66,33,11,22,21,65,78,33,22]
# least_number = lst[0]
# for i in lst:
#     if i < least_number:
#         least_number = i
# print(least_number)         #op:- 11

# # or
# lst = [55,66,33,11,22,21,65,78,33,22]
# lst.sort()
# print(lst[0])  
# #op:- 7

# # or

# lst = [55,66,33,11,22,21,65,78,33,22]
# lst.sort(reverse=True)
# print(lst[-1])
# #op:- 7

# # or

# lst = [55,66,33,11,22,21,65,78,33,22]
# print(min(lst))


'''Q20. WAP TO FIND THE TOTAL SUM OF THE NUMBERS PRESENT IN A GIVEN LIST .'''
# lst = [55,66,33,11,22,21,65,78,33,22]
# sum = 0
# for i in lst:
#     sum+=i
# print(sum)

# op:- 406

'''Q21. WAP TO FIND THE MEAN OF THE LIST .'''
# lst = [55,66,33,11,22,21,65,78,33,22]
# sum = 0
# for i in lst:
#     sum = sum + i
# mean = sum // len(lst)
# print(mean)

# op:-  40


'''Q22. WAP TO CREATE A DICTIONARY FROM A LIST WITH KEY AS FIRST HALF OF THE ELEMENT AND VALUE AS SECOND HALF OF THE ELEMENT .'''
# lst = ["apple","mango","grapes","orange"]
# dic={}
# for i in lst:
#     dic[i[:len(lst)//2]] = i[len(lst)//2:]
# print(dic)

# op:-  {'ap': 'ple', 'ma': 'ngo', 'gr': 'apes', 'or': 'ange'}

# lst = ["apple","mango","grapes","orange"]
# dic={}
# for i in lst:
#     key = i[:len(lst)//2]
#     value = i[len(lst)//2:]
#     dic[key] = value
# print(dic)

# op:- {'ap': 'ple', 'ma': 'ngo', 'gr': 'apes', 'or': 'ange'}


'''Q23. WAP TO REMOVE DUPLICATES FROM A LIST .'''
# lst = [11,22,44,33,55,22,11,55,66,33]
# res=[]
# for i in lst:
#     if i not in res:
#         res.append(i)
# print(res)

# op:-[11, 22, 44, 33, 55, 66]

# lst = [11,22,44,33,55,22,11,55,66,33]
# s = set(lst)
# print(list(s))

# op:- [33, 66, 11, 44, 22, 55]


'''Q24. WAP TO CREATE A DICTIONARY FROM A LIST WITH KEY AS INDEX AND VALUE AS ELEMENT IF THE INDEX IS EVEN ELSE KEY AS LENGTH OF THE ELEMENT AND VALUE AS ELEMENT .'''
lst = ["apple","mango","grape","orange"]
dic={}
for i in range(len(lst)):
    if i%2==0:
        dic[i] = lst[i]
    else:
        dic[len(lst[i])] = lst[i]
print(dic)

# op:- {0: 'apple', 5: 'mango', 2: 'grape', 6: 'orange'}


'''Q25. WAP TO CREATE A DICTIONARY FROM A STRING WITH KEY AS ELEMENT AND VALUE AS OPPOSITE CASE OF THE ELEMENT .'''
s = 'MaNgO'
dic={}
for i in s:
    dic[i] = i.swapcase()
print(dic)

# op:- {'M': 'm', 'a': 'A', 'N': 'n', 'g': 'G', 'O': 'o'}

s = "MaNgO"
dic={}
for i in s:
    if i.isupper():
        dic[i] = i.lower()
    else:
        dic[i] = i.upper()
print(dic)

# op:- {'M': 'm', 'a': 'A', 'N': 'n', 'g': 'G', 'O': 'o'}













              




































