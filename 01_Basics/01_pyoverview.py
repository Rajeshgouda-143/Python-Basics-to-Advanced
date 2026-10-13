#  What is Python ?

'''Python is a high-level, general-purpose, interpreted programming language created by Guido van Rossum and first released in 1991. It is known for its simple and readable syntax, which makes it easier for developers to write, understand, and maintain code. Python is widely used in web development, automation, data science, artificial intelligence, machine learning, and software development. '''

# Features of Python
# ------------------
# 1.easy syntax
# 2.High-level language
# 3.interpreted language
# 4.Platform independent language
# 5.Contains large standard library
# 6.It support OOPs 100%
# 7.Automatic garbage collected
# 8.Dynamic typed language
# 9.Support dynamic memory allocation

# High Level language 
# --------------------

'''
A high-level language is a programming language that uses human-readable syntax and familiar words, making it easier for programmers to write, understand, debug, and maintain programs without dealing directly with the complex details of computer hardware.

Example in Python:
a = 10
b = 20
print(a + b)
Output:
30

In Python, we can write simple instructions like print(a + b) instead of writing complex machine instructions using binary digits (0 and 1).
that is we called python is a High Level programming langauage.
'''

# Low Level Language
# ------------------
'''
A low-level language is a type of programming language that is closely related to the computer's hardware and provides little or no abstraction from the machine's internal operations. It is generally harder for humans to read, write, and understand compared to a high-level language.

There are two main types of low-level languages:

1. Machine Language: Uses binary digits (0 and 1) directly understood by the CPU.
2. Assembly Language: Uses symbolic instructions such as MOV, ADD, and SUB, which are translated into machine language by an assembler.

Example:
Machine language (illustrative):
10110000 00000101

Assembly language:
MOV AL, 5

Key characteristics:
- Closely related to computer hardware.
- Provides greater control over hardware operations.
- Generally more difficult to write and maintain.
- Often used in embedded systems, device drivers, and hardware-level programming.
'''

# proggramming Language
# ---------------------

'''A programming language is a formal language used to communicate instructions to a computer so that it can perform specific tasks, process data, and solve problems according to the programmer's requirements.

Or Simple Word We can say:- It is a mediater which convert high level language into low-level language and low-level langauge into high-level langauage is called programming langauage.

Examples: Python, Java, C, C++, JavaScript, and C#.

Example in Python:

print("Hello, World!")

Output:
Hello, World!


Here, print("Hello, World!") is an instruction written in Python that tells the computer to display the text Hello, World!.
'''

# Interpreted Langauage
# ---------------------

'''An interpreted language is a programming language in which the code is executed with the help of an interpreter, which translates or processes the program's instructions into actions the computer can perform.

Or we can say: The source code is first compiled into bytecode, which is then executed by the Python virtual machine. and display the result it is called interpreted language.

Example: Python

a = 10
b = 20
print(a + b)

Output:
30


Here, the Python runtime processes the code and executes the instructions to produce the output.
How does it work?

1. The programmer writes code in a source file.
2. The Python interpreter environment processes the code.
3. If the code is valid, the instructions are executed and the output is produced.

'''

# Automatic Garbage Collected
# ---------------------------
'''It means Whenever the reference count of a value become zero garbage collector will remove the value from the memory.

for example:-

a = 10
b = 20
c = 10

here we update the value
-----------------------
a = 20
c = 30

Now the a becomes 20 and b also 20 so they stored in the same memory and c becomes 30 , so now there is no variable which conatains the 10 so the garbage collector delete the value from the memory. 
'''

# Dynamic typed language
# ----------------------
''' In python declaration of datatype are not mandatory , the python interpreter assign the datatype during execution of a program.

it means: - 
suppose in java we have to declare the data type like int, str....etc

int a = 10;
str b = "rajesh";

But:- In python there is no declaration of data type for example

a = 10;
name = "rajesh"

'''

# Dynamic memory allocation
# -------------------------
''' Whenever we are storing same value in more than one variable python interpreter while store the value only once in the memory
and all the variables will findout to same memory.

for examples:- 

a = 10
b = 10

c = 20
d = 10

Here all the 10 are stored in the same memory. and for 20 different.

'''
