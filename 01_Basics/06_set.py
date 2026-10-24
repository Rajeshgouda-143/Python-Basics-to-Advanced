# SET() DATATYPE
''' It is a collection of homogeneous and hetrogeneous type of data .
--> Boundaries of set() id curly braces {} .
--> set() is a unordered datatype .
--> set() doesn't support indexing and slicing .
--> It doesn't allows duplicate elements .
--> set() is a mutable datatype but values must be immutable datatype .
--> default value of set is set() .'''

# examples:-

s = {11, 22, 33, 44}
print(s)
# op:- {33, 11, 44, 22}
print(type(s))
# op:- <class 'set'>

'''Indexing and Slicing not allowed it raises TypeError 
# print(s[::-1])
# op:- TypeError: 'set' object is not subscriptable

print(s[0])
# op:- TypeError: 'set' object is not subscriptable   '''


'''look this code if we pass duplicate value , set remove the duplicates and print only once the value  .'''
# for examples:-
s = {11,"a",33,"a",22,11,"b",33,"a"}
print(s)
# op:- {33, 22, 'b', 11, 'a'}

# interesting part 

s = {1,2.2,True,2+3j,"hello",0,False}
print(len(s))     #op:- 5
print(s)
# op:-  {0, 1, 2.2, 'hello', (2+3j)}

'''Look there "True" and "False" appears only one time also set remove them , why ? because the default value of True is 1 
and default value of False is 0 , so 1 and 0 already present into the set that is why it removes the True and False and keep 1 and 0 .
because before True and False we were pass 1 and 0 .'''
# example:-2

s = {1, True, False, 0}
print(s)
# op:- {False, 1}

'''here it print False instead of 0 , because we passed there False first .'''


''' datatypes are set() accepts '''
'''(int, float, Boolean, complex, string, tuple)  they all are immutable datatype .'''
# examples:-

s = {1, 2.2, False, 3+2j, "hii", (1,2,3)}
print(s)
# op:- {False, 1, 2.2, (3+2j), (1, 2, 3), 'hii'}

'''instead of immutable datatypes if we try to pass any other datatype it will raises an error .
# for examples:-
s = {[1,2,3],[4,5,6]}
print(s)
# op:-  TypeError: cannot use 'list' as a set element (unhashable type: 'list')    
# 
# s = {{1,2,3},{2,5,6}}
print(s)
# op:- TypeError: cannot use 'set' as a set element (unhashable type: 'set') '''


# METHODS IN SET():-
# -------------------

# 1. UNION():-
# ------------
''' It is an inbuild function which is used to combine both Baseset and iterable by removing the duplicates .
--> It won't update the Baseset .
--> It represent the symbol called pipeline (|) .
--> It accepts multiple iterables at the same time .

Syntax:- baseset.union(iterable1,iterable2,....)'''
# examples:-

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1.union(s2))     #op:- {1, 2, 3, 4, 5, 6}
print(s1)               #op:- {1, 2, 3, 4}            see the baseset has not updated yet, it has as it is .

'''and also we can do by using pipeline symbol '''
# for example:-
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {3, 7, 8, 9}
print(s1 | s2 | s3)      #op:- {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(s1)                 #op:- {1, 2, 3, 4}    

'''as it is the baseset , so update the baseset by removing the duplicates we use upadte() .'''

# 2. update():-
# ------------
''' It is used to update the baseset by removing the duplicates from both baseset and iterable .
--> It accepts multiple iterables at the same time .

Syntax:- baseset.update(iterable1, iterable2,......)'''
# examples:-
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s1.update(s2)
print(s1)        #op:- {1, 2, 3, 4, 5, 6}      see now the baseset is updated by removing the duplicates .
print(s2)        #op:- {3, 4, 5, 6}

'''or we can also do like this by using list and tuple'''

s1 = {1,2,3,4}
s1.update({3,4,5,6},[1,2,"a","b"])
print(s1)
# op:-  {1, 2, 3, 4, 5, 6, 'b', 'a'}


s1 = {1,2,3,4}
s1.update({3,4,5,6},(1,2,"a","b"))
print(s1)

# op:- {'b', 1, 2, 3, 4, 5, 6, 'a'}


# 3. intersection():-
# ------------------
''' It is used to returns the common elements present in both baseset and iterable .
--> It won't update the baseset .
--> to represent the intersection we use the symbol call AND (&) .
--> It accepts multiple iterables at the same time .

Syntax:- baseset.intersection(iterable1,iterable2.....)'''
# examples:-

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1.intersection(s2))      #op:-  {3, 4}
print(s1)                       #op:- {1, 2, 3, 4}    it will not update the baseset .

'''we can also do the intersection by using AND symbol & .'''
# for examples:-
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 & s2)          #op:- {3, 4}

# or
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {3, 4, 7, 8}
print(s1 & s2 & s3)      #op:- {3, 4}    it present in all the sets .


'''also we can do '''
s1 = {1, 2, 3, 4}
print(s1.intersection([3,4,5,6],(3,4,5,6,7)))     #op:-  {3, 4}

'''suppose all the sets are diiferent there is no common elements . it returns default value set()'''
# examples:-
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {7, 8, 9, 10}
print(s1.intersection(s2,s3))       #op:- set()



# 4. intersection_update():-
# --------------------------
''' It is used to update the baseset with the common elements which are present in both baseset and iterabale .
--> It accepts multiple iterables at the same time .

Syntax:- baseset.intersection_update(iterable1,iterable2,......)'''
# examples:-
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {3,4, 9, 10}
s1.intersection_update(s2,s3)
print(s1)
# op:-  {3, 4}     look, it update the baseset with the common elements , which are present in all three sets .



# 5. difference():-
# -----------------
''' It is an inbuild function which is used to returns the elements which are present in only baseset but not in iterable .
--> It won't update the baseset .
--> To represents the difference we use the symbol (-) .
--> It accepts multiple iterables at the same time .

Syntax:- baseset.difference(iterable1,iterable2,......)'''
# examples:-
s1 = {1,2,"a","b",2.2,5,6}
s2 = {1,2,"b",2.3,7,8}
print(s1.difference(s2))   

# op:- {'a', 2.2, 5, 6}     this datas are not present in iterables .

# or

s1 = {1,2,3,4,5}
s2 = [4,5,7,8,9]
s3 = (3,4,5,6,7,8)
print(s1.difference(s2,s3))     #op:- {1, 2}
print(s1)                       #op:- {1,2,3,4,5}

''' by using symbol (-)'''
'''remember:- performing the operation by using the symbol , we should have the same datatype , otherwise  it raises an error .'''
# examples:-
'''
s1 = {1,2,3,4,5}
s2 = [4,5,7,8,9]
s3 = (3,4,5,6,7,8)
print(s1 - s2 - s3)

# op:-  TypeError: unsupported operand type(s) for -: 'set' and 'list'  '''

# correct way:-
s1 = {1,2,3,4,5}
s2 = {4,5,7,8,9}
s3 ={3,4,5,6,7,8}
print(s1 - s2 - s3)      #op:- {1, 2}
print(s1)                #op: {1,2,3,4,5}


# 6. difference_update():-
# ------------------------
''' It is used to update the baseset with the elements which are present in only baseset but not in iterables
--> It accepts multiple iterables at the same time .

Syntax:- baseset.difference_update(iterable1,iterable2,......)'''
# examples:-
s1 = {1,2,3,4,5}
s2 = {4,5,7,8,9}
s3 ={3,4,5,6,7,8}
s1.difference_update(s2,s3)

print(s1)   # op:- {1, 2}
print(s2)   #op:- {4, 5, 7, 8, 9}


# 7. symmetric_difference():-
# ---------------------------
''' It is an inbuild function which is used to returns the unique values which are present in both baseset and iterable .
--> It accepts only one iterable .
--> It won't update the baseset .

Syntax:- baseset.symmetric_difference(iterable) .'''
# examples:-
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1.symmetric_difference(s2))     #op:- {1, 2, 5, 6}

print(s1)    # op:- {1, 2, 5, 6}


''' if we pass morethan one iterable it will raises an error .
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {5 , 6, 7, 8}
print(s1.symmetric_difference(s2,s3))
# op:- TypeError: set.symmetric_difference() takes exactly one argument (2 given)  '''

s1 = {1, 2, 3, 4}
s2 = [3, 4, 5, 6]
print(s1.symmetric_difference(s2))    #op:- {1, 2, 5, 6}

print(s1)   #op:- {1, 2, 3, 4}       it will not update the baseset 


# 8. symmetric_difference_update():-
# ----------------------------------
''' It is used to update the baseset with the unique values which are present in both baseset and iterable .
--> It accepts only one iterable .

Syntax:- baseset.symmetric_difference_update(iterable) '''
# examples:-
s1 = {1, 2, 3, 4}
s2 = [3, 4, 5, 6]
s1.symmetric_difference_update(s2)

print(s1)     #op:- {1, 2, 5, 6}     now it will update the baseset with the unique values which are present in both baseset and iterable .

print(s2)      #op:- [3, 4, 5, 6]


# TO ADD THE ELEMENTS:-
# --------------------

# 1. add():-
# ----------
''' It is an inbuild function which is used to add the element randomly into a set() .
--> It accepts only immutable datatype .
--> It accepts only one argument .

Syntax:- variable_name.add(element)'''
# examples:-

s = {11, 22, 33, 44}
s.add(55)
print(s)    

# op:-  {33, 11, 44, 22, 55}

print(s.add(66))        #op:- None

s.add(66)
print(s)
# op:-   {33, 66, 11, 44, 22, 55}

s.add("hello")
print(s)
# op:-  {33, 66, 11, 44, 22, 55, 'hello'}

''' if we pass morethan one or mutable datatype it will raises an error 
# examples:-

s = {11, 22, 33, 44}
s.add([1,2,3,4])
print(s)

# op:- TypeError: cannot use 'list' as a set element (unhashable type: 'list') 
# 
# s = {11, 22, 33, 44}
s.add(55,77)
print(s)

# op:-TypeError: set.add() takes exactly one argument (2 given)  '''



'''Note:-  Whenever we want to add morethan one elements into a set() we can use a method called update .'''
# examples:-
s = {"apple","orange","mango"}
s.update([1,2,3],{"Grapes","banana","mango"})

print(s)
# op:-  {1, 2, 3, 'Grapes', 'banana', 'orange', 'mango', 'apple'}


# TO REMOVE THE ELMENTS 
# ---------------------

# 1. remove():-
# ------------
''' It is an inbuild function which is used to remove the specified element from a set() .
--> It accepts only one argument .
--> It raises KeyError if the specified element is not present .

Syntax:- variable_name.remove(element)'''
# examples:-
s = {11, 22, 33, 44, 11, 22, 33}
s.remove(44)
print(s)        #op:- {33, 11, 22}

'''s.remove(55) 
print(s)        #op:- KeyError: 55   because the specified element is not present in the set() .'''


# 2. discard():-
# --------------
''' It is used to remove the specified element from a set() .
--> It returns None if the specified element is not present .
--> It accepts only one argument .

Syntax:- variable_name.discard(element)'''
# examples:-
s = {11, 22, 33, 44}
s.discard(22)
print(s)        #op:-{33, 11, 44}

'''if the specified element is not present it will return "None" .'''
# examples:-
s = {11, 22, 33, 44}
print(s.discard(55))           #op:- None


# 3. pop():-
# ---------
''' It is used to remove the element from first based on the storage .
--> It won't accepts any arguments .
--> It raises keyError if the set() is empty .

Syntax:- variable_name.pop() .'''
# examples:-

s = {11 , "a", 22, "b"}

print(s)        #op:- {'b', 11, 'a', 22}

s.pop()
print(s)   #op:- {11, 22, 'a'}

print(s.pop())    #op:- 11

s.pop()
print(s)       #op:- {22}

s.pop()
print(s)        #op:- set()

'''Now set is become empty , if we try to use pop then it will raises an KeyError
s.pop()
print(s)  
# op:- KeyError: 'pop from an empty set'    '''


# 4. clear():-
# -----------
''' It is used to remove all the elements present in a set() . but the default value of set() will be present , that is set() .
--> It won't accepts any argument .

Syntax:- variable_name.clear()'''
# examples:-

s = {11, 22, "a", 33,"b", 44, "c"}
s.clear()
print(s)       #op:- set()




# Not that much Important ..

# 5. issubset():-
# ----------------
''' It checks whether all elements of one set are present in another set or not .
--> It returns boolean value True or False .'''
# examples:-

s1 = {1, 2, 3, 4}
s2 = {5, 6, 4 , 3 , 1}
print(s1.issubset(s2))         #op:- True


print(s1.isdisjoint(s2))   

print(s1.issuperset(s2))



# ----------------------------------Thank You ---------------------------------





















































