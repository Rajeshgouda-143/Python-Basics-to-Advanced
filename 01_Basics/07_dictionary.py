# DICTIONARY 
# -----------

''' It is a collection of key and value pairs .
--> key and Value are separate by (Key : Value) .
--> Key : value pairs are separate by ( , ) .
--> Dulpicate keys are not allowed but duplicate values are allowed .
--> Boundaries of dictionary is curly braces {} .
--> Keys must be immutable but values can be any python valid datatype .
--> Dictionary is a orderd  datatype .
--> Dictionary doesn't supports indexing and slicing .
--> default value of dictionary is empty curly braces {} .
--> It takes latest data from the dictionary .'''

# examples:-

d = {"a":1, "b":2, "c":3}
print(d)
# op:-  {'a': 1, 'b': 2, 'c': 3}

'''duplicate keys'''
d = {"a":1, "b":2, "a":3}
print(d)
# op:- {'a': 3, 'b': 2}      it always takes the latest key and value pairs if there is any duplicates keys .

'''duplicate Values '''
d = {"a":1, "b":2, "c":1, "d":2}
print(d)
# op:- {'a': 1, 'b': 2, 'c': 1, 'd': 2}

'''We can't use a list as a dictionary key  for examples 

d = {[1,2,3]:"list", [4,5,6]:"list1"}
print(d)
# op:-  TypeError: cannot use 'list' as a dict key (unhashable type: 'list')  .'''


d = {1:"int", 2.2:"float", True:"boolean", 2+3j:"complex", "hii":"string", (1,2):"tuple"}
print(d)
# op:- {1: 'boolean', 2.2: 'float', (2+3j): 'complex', 'hii': 'string', (1, 2): 'tuple'}


'''We can't use set() as a dictionary key . for example

d = { {1,2,3,4}: "set"}
print(d)
# op:- TypeError: cannot use 'set' as a dict key (unhashable type: 'set')   '''


'''Why ? because list and set are mutabel datatype but rest of all are immutable, so key is always a unique in nature that is way it won't accepts mutable datatypes .'''

'''to access the values .'''
d = {(1,2):"hello",(3,4):["a","b"]}

print(d[(1,2)])   
# op:-  hello

print(d[(3,4)])
# op:- ['a', 'b']



# METHODS IN DICTIONARY
# ---------------------

# 1. TO GET THE VALUE:-
# ----------------------
# example:-
d = {"a":"apple","b":"banana","c":"carot"}

print(d["a"])      #op:- apple
print(d["b"])      #op:- banana
print(d["c"])      #op:- carot

'''if the specified key is not present it will raises an KeyError for example .'''
# print(d["d"])      #op:- KeyError: 'd'


# 2. TO UPDATE THE KEYS VALUE:-
# ----------------------------
''' It will update the value if the specified key is present, else it will add the key and value pair if the key is not present .'''
# examples:-

d["a"] = "avagado"
print(d)
# op:- {'a': 'avagado', 'b': 'banana', 'c': 'carot'}


'''if the specified key is not present it will add the key and value pair into the dictionary .'''
# example:-

d["d"] = "dragon fruit"
print(d)
# op:- {'a': 'avagado', 'b': 'banana', 'c': 'carot', 'd': 'dragon fruit'}


# 3. keys():-
# ----------
''' It is an inbuild function which is used to return all the keys present in a dictionary .
--> It won't accepts any arguments .
--> The return type of keys() is "dict_keys()" of a list of values .

Syntax:- variable_name.keys() '''
# examples:-
dic = {"a":1, "b":2, "c":3}

print(type(dic))    #op:- <class 'dict'>

print(dic.keys())    #op:- dict_keys(['a', 'b', 'c'])


'''It won't accepts any arguments , if we pass it returns a TypeError

print(dic.keys("b"))
# op:- TypeError: dict.keys() takes no arguments (1 given)    '''



# 4. values():-
# -------------
''' It is used to return all the values present in a dictionary .
--> The return type of values is "dict_values()" , list of values .
--> It won't accepts any arguments .

Syntax:- variable_name.values() '''
# examples:-
dic = {"a":1, "b":2, "c":3}

print(type(dic))    #op:- <class 'dict'>

print(dic.values())    #op:- dict_values([1, 2, 3])


'''It won't accepts any arguments , if we pass it returns a TypeError

print(dic.values("b"))
# op:- TypeError: dict.values() takes no arguments (1 given)    '''



# 5. items():-
# ------------
''' It is used returns all the key and value pairs inside a tuple .
--> The return type of items() is "dict_items()" , list of tuple of values .
--> It won't accepts any arguments .

Syntax:- variable_name.items()'''
# examples:-
dic = {"name":"rajesh","age":23,"phno":1234567890,"state":"odisha"}
print(dic)
# op:- {'name': 'rajesh', 'age': 23, 'phno': 1234567890, 'state': 'odisha'}

print(dic.items()) 
# op:- dict_items([('name', 'rajesh'), ('age', 23), ('phno', 1234567890), ('state', 'odisha')])


''' It won't accepts any argument so if we pass any argument it will raises TypeError
print(dic.items("name"))
# op:-  TypeError: dict.items() takes no arguments (1 given) '''



# 6.get():-
# ---------
''' It is used to return the values based on the key specified .
--> By default it will returns "None" if the specified key is not present .
--> Instead of "None" we can give our own value .
--> It accepts two argumen .
    1.key
    2.value
    
Syntax:- variable_name.get(key,[value])  '''
# examples:-

dic = {"name":"rajesh","age":23,"phno":1234567890,"state":"odisha"}
print(dic.get("name"))   
# op:-  rajesh

print(dic.get("phno"))
# op:- 1234567890

''' what if the specified key is not present , for example ...'''
print(dic.get("fullName"))      
# op:-  None

''' To avoid the "None" we can give our own value, for example......'''
print(dic.get("fullName","fullname is not present in the dictionary"))
# op:- fullname id not present in the dictionary



# 7. update():-
# -------------
''' It is used to add or update morethan one key and value pairs into a dictionary .
--> It accepts dictionary as an argument .

Syntax:-  variable_name.update({dictionary})   '''
# examples:-

d = {"a":1,"b":2,"c":3}

# For update without update method
d["b"] = 22
print(d)
# op;-  {'a': 1, 'b': 22, 'c': 3}


# For add without update() method
d["d"] = 4
print(d)
# op:-  {'a': 1, 'b': 22, 'c': 3, 'd': 4}


# By using update() method
d.update({"c":33,"a":11,"e":55,"f":66,"g":77})
print(d)

# op:- {'a': 11, 'b': 22, 'c': 33, 'd': 4, 'e': 55, 'f': 66, 'g': 77}

''' look here the old values are update with new , if the specified keys are already present there .
 and if the keys not present it will add the key and value pairs normally .'''



#  8. setdefault():-
# ------------------
''' It is used to add the key and value into a dictionary .
--> By default it will assign the value as "None" for the key .
--> It accepts two arguments .
    1.key
    2.value
    
Syntax:- variable_name.setdefault(key,[value])   '''
# examples:-

d = {"a":1,"b":2,"c":3}
d.setdefault("d")
print(d)
# op:-  {'a': 1, 'b': 2, 'c': 3, 'd': None}

'''instead of None add the value for example...'''
d.setdefault("e",55)
print(d)
# op:-  {'a': 1, 'b': 2, 'c': 3, 'd': None, 'e': 55}

'''if the key is present , and we want to update the keys then it will print the dictionary as it is .for example.......'''
d.setdefault("b",22)
print(d)
# op:-  {'a': 1, 'b': 2, 'c': 3, 'd': None, 'e': 55}     // look at here the value of "b" is won't change .


''' if we try to access then it will print the values specified with the keys , although if we try to update also  for example ........'''
print(d.setdefault("a"))         #op:- 1
print(d.setdefault("b",22))      #op:: 2



# 9. fromkeys():-
# ---------------
''' It is used to add morethan one keys at a time into a dictionary .
--> It assign the value for all the keys by default as "None" .
--> It accepts two arguments .
    1. collection
    2. value
    
Syntax:- variable_name.fromkeys(collection,[values]) '''
# examples:-

d = {"a":1,"b":2}
res = d.fromkeys(["a","b","c","d","e","f"])
print(res)
# op:- {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None}

dic = dic.fromkeys(("a","b","c","d","e"),3)
print(dic)
# op:- {'a': 3, 'b': 3, 'c': 3, 'd': 3, 'e': 3}     // see it has assign the value for each element as "3"

'''if we pass morethan one argument it will raises error for example.......

dic = dic.fromkeys(("a","b","c","d","e"),3,4)
print(dic)
# op:- TypeError: fromkeys expected at most 2 arguments, got 3    '''



# REMOVE METHODS
# ---------------

# 10. pop():-
# -----------
''' It is used to remove the key value pairs based on the key specified .
--> It raises KeyError if the specified key is not present .
--> It returns the value which is associated with the key .

Syntax:- variable_name.pop(key)   '''
# examples:-

dic = {'a': 3, 'b': 3, 'c': 3, 'd': 3, 'e': 3}
print(dic.pop("b"))
# op:- 3

print(dic)
# op:- {'a': 3, 'c': 3, 'd': 3, 'e': 3}

'''
It raises KeyError if the specified key is not present for example ....
print(dic.pop("g"))
# op:- KeyError: 'g   '''



# 11. popitem():-
# ---------------
''' It is used to remove the key and value pair atlast from a dictionary .
--> It won't accepts any arguments .
--> It returns tuple of (key,value) which got removed .
--> It raises KeyError if the dictionary is empty .

Syntax:- variable_name.popitem()  '''
# examples:-
dic = {'a': 3, 'c': 3, 'd': 3, 'e': 3}
print(dic.popitem())
# op:- ('e', 3)


''' It won't accepts any arguments, if we pass it will raises an error .
print(dic.popitem("b"))
op:- TypeError: dict.popitem() takes no arguments (1 given) '''


print(dic.popitem())        #op:- ('d', 3)
print(dic.popitem())        #op:- ('c', 3)
print(dic.popitem())        #op:- ('a', 3)
print(dic)                  #op:- {}

'''Now the dictionary is become empty so , if we try to peform the popitem() it will raises an error for example........
print(dic.popitem())
op:- KeyError: 'popitem(): dictionary is empty'     '''



# -----------------------------------Thank You  ------------------------------------------------------





























