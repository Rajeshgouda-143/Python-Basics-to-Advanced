# Eval():-
# --------
'''It is an inbuild function which is used to convert the data into particular datatype based on the boundaries .
--> It accepts string as an Input .

Syntax:- eval("string") '''
# examples:-

# sample = eval(input('enter your data: '))
# print(sample, type(sample))

'''  op:-

enter your data: [1,2,3,4,5]
[1, 2, 3, 4, 5] <class 'list'>

enter your data: "rajesh"
rajesh <class 'str'>

enter your data: 1234
1234 <class 'int'>

enter your data: {1,2,3,45}
{1, 2, 3, 45} <class 'set'>

enter your data: (1,2,"rajesh",45,"pradeep")
(1, 2, 'rajesh', 45, 'pradeep') <class 'tuple'>

enter your data: {1:"a",2:"b",3:"c"}
{1: 'a', 2: 'b', 3: 'c'} <class 'dict'>

'''

'''Q1. WAP TO CHECK WHETHER GIVEN LIST CONTAINS DUPLICATES ELEMENT OR NOT .'''
# lst = eval(input("enter the list: "))
# res = []
# for i in lst:
#     if i not in res:
#         res.append(i)
# if lst == res:
#     print("duplicate is not present in the list")
# else:
#     print("duplicate is present in the list")

# or by using set()

# lst = eval(input("enter the list: "))
# s = set(lst)
# if len(lst) == len(list(s)):
#     print("duplicate not present")
# else:
#     print("duplicate present")

# or by using dictionary

# lst = eval(input("enter the list: "))
# dic={}
# for i in lst:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i]+=1
# for i in dic:
#     if dic[i] > 1:
#         print("duplicate present")
#         break
# else:
#     print("duplicate not present")


# 1. What is a homogeneous:-
# -----------------------------
'''Homogeneous means when all its elements belong to the same data type.

Example: a = [10, 20, 30, 40]
All elements are integers, so it is a homogeneous list.

a = ["Python", "Java", "SQL"]
All elements are strings, so it is also homogeneous.'''


# 2. What is a heterogeneous:-
# ----------------------------
'''Heterogeneous means when its elements belong to different data types.

Example: a = [10, "Python", 20.5, True]
Here, we have integer, string, float and boolean values.
Therefore, it is a heterogeneous list.

'''

# 3. Python program using for loop
# We will use type() to compare the data types.

'''Q2. WAP TO CHECK WHETHER GIVEN LIST IS A HOMOGENEOUS OR NOT .'''

# a = [10, 20, 30, 40, 50]
# first = type(a[0])
# count = 0
# for i in a:    
#     if type(i) != first:        
#         count = count + 1
# if count == 0:    
#     print("Homogeneous List")
# else:    
#     print("Heterogeneous List")


'''It checks whether the current element's data type is different from the first element's type.
Element	Data type	Same as first type?
10	        int	Yes
20	        int	Yes
"Python"	str	No
40	        int	Yes

Since one element has a different data type, the list is heterogeneous.

Output: Heterogeneous List
'''

# Break:-
# -------
''' It is a keyword which is used to stop the execution of a program .
--> It Is used inside loops .
--> Does not return a value .
--> Execution continues after the loop .

'''
# example:-
# for i in range(1,11):
#     if i == 5:
#         break
#     else:
#         print(i)

'''op:-
1
2
3
4

Look at here after the loop reached at 5 it will stop the execution .'''

# continue:-
# ----------
''' It is used to skip the current iteration and continue with the next iteration .'''
# example:-
# for i in range(1,11):
#     if i == 5:
#         continue
#     else:
#         print(i , end=" ")

# op:- 1 2 3 4 6 7 8 9 10 


# pass:-
# ------
''' It is used to specify the given block is empty .'''
# age = 19
# if age > 18:
#     pass
# else:
#     print("not matching.....")

'''Q3. WAP TO CHECK GIVEN LIST IS A HOMOGENEOUS OR HETEROGENEOUS .'''
# lst = [1,"hi",3,4]
# d = type(lst[0])
# is_homo = True

# for i in lst:
#     if d!=type(i):
#         is_homo = False
# if is_homo:
#     print("Homogeneous")
# else:
#     print("Hoterogeneous")


'''Q4. WAP TO CREATE A NEW LIST IF THE LENGTH OF THE ELEMENTS IS MORETHAN 6 .'''
# lst = ["Qspider","neem","tamarind","dinag","manga"]
# ls = []
# for i in lst:
#     if len(i) > 6:
#         ls.append(i)
# print(ls)

# by using list comprehension

# lst = ["Qspider","neem","tamarind","dinag","manga"]
# ls = [i for i in lst if len(i) > 6]
# print(ls)


'''Q5. WAP TO CREATE A LIST FROM THE EXISTING LIST IF THE ELEMENTS PRESENT IN THE LIST STARTING WITH UPPERCASE .'''
# lst = ["Apple","banana","Grapes","Qspider","jspider"]
# ls= []
# for i in lst:
#     if i[0].isupper():
#         ls.append(i)
# print(ls)                       #op:- ['Apple', 'Grapes', 'Qspider']


# by using list comprehension

# lst = ["Apple","banana","Grapes","Qspider","jspider"]
# ls = [i for i in lst if i[0].isupper()]
# print(ls)
# op:-  ['Apple', 'Grapes', 'Qspider']


'''Q6. WAP TO TRAVERSE THROUGH A DICTIONARY AND CREATE A NEW DICTIONARY OF FRUIT AND IT'S PRICE IF THE PRICE IS EVEN ADD 10 RUPEES , IF IT IS  ODD ADD 20 RUPEES .'''
# fruits = {"apple":1000,"grapes":2345,"banana":1200,"orange":9873,"mango":7001}
# fruit = {}
# for i in fruits:
#     if fruits[i]%2==0:
#         fruits[i] += 10
#     else:
#         fruits[i]+=20
# print(fruits)

# op:- {'apple': 1010, 'grapes': 2365, 'banana': 1210, 'orange': 9893, 'mango': 7021}

# or

# fruits = {"apple":1000,"grapes":2345,"banana":1200,"orange":9873,"mango":7001}
# dic={}
# for i in fruits:
#     key = i
#     value = fruits[key]
#     if value % 2 == 0:
#         value += 10
#     else:
#         value += 20
#     dic[key] = value
# print(dic)

# op:- {'apple': 1010, 'grapes': 2365, 'banana': 1210, 'orange': 9893, 'mango': 7021}


'''Q7. WAP TO CREATE A DICTIONARY INTO A LIST WITH KEY AS INDEX AND VALUE AS SQUARE OF THE INDEX , IF THE ELEMENT IS STARTING WITH CONSONANT ELSE ELEMENT AND LENGTH PAIR .'''
# lst = ["apple","grapes","qspider","prospiders"]
# dic={}
# for i in range(len(lst)):
#     key = i
#     if lst[i][0] not in "aeiou":
#         value = key**2
#     else:
#         value = len(lst[i])
#     dic[key] = value
# print(dic)

# op:-  {0: 5, 1: 1, 2: 4, 3: 9}

# lst = ["apple","grapes","qspider","prospiders"]
# dic={i:i**2 if lst[i][0] not in "aeiou" else len(lst[i]) for i in range(len(lst))}
# print(dic)

# op:- {0: 5, 1: 1, 2: 4, 3: 9}

'''
What if you want the word itself as the key instead of its index?

For example: {"apple": 5,"grapes": 1,"qspider": 4,"prospiders": 9}

Can you modify the dictionary comprehension to achieve this?   '''
# code:-
# lst = ["apple","grapes","qspider","prospiders"]
# dic={lst[i]:i**2 if lst[i][0] not in "aeiou" else len(lst[i]) for i in range(len(lst))}
# print(dic)
# op:-  {'apple': 5, 'grapes': 1, 'qspider': 4, 'prospiders': 9}


'''Q.8
 s = "aaabbbbcc" 
op:- {"a":3,"b":4,"c":2}'''

# s = "aaabbbbcc"
# dic={}
# for i in s:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i]+=1
# print(dic)                    #op:- {'a': 3, 'b': 4, 'c': 2}

# or

# s = "aaabbbbcc"
# dic={}
# for i in s:
#     key = i
#     value = s.count(i)
#     dic[key] = value
# print(dic)                    #op:- {'a': 3, 'b': 4, 'c': 2}

# or

# s = "aaabbbbcc"
# dic={i:s.count(i) for i in s}
# print(dic)

# op:- {'a': 3, 'b': 4, 'c': 2}


'''Q9.
s = "a3b2c6"
op:- "aaabbcccccc"  '''
# code:-
# s = "a3b2c6"
# res=""
# for i in range(0,len(s),2):
#     char = s[i]
#     num = int(s[i+1])
#     res = res + char * num
# print(res)                         #op:- aaabbcccccc


# s = "a3b2c6"
# res = ""
# for i in range(len(s)):
#     ele = s[i]
#     if ele.isalpha():
#         num = s[i+1]
#         res = res+ ele*int(num)
# print(res)                              #op:- aaabbcccccc


'''Q10. FIND THE MOST REPEATED ELEMENT .'''
# lst = [1,1,2,3,2,4,2,1,2]
# dic={}
# for i in lst:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1
# most_repeated_char = 0
# for i in dic:
#     if dic[i] > most_repeated_char:
#         most_repeated_char = i
# print(most_repeated_char)

# op:- 2


'''Q11. 
lst = [[1,2],[3,4]]
op:- [[1,3],[2,4]]
'''
# code:-
# lst = [[1,2],[3,4]]
# res = []
# for i in range(len(lst)):
#     ele1 = lst[0][i]
#     ele2 = lst[1][i]
#     res.append([ele1,ele2])
# print(res)

# op:- [[1, 3], [2, 4]]


'''Q12. 
lst = ["hi","hello","to","hii"]
op:- {2:["hi","to"], 5:["hello"], 3:["hii]}'''
# code:-
# lst = ["hi","hello","to","hii"]
# dic={}
# for i in lst:
#     key = len(i)
#     if key not in dic:
#         dic[key] = [i]
#     else:
#         dic[key]+=[i]
# print(dic)


'''Q13. WAP TO CREATE A DICTIONARY FROM A LIST WITH KEY AS ELEMENT AND VALUE AS REVERSED ELEMENT IF THE ELEMENT IS HAVING EVEN LENGTH ELSE KEY WILL BE ELEMENT AND VALUE WILL BE LENGTH .'''
# lst = eval(input("enter the list: "))
# dic={}
# for i in lst:
#     key = i
#     if len(i)%2 == 0:
#         value = i[::-1]
#     else:
#         value = len(i)
#     dic[key] = value
# print(dic)

# or by using dictionary comprehension

# lst = eval(input("enter the list: "))
# dic={i:i[::-1] if len(i)%2==0 else len(i) for i in lst}
# print(dic)

# op:- {'apple': 5, 'grapes': 'separg', 'mango': 5, 'tamarind': 'dniramat'}


'''Q14. WAP to create a dictionary where the key is the first character of each word and the value is the list of words starting with that character.'''
# lst = ["apple", "ant", "ball", "bat", "cat", "car"]
# dic={}
# for i in lst:
#     if i[0] not in dic:
#         dic[i[0]] = [i]
#     else:
#         dic[i[0]] += [i]
# print(dic)

# op:- {'a': ['apple', 'ant'], 'b': ['ball', 'bat'], 'c': ['cat', 'car']}

'''Q15. WAP TO PRINT FOUND IF 7 IS PRESENT IN THE GIVEN LIST ELSE PRINT NOT FOUND .'''
# code:-
# lst = [1, 2, 3, 6, 8, 7, 5]
# for i in lst:
#     if i == 7:
#         print("Found")
#         break
# else:
#     print("Not Found")


''' Q16. WAP TO CHECK WHETHER GIVEN NUMBER IS PRIME NUMBER OR NOT .'''
# no = int(input("enter the no: "))
# if no <= 1:
#     print("not a prime number")
# else:
#     is_prime = True
#     for i in range(2,no):
#         if no%i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print("Prime Number")
#     else:
#         print("Not a Prime Number")

'''or  (but this will not handle the negative number)'''

# no = int(input("Enter the no: "))
# for i in range(2,no):
#     if no%i == 0:
#         print("Not a prime Number")
#         break
# else:
#     print("Prime number")


'''Q17. WAP TO CREATE A DICTIONARY FROM TWO LIST WITH KEY FROM FIRST AND VALUE FROM SECOND LIST .'''
# lst1 = ["a","b","c","d"]
# lst2 = ["apple","banana","cat","dog"]

# dic = {}
# for i in range(len(lst1)):
#     key = lst1[i]
#     value = lst2[i]
#     dic[key] = value
# print(dic)        

# op:-  {'a': 'apple', 'b': 'banana', 'c': 'cat', 'd': 'dog'}



# by using zip() and ziplongest()

# lst1 = ["a","b","c","d"]
# lst2 = ["apple","banana","cat","dog"]
# dic={}
# for i,j in zip(lst1,lst2):
#     dic[i] = j
# print(dic)

# op:- {'a': 'apple', 'b': 'banana', 'c': 'cat', 'd': 'dog'}

# zip_longest()
# from itertools import zip_longest
# lst1 = ["a","b","c","d"]
# lst2 = ["apple","banana","cat","dog"]
# dic={}
# for i,j in zip_longest(lst1,lst2):
#     dic[i] = j
# print(dic)

# op:- {'a': 'apple', 'b': 'banana', 'c': 'cat', 'd': 'dog'}

# lst1 = ("a","b","c","d")
# lst2 = ["apple","banana","cat","dog"]

# dic = {}
# for i in range(len(lst1)):
#     key = lst1[i]
#     value = lst2[i]
#     dic[key] = value
# print(dic)        

# # op:-  {'a': 'apple', 'b': 'banana', 'c': 'cat', 'd': 'dog'}



'''Q18. WAP TO CREATE A LIST FROM THE EXISTING TWO LIST WITH THE PRODUCT OF THE ELEMENT PRESENT IN THE SAME INDEX .'''
# lst1 = [1, 2, 3, 4]
# lst2 = [5, 6, 7, 8]
# res = []
# for i in range(len(lst1)):
#     product = lst1[i] * lst2[i]
#     res.append(product)
# print(res)

# op:- [5, 12, 21, 32]

# or 

# lst1 = [1, 2, 3, 4]
# lst2 = [5, 6, 7, 8]
# res = []
# for i,j in zip(lst1,lst2):
#     product = i * j
#     res.append(product)
# print(res)

# op:- [5, 12, 21, 32]

# or

# from itertools import zip_longest
# lst1 = [1, 2, 3, 4]
# lst2 = [5, 6, 7, 8]
# res = []
# for i,j in zip_longest(lst1,lst2):
#     product = i * j
#     res.append(product)
# print(res)

# op:- [5, 12, 21, 32]


'''Q19. WAP TO CREATE A DICTIONARY FROM TWO COLLECTIONS WITH KEY FROM FIRST AND VALUE FROM SECOND .'''
# s = "abc"
# lst = ["apple","banana","cow"]
# dic={}
# for i in range(len(lst)):
#     key = s[i]
#     value = lst[i]
#     dic[key] = value
# print(dic)

# op:- {'a': 'apple', 'b': 'banana', 'c': 'cow'}

# or

# s = "abc"
# lst = ["apple","banana","cow"]
# dic={}
# for i,j in zip(s,lst):
#     dic[i] = j
# print(dic)

# op:- {'a': 'apple', 'b': 'banana', 'c': 'cow'}

# or

# from itertools import zip_longest
# s = "abc"
# lst = ["apple","banana","cow"]
# dic={}
# for i,j in zip_longest(s,lst):
#     dic[i] = j
# print(dic)

# op:- {'a': 'apple', 'b': 'banana', 'c': 'cow'}


'''important'''

# zip():-
# -------
''' 
    zip() is a built-in Python function used to traverse multiple collections simultaneously by pairing their elements according to their positions.
--> zip() will always traverse through least length of times . (always take less length)

Syntax:- zip(iterable1, iterable2, iterable3, ...)

We can pass lists, tuples, strings, and other iterables.

Important point
---------------
zip() normally stops when the shortest iterable is exhausted.

Example:
lst1 = [10, 20, 30, 40]
lst2 = ["Python", "Java", "SQL"]
for i in zip(lst1, lst2):    
    print(i)

Output:
(10, 'Python')
(20, 'Java')
(30, 'SQL')


Why only three pairs?
- lst1 contains 4 elements.
- lst2 contains 3 elements.
- Therefore, zip() creates only 3 pairs.

3. Creating a dictionary using zip()
We can directly convert the zipped pairs into a dictionary using dict().

lst1 = ["a", "b", "c", "d"]
lst2 = ["apple", "banana", "cat", "dog"]
dic = dict(zip(lst1, lst2))
print(dic)

Output:
{'a': 'apple', 'b': 'banana', 'c': 'cat', 'd': 'dog'}



4. Traversing three collections
names = ["Raj", "Ram", "Sam"]
ages = [22, 23, 24]
cities = ["Chennai", "Bangalore", "Hyderabad"]
for n, a, c in zip(names, ages, cities):   
      print(n, a, c)

Output:
Raj 22 Chennai
Ram 23 Bangalore
Sam 24 Hyderabad


5. Important difference: zip() vs zip_longest()
        zip()	                                                     zip_longest()
-----------------------                                    ------------------------------
Stops at the shortest iterable	                       Continues until the longest iterable ends
Ignores remaining elements	                           Fills missing values with a default value

zip_longest() is available in the itertools module.

'''

'''Q1. WAP TO CREATE A DICTIONARY FROM 2 LIST WITH KEY FROM FIRST AND VALUE FROM SECOND LIST .'''
# lst1 = ["a","b","c","d"]
# lst2 = ["apple","banana","cat","dog"]
# dic={}
# for key,value in zip(lst1,lst2):
#     dic[key] = value
# print(dic)

# op:- {'a': 'apple', 'b': 'banana', 'c': 'cat', 'd': 'dog'}


'''Q2. WAP TO CREATE A LIST FROM THE EXISTING TWO LIST WITH THE PRODUCT OF THE ELEMENT IN THE SAME INDEX .'''
# lst1 = [1,2,3,4]
# lst2 = [5,6,7,8]
# res = []
# for i,j in zip(lst1,lst2):
#     product = i * j
#     res.append(product)
# print(res)

# op:- [5, 12, 21, 32]


'''Q3. WAP TO CREATE A LIST FROM TWO COLLECTION IF THE ELEMENTS ARE SAME IN SAME INDEX . '''
# lst1 = [1,2,3,4,5]
# lst2 = [6,2,1,7,5]
# res = []
# for i,j in zip(lst1,lst2):
#     if i == j:
#         res.append(i)
# print(res)

# op:- [2, 5]

'''without zip()'''
# lst1 = [1,2,3,4,5]
# lst2 = [6,2,1,7,5]
# res = []
# for i in range(len(lst1)):
#     ele1 = lst1[i]
#     ele2 = lst2[i]

#     if ele1 == ele2:
#         res.append(ele2)
# print(res)

# op:- [2, 5]


'''Q4. WAP TO CREATE A DICTIONARY FROM TWO LISTS WITH KEY FROM FIRST AND VALUE FROM SECOND LIST IN REVERSE ORDER .'''
# lst1 = [1,2,3,4,5]
# lst2 = [11,22,33,44,55]
# dic = {}
# for i,j in zip(lst1,lst2[::-1]):
#     dic[i] = j
# print(dic)

# op:- 1: 55, 2: 44, 3: 33, 4: 22, 5: 11}

'''without zip()'''
# lst1 = [1,2,3,4,5]
# lst2 = [11,22,33,44,55]
# dic = {}
# for i in range(len(lst1)):
#     key = lst1[i]
#     value = lst2[::-1][i]
#     dic[key] = value
# print(dic)

# op:-  {1: 55, 2: 44, 3: 33, 4: 22, 5: 11}


'''what If both the list have different length ?'''
# example:-
# lst1 = ["a","b","c"]
# lst2 = ["apple","banana","cat","dog","elephant"]
# dic = {}
# for i,j in zip(lst1,lst2):
#     dic[i] = j
# print(dic)

# op:- {'a': 'apple', 'b': 'banana', 'c': 'cat'}
# here It will traverse through to with least length and remains are Ignored .



# zip_longest():-
# ---------------
''' zip_longest() is a built-in Python function used to traverse multiple collections simultaneously at the same time .
--> zip_longest() will always traverse through  highest length collection .
--> By default zip_longest() fill the values with None .
--> zip_longest() is present in a module called itertools .

--> Instead of "None" If we want to give our own value then we can use one module called fillvalue() .

Syntax:- from itertools import zip_longest
         zip_longest(iterable1, iterable2,..............)     '''

# examples:-
# lst1 = [1,2,3]
# lst2 = [11,22,33,44]
# for i,j in zip(lst1,lst2):
#     print(i,j)

'''op:-
1 11
2 22
3 33
'''
# by using zip_longest()

# from itertools import zip_longest
# lst1 = [1,2,3]
# lst2 = [11,22,33,44]
# for i,j in zip_longest(lst1,lst2):
#     print(i,j)

'''op:-
1 11
2 22
3 33
None 44
'''
'''see the difference between zip() and zip_longest() , the zip_longest() will fill the value with None If the length of the two collections Is difference , but zip() will Ignore .'''


'''Q1. WAP TO CREATE A LIST WITH THE ELEMENTS FROM TWO LISTS AS A TUPLE IF THE ELEMENTS ARE NOT PRESENT MENTION ELEMENT NOT THERE .'''

# from itertools import zip_longest
# lst1 = [1,2,3,4]
# lst2 = [11, 22]
# res = []
# for i,j in zip_longest(lst1,lst2,fillvalue="element is not there"):
#     res.append((i,j))
# print(res)

# op:- [(1, 11), (2, 22), (3, 'element is not there'), (4, 'element is not there')]


'''Q2. WAP TO CREATE A DICTIONARY FROM NAME AS THE KEY AND VALUE IS 12% HIKE .'''
# from itertools import zip_longest
# name = ["Rajesh","Pradeep","Sameer","kali","Ganguly"]
# salary = [20000, 25000, 33000, 45000]
# dic={}

# for i,j in zip_longest(name,salary,fillvalue=0):
#     key = i
#     value = j + j*12//100
#     dic[key] = value
# print(dic)

# op:- {'Rajesh': 22400, 'Pradeep': 28000, 'Sameer': 36960, 'kali': 50400, 'Ganguly': 0}

'''Note:- If we are not use fillvalue "0" then the value becomes automatically "None" that the reason it display 
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int' 

because:- it will multiple the ,   None + None * 12 // 100'''



# enumerate():-
# -------------
''' It is used to traverse through a collection and returns the Integer value along with the elements present in a collection .
--> By default integer values will start from zero .

Syntax:- enumerate(collection,[start= ])'''

# lst = ["a","b","c","d"]
# for i in enumerate(lst):
#     print(i)

'''op:-
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
'''

# lst = ["a","b","c","d"]
# for i,j in enumerate(lst,start=100):
#     print(i,j)

'''op:-
100 a
101 b
102 c
103 d
'''

'''Q1. WAP TO CREATE A DICTIONARY FROM A LIST WITH KEY AS ELEMENT AND VALUE AS INDEX .'''
# lst = ["a","b","c","d"]
# dic={}
# for i,j in enumerate(lst):
#     dic[j] = i
# print(dic)

# op:- {'a': 0, 'b': 1, 'c': 2, 'd': 3}

# without enumarate()

# lst = ["a","b","c","d"]
# dic={}
# for i in range(len(lst)):
#     key = lst[i]
#     value = i
#     dic[key] = value
# print(dic)

# op:- {'a': 0, 'b': 1, 'c': 2, 'd': 3}

'''Q2. WAP TO CREATE A LIST FROM A STRING AND ADD THE ELEMENTS WHICH ARE PRESENT IN EVEN INDEX .'''
# s = "abcd"
# res = []
# for i,j in enumerate(s):
#     if i%2==0:
#         res.append(j)
# print(res)

# op:- ['a', 'c']


'''Q3. WAP TO CREATE A DICTIONARY FROM A LIST WITH KEY AS INDEX AND VALUE AS ELEMENT IF THE INDEX IS EVEN ELSE KEY AS LENGTH AND VALUE AS REVERSED ELEMENT .'''
lst = ["apple","mango","grapes","tamarind","orange"]
dic={}
for i,j in enumerate(lst):
    if i%2==0:
        key = i
        value = j
    else:
        key = len(j)
        value = j[::-1]
    dic[key] = value
print(dic)

# op:- {0: 'apple', 5: 'ognam', 2: 'grapes', 8: 'dniramat', 4: 'orange'}


'''Q4. WAP TO CREATE A DICTIONARY FROM A LIST WITH KEY AS FIRST HALF OF THE ELEMENT AND VALUE AS SECOND HALF IF THE ELEMENT INDEX IS A MULTIPLE OF 3 . '''
# lst = ["apple","grapes","tamarind","orange"]
# dic={}
# for i,j in enumerate(lst):
#     key = j[len(j)//2:]
#     if i%3 == 0:
#         value = j[:len(j)//2]

#     dic[key] = value
# print(dic)

# op:- {'ple': 'ap', 'pes': 'ap', 'rind': 'ap', 'nge': 'ora'}













































