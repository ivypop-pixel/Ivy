# File: homework1 . py
# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a is an int 
b = 1.5 
print (b)
print(type(b)) # float
c = 3j 
print (c)
print(type(c)) # complex
d = "hello" 
print (d)
print(type(d)) #str
e = [1, 2, 3] 
print (e)
print(type(e)) #list
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print (f)
print(type(f)) #dict
g = (1, 2)
print (g)
print(type(g)) #tuple
h = ["apple", "banana", "strawberry"]
print (h)
print(type(h)) #list
i = True
print(i)
print(type(i)) #bool
j = None
print(j)
print(type(j)) #NoneType
k = [True, "blue", 12]
print(k)
print(type(k)) #list
l = str(14)
print(l)
print(type(l)) #str
m = 1e4
print(m)
print(type(m)) #float
# Questions
# 11
# int, float, str, tuple, list, NoneType, bool,dict,complex
# b and m,d and l,e and h and k
# str() creates a new string from your given objects
n = range (5)
print(n)
print(type(n)) #range

# --- Booleans ---
print(10 > 9) #true
print(0 == 9)#false
print(10 <= 9)#false
print(bool("abc"))#true
print(bool(123))#true
print(bool(["apple","‘cherry", "banana"]))#true
print(bool(True))#true
print(bool(False))#false
print(bool(0))#false
print(bool(""))#false
print(bool(" "))#true
print(bool(()))#false
print(bool([]))#false
print(bool({}))#false
print(bool(True and False))#false
print(bool(True and True))#true
print(bool(False and False))#false
print(bool(True or False))#true
print(bool(True or True))#true
print(bool(False or False))#false
print(bool(not(False)))#true
print(bool(not(True)))#false
# #Questions
# 1. it depends on the words 'and' & 'or'
# 2.print(bool(["apple","‘cherry", "banana"]))#true
print(bool(1+3)) #its true since the expression is defined
print(bool(5-5)) #its false since the expression comes to 0

# --- Operators ---
print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, + performs addition
print(2 * 4) # 8, + performs multiplication
print(6/3) # 2.0, + performs div
print(5 % 2) # 1, + modular (remainder of 5/2)
print(3**2) # 9, + performs 2 squared
print(15//2) # 7, + floor div, rounds down esult of 15/2
print(5 == 2) # false, + 5 is not eqaul to2 so its false
print(10 != 10) # false, its saying 10 is not eqaul to 10
print(2 < 5) # true, + verifies 2 less than 5
print(12 > 5) # true, + verifies 12 greateer than 5
print(5 <= 6) # true, + verifies  5 is less or equal to 6
print(1 >= 10) # true, + states  1 is not greater or equal to 10

x = 5
x += 5
print(x) #5
x -= 4
print(x) #6
x *= 3
print(x)#18

# 1. it looks at two given expressions and prints T if both sides are T. if one ir both are false then its F
print((0 > -1) and (1 == 1)) # T
print((0 > -1) and (1 == 0)) # F

# 2. prints T if at least one side is true, or else false
print((0 > 1) or (1 == 1)) # T
print((0 > 1) or (1 == 10)) # F
print ((not (9 < 7)))# T
print ((not (0 < 7)))# F

# / is dividing, and // divides and rounds down to nearest whole number
# % gives the remainder when you divide
# the %. 
print(33%7)
# += means adding whatever value on rhs to x. -= means same but ubtract, and *=

# --- Strings ---
my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0])# Prints: h
print(my_string[1])# Prints: e
print(my_string[2])# Prints: l
print(my_string[3])# Prints: l
print(my_string[4])# Prints: o
print(my_string[-1])# Prints: o
print(my_string[1:3])# Prints: el
print(my_string[0:5:2])# Prints: hlo
print(len(my_string))# Prints: 5
print(my_string + "goodbye") # Prints: hellogoodbye
print(my_string * 7) # Prints: hellohellohellohellohellohellohello

# you gret specific components of a string. 8 and 9 did this
name = "Oski"
print("Hello, my name is", name)
name = "Oski"
print(f"Hello, my name is {name}")# this is a formatted version

# cd
# change directories
# Example: cd Desktop

# ls
# lists files and folders in working directory
# Example: ls downloads

# ls -a 
# shows hidden files
# not sure maybe just ls -a 

# mkdir 
# makes new directory
# mkdir hw1

# cat
# concatenate text files
# cat somehthing.txt

# pwd
# prints current working directory
# pwd file

# cd ..
# move up to parent directory
# cd ..  downloads

# cd .
# changes directory to current ver
# cd .  downloads

# cd ~
# changes current directory to users home directory
# cd ~  downloads

# cp
# copies of files from one source to some place
# cp filename.txt

# mv
# move files
# mv filename.txt /v/v/v/ i think

# rm
# remove files permamnetly 
# rm file.pdf

# clear
# clears the text in the windoe
# clear

# grep
# searches for text patterns in your files
# grep "something" file.pdf

# Question
# ls-l, provides long format list
# find, can find files on the systme
# rmdir, remove empty directories

# one is listing evething, the other is the hiddne files

# ls -l, provides long format list
# cp -r, recrusive copying
# grep -i ignore case