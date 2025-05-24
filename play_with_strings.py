# -*- coding: utf-8 -*-
"""
Created on Sat May 24 10:12:39 2025

@author: Admin
"""

test_str = "this is a test string \nand this is another line of the test string"

print(test_str)

list_str_lines = test_str.splitlines()

print(list_str_lines)

str_list_sepbynewlinechar = test_str.split("\n")

print(str_list_sepbynewlinechar)

check_if_true = test_str.startswith('this')

if check_if_true:
    print("above string starts with 'this'")
else:
    print("above string doesn't start with 'this'")
    
test_str_2 = '''this is a multi-line
string, this will bring more
clarity to how strings
work in python'''

list_str_lines_2 = test_str_2.splitlines()

print(list_str_lines_2)

str_list_sepbynewlinechar_2 = test_str_2.split("\n")

print(str_list_sepbynewlinechar_2)

if list_str_lines_2 == str_list_sepbynewlinechar_2:
    print("both splitlines & split with a new line char work fine")
    
test_str_3 = "Programming in Python is fun"
test_str_4 = "programming in python is FUN"

if test_str_3.lower() == test_str_4.lower():
    print("lower function worked as expected")
if test_str_3 != test_str_4:
    print("strings are case-sensitive")
    
#substring concepts

print(test_str_3[0] == 'P')

print(test_str_3[2:10])

print(test_str_3[:16])

#some other common methods for strings

print(test_str_3.swapcase()) #changes lower to caps and viceversa for all chars ina string

print(test_str_3.capitalize()) # capitalises the first letter of a sentence

print(test_str_3.casefold()) # makes strings comparable where char case doesn't matter

print(test_str_3.center(70,"*")) #padding

print(test_str_3.count("fun")) #counts the number of occrrences of a substring

print(test_str_3.endswith("fun")) #checks if it ends with given substring

print(test_str_3.find("python")) #returns the position where substring is found, returns -1 if not found

print(test_str_3.find("Python"))

formatted_str = "programming in {} is {}".format("python", "fun") #formats the string

print(formatted_str)

formatted_str_2 = "programming in {name} is {adjective}".format(name="python",adjective="easy")

print(formatted_str_2)

#usage of format_map() that allows passing key value pair in a dictionary

template_str = "programming in {name} is {adjective}"

data = {"name": "python", "adjective": "funniest"}

formatted_str_3 = template_str.format_map(data)

print(formatted_str_3)

print(test_str_3.index("fun")) #returns the lowest index where substring is found

if test_str_3.isalnum():
    print(test_str_3 + " is an alphanumeric string")
else:
    print(test_str_3 + " is not an alphanumeric string")
    
test_str_5 = test_str_3.replace(" ", "")
print(test_str_5)

if test_str_5.isalnum():
    print(test_str_5 + " is an alphanumeric string")
else:
    print(test_str_5 + " is not an alphanumeric string")
    
print(test_str_3.isascii())

print(test_str_3.isdecimal())

test_int = "8"

print(test_int.isdecimal())

print(test_str_3.isdigit())
print(test_int.isdigit())

print(test_str_3.isidentifier()) # returns true if string is a valid python identifier else false

print("elif".isidentifier())

print(test_str_3.isspace())
print(" ".isspace())

print("-".join(["word_1","word_2","word_3"]))

print(test_str_3)

print(test_str_3.ljust(60,'*'))

test_str_6 = "stringwithoutspaces"
print(test_str_6.ljust(70,'*'))

test_str_7 = "     string with leading whitespaces"
print(test_str_7.lstrip())
print(len(test_str_7))

print(test_str_6.partition("th")) #partitions the string into a tuple with first element being the part before the sep, the second beind the sep itself and third part being the part after the sep

print(test_str_6.removeprefix("str"))

print(test_str_6.removesuffix("spaces"))

test_str_8 = "thisxxstringxxcontainsxxmultiplexxsubxxstringsxxtoxxbexxreplaced"

print(test_str_8.replace("xx", "yy",3)) #last argument if of max number of instances to be replaced

print(test_str_8.rfind("xx"))

print(len(test_str_8))

print(test_str_8.rindex("xx")) #same as rfind with the only difference that when sub string not found it returns ValueError and rfind() returns -1

print(test_str_8.rjust(70,'+'))

print(test_str_8.rpartition('xx'))

print(test_str_8.rsplit('xx',5))

print(test_str_8.rstrip('replaced'))

print(test_str_8.upper())

print(test_str_8.zfill(70))
