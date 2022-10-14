

print("\nLesson3: String & concatenation\n")

# Escape sequence eg \', \", \n, \t, \v, \\, \b, \r

article = "This is an article\na multiline article\n\t the period will be removed from this line.\b\n I want to see what this sequence does\r"
print(article)

# Raw string
anotherArticle = r"This is an article\na multiline article\n\t the period will be removed from this line.\b\n "
print(anotherArticle)

# Concatenation
group = "wood"
attr = "pecker"
bird = group + attr
print(bird)

print("\nLesson 4: Basic Arithmetic Operators\n")
print('Arithmetic operators\n') # They are + - / * ** // %
result = 4 + 6
print(result)

result = 10 / 2
print(result)

result = 10 % 5
print(result)

result = 10 ** 3
print(result)

result = 10 // 5
print(result)

print('Compound operators\n') # They are += -= /= *= **= //=

result = 4
result += 3
print(result)

result = 4
result -= 3
print(result)

result = 4
result *= 3
print(result)

result = 4
result /= 2
print(result)

result = 4
result %= 3
print(result)

result = 4
result **= 3
print(result)

result = 4
result //= 3
print(result)

print("\nLesson 5: Conditional and Relational operators\n")
# Conditional operators: if, if else and elif
# Relational operators are also known as comparison operators: <, >, <=, >=, ==, !=
print("if statement\n")
age = 10

if age == 10:
    print("You are young")

print("if-else statement\n")
age = 20
if age <= 10:
    print("You are young")
else:
    print("You are not too young")

print("elif statement\n")
age = 20
if age <= 10:
    print("You are too young")
elif age == 18:
    print("You can vote")
elif age == 12:
    print("You are now a teen")
elif age != 12:
    print("You are not 12 years")
else:
    print("You are not too young")

print("\nlesson 6: Conditional and logical operators\n")
print("\nLogical operators are \n: and , or, not")

print("\nlesson 7: Loops( For and while loops)\n")

print('\nFor loop')
# iterate sequence
fruits = ["Apples", "Mango", "pear"]
for fruit in fruits:
    print("Fruit:", fruit)

# another example
name = "python"
for ch in name:
    print("character", ch)

# iterate number
number = 5
for i in range(number):
    print("number", i)


# while loop
print("\n While loop\n")
number = 10

while number > 0:
    print("Number is:", number)
    number -= 1

# Lesson 8: Break, Continue and Else statements
print("\n Break\n")

number = 5
for i in range(number):
    if i == 3:
        break
    print("for: Number", i)

print("\nanother method with the variable directly & not its index\n")
for number in range(number):
    if number == 3:
        break
    print("for: Number", number)

number = 5
while number > 0:
    if number == 3:
        break
    print("while: Number:", number)
    number -= 1


print("\ncontinue\n")
number = 5
for i in range(number):
    if i == 3:
        continue
    print("for: Number", i)

while number > 0:
    if number == 3:
        number -= 1
        continue
    print("while: Number:", number)
    number -= 1

print("\n else statement and continue\n")

number = 10
for i in range(number):
    if i == 3:
        continue
    print("for: Number", i)
else:
    print("end of loop")

while number > 0:
    if number == 3:
        number -= 1
        continue
    print("while: Number:", number)
    number -= 1
else:
    print("end of loop")


print("\n else statement and break\n")

number = 10
for i in range(number):
    if i == 3:
        break
    print("for: Number", i)
else:
    print("end of loop")

while number > 0:
    if number == 3:
        number -= 1
        break
    print("while: Number:", number)
    number -= 1
else:
    print("end of loop")


print("\nLesson 9: Functions\n")
# Functions are reuseable block of code that can be called (invoked) at any point in the program
# There are 3 types of functions in python: Built-in, User define functions (UDF), Anonymous function
# Built in functions: These are functions that come predefined with python library. Eg print, len, min, max
# UDF: functions created by users to perform a particular logic in the program and are denoted using 'def' keyword
# Anonymous: These are user define functions that are not declared using the def keyword & dont have a name. They are AKA lambda
# structure of function is: def <function keyword> (<parameters>)
# python does not allow for empty functions (with no code or logic under). Instead ypu can use 'pass' as code block

def name():
    print("I am Udy")

def greeting():
    print("Hello! Good morning")

def goodbye():
    print("Thank you")
    print("Goodbye")

name()
greeting()
goodbye()

# Empty functions are not allowed in python except pass is used in place of the logic(code block)

def login_test():
    pass

login_test()


print("\nLesson 10: Anonymous functions\n")
# Also called lambda, its used when a) function has short lifespan, b)function has 1 expression c)function is to be passed into another function
# structure of anonymous function is lambda: code block

greet = lambda: print("Hello World Anonymous")
def accept(cb):
    cb("Hello")


greet()   # use b) function has 1 expression
accept(lambda x: "Hello All")   # use c) function inside a function


print("\nLesson 11: Functions- Argument & return statements\n")
# parameters = the variables defined within the () of a function
# argument = the values passed into the function
# 5 types of arguments in python are: required, default, keyword, arbitrary, arbitrary keyword
print("\n Required Argument\n")  # the order of the arguments and parameter matter
def add(num1,num2):
    print(num1+num2)

add(2,5)

# example 2
def greet(name):
    print("Hello", name)

greet("Bolu")

print("\n Default Argument\n")  # the order of the arguments and parameter matter
def add(num1,num2=3):
    print(num1+num2)

add(2) # if only 1 value (argument) is passed, the function will use 3 for num2 as the default second value

# example2  # multiple applications for default argument
def add(num1=67,num2=13):
    result = num1+num2
    print(result)

add()
add(7)
add(3,3)

print("\n Arbitrary/variadic Argument\n") # used to denote what value belongs to which parameter and does not matter the order
def add(num1,num2):
    print(num1+num2)

def minus(num1,num2):
    result = num1 - num2
    print(result)


add(num1=4,num2=5)
add(num2=5,num1=4)
minus(num1=10, num2 = 7)
minus(num2=1, num1 = 3)

def print_value(*args):
    print("Args:", args)

print_value(1, 7, 9)

print("\n Arbitrary Keyword Argument\n")  # used when you do not know the number of arguments to be passed in the function
# it is preceeded with **
def add(** kwargs):
    print(kwargs['num1']+kwargs['num2']+kwargs['num3']+kwargs['num4'])

add(num1=4,num2=9,num3=4,num4=10)


print("\n Return Statements\n")
def add_and_return(num1,num2):
    result = num1 + num2
    return result

res = add_and_return(50,50)
print("50:50", res)

def check_number(number):
    if number > 5:
        return
    print("Number:", number)


check_number(1)
check_number(2)
check_number(3)
check_number(6)


print("\nLesson 12: Global & local variables\n")
# Global variables can be accessed at any part of the code while local variables are accessible only within the function they are called
name = "Testify"  #Global variable

def hello():
    language = "Python"  #local variable
    print("Global variable:", name, "Local variable:",language)

def greet():
    framework = "Selenium"  #local variable
    print("Global variable:", name,"Local variable:",framework)

print(name) #Global
# print(language) # cant be called since they are variables within a function
# print(framework) # cant be called since they are variables within a function
hello()
greet()

# variable shadowing: This is the masking of an outer variable by the inner variable.
# This is done when the inner variable bears the same name as that of the outer variable

platform = "Web"            #global variable

def name():
    platform = "mobile"             # this variable is shadowing the global variable of value web
    print("Platform:", platform)

name()

print("\n Lesson 13: Function & loops: Recursion\n")
# Recursion is a feature in python where a function can call itself.
# It can be used just like 'for' & 'while' loops but dont guaranty the same optimal behaviour

def reduce_number_loop(num):
    while num >= 0:
        print(num)
        num -= 1

print("\nRecursionError\n")
# This error occurs when function calls itself repeatedly for the maximum number of depth configured in python
#def print_hello():
#    print("Hello World")
#    print_hello()

#print_hello()


#def reduce_number_recurssion(num):
#    print(num)
#    if number == 0:
#        return
#    reduce_number_recurssion(num-1)

reduce_number_loop(5)
print()
#reduce_number_recurssion(5)

print("\n Lesson 14: Basic String Operation\n")
# some string operations are: len(), upper(), lower(), capitalize(), count(), find()
# index(), strip(), rstrip(), lstrip(), split(), format()
name = "testify is the name of a software testing training company that trains testers"
name2 = "   testify is    the name of a software testing training company that   trains testers  "

# size of the string
size = len(name)
print(size)

# upper case
upper_case = name.upper()
print(upper_case)
# lower case
lower_case = name.lower()
print(lower_case)
# capitalized will only apply upper case to the first letter
cap = name.capitalize()
print(cap)
# count is used to check the number of reoccurrence of a specified entity(word, letter, figure etc)
count_value = name.count("test")
print("test count: ", count_value)
t_value = name.count("t")
print("t_count: ", t_value)
# find -> used to get the value of a position in a string, if the value does not exist in the string -1 is returned
find_value = name.find("is")
print("is- find position:", find_value)
# find for non existing value
python_value = name.find("python")
print("python position:", python_value)
# index -> used to get the value of a position in a string, if the value does not exist in the string it throws an exception
index_value = name.index("is")
print("is- index position:", index_value)
# index for non existing value
#java_value = name.index("java")
#print("java index position:", java_value)  #an exception error is thrown

# strip -> trims the string, removes excess white space at the beginning & end of the string
strip_value = name2.strip()
print("strip value:", strip_value)

# lstrip -> removes excess white space from beginning
leftstrip_value = name2.lstrip()
print("left strip value:", leftstrip_value)
# rstrip -> removes excess white space from beginning
rightstrip_value = name2.rstrip()
print("right strip value:", rightstrip_value)
# split -> splits the string into array using the specified value
split_value = name.split()      # When no value is passed
print("split no-value:", split_value)
split_value = name.split("that")  # when a value of 'that' is passed
print("split value (that):", split_value)
split_value = name.split(' ')  # same result as when no value is passed
print("split space(' '):", split_value)
# format -> used to format a value in a string.They are of 2 kinds:
# named format
unformatted = "My name is {name}. I am a {occupation}"
formatted_one = unformatted.format(name="Peter", occupation="Tester")
formatted_one2 = unformatted.format(name="Meghan", occupation="Princess")
print("Formatted(named) result:",formatted_one)
print("Formatted(named) result:",formatted_one2)

# index format
unformatted = "My name is {0}. I am a {1}"
formatted_one = unformatted.format("Peter","Tester")
formatted_one2 = unformatted.format("Meghan", "Princess")
print("Formatted(index) result:",formatted_one)
print("Formatted(index) result:",formatted_one2)

# unindex format
unformatted = "My name is {}. I am a {}"
formatted_one = unformatted.format("Peter","Tester")
formatted_one2 = unformatted.format("Meghan", "Princess")
print("Formatted(unindex) result:",formatted_one)
print("Formatted(unindex) result:",formatted_one2)

print("\nLesson 15: Basic List Operations")
# list item is the same as array in js. Its used to store a number of items under the same variable
# List functions: append(add item to end of list), insert(add item to a specified part of list),
# pop(remove item from specified location by index), remove(remove an item from list by the value),
# count(return the number of items in the list), clear(remove all the items from the list)
# copy(return a deep copy of the list), reversal(reverse order of the list), sort(sort the list)
# extend(add a list or any other iterable items to the end of the list)
languages = ["Python", "Java", "C#"]

# append -> add item to end of list
languages.append("Javascript")
print("appended an item: ", languages)

# insert -> add item to a specified part of list
languages.insert(0, "C")
languages.insert(2, "PHP")

print("inserted items: ", languages)

# pop-> remove item from specified location by index
languages.pop(0)
languages.pop() # if you dont specify the index, the last item will be removed
print("popped an item: ", languages)

# remove-> remove an item by the value from list
remove = languages.remove("PHP")
print("remove: ", languages)

# count-> return the number of occurrence of an item in the list
languages.append("Java")
count = languages.count("Java")
print("list: ", languages)
print("count : ", count)

# len -> count the number of items in the list
length = len(languages)
print("list: ", languages)
print("length of list: ", length)

# clear -> remove all the items from the list
languages.clear()
print("clear: ", languages)

# copy -> return a deep copy of the list
languages = ["Python", "Java", "C#"]
lang_copy = languages.copy()
print("copy: ", lang_copy)

# reversal -> reverse order of the list
languages.reverse()
print("reversal: ", languages)

# sort(sort the list in asc order)
languages.append("Javascript")
languages.sort()
print("sort in asc order: ", languages)

# sort(sort the list in desc order)
languages.copy()
languages.sort(reverse=True)
print("sort in desc order: ", languages)

# extend -> add a list or any other iterable items to the end of the list
languages.extend(["Fortran", "PHP", "Ruby", "C"])
print("extend: ", languages)

print("\nLesson 16: Basic Dictionary Operations\n")
# Dictionary are a set of key-value pairs (object in js) and are created using curly bracket
# get(return the value of the specified key), items(returns the list of the tuple of the dictionary key-value),
# keys(returns list containing dictionary key), values(returns list containing dictionary values),
# pop(removes item with the specified key), popitem(removes last inserted key-value pair),
# update(updates the dictionary with the specified key-value pair), clear(removes all element from dictionary)
# copy(returns a copy of the dictionary)
animals = {
    "bird": "Parrot",
    "mammal": "Cow",
    "fish": "Titus"
}
print("dictionary:", animals)

# get-> return the value of the specified key
get_bird = animals.get("bird")
get_fish = animals.get("fish")
print("get1:", get_bird)
print("get2:", get_fish)

# items-> returns the list of the tuple of the dictionary key-value
# tuple is denoted with () while list aka array in js is denoted with []
# eg t = (1,2) while l = [1,2]
animal_items = animals.items()
print("items:", animal_items)

# keys-> returns list containing dictionary key
animal_keys = animals.keys()
print("keys:", animal_keys)

# values-> returns list containing dictionary values
animal_values = animals.values()
print("values:", animal_values)

# pop -> removes item with the specified key
animals.pop("mammal")
print("popped list:", animals)

# popitem -> removes last inserted key-value pair
animals.popitem()
print("poppeditem list:", animals)

# update -> updates the dictionary with the specified key-value pair
animals.update({"mammal": "Elephant", "fish": "Salmon", "reptile": "lizard"})
print("updated list:", animals)

# clear -> removes all element from dictionary
animals.clear()
print("cleared list", animals)

# copy -> returns a copy of the dictionary
animals.update({"mammal": "Elephant", "fish": "Salmon", "reptile": "lizard"})
print("copied list:", animals)
print(animals)

print("\n Lesson 17: Object Oriented Programming- OOP")
# OOP is a programming paradigm that relies on classes and objects
# Its used to structure code into reuseable components which are called classes
# the building blocks of OOP:COAM classes, objects, attributes, methods
# Classes contain attributes and methods, individual objects are created from a class
# The first parameter in a method in python is called 'self'
# eg
# class Animal:               # Class
#    name = "Cat"             # Attribute
#    group = "Mammal"         # Attribute
#    part = Part()            # Object

#    def get_name(self):     # Method
#        return self.name

# Object is an instance of a class and contains specific data. Eg a dog object of the animal class above can have attributes name and group of its own

# Class
class Animal:               # Class

    name = "Cow"             # Attribute
    group = "Mammal"         # Attribute

    def get_name_group(self):     # Method
        return self.name + ":" + self.group

# Object

cow = Animal()
print(cow.name, cow.group, cow.get_name_group())

#cow2 = Animal()
#cow3 = Animal()
#cow4 = Animal()

print("\n Lesson 18: OOP Attributes")
# Attributes are info stored in a class and if an object is present in a class the attributes store info of the element in the object
# In otherwords, attributes are like variables that are exclusive to a class
# There are 2 types of attributes: Class & instance
# class attributes: Attributes declared inside class but outside method. They are not tied to any instance method & thus are shared across all class method
# instance attributes: Attributes declared inside a class constructor or method. They are tied to a particular object instance & modifying them does not change the object instance
# eg
class Animal:

    group = "Mammal"           # class variable
    can_walk = True

    def __init__(self, name):
        self.name = name       # instance variable

cat = Animal("Cat")
dog = Animal("Dog")

print(cat.name)                 # instance variable
print(dog.name)

print(cat.group)                # class variable
print(dog.group)

print("\nLesson 19: OOP Methods")
# Method is a function defined inside a class to perform a specific action. It can return value, accept parameter
# Constructor: special type of method used to instantiate a class object. the instance attribute are created in the constructor
# The name of the constructor in python is __init__
# There are 2 types of constructors: default (doesnt accept parameters), parameterised constructors
class Animal:

    group = "Mammal"           # class variable
    leg_count = 4

    def __init__(self, name):   # Method: Constructor
        self.name = name

    def get_name(self):         # Method:
        return self.name

    def get_group(self):        # Method:
        return self.group

# Examples

class Animal:

    group = "Mammal"
    leg_count = 4

# Default constructor
    def __init__(self):
        self.name = "Unknown`"

animal = Animal()
print("Animal: ", animal.name, animal.group)


class Vehicle:

    can_fly = False
    tire_count = 4

# Parameterized constructor
    def __init__(self, make):  # Adding a parameter called make to the class
        self.make = make

# Normal parameterised method
    def set_tire_count(self, count):        # A method to set_tire_count using the parameter 'count'
        self.tire_count = count

    def set_flyability(self, cfly):        # A method to set flyability using the parameter 'cfly'
        self.can_fly = cfly

# Normal unparameterised method
    def set_make_tire_count(self):        # A method to set 2 variables of make and tire count
        return self.make + ":" + str(self.tire_count)

    def check_type(self):
        if self.make == "Aeroplane":
            print("This is an Aeroplane")
        else:
            print("This is likely a car")

toyota = Vehicle("Toyota")
print("\nVehicle: ", toyota.make, toyota.tire_count)
toyota.check_type()


lexus = Vehicle("Lexus")
print("\nVehicle: ", lexus.make, lexus.can_fly)
lexus.check_type()

plane = Vehicle("Aeroplane")
plane.set_tire_count(3)                     # invoking the set_tire_count method
plane.set_flyability(True)                  # invoking the flyability method
plane.set_make_tire_count()                  # invoking the set make & tire count method
print("Vehicle: ", plane.make, plane.tire_count, plane.can_fly)
print("Vehicle\'s make & tire count: ", plane.set_make_tire_count())
plane.check_type()

print("\n Lesson 20: OOP: Inheritance\n")
# 4 principles of OOP in python are: Inheritance, Polymorphism, Encapsulation, Data Abstraction
# Inheritance: ability of a class to inherit objects, attributes & methods from another class
# Polymorphism: ability for a method to perform any function/logic
# Encapsulation: ability to hide some data and only expose data you need
# Data Abstraction: allows us to have attributes & core logic to be in the class while exposing only the method to the user
# Base class/parent class (class that gives the properties) ---> derived/child class (class that recieves the properties)

class Vehicle:
    model = "unknown"
    make = "unknown"
    production_year = 1990

    def print_vehicle_info(self):
        print("\n Vehicle{", self.model + ":" + self.make + "}")

class Car(Vehicle):
    wheel_count = 4

    def __init__(self, make, model):        # we used a constructor to modify the attributes in vehicle class
        self.make = make
        self.model = model

class Plane(Vehicle):
    model = "Aeroplane"         # We assigned another value to the attributes in vehicle (make & model)
    make = "Boeing"

vehicle1 = Vehicle()
vehicle1.print_vehicle_info()

car1 = Car("Toyota", "Camry")
car1.print_vehicle_info()

plane1 = Plane()
plane1.print_vehicle_info()


print("\nLesson 21: Polymorphism")
# Capability of many class methods to perform the same task
# Using inheritance a class can override the parent method & polymorphism allows the same method to perform
# different functions

class Vehicle:

    def drive_direction(self):
        print("Vehicle: Drive forward")

vehicle = Vehicle()
vehicle.drive_direction()

class Plane(Vehicle):

    def drive_direction(self):
        print("Plane: Drive upward")

plane = Plane()
plane.drive_direction()


class Submarine(Vehicle):

    def drive_direction(self):
        print("Submarine: Drive downward")

submarine = Submarine()
submarine.drive_direction()

print("\n Lesson 22: Encapsulation")
# Idea pf enclosing info in a class and exposing only selected info.
# This puts a restriction on accessing attributes and methods which can lead to accidental manipulation of data
# we use __ infront of an attribute to denote a private attribute

class User:

    __first_name = "Testify"
    __last_name = "QA"
    __attendance = 1

    def get_name(self):
        return "User: " + self.__first_name

    def get_attendance(self):
        value = self.__attendance * 20
        return value

user = User()
print(user.get_name())
print(user.get_attendance())


print("\n Lesson 23: OOP Data Abstraction")
# This is used to hide unneccesary info from user. Its similar to encapsulation but uses masking to hide info
# Data abstraction uses private attributes & abstract classes

class LoginSession:

    __email = "user@test.com"
    __password = "password"

    def get_email(self):
        return self.__email

    def get_password(self,):
        return "**********"     # masking the actual value

session = LoginSession()
print(session.get_email())
print(session.get_password())


print("\n Lesson 24: Abstract Class & Interface\n")
# Abstract classes are classes that contain abstract methods.
# Abstract methods are methods that are declared but not implemented
# A class inheriting from an abstract class must implement the abstract method
# Python has a built-in ABC(Abstract Base Classes) library that enables us create & use abstract classes
# To declare an abstract class, the class metaclass value should be set abc.ABCMeta or the class should inherit
# from abc.ABC class
# Interfaces are similar to abstract methods in that they define abstract methods. The difference in interface is
# that it does not implement method when subclassed

# When to use abstract classes & interfaces:
# 1. When the parent class wants to transfer logic to the child
# 2. For new features you want to implement in the future
# 3. If the API wont be changing for awhile
# 4. for the blueprint of business components

import abc

class IWebElement(metaclass=abc.ABCMeta): # declaring an abstract class by setting metaclass

    @abc.abstractmethod    # notation
    def get_name(self):
        pass

    @abc.abstractmethod
    def set_style(self, style):
        pass

class DivElement(IWebElement):

    def get_name(self):
        return "div"

    @abc.abstractmethod
    def set_style(self, style):
        print("Div style:", style)

class SpanElement(IWebElement):

    def get_name(self):
        return "span"

    @abc.abstractmethod
    def set_style(self, style):
        print("Span style:", style)

class ButtonElement(IWebElement):

    def get_name(self):
        return "button"

    @abc.abstractmethod
    def set_style(self, style):
        print("Button style:", style)

div_element = DivElement()
print(div_element.get_name())
div_element.set_style("Width: 100px; height: 100px;")

span_element = SpanElement()
print(span_element.get_name())
# div_element.set_style("Width: 100px; height: 100px;")

button_element = ButtonElement()
print(button_element.get_name())
# div_element.set_style("Width: 100px; height: 100px;")
