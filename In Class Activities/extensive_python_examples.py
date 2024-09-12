
import math
import re
import requests
import pandas as pd
from multiprocessing import Process

# Function to demonstrate variables and data types
def variables_and_data_types():
    ''' Demonstrates basic variable assignment and types in Python. '''
    x = 5  # Integer
    y = 3.14  # Float
    name = "John"  # String
    numbers = [1, 2, 3]  # List

    print(f"Name: {name}, Numbers: {numbers}")

# Function to demonstrate control structures
def control_structures():
    ''' Demonstrates if-else statements and looping in Python. '''
    age = 18
    if age >= 18:
        print("Adult")
    else:
        print("Minor")

    fruits = ['apple', 'banana', 'cherry']
    for fruit in fruits:
        print(fruit)

# Function to demonstrate basic functions
def functions_demo():
    ''' Demonstrates defining and using functions in Python. '''
    def greet(name):
        return f"Hello, {name}!"

    print(greet("Alice"))

# Function to demonstrate OOP
def oop_demo():
    ''' Demonstrates Object-Oriented Programming concepts in Python. '''
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

# Function to demonstrate modules
def modules_demo():
    ''' Demonstrates usage of external modules in Python. '''
    print(math.sqrt(16))  # Output: 4.0

# Function to demonstrate File I/O
def file_io_demo():
    ''' Demonstrates reading from and writing to a text file in Python. '''
    with open('example.txt', 'w') as file:
        file.write("Hello, World!")

    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)

# Function to demonstrate List Comprehensions
def list_comprehension_demo():
    ''' Demonstrates list comprehensions in Python. '''
    squares = [x**2 for x in range(10)]
    print(squares)

# Function to demonstrate error handling
def error_handling_demo():
    ''' Demonstrates error handling in Python using try-except. '''
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    finally:
        print("This will always run.")

# Function to demonstrate decorators
def decorators_demo():
    ''' Demonstrates usage of decorators in Python. '''
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

# Function to demonstrate generators
def generators_demo():
    ''' Demonstrates generators and iterators in Python. '''
    def my_generator():
        yield 1
        yield 2
        yield 3

    for value in my_generator():
        print(value)

# Function to demonstrate lambda functions
def lambda_demo():
    ''' Demonstrates lambda (anonymous) functions in Python. '''
    add = lambda x, y: x + y
    print(add(2, 3))  # Output: 5

# Function to demonstrate regular expressions
def regex_demo():
    ''' Demonstrates usage of regular expressions in Python. '''
    pattern = r"hello"
    text = "hello world"
    match = re.search(pattern, text)
    if match:
        print("Pattern found!")

# Function to demonstrate working with APIs
def api_demo():
    ''' Demonstrates how to make a GET request to an API using the requests module. '''
    response = requests.get('https://api.github.com')
    if response.status_code == 200:
        print(response.json())

# Function to demonstrate working with CSV files
def csv_demo():
    ''' Demonstrates reading from and writing to CSV files using pandas. '''
    data = {'Name': ['John', 'Anna'], 'Age': [28, 24]}
    
    # Writing CSV
    df = pd.DataFrame(data)
    df.to_csv('example.csv', index=False)
    print("CSV written successfully.")

    # Reading CSV
    df_read = pd.read_csv('example.csv')
    print("CSV content:")
    print(df_read)

# Function to demonstrate multiprocessing
def multiprocessing_demo():
    ''' Demonstrates basic multiprocessing in Python. '''
    def worker():
        print("Worker")

    p = Process(target=worker)
    p.start()
    p.join()

# Main function to call all the demos
def main():
    print("Running Variables and Data Types Demo:")
    variables_and_data_types()
    
    print("\nRunning Control Structures Demo:")
    control_structures()
    
    print("\nRunning Functions Demo:")
    functions_demo()
    
    print("\nRunning OOP Demo:")
    oop_demo()
    
    print("\nRunning Modules Demo:")
    modules_demo()
    
    print("\nRunning File I/O Demo:")
    file_io_demo()
    
    print("\nRunning List Comprehensions Demo:")
    list_comprehension_demo()
    
    print("\nRunning Error Handling Demo:")
    error_handling_demo()
    
    print("\nRunning Decorators Demo:")
    decorators_demo()
    
    print("\nRunning Generators Demo:")
    generators_demo()
    
    print("\nRunning Lambda Demo:")
    lambda_demo()
    
    print("\nRunning Regular Expressions Demo:")
    regex_demo()
    
    print("\nRunning API Demo:")
    api_demo()
    
    print("\nRunning CSV Demo:")
    csv_demo()
    
    print("\nRunning Multiprocessing Demo:")
    multiprocessing_demo()

# Call the main function
if __name__ == "__main__":
    main()
