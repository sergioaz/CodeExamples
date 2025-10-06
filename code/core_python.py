#!/usr/bin/env python3
"""
Core Python Concepts - 27 Examples Across 9 Topics

This script demonstrates essential Python 3 programming concepts through practical examples.
Each section contains 3 examples that build upon each other, showcasing different aspects
of the topic.

Topics covered:
1. Python Dictionaries (3 examples)
2. Python File I/O (3 examples) 
3. Python Functions (3 examples)
4. Python Lists and Tuples (3 examples)
5. Python Classes (3 examples)
6. Python Control Flow (3 examples)
7. Python Exception Handling (3 examples)
8. Python Comprehensions (3 examples)
9. Python Strings (3 examples)

Usage:
    python core_python.py          # Run all examples
    python core_python.py --demo N # Run specific topic (1-9)

Author: Generated for Python learning
"""

import os
import socket
import json
import tempfile
import time
from collections import defaultdict, Counter
from functools import reduce
from typing import Dict, List, Any, Optional, Union


# ============================================================================
# 1. PYTHON DICTIONARIES - 3 Examples
# ============================================================================

def demo_dict_basics():
    """Example 1: Dictionary definition, value setting, and basic operations"""
    print("=== Dictionary Basics ===")
    
    # Creating and populating dictionaries
    student = {}  # Empty dictionary
    student['name'] = 'Alice'
    student['age'] = 20
    student['grades'] = [85, 92, 78]
    
    # Alternative creation methods
    student2 = dict(name='Bob', age=21, grades=[90, 88, 95])
    student3 = {'name': 'Charlie', 'age': 19, 'grades': [82, 87, 91]}
    
    print(f"Student 1: {student}")
    print(f"Student 2: {student2}")
    print(f"Student 3: {student3}")
    
    # Key operations
    print(f"Keys: {list(student.keys())}")
    print(f"Values: {list(student.values())}")
    print(f"Items: {list(student.items())}")


def demo_dict_default_values():
    """Example 2: Using default values and advanced dictionary methods"""
    print("=== Dictionary Default Values ===")
    
    # Using get() with defaults
    config = {'host': 'localhost', 'port': 8080}
    
    host = config.get('host', '127.0.0.1')
    port = config.get('port', 3000)
    timeout = config.get('timeout', 30)  # Default value used
    
    print(f"Host: {host}, Port: {port}, Timeout: {timeout}")
    
    # Using setdefault()
    config.setdefault('debug', True)
    config.setdefault('port', 9000)  # Won't change existing value
    
    print(f"Config after setdefault: {config}")
    
    # Using defaultdict for automatic default values
    word_count = defaultdict(int)
    text = "hello world hello python world"
    
    for word in text.split():
        word_count[word] += 1
    
    print(f"Word count: {dict(word_count)}")


def demo_dict_iterations():
    """Example 3: Dictionary iteration patterns and advanced usage"""
    print("=== Dictionary Iterations ===")
    
    inventory = {
        'apples': {'price': 0.5, 'stock': 100},
        'bananas': {'price': 0.3, 'stock': 150},
        'oranges': {'price': 0.8, 'stock': 75}
    }
    
    # Different iteration approaches
    print("Inventory Report:")
    for item, details in inventory.items():
        price = details['price']
        stock = details['stock']
        total_value = price * stock
        print(f"  {item.capitalize()}: ${price:.2f} each, {stock} in stock, Total: ${total_value:.2f}")
    
    # Dictionary comprehension with filtering
    expensive_items = {k: v for k, v in inventory.items() if v['price'] > 0.4}
    print(f"\nExpensive items (>$0.40): {list(expensive_items.keys())}")
    
    # Merging dictionaries (Python 3.9+)
    new_items = {'grapes': {'price': 1.2, 'stock': 50}}
    updated_inventory = inventory | new_items
    print(f"Updated inventory has {len(updated_inventory)} items")


# ============================================================================
# 2. PYTHON FILE I/O - 3 Examples
# ============================================================================

def demo_basic_file_operations():
    """Example 1: Basic file reading and writing operations"""
    print("=== Basic File Operations ===")
    
    # Writing to a file
    filename = "sample_data.txt"
    data_to_write = ["Line 1: Hello World", "Line 2: Python File I/O", "Line 3: Example Data"]
    
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for line in data_to_write:
                file.write(line + '\n')
        print(f"Successfully wrote {len(data_to_write)} lines to {filename}")
        
        # Reading from the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"File content:\n{content}")
            
        # Reading line by line
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(f"Read {len(lines)} lines individually")
            
    except IOError as e:
        print(f"File operation failed: {e}")
    finally:
        # Cleanup
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Cleaned up {filename}")


def demo_json_file_handling():
    """Example 2: Working with JSON files and structured data"""
    print("=== JSON File Handling ===")
    
    # Sample data structure
    employees = {
        "company": "TechCorp",
        "employees": [
            {"id": 1, "name": "Alice Johnson", "position": "Developer", "salary": 75000},
            {"id": 2, "name": "Bob Smith", "position": "Designer", "salary": 65000},
            {"id": 3, "name": "Charlie Brown", "position": "Manager", "salary": 85000}
        ]
    }
    
    json_filename = "employees.json"
    
    try:
        # Writing JSON data
        with open(json_filename, 'w', encoding='utf-8') as file:
            json.dump(employees, file, indent=2, ensure_ascii=False)
        print(f"JSON data written to {json_filename}")
        
        # Reading JSON data
        with open(json_filename, 'r', encoding='utf-8') as file:
            loaded_data = json.load(file)
            
        print(f"Company: {loaded_data['company']}")
        print("Employee list:")
        for emp in loaded_data['employees']:
            print(f"  {emp['name']} - {emp['position']}: ${emp['salary']:,}")
            
        # Modifying and saving back
        loaded_data['employees'].append({
            "id": 4, "name": "Diana Prince", "position": "Analyst", "salary": 70000
        })
        
        with open(json_filename, 'w', encoding='utf-8') as file:
            json.dump(loaded_data, file, indent=2)
        print("Added new employee to JSON file")
        
    except (IOError, json.JSONDecodeError) as e:
        print(f"JSON operation failed: {e}")
    finally:
        if os.path.exists(json_filename):
            os.remove(json_filename)
            print(f"Cleaned up {json_filename}")


def demo_advanced_file_operations():
    """Example 3: Advanced file operations and temporary files"""
    print("=== Advanced File Operations ===")
    
    # Using temporary files
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.log', delete=False) as temp_file:
        temp_filename = temp_file.name
        
        # Write log entries
        log_entries = [
            "2024-01-01 10:00:00 INFO Application started",
            "2024-01-01 10:05:00 DEBUG User login attempt",
            "2024-01-01 10:05:01 INFO User authenticated successfully",
            "2024-01-01 10:10:00 ERROR Database connection timeout",
            "2024-01-01 10:10:30 INFO Database connection restored"
        ]
        
        for entry in log_entries:
            temp_file.write(entry + '\n')
        
    print(f"Created temporary log file: {temp_filename}")
    
    try:
        # Analyze the log file
        error_count = 0
        info_count = 0
        
        with open(temp_filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                if 'ERROR' in line:
                    error_count += 1
                    print(f"Line {line_num}: {line.strip()}")
                elif 'INFO' in line:
                    info_count += 1
        
        print(f"Log analysis: {info_count} INFO messages, {error_count} ERROR messages")
        
        # File statistics
        file_stats = os.stat(temp_filename)
        print(f"File size: {file_stats.st_size} bytes")
        print(f"Last modified: {time.ctime(file_stats.st_mtime)}")
        
    except IOError as e:
        print(f"Log analysis failed: {e}")
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
            print("Temporary file cleaned up")


# ============================================================================
# 3. PYTHON FUNCTIONS - 3 Examples  
# ============================================================================

def demo_function_basics():
    """Example 1: Function definition, parameters, and return values"""
    print("=== Function Basics ===")
    
    def greet(name, greeting="Hello"):
        """Simple function with default parameter"""
        return f"{greeting}, {name}!"
    
    def calculate_area(length, width):
        """Function returning a value"""
        return length * width
    
    def get_user_info(name, age, city="Unknown"):
        """Function with mixed parameters"""
        return {
            'name': name,
            'age': age,
            'city': city,
            'is_adult': age >= 18
        }
    
    # Function calls
    print(greet("Alice"))
    print(greet("Bob", "Hi there"))
    
    area = calculate_area(5, 3)
    print(f"Area of 5x3 rectangle: {area}")
    
    user1 = get_user_info("Charlie", 25)
    user2 = get_user_info("Diana", 17, "New York")
    print(f"User 1: {user1}")
    print(f"User 2: {user2}")


def demo_advanced_functions():
    """Example 2: Advanced function features - *args, **kwargs, nested functions"""
    print("=== Advanced Functions ===")
    
    def statistics(*numbers, operation="mean"):
        """Function accepting variable number of arguments"""
        if not numbers:
            return None
        
        if operation == "mean":
            return sum(numbers) / len(numbers)
        elif operation == "sum":
            return sum(numbers)
        elif operation == "max":
            return max(numbers)
        elif operation == "min":
            return min(numbers)
        else:
            return None
    
    def create_profile(**kwargs):
        """Function accepting arbitrary keyword arguments"""
        profile = {
            'name': kwargs.get('name', 'Anonymous'),
            'age': kwargs.get('age', 0),
            'city': kwargs.get('city', 'Unknown')
        }
        
        # Add any additional fields
        for key, value in kwargs.items():
            if key not in profile:
                profile[key] = value
                
        return profile
    
    def make_multiplier(factor):
        """Nested function (closure) example"""
        def multiply(number):
            return number * factor
        return multiply
    
    # Testing variable arguments
    print(f"Mean of 1,2,3,4,5: {statistics(1, 2, 3, 4, 5)}")
    print(f"Sum of 10,20,30: {statistics(10, 20, 30, operation='sum')}")
    print(f"Max of 7,3,9,1: {statistics(7, 3, 9, 1, operation='max')}")
    
    # Testing keyword arguments
    profile1 = create_profile(name="Alice", age=25, city="Boston")
    profile2 = create_profile(name="Bob", occupation="Engineer", hobby="Reading")
    print(f"Profile 1: {profile1}")
    print(f"Profile 2: {profile2}")
    
    # Testing closures
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(f"Double 7: {double(7)}")
    print(f"Triple 7: {triple(7)}")


def demo_lambda_functions():
    """Example 3: Lambda expressions and functional programming"""
    print("=== Lambda Functions ===")
    
    # Basic lambda examples
    square = lambda x: x ** 2
    add = lambda a, b: a + b
    is_even = lambda n: n % 2 == 0
    
    print(f"Square of 6: {square(6)}")
    print(f"Add 3 + 7: {add(3, 7)}")
    print(f"Is 8 even? {is_even(8)}")
    print(f"Is 7 even? {is_even(7)}")
    
    # Lambda with built-in functions
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Using map()
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print(f"Squared numbers: {squared_numbers}")
    
    # Using filter()
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {even_numbers}")
    
    # Using reduce()
    product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
    print(f"Product of 1-5: {product}")
    
    # Lambda for sorting
    students = [
        {'name': 'Alice', 'grade': 85},
        {'name': 'Bob', 'grade': 92},
        {'name': 'Charlie', 'grade': 78},
        {'name': 'Diana', 'grade': 96}
    ]
    
    # Sort by grade (descending)
    sorted_students = sorted(students, key=lambda student: student['grade'], reverse=True)
    print("Students sorted by grade:")
    for student in sorted_students:
        print(f"  {student['name']}: {student['grade']}")


# ============================================================================
# 4. PYTHON LISTS AND TUPLES - 3 Examples
# ============================================================================

def demo_list_tuple_basics():
    """Example 1: Basic list and tuple operations, indexing, slicing"""
    print("=== List and Tuple Basics ===")
    
    # Lists (mutable)
    fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']
    print(f"Original fruits: {fruits}")
    
    # Indexing and slicing
    print(f"First fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")
    print(f"First three fruits: {fruits[:3]}")
    print(f"Last two fruits: {fruits[-2:]}")
    print(f"Every other fruit: {fruits[::2]}")
    
    # Modifying lists
    fruits.append('mango')
    fruits.insert(1, 'pear')
    print(f"After additions: {fruits}")
    
    fruits.remove('banana')
    popped_fruit = fruits.pop()
    print(f"After removal and pop: {fruits}")
    print(f"Popped fruit: {popped_fruit}")
    
    # Tuples (immutable)
    coordinates = (10, 20)
    rgb_color = (255, 128, 0)
    person_info = ('Alice', 25, 'Engineer')
    
    print(f"Coordinates: {coordinates}")
    print(f"RGB Color: {rgb_color}")
    print(f"Person: {person_info}")
    
    # Tuple unpacking
    name, age, profession = person_info
    print(f"Unpacked: {name} is {age} years old and works as an {profession}")


def demo_list_functions():
    """Example 2: List methods and built-in functions"""
    print("=== List Functions and Methods ===")
    
    numbers = [45, 22, 88, 12, 67, 22, 90, 33]
    print(f"Original numbers: {numbers}")
    
    # List methods
    print(f"Length: {len(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Max: {max(numbers)}")
    print(f"Min: {min(numbers)}")
    print(f"Count of 22: {numbers.count(22)}")
    print(f"Index of 88: {numbers.index(88)}")
    
    # List operations
    numbers_copy = numbers.copy()
    numbers.sort()
    print(f"Sorted (ascending): {numbers}")
    
    numbers.sort(reverse=True)
    print(f"Sorted (descending): {numbers}")
    
    # List comprehension examples
    even_numbers = [n for n in numbers if n % 2 == 0]
    squared_numbers = [n ** 2 for n in numbers if n < 50]
    
    print(f"Even numbers: {even_numbers}")
    print(f"Squared numbers (< 50): {squared_numbers}")
    
    # Nested lists
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Matrix: {matrix}")
    print(f"Matrix[1][2]: {matrix[1][2]}")
    
    # Flatten matrix
    flattened = [item for row in matrix for item in row]
    print(f"Flattened matrix: {flattened}")


def demo_sorting_searching():
    """Example 3: Advanced sorting and searching techniques"""
    print("=== Sorting and Searching ===")
    
    # Sample data for sorting
    books = [
        {'title': 'Python Programming', 'author': 'Smith', 'year': 2020, 'pages': 450},
        {'title': 'Web Development', 'author': 'Johnson', 'year': 2019, 'pages': 320},
        {'title': 'Data Science', 'author': 'Brown', 'year': 2021, 'pages': 520},
        {'title': 'Machine Learning', 'author': 'Davis', 'year': 2022, 'pages': 380}
    ]
    
    print("Original books:")
    for book in books:
        print(f"  {book['title']} by {book['author']} ({book['year']})")
    
    # Sort by different criteria
    books_by_year = sorted(books, key=lambda x: x['year'])
    books_by_pages = sorted(books, key=lambda x: x['pages'], reverse=True)
    books_by_author = sorted(books, key=lambda x: x['author'])
    
    print("\nSorted by year:")
    for book in books_by_year:
        print(f"  {book['year']}: {book['title']}")
    
    print("\nSorted by pages (descending):")
    for book in books_by_pages:
        print(f"  {book['pages']} pages: {book['title']}")
    
    # Searching examples
    def find_book_by_title(books_list, title):
        """Linear search for book by title"""
        for book in books_list:
            if title.lower() in book['title'].lower():
                return book
        return None
    
    def find_books_by_year_range(books_list, start_year, end_year):
        """Find books within year range"""
        return [book for book in books_list 
                if start_year <= book['year'] <= end_year]
    
    # Search demonstrations
    found_book = find_book_by_title(books, "Python")
    if found_book:
        print(f"\nFound book: {found_book['title']}")
    
    recent_books = find_books_by_year_range(books, 2020, 2022)
    print(f"\nRecent books (2020-2022): {len(recent_books)} found")
    for book in recent_books:
        print(f"  {book['title']} ({book['year']})")


# ============================================================================
# 5. PYTHON CLASSES - 3 Examples
# ============================================================================

def demo_basic_classes():
    """Example 1: Basic class definition, methods, and attributes"""
    print("=== Basic Classes ===")
    
    class Student:
        """Basic Student class demonstrating OOP concepts"""
        
        # Class variable (shared by all instances)
        school_name = "Python Academy"
        
        def __init__(self, name, age, student_id):
            """Constructor method"""
            self.name = name
            self.age = age
            self.student_id = student_id
            self.grades = []
        
        def add_grade(self, subject, grade):
            """Add a grade for a subject"""
            self.grades.append({'subject': subject, 'grade': grade})
        
        def get_average_grade(self):
            """Calculate average grade"""
            if not self.grades:
                return 0.0
            total = sum(grade['grade'] for grade in self.grades)
            return total / len(self.grades)
        
        def get_info(self):
            """Return student information"""
            avg_grade = self.get_average_grade()
            return f"{self.name} (ID: {self.student_id}), Age: {self.age}, Average: {avg_grade:.2f}"
        
        def __str__(self):
            """String representation"""
            return f"Student({self.name}, {self.age})"
        
        def __repr__(self):
            """Developer-friendly representation"""
            return f"Student(name='{self.name}', age={self.age}, student_id='{self.student_id}')"
    
    # Create instances
    alice = Student("Alice Johnson", 20, "S001")
    bob = Student("Bob Smith", 19, "S002")
    
    # Add grades
    alice.add_grade("Math", 85)
    alice.add_grade("Science", 92)
    alice.add_grade("English", 88)
    
    bob.add_grade("Math", 78)
    bob.add_grade("Science", 85)
    bob.add_grade("English", 82)
    
    print(f"School: {Student.school_name}")
    print(alice.get_info())
    print(bob.get_info())
    print(f"Alice's grades: {alice.grades}")


def demo_inheritance_polymorphism():
    """Example 2: Inheritance and polymorphism"""
    print("=== Inheritance and Polymorphism ===")
    
    class Shape:
        """Base class for all shapes"""
        
        def __init__(self, name):
            self.name = name
        
        def area(self):
            """Abstract method - should be overridden"""
            raise NotImplementedError("Subclass must implement area()")
        
        def perimeter(self):
            """Abstract method - should be overridden"""
            raise NotImplementedError("Subclass must implement perimeter()")
        
        def describe(self):
            """Common method for all shapes"""
            return f"{self.name} - Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"
    
    class Rectangle(Shape):
        """Rectangle class inheriting from Shape"""
        
        def __init__(self, width, height):
            super().__init__("Rectangle")
            self.width = width
            self.height = height
        
        def area(self):
            return self.width * self.height
        
        def perimeter(self):
            return 2 * (self.width + self.height)
    
    class Circle(Shape):
        """Circle class inheriting from Shape"""
        
        def __init__(self, radius):
            super().__init__("Circle")
            self.radius = radius
        
        def area(self):
            return 3.14159 * self.radius ** 2
        
        def perimeter(self):
            return 2 * 3.14159 * self.radius
    
    class Triangle(Shape):
        """Triangle class inheriting from Shape"""
        
        def __init__(self, side1, side2, side3):
            super().__init__("Triangle")
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        
        def area(self):
            # Using Heron's formula
            s = self.perimeter() / 2
            return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        
        def perimeter(self):
            return self.side1 + self.side2 + self.side3
    
    # Create different shapes
    shapes = [
        Rectangle(5, 3),
        Circle(4),
        Triangle(3, 4, 5)
    ]
    
    # Polymorphism in action
    print("Shape descriptions:")
    for shape in shapes:
        print(f"  {shape.describe()}")
    
    # Calculate total area
    total_area = sum(shape.area() for shape in shapes)
    print(f"Total area of all shapes: {total_area:.2f}")


def demo_static_private_methods():
    """Example 3: Static methods and private attributes"""
    print("=== Static Methods and Private Attributes ===")
    
    class BankAccount:
        """Bank account class demonstrating static methods and private attributes"""
        
        # Class variables
        _interest_rate = 0.02  # Protected attribute (convention)
        _account_counter = 1000  # Private class attribute
        
        def __init__(self, owner_name, initial_balance=0):
            self.owner_name = owner_name
            self._balance = initial_balance  # Protected attribute
            self.__account_number = BankAccount._account_counter  # Private attribute
            BankAccount._account_counter += 1
            self.__transaction_history = []  # Private attribute
        
        def deposit(self, amount):
            """Deposit money into account"""
            if amount > 0:
                self._balance += amount
                self.__add_transaction("Deposit", amount)
                return True
            return False
        
        def withdraw(self, amount):
            """Withdraw money from account"""
            if 0 < amount <= self._balance:
                self._balance -= amount
                self.__add_transaction("Withdrawal", -amount)
                return True
            return False
        
        def get_balance(self):
            """Get current balance"""
            return self._balance
        
        def get_account_info(self):
            """Get account information"""
            return {
                'owner': self.owner_name,
                'account_number': self.__account_number,
                'balance': self._balance
            }
        
        def __add_transaction(self, transaction_type, amount):
            """Private method to add transaction to history"""
            self.__transaction_history.append({
                'type': transaction_type,
                'amount': amount,
                'balance_after': self._balance
            })
        
        def get_transaction_history(self):
            """Get transaction history (public access to private data)"""
            return self.__transaction_history.copy()
        
        @staticmethod
        def calculate_compound_interest(principal, rate, time):
            """Static method for calculating compound interest"""
            return principal * ((1 + rate) ** time)
        
        @classmethod
        def get_interest_rate(cls):
            """Class method to get interest rate"""
            return cls._interest_rate
        
        @classmethod
        def set_interest_rate(cls, new_rate):
            """Class method to set interest rate"""
            if 0 <= new_rate <= 1:
                cls._interest_rate = new_rate
                return True
            return False
    
    # Create accounts
    account1 = BankAccount("Alice Johnson", 1000)
    account2 = BankAccount("Bob Smith", 500)
    
    # Test operations
    account1.deposit(200)
    account1.withdraw(150)
    account2.deposit(300)
    
    print("Account Information:")
    print(f"  {account1.get_account_info()}")
    print(f"  {account2.get_account_info()}")
    
    # Test static method
    future_value = BankAccount.calculate_compound_interest(1000, 0.05, 3)
    print(f"$1000 at 5% for 3 years: ${future_value:.2f}")
    
    # Test class methods
    print(f"Current interest rate: {BankAccount.get_interest_rate():.2%}")
    BankAccount.set_interest_rate(0.025)
    print(f"New interest rate: {BankAccount.get_interest_rate():.2%}")
    
    print(f"Alice's transaction history: {len(account1.get_transaction_history())} transactions")


# ============================================================================
# 6. PYTHON CONTROL FLOW - 3 Examples
# ============================================================================

def demo_conditional_statements():
    """Example 1: if/elif/else statements and conditional expressions"""
    print("=== Conditional Statements ===")
    
    def classify_grade(score):
        """Classify a numeric grade"""
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    
    def check_eligibility(age, has_license, years_experience):
        """Check driving eligibility with multiple conditions"""
        if age < 16:
            return "Too young to drive"
        elif age >= 16 and not has_license:
            return "Needs license"
        elif has_license and years_experience < 1:
            return "Beginner driver"
        elif has_license and 1 <= years_experience < 5:
            return "Intermediate driver"
        else:
            return "Experienced driver"
    
    # Test grade classification
    test_scores = [95, 87, 73, 68, 45, 92]
    print("Grade Classification:")
    for score in test_scores:
        grade = classify_grade(score)
        print(f"  Score {score}: Grade {grade}")
    
    # Test driving eligibility
    drivers = [
        (15, False, 0),
        (17, False, 0),
        (18, True, 0.5),
        (25, True, 3),
        (35, True, 10)
    ]
    
    print("\nDriving Eligibility:")
    for age, has_license, experience in drivers:
        status = check_eligibility(age, has_license, experience)
        print(f"  Age {age}, License: {has_license}, Experience: {experience} years → {status}")
    
    # Conditional expressions (ternary operator)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_odd = [("even" if n % 2 == 0 else "odd") for n in numbers]
    print(f"\nEven/Odd classification: {even_odd}")


def demo_loops_basic():
    """Example 2: for and while loops with break, continue, and range"""
    print("=== Basic Loops ===")
    
    # For loop with range
    print("Counting with range:")
    for i in range(1, 6):
        print(f"  Count: {i}")
    
    print("\nCounting by 2s:")
    for i in range(0, 11, 2):
        print(f"  Even number: {i}")
    
    # For loop with lists
    fruits = ["apple", "banana", "orange", "grape"]
    print("\nFruits with index:")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")
    
    # While loop example
    print("\nCountdown:")
    countdown = 5
    while countdown > 0:
        print(f"  {countdown}...")
        countdown -= 1
    print("  Blast off!")
    
    # Break and continue examples
    print("\nNumbers 1-10, skip multiples of 3:")
    for num in range(1, 11):
        if num % 3 == 0:
            continue  # Skip multiples of 3
        print(f"  {num}")
    
    print("\nFind first number divisible by 7:")
    for num in range(20, 100):
        if num % 7 == 0:
            print(f"  Found: {num}")
            break
    
    # Nested loops
    print("\nMultiplication table (3x3):")
    for i in range(1, 4):
        for j in range(1, 4):
            product = i * j
            print(f"  {i} × {j} = {product}")


def demo_advanced_control_flow():
    """Example 3: Advanced control flow with pass, else clauses, and complex logic"""
    print("=== Advanced Control Flow ===")
    
    def find_prime_numbers(limit):
        """Find prime numbers up to limit using control flow"""
        primes = []
        
        for num in range(2, limit + 1):
            is_prime = True
            
            # Check if num is divisible by any number from 2 to sqrt(num)
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break  # Not prime, no need to check further
            else:
                # This else belongs to the for loop, executed if loop wasn't broken
                pass  # Could add logic here if needed
            
            if is_prime:
                primes.append(num)
        
        return primes
    
    def process_user_input():
        """Simulate processing user input with control flow"""
        commands = ["start", "invalid_command", "stop", "pause", "resume", "quit"]
        
        for command in commands:
            print(f"Processing command: '{command}'")
            
            if command == "start":
                print("  → System started")
            elif command == "stop":
                print("  → System stopped")
            elif command == "pause":
                print("  → System paused")
            elif command == "resume":
                print("  → System resumed")
            elif command == "quit":
                print("  → Quitting...")
                break
            else:
                print("  → Unknown command, ignoring")
                continue
            
            # This would be executed for valid commands (not skipped by continue)
            print("  → Command processed successfully")
    
    def search_with_while():
        """Demonstrate while-else and complex conditions"""
        data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        target = 11
        index = 0
        
        while index < len(data):
            if data[index] == target:
                print(f"  Found {target} at index {index}")
                break
            index += 1
        else:
            # while-else: executed if loop completed without break
            print(f"  {target} not found in data")
    
    # Test prime number finder
    primes = find_prime_numbers(20)
    print(f"Prime numbers up to 20: {primes}")
    
    # Test command processor
    print("\nCommand Processing:")
    process_user_input()
    
    # Test while-else
    print("\nSearch demonstration:")
    search_with_while()
    
    # Complex conditional with multiple operators
    def evaluate_student(name, attendance, assignments_completed, exam_score):
        """Complex conditional logic"""
        print(f"\nEvaluating {name}:")
        
        if attendance >= 0.8 and assignments_completed >= 8 and exam_score >= 70:
            result = "Pass with distinction"
        elif attendance >= 0.7 and assignments_completed >= 6 and exam_score >= 60:
            result = "Pass"
        elif attendance >= 0.6 or assignments_completed >= 5 or exam_score >= 50:
            result = "Conditional pass - needs improvement"
        else:
            result = "Fail - must retake course"
        
        print(f"  Attendance: {attendance:.1%}, Assignments: {assignments_completed}/10, Exam: {exam_score}")
        print(f"  Result: {result}")
    
    # Test complex evaluation
    students = [
        ("Alice", 0.95, 9, 85),
        ("Bob", 0.75, 7, 72),
        ("Charlie", 0.65, 5, 58),
        ("Diana", 0.50, 3, 45)
    ]
    
    for name, attendance, assignments, exam in students:
        evaluate_student(name, attendance, assignments, exam)


# ============================================================================
# 7. PYTHON EXCEPTION HANDLING - 3 Examples
# ============================================================================

def demo_basic_exception_handling():
    """Example 1: Basic try/except/finally blocks"""
    print("=== Basic Exception Handling ===")
    
    def safe_divide(a, b):
        """Safely divide two numbers with exception handling"""
        try:
            result = a / b
            print(f"  {a} ÷ {b} = {result}")
            return result
        except ZeroDivisionError:
            print(f"  Error: Cannot divide {a} by zero!")
            return None
        except TypeError:
            print(f"  Error: Invalid types for division: {type(a)}, {type(b)}")
            return None
        finally:
            print(f"  Division operation attempted with {a} and {b}")
    
    def safe_list_access(lst, index):
        """Safely access list elements"""
        try:
            value = lst[index]
            print(f"  Value at index {index}: {value}")
            return value
        except IndexError:
            print(f"  Error: Index {index} is out of range for list of length {len(lst)}")
            return None
        except TypeError:
            print(f"  Error: Invalid index type: {type(index)}")
            return None
    
    def safe_file_read(filename):
        """Safely read file contents"""
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print(f"  Successfully read {len(content)} characters from {filename}")
                return content
        except FileNotFoundError:
            print(f"  Error: File '{filename}' not found")
            return None
        except PermissionError:
            print(f"  Error: Permission denied to read '{filename}'")
            return None
        except IOError as e:
            print(f"  Error reading file: {e}")
            return None
    
    # Test safe division
    print("Safe Division Tests:")
    safe_divide(10, 2)
    safe_divide(10, 0)
    safe_divide(10, "2")
    
    # Test safe list access
    print("\nSafe List Access Tests:")
    test_list = [1, 2, 3, 4, 5]
    safe_list_access(test_list, 2)
    safe_list_access(test_list, 10)
    safe_list_access(test_list, "invalid")
    
    # Test safe file reading
    print("\nSafe File Reading Tests:")
    safe_file_read("nonexistent_file.txt")


def demo_custom_exceptions():
    """Example 2: Custom exceptions and advanced error handling"""
    print("=== Custom Exceptions ===")
    
    # Define custom exception classes
    class ValidationError(Exception):
        """Custom exception for validation errors"""
        def __init__(self, message, field_name=None):
            super().__init__(message)
            self.field_name = field_name
    
    class InsufficientFundsError(Exception):
        """Custom exception for insufficient funds"""
        def __init__(self, requested_amount, available_amount):
            self.requested_amount = requested_amount
            self.available_amount = available_amount
            message = f"Insufficient funds: requested ${requested_amount}, available ${available_amount}"
            super().__init__(message)
    
    class BankAccountProcessor:
        """Class demonstrating custom exception handling"""
        
        def __init__(self):
            self.accounts = {}
        
        def create_account(self, account_id, initial_balance, owner_name):
            """Create a new account with validation"""
            try:
                # Validation
                if not account_id or not isinstance(account_id, str):
                    raise ValidationError("Account ID must be a non-empty string", "account_id")
                
                if account_id in self.accounts:
                    raise ValidationError(f"Account {account_id} already exists", "account_id")
                
                if initial_balance < 0:
                    raise ValidationError("Initial balance cannot be negative", "initial_balance")
                
                if not owner_name or not isinstance(owner_name, str):
                    raise ValidationError("Owner name must be a non-empty string", "owner_name")
                
                # Create account
                self.accounts[account_id] = {
                    'balance': initial_balance,
                    'owner': owner_name
                }
                
                print(f"  Account {account_id} created successfully for {owner_name}")
                return True
                
            except ValidationError as e:
                print(f"  Validation Error: {e}")
                if e.field_name:
                    print(f"  Field: {e.field_name}")
                return False
        
        def withdraw(self, account_id, amount):
            """Withdraw money with custom exception handling"""
            try:
                if account_id not in self.accounts:
                    raise ValidationError(f"Account {account_id} not found", "account_id")
                
                if amount <= 0:
                    raise ValidationError("Withdrawal amount must be positive", "amount")
                
                account = self.accounts[account_id]
                if amount > account['balance']:
                    raise InsufficientFundsError(amount, account['balance'])
                
                account['balance'] -= amount
                print(f"  Withdrew ${amount} from {account_id}. New balance: ${account['balance']}")
                return True
                
            except ValidationError as e:
                print(f"  Validation Error: {e}")
                return False
            except InsufficientFundsError as e:
                print(f"  Transaction Failed: {e}")
                print(f"  Shortfall: ${e.requested_amount - e.available_amount}")
                return False
    
    # Test custom exceptions
    processor = BankAccountProcessor()
    
    print("Account Creation Tests:")
    processor.create_account("ACC001", 1000, "Alice Johnson")
    processor.create_account("", 500, "Bob Smith")  # Invalid account ID
    processor.create_account("ACC002", -100, "Charlie Brown")  # Invalid balance
    
    print("\nWithdrawal Tests:")
    processor.withdraw("ACC001", 200)  # Valid
    processor.withdraw("ACC001", 2000)  # Insufficient funds
    processor.withdraw("ACC999", 100)  # Account not found


def demo_exception_propagation():
    """Example 3: Exception propagation and cleanup with context managers"""
    print("=== Exception Propagation and Cleanup ===")
    
    class ResourceManager:
        """Context manager for resource cleanup demonstration"""
        
        def __init__(self, resource_name):
            self.resource_name = resource_name
            self.is_acquired = False
        
        def __enter__(self):
            print(f"    Acquiring resource: {self.resource_name}")
            self.is_acquired = True
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type:
                print(f"    Exception occurred: {exc_type.__name__}: {exc_val}")
            
            if self.is_acquired:
                print(f"    Releasing resource: {self.resource_name}")
                self.is_acquired = False
            
            # Return False to propagate exception, True to suppress it
            return False
    
    def risky_operation_level_3():
        """Deepest level function that might raise exceptions"""
        import random
        
        operations = [
            lambda: 10 / 0,  # ZeroDivisionError
            lambda: int("not_a_number"),  # ValueError
            lambda: [1, 2, 3][10],  # IndexError
            lambda: "success"  # Success case
        ]
        
        # Randomly pick an operation
        operation = random.choice(operations)
        return operation()
    
    def risky_operation_level_2():
        """Middle level function"""
        try:
            result = risky_operation_level_3()
            print(f"    Level 2: Operation succeeded with result: {result}")
            return result
        except ValueError as e:
            print(f"    Level 2: Caught and handling ValueError: {e}")
            return "handled_value_error"
        # Let other exceptions propagate up
    
    def risky_operation_level_1():
        """Top level function with comprehensive error handling"""
        with ResourceManager("Database Connection"):
            with ResourceManager("File Handle"):
                try:
                    result = risky_operation_level_2()
                    print(f"    Level 1: Final result: {result}")
                    return result
                except ZeroDivisionError as e:
                    print(f"    Level 1: Caught ZeroDivisionError: {e}")
                    return "handled_zero_division"
                except Exception as e:
                    print(f"    Level 1: Caught unexpected exception: {type(e).__name__}: {e}")
                    return "handled_unexpected_error"
    
    # Multiple-level exception handling demonstration
    print("Exception Propagation Test (run multiple times to see different outcomes):")
    
    for attempt in range(3):
        print(f"\n  Attempt {attempt + 1}:")
        try:
            result = risky_operation_level_1()
            print(f"  Final outcome: {result}")
        except Exception as e:
            print(f"  Unhandled exception reached top level: {type(e).__name__}: {e}")
    
    # Demonstrate proper cleanup with nested context managers
    print("\nNested Context Managers Test:")
    try:
        with ResourceManager("Primary Resource"):
            with ResourceManager("Secondary Resource"):
                # Simulate an error
                raise RuntimeError("Simulated error for cleanup demonstration")
    except RuntimeError as e:
        print(f"  Caught and handled: {e}")


# ============================================================================
# 8. PYTHON COMPREHENSIONS - 3 Examples
# ============================================================================

def demo_list_comprehensions():
    """Example 1: List comprehensions with filtering and transformations"""
    print("=== List Comprehensions ===")
    
    # Basic list comprehensions
    numbers = range(1, 11)
    
    # Simple transformation
    squares = [x ** 2 for x in numbers]
    print(f"Squares: {squares}")
    
    # With filtering
    even_squares = [x ** 2 for x in numbers if x % 2 == 0]
    print(f"Even squares: {even_squares}")
    
    # More complex filtering and transformation
    words = ["hello", "world", "python", "programming", "code", "data"]
    long_words_upper = [word.upper() for word in words if len(word) > 4]
    print(f"Long words (uppercase): {long_words_upper}")
    
    # Nested loops in comprehensions
    colors = ["red", "green", "blue"]
    sizes = ["small", "medium", "large"]
    products = [f"{size} {color} shirt" for color in colors for size in sizes]
    print(f"Product combinations: {products[:6]}...")  # Show first 6
    
    # Conditional expressions in comprehensions
    temperatures_celsius = [0, 10, 20, 30, 40, 100]
    temperature_descriptions = [
        f"{temp}°C is {'freezing' if temp <= 0 else 'cold' if temp < 10 else 'warm' if temp < 30 else 'hot'}"
        for temp in temperatures_celsius
    ]
    
    print("Temperature descriptions:")
    for desc in temperature_descriptions:
        print(f"  {desc}")
    
    # Working with nested data
    students_grades = [
        {"name": "Alice", "grades": [85, 92, 78, 88]},
        {"name": "Bob", "grades": [90, 87, 85, 92]},
        {"name": "Charlie", "grades": [78, 82, 85, 79]}
    ]
    
    # Calculate averages using comprehension
    averages = [
        {"name": student["name"], "average": sum(student["grades"]) / len(student["grades"])}
        for student in students_grades
    ]
    
    print("\nStudent averages:")
    for avg in averages:
        print(f"  {avg['name']}: {avg['average']:.2f}")


def demo_dict_set_comprehensions():
    """Example 2: Dictionary and set comprehensions"""
    print("=== Dictionary and Set Comprehensions ===")
    
    # Dictionary comprehensions
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    
    # Create word length dictionary
    word_lengths = {word: len(word) for word in words}
    print(f"Word lengths: {word_lengths}")
    
    # Filter and transform keys and values
    long_words = {word.upper(): len(word) for word in words if len(word) > 5}
    print(f"Long words (uppercase): {long_words}")
    
    # Dictionary from two lists
    countries = ["USA", "Canada", "Mexico", "Brazil", "Argentina"]
    populations = [331, 38, 128, 213, 45]  # millions
    country_population = {country: pop for country, pop in zip(countries, populations)}
    print(f"Country populations: {country_population}")
    
    # Invert dictionary
    population_country = {pop: country for country, pop in country_population.items()}
    print(f"Population to country: {population_country}")
    
    # Set comprehensions
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
    
    # Square unique numbers
    unique_squares = {x ** 2 for x in numbers}
    print(f"Unique squares: {sorted(unique_squares)}")
    
    # Set of vowels in words
    text = "the quick brown fox jumps over the lazy dog"
    vowels_in_text = {char.lower() for char in text if char.lower() in 'aeiou'}
    print(f"Vowels in text: {sorted(vowels_in_text)}")
    
    # Complex set operations
    even_squares = {x ** 2 for x in range(1, 11) if x % 2 == 0}
    odd_cubes = {x ** 3 for x in range(1, 11) if x % 2 == 1}
    
    print(f"Even squares: {sorted(even_squares)}")
    print(f"Odd cubes: {sorted(odd_cubes)}")
    print(f"Intersection: {sorted(even_squares & odd_cubes)}")
    print(f"Union: {sorted(even_squares | odd_cubes)}")
    
    # Nested dictionary comprehension
    multiplication_table = {
        i: {j: i * j for j in range(1, 6)} 
        for i in range(1, 6)
    }
    
    print("\nMultiplication table:")
    for i, row in multiplication_table.items():
        print(f"  {i}: {row}")


def demo_functional_tools():
    """Example 3: map, filter, reduce and advanced comprehensions"""
    print("=== Functional Tools with Comprehensions ===")
    
    # Sample data
    employees = [
        {"name": "Alice", "department": "Engineering", "salary": 75000, "years": 3},
        {"name": "Bob", "department": "Marketing", "salary": 65000, "years": 2},
        {"name": "Charlie", "department": "Engineering", "salary": 85000, "years": 5},
        {"name": "Diana", "department": "Sales", "salary": 70000, "years": 4},
        {"name": "Eve", "department": "Engineering", "salary": 95000, "years": 7}
    ]
    
    # Using map() - transform all elements
    names = list(map(lambda emp: emp["name"], employees))
    print(f"Employee names: {names}")
    
    # Comprehension equivalent
    names_comp = [emp["name"] for emp in employees]
    print(f"Names (comprehension): {names_comp}")
    
    # Using filter() - select elements based on condition
    senior_employees = list(filter(lambda emp: emp["years"] >= 5, employees))
    print(f"\nSenior employees (≥5 years):")
    for emp in senior_employees:
        print(f"  {emp['name']}: {emp['years']} years")
    
    # Comprehension equivalent
    senior_employees_comp = [emp for emp in employees if emp["years"] >= 5]
    print(f"Senior employees (comprehension): {[emp['name'] for emp in senior_employees_comp]}")
    
    # Using reduce() - combine elements
    from functools import reduce
    
    total_salary = reduce(lambda acc, emp: acc + emp["salary"], employees, 0)
    print(f"\nTotal salary (reduce): ${total_salary:,}")
    
    # Comprehension equivalent
    total_salary_comp = sum(emp["salary"] for emp in employees)
    print(f"Total salary (comprehension): ${total_salary_comp:,}")
    
    # Complex transformations combining techniques
    # Get department salary statistics
    from collections import defaultdict
    
    # Using traditional approach with comprehensions
    dept_stats = defaultdict(list)
    for emp in employees:
        dept_stats[emp["department"]].append(emp["salary"])
    
    dept_summary = {
        dept: {
            "count": len(salaries),
            "total": sum(salaries),
            "average": sum(salaries) / len(salaries),
            "max": max(salaries),
            "min": min(salaries)
        }
        for dept, salaries in dept_stats.items()
    }
    
    print("\nDepartment salary statistics:")
    for dept, stats in dept_summary.items():
        print(f"  {dept}:")
        print(f"    Employees: {stats['count']}")
        print(f"    Total: ${stats['total']:,}")
        print(f"    Average: ${stats['average']:,.0f}")
        print(f"    Range: ${stats['min']:,} - ${stats['max']:,}")
    
    # Generator expressions for memory efficiency
    print("\nGenerator expressions:")
    
    # Large dataset simulation
    large_numbers = range(1, 1000001)  # 1 million numbers
    
    # Generator expression - memory efficient
    even_squares_gen = (x ** 2 for x in large_numbers if x % 2 == 0)
    
    # Take first 10 values
    first_10_even_squares = [next(even_squares_gen) for _ in range(10)]
    print(f"First 10 even squares: {first_10_even_squares}")
    
    # Nested comprehensions for complex data structures
    # Create a grade book
    subjects = ["Math", "Science", "English"]
    students = ["Alice", "Bob", "Charlie"]
    
    # Generate random-like grades
    import hashlib
    
    gradebook = {
        student: {
            subject: (hash(f"{student}-{subject}") % 40) + 60  # Grades 60-99
            for subject in subjects
        }
        for student in students
    }
    
    print("\nGradebook:")
    for student, grades in gradebook.items():
        avg = sum(grades.values()) / len(grades)
        print(f"  {student}: {grades}, Average: {avg:.1f}")
    
    # Find top performer in each subject
    top_performers = {
        subject: max(students, key=lambda s: gradebook[s][subject])
        for subject in subjects
    }
    
    print(f"\nTop performers: {top_performers}")


# ============================================================================
# 9. PYTHON STRINGS - 3 Examples
# ============================================================================

def demo_string_basics():
    """Example 1: String slicing, operations, and basic manipulation"""
    print("=== String Basics ===")
    
    # String creation and basic operations
    text = "Python Programming Language"
    print(f"Original text: '{text}'")
    print(f"Length: {len(text)}")
    print(f"Uppercase: '{text.upper()}'")
    print(f"Lowercase: '{text.lower()}'")
    print(f"Title case: '{text.title()}'")
    
    # String slicing
    print(f"\nSlicing examples:")
    print(f"First 6 characters: '{text[:6]}'")
    print(f"Last 8 characters: '{text[-8:]}'")
    print(f"Characters 7-18: '{text[7:18]}'")
    print(f"Every 2nd character: '{text[::2]}'")
    print(f"Reversed: '{text[::-1]}'")
    
    # String methods
    print(f"\nString analysis:")
    print(f"Starts with 'Python': {text.startswith('Python')}")
    print(f"Ends with 'Language': {text.endswith('Language')}")
    print(f"Contains 'gram': {'gram' in text}")
    print(f"Position of 'Program': {text.find('Program')}")
    print(f"Count of 'a': {text.count('a')}")
    
    # String splitting and joining
    words = text.split()
    print(f"Words: {words}")
    print(f"Joined with '-': '{'-'.join(words)}'")
    
    # String replacement
    replaced = text.replace("Programming", "Scripting")
    print(f"Replaced text: '{replaced}'")
    
    # String validation methods
    test_strings = ["123", "abc", "123abc", "Hello World", "python_var", ""]
    print(f"\nString validation:")
    for s in test_strings:
        checks = []
        if s.isdigit():
            checks.append("digits")
        if s.isalpha():
            checks.append("letters")
        if s.isalnum():
            checks.append("alphanumeric")
        if s.islower():
            checks.append("lowercase")
        if s.isupper():
            checks.append("uppercase")
        if s.isspace():
            checks.append("whitespace")
        
        check_str = ", ".join(checks) if checks else "none"
        print(f"  '{s}': {check_str}")


def demo_string_formatting():
    """Example 2: String formatting techniques"""
    print("=== String Formatting ===")
    
    # Sample data
    name = "Alice"
    age = 25
    salary = 75000.50
    pi = 3.14159265359
    
    # Old-style % formatting
    old_format = "Name: %s, Age: %d, Salary: $%.2f" % (name, age, salary)
    print(f"Old-style formatting: {old_format}")
    
    # .format() method
    format_method = "Name: {}, Age: {}, Salary: ${:.2f}".format(name, age, salary)
    print(f"Format method: {format_method}")
    
    # .format() with positional and named arguments
    format_named = "Name: {name}, Age: {age}, Salary: ${salary:.2f}".format(
        name=name, age=age, salary=salary
    )
    print(f"Named format: {format_named}")
    
    # f-strings (Python 3.6+)
    f_string = f"Name: {name}, Age: {age}, Salary: ${salary:.2f}"
    print(f"F-string: {f_string}")
    
    # Advanced f-string formatting
    print(f"\nAdvanced formatting:")
    print(f"Pi to 2 decimal places: {pi:.2f}")
    print(f"Pi to 4 decimal places: {pi:.4f}")
    print(f"Salary with thousands separator: ${salary:,.2f}")
    print(f"Age padded to 5 characters: '{age:>5}'")
    print(f"Name left-aligned in 15 chars: '{name:<15}'")
    print(f"Name centered in 15 chars: '{name:^15}'")
    print(f"Number as percentage: {0.875:.1%}")
    
    # Binary, octal, and hexadecimal formatting
    number = 255
    print(f"\nNumber formatting for {number}:")
    print(f"Binary: {number:b}")
    print(f"Octal: {number:o}")
    print(f"Hexadecimal (lower): {number:x}")
    print(f"Hexadecimal (upper): {number:X}")
    
    # Complex formatting with expressions
    items = [
        {"product": "Laptop", "price": 999.99, "quantity": 2},
        {"product": "Mouse", "price": 29.99, "quantity": 5},
        {"product": "Keyboard", "price": 79.99, "quantity": 3}
    ]
    
    print(f"\nInvoice:")
    print(f"{'Product':<12} {'Price':>8} {'Qty':>4} {'Total':>10}")
    print("-" * 36)
    
    total_cost = 0
    for item in items:
        item_total = item["price"] * item["quantity"]
        total_cost += item_total
        print(f"{item['product']:<12} ${item['price']:>7.2f} {item['quantity']:>4} ${item_total:>9.2f}")
    
    print("-" * 36)
    print(f"{'Total':<25} ${total_cost:>9.2f}")
    
    # Template strings (alternative formatting)
    from string import Template
    
    template = Template("Hello $name, you have $count new messages!")
    message = template.substitute(name="Bob", count=3)
    print(f"\nTemplate string: {message}")


def demo_unicode_encoding():
    """Example 3: Unicode handling and string encoding"""
    print("=== Unicode and Encoding ===")
    
    # Unicode strings
    multilingual_text = {
        "english": "Hello, World!",
        "spanish": "¡Hola, Mundo!",
        "french": "Bonjour, le monde!",
        "german": "Hallo, Welt!",
        "russian": "Привет, мир!",
        "chinese": "你好，世界！",
        "japanese": "こんにちは、世界！",
        "arabic": "مرحبا بالعالم!",
        "emoji": "Hello 🌍 World! 🐍 Python 🚀"
    }
    
    print("Multilingual greetings:")
    for language, text in multilingual_text.items():
        print(f"  {language.capitalize()}: {text}")
    
    # String encoding and decoding
    sample_text = "Python 🐍 Programming with Unicode 🌟"
    
    print(f"\nEncoding examples for: '{sample_text}'")
    
    # Different encodings
    encodings = ['utf-8', 'utf-16', 'utf-32', 'ascii', 'latin-1']
    
    for encoding in encodings:
        try:
            encoded = sample_text.encode(encoding)
            decoded = encoded.decode(encoding)
            
            print(f"  {encoding:>8}: {len(encoded):>3} bytes - {encoded[:20]}...")
            print(f"           Decoded successfully: {decoded == sample_text}")
            
        except UnicodeEncodeError as e:
            print(f"  {encoding:>8}: Encoding error - {e}")
        except UnicodeDecodeError as e:
            print(f"  {encoding:>8}: Decoding error - {e}")
    
    # Working with escape sequences
    print(f"\nEscape sequences:")
    escape_examples = [
        ("\\n", "Line break"),
        ("\\t", "Tab character"),
        ("\\\\", "Backslash"),
        ("\\\"", "Double quote"),
        ("\\'", "Single quote"),
        ("\\r", "Carriage return"),
        ("\\u0041", "Unicode A"),
        ("\\u03B1", "Unicode α (alpha)"),
        ("\\U0001F40D", "Unicode 🐍 (snake)")
    ]
    
    for escape, description in escape_examples:
        # Need to use repr to show the escape sequences properly
        actual = eval(f"'{escape}'")
        print(f"  {repr(escape):>12} ({description}): {repr(actual)}")
    
    # String normalization
    print(f"\nUnicode normalization:")
    
    # Different ways to represent the same character
    cafe1 = "café"  # é as a single character
    cafe2 = "cafe\u0301"  # e + combining acute accent
    
    print(f"String 1: '{cafe1}' (length: {len(cafe1)})")
    print(f"String 2: '{cafe2}' (length: {len(cafe2)})")
    print(f"Equal? {cafe1 == cafe2}")
    
    import unicodedata
    
    # Normalize both strings
    cafe1_normalized = unicodedata.normalize('NFC', cafe1)
    cafe2_normalized = unicodedata.normalize('NFC', cafe2)
    
    print(f"After normalization: {cafe1_normalized == cafe2_normalized}")
    
    # Character analysis
    print(f"\nCharacter analysis for 'Pythön 🐍':")
    test_string = "Pythön 🐍"
    
    for i, char in enumerate(test_string):
        try:
            name = unicodedata.name(char)
        except ValueError:
            name = "NO NAME"
        
        print(f"  [{i}] '{char}' U+{ord(char):04X} {name}")
    
    # Practical encoding example - handling file names
    filenames = [
        "document.txt",
        "résumé.pdf",
        "データ.xlsx",
        "файл.docx",
        "🐍_python_script.py"
    ]
    
    print(f"\nFilename encoding compatibility:")
    for filename in filenames:
        try:
            # Try to encode as ASCII (strict filesystem compatibility)
            ascii_safe = filename.encode('ascii')
            print(f"  '{filename}': ASCII safe ✓")
        except UnicodeEncodeError:
            # Create ASCII-safe version
            ascii_safe = filename.encode('ascii', errors='ignore').decode('ascii')
            print(f"  '{filename}': ASCII unsafe → '{ascii_safe}' ✗")


# ============================================================================
# MAIN PROGRAM - Interactive Demo Runner
# ============================================================================

def print_separator(title=""):
    """Print a visual separator with optional title"""
    width = 80
    if title:
        print(f"\n{'=' * width}")
        print(f"{title.center(width)}")
        print(f"{'=' * width}")
    else:
        print(f"{'=' * width}")


def run_all_demos():
    """Run all demonstration functions"""
    demos = [
        # Topic 1: Dictionaries
        ("1.1 Dictionary Basics", demo_dict_basics),
        ("1.2 Dictionary Default Values", demo_dict_default_values),
        ("1.3 Dictionary Iterations", demo_dict_iterations),
        
        # Topic 2: File I/O
        ("2.1 Basic File Operations", demo_basic_file_operations),
        ("2.2 JSON File Handling", demo_json_file_handling),
        ("2.3 Advanced File Operations", demo_advanced_file_operations),
        
        # Topic 3: Functions
        ("3.1 Function Basics", demo_function_basics),
        ("3.2 Advanced Functions", demo_advanced_functions),
        ("3.3 Lambda Functions", demo_lambda_functions),
        
        # Topic 4: Lists and Tuples
        ("4.1 List and Tuple Basics", demo_list_tuple_basics),
        ("4.2 List Functions", demo_list_functions),
        ("4.3 Sorting and Searching", demo_sorting_searching),
        
        # Topic 5: Classes
        ("5.1 Basic Classes", demo_basic_classes),
        ("5.2 Inheritance and Polymorphism", demo_inheritance_polymorphism),
        ("5.3 Static Methods and Private Attributes", demo_static_private_methods),
        
        # Topic 6: Control Flow
        ("6.1 Conditional Statements", demo_conditional_statements),
        ("6.2 Basic Loops", demo_loops_basic),
        ("6.3 Advanced Control Flow", demo_advanced_control_flow),
        
        # Topic 7: Exception Handling
        ("7.1 Basic Exception Handling", demo_basic_exception_handling),
        ("7.2 Custom Exceptions", demo_custom_exceptions),
        ("7.3 Exception Propagation", demo_exception_propagation),
        
        # Topic 8: Comprehensions
        ("8.1 List Comprehensions", demo_list_comprehensions),
        ("8.2 Dictionary and Set Comprehensions", demo_dict_set_comprehensions),
        ("8.3 Functional Tools", demo_functional_tools),
        
        # Topic 9: Strings
        ("9.1 String Basics", demo_string_basics),
        ("9.2 String Formatting", demo_string_formatting),
        ("9.3 Unicode and Encoding", demo_unicode_encoding),
    ]
    
    print_separator("PYTHON CORE CONCEPTS - 27 EXAMPLES")
    print(f"Running all {len(demos)} demonstrations...")
    
    for i, (title, demo_func) in enumerate(demos, 1):
        print_separator(f"DEMO {i}: {title}")
        try:
            demo_func()
        except Exception as e:
            print(f"Error in demo '{title}': {e}")
        
        if i < len(demos):  # Don't pause after the last demo
            print(f"\n{'.' * 80}")


def run_topic_demo(topic_number):
    """Run demos for a specific topic"""
    topic_demos = {
        1: [
            ("Dictionary Basics", demo_dict_basics),
            ("Dictionary Default Values", demo_dict_default_values),
            ("Dictionary Iterations", demo_dict_iterations),
        ],
        2: [
            ("Basic File Operations", demo_basic_file_operations),
            ("JSON File Handling", demo_json_file_handling),
            ("Advanced File Operations", demo_advanced_file_operations),
        ],
        3: [
            ("Function Basics", demo_function_basics),
            ("Advanced Functions", demo_advanced_functions),
            ("Lambda Functions", demo_lambda_functions),
        ],
        4: [
            ("List and Tuple Basics", demo_list_tuple_basics),
            ("List Functions", demo_list_functions),
            ("Sorting and Searching", demo_sorting_searching),
        ],
        5: [
            ("Basic Classes", demo_basic_classes),
            ("Inheritance and Polymorphism", demo_inheritance_polymorphism),
            ("Static Methods and Private Attributes", demo_static_private_methods),
        ],
        6: [
            ("Conditional Statements", demo_conditional_statements),
            ("Basic Loops", demo_loops_basic),
            ("Advanced Control Flow", demo_advanced_control_flow),
        ],
        7: [
            ("Basic Exception Handling", demo_basic_exception_handling),
            ("Custom Exceptions", demo_custom_exceptions),
            ("Exception Propagation", demo_exception_propagation),
        ],
        8: [
            ("List Comprehensions", demo_list_comprehensions),
            ("Dictionary and Set Comprehensions", demo_dict_set_comprehensions),
            ("Functional Tools", demo_functional_tools),
        ],
        9: [
            ("String Basics", demo_string_basics),
            ("String Formatting", demo_string_formatting),
            ("Unicode and Encoding", demo_unicode_encoding),
        ],
    }
    
    topic_names = {
        1: "Python Dictionaries",
        2: "Python File I/O",
        3: "Python Functions",
        4: "Python Lists and Tuples",
        5: "Python Classes",
        6: "Python Control Flow",
        7: "Python Exception Handling",
        8: "Python Comprehensions",
        9: "Python Strings",
    }
    
    if topic_number not in topic_demos:
        print(f"Invalid topic number: {topic_number}")
        print("Valid topics: 1-9")
        return
    
    topic_name = topic_names[topic_number]
    demos = topic_demos[topic_number]
    
    print_separator(f"TOPIC {topic_number}: {topic_name.upper()}")
    
    for i, (title, demo_func) in enumerate(demos, 1):
        print_separator(f"{topic_number}.{i}: {title}")
        try:
            demo_func()
        except Exception as e:
            print(f"Error in demo '{title}': {e}")
        
        if i < len(demos):
            print(f"\n{'.' * 80}")


def show_menu():
    """Display interactive menu"""
    print_separator("PYTHON CORE CONCEPTS - INTERACTIVE MENU")
    print("Choose an option:")
    print("  0  - Run all 27 examples")
    print("  1  - Python Dictionaries (3 examples)")
    print("  2  - Python File I/O (3 examples)")
    print("  3  - Python Functions (3 examples)")
    print("  4  - Python Lists and Tuples (3 examples)")
    print("  5  - Python Classes (3 examples)")
    print("  6  - Python Control Flow (3 examples)")
    print("  7  - Python Exception Handling (3 examples)")
    print("  8  - Python Comprehensions (3 examples)")
    print("  9  - Python Strings (3 examples)")
    print("  q  - Quit")
    print_separator()


def main():
    """Main program entry point"""
    import sys
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--demo" and len(sys.argv) > 2:
            try:
                topic_num = int(sys.argv[2])
                run_topic_demo(topic_num)
                return
            except ValueError:
                print("Invalid topic number. Use --demo N where N is 1-9")
                return
        elif sys.argv[1] == "--help":
            print(__doc__)
            return
    
    # Interactive mode or run all
    if len(sys.argv) == 1:
        while True:
            show_menu()
            choice = input("Enter your choice: ").strip().lower()
            
            if choice == 'q':
                print("Goodbye!")
                break
            elif choice == '0':
                run_all_demos()
                input("\nPress Enter to continue...")
            elif choice.isdigit() and 1 <= int(choice) <= 9:
                run_topic_demo(int(choice))
                input("\nPress Enter to continue...")
            else:
                print("Invalid choice. Please try again.")
    else:
        # No arguments - run all demos
        run_all_demos()


if __name__ == "__main__":
    main()