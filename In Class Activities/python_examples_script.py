
# Variables and Data Types
# In Python, we can use several built-in data types like integers, floats, strings, lists, etc.

x = 5  # Integer
y = 3.14  # Float
name = "John"  # String
numbers = [1, 2, 3]  # List

print(f"Name: {name}, Numbers: {numbers}")

# Control Structures
# If-else statements and loops (for, while) are used to control the flow of execution.

age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Functions
# Functions allow us to create reusable blocks of code.

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Object-Oriented Programming (OOP)
# OOP in Python allows us to create objects and classes.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

dog = Dog("Buddy")
dog.speak()

# Modules and Packages
# Python provides built-in modules and external packages for code reuse.

import math
print(math.sqrt(16))  # Output: 4.0

# File I/O
# Python can handle file reading and writing.

with open('example.txt', 'w') as file:
    file.write("Hello, World!")

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# List Comprehensions
# List comprehensions provide a concise way to create lists.

squares = [x**2 for x in range(10)]
print(squares)

# Error and Exception Handling
# Exception handling is used to manage runtime errors.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always run.")

# Decorators
# Decorators allow us to modify the behavior of functions.

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Generators and Iterators
# Generators allow for memory-efficient looping over large data sets.

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

# Lambda Functions
# Lambda functions are anonymous functions used for short tasks.

add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# Regular Expressions
# Python provides the 're' module for regular expression operations.

import re
pattern = r"hello"
text = "hello world"
match = re.search(pattern, text)
if match:
    print("Pattern found!")

# Working with APIs
# We can use the requests module to interact with web APIs.

import requests
response = requests.get('https://api.github.com')
if response.status_code == 200:
    print(response.json())

# Data Science Libraries
# Libraries like Pandas are used for data analysis in Python.

import pandas as pd
data = {'Name': ['John', 'Anna'], 'Age': [28, 24]}
df = pd.DataFrame(data)
print(df)

# Multithreading and Multiprocessing
# Python provides the multiprocessing module for parallel execution of tasks.

from multiprocessing import Process

def worker():
    print("Worker")

p = Process(target=worker)
p.start()
p.join()

