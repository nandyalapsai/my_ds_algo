# Complete Classes & Data Structures Study Guide

*A comprehensive guide covering everything you need to know about classes and their application to data structures*

---

## 📚 Table of Contents

1. [Quick Reference](#quick-reference)
2. [Fundamental Concepts](#fundamental-concepts)
3. [Visual Diagrams](#visual-diagrams)
4. [Working Code Examples](#working-code-examples)
5. [Practice Exercises](#practice-exercises)
6. [Advanced Topics](#advanced-topics)
7. [Troubleshooting Guide](#troubleshooting-guide)

---

# Quick Reference

## 🚀 Essential Syntax

### Class Definition
```python
class ClassName:                    # PascalCase naming
    def __init__(self, param):      # Constructor
        self.attribute = param      # Instance attribute
    
    def method_name(self):          # Instance method
        return self.attribute       # Access attribute
```

### Object Creation & Usage
```python
obj = ClassName("value")           # Create object
result = obj.method_name()         # Call method
obj.attribute = "new_value"        # Direct access (not recommended)
```

## 🔑 Key Concepts Cheat Sheet

| Concept | Definition | Example |
|---------|------------|---------|
| **Class** | Blueprint for objects | `class Cookie:` |
| **Object** | Instance of a class | `cookie1 = Cookie("red")` |
| **Constructor** | Special method to initialize | `def __init__(self, color):` |
| **self** | Reference to current instance | `self.color = color` |
| **Attribute** | Data stored in object | `self.color` |
| **Method** | Function belonging to class | `def get_color(self):` |
| **Instance** | Specific object from class | `cookie1`, `cookie2` |

## ⚡ Common Patterns

### Getter/Setter Pattern
```python
def get_attribute(self):
    return self.attribute

def set_attribute(self, value):
    self.attribute = value
```

### Validation in Setter
```python
def set_grade(self, grade):
    if 0 <= grade <= 100:
        self.grade = grade
    else:
        raise ValueError("Grade must be 0-100")
```

## 📊 Complexity Quick Reference

### Basic Operations
- **Object creation**: O(1)
- **Attribute access**: O(1)
- **Method call**: O(1) + method complexity

### Data Structure Preview
| Structure | Insert | Delete | Search |
|-----------|--------|--------|--------|
| Array | O(n) | O(n) | O(n) |
| Linked List | O(1) at ends | O(n) | O(n) |
| Hash Table | O(1) avg | O(1) avg | O(1) avg |
| Binary Tree | O(log n) avg | O(log n) avg | O(log n) avg |

---

# Fundamental Concepts

## 🎯 What are Classes?

### Definition
A **class** is a blueprint or template for creating custom data types in Python. It's a way to create your own data structure with specific properties and behaviors.

### Key Concepts
- Classes allow you to create **custom data types**
- Python has built-in types (int, str, list) but classes let you create your own
- Every data structure we'll implement uses classes
- Classes encapsulate data (attributes) and behavior (methods)

### Real-World Example
Think of a class like a blueprint for a house:
- The blueprint (class) defines what rooms, doors, windows the house should have
- Each actual house built from that blueprint is an **instance** or **object**
- All houses follow the same blueprint but can have different colors, addresses, etc.

## 🍪 Cookie Cutter Analogy

### The Analogy Explained
```
Cookie Cutter (Class) → Cookie (Object/Instance)
     Blueprint      →     Actual Thing
```

- **Class = Cookie Cutter**: Defines the shape and properties
- **Object = Cookie**: The actual item created from the class
- **Attributes = Cookie Color**: Properties that can vary between instances
- **Methods = Cookie Actions**: Things you can do with the cookie

### Why This Analogy Works
1. **One cutter, many cookies**: One class can create multiple objects
2. **Same shape, different details**: All objects share methods but have unique attributes
3. **Independent cookies**: Changing one cookie doesn't affect others
4. **Reusable pattern**: You can make as many cookies as needed

## 🏗️ Class Components

### 1. Class Declaration
```python
class Cookie:  # Capital letter by convention
    # Class body goes here
```

### 2. Constructor (`__init__`)
- Special method that runs when creating new objects
- Initializes the object's attributes
- **Always** the first method in a class

### 3. Instance Methods
- Functions that belong to the class
- Always have `self` as first parameter
- Operate on specific instances of the class

### 4. Attributes
- Variables that store data for each instance
- Accessed using dot notation: `object.attribute`

## 🔧 Constructor Method

### Syntax & Purpose
```python
def __init__(self, parameter1, parameter2, ...):
    self.attribute1 = parameter1
    self.attribute2 = parameter2
```

### Key Points
- **`__init__`**: Special method name (double underscores)
- **`self`**: Refers to the specific instance being created
- **Parameters**: Values passed when creating the object
- **Assignment**: `self.attribute = value` stores data in the instance

### Example Breakdown
```python
def __init__(self, color):
    self.color = color
    #    ↑       ↑
    #    │       └── Parameter passed to constructor
    #    └── Instance attribute
```

## 🔄 Instance Methods

### Getter Method
```python
def get_color(self):
    return self.color
```
- **Purpose**: Retrieve attribute values
- **Parameters**: Only `self` (no additional arguments)
- **Returns**: The requested attribute value

### Setter Method
```python
def set_color(self, color):
    self.color = color
```
- **Purpose**: Modify attribute values
- **Parameters**: `self` + new value
- **Action**: Updates the instance attribute

### Method vs Function
| Aspect | Method | Function |
|--------|--------|----------|
| Location | Inside a class | Outside any class |
| First Parameter | Always `self` | Any parameters |
| Purpose | Operates on objects | General computation |
| Call Syntax | `object.method()` | `function()` |

## 🎯 The `self` Keyword

### What is `self`?
- **Reference** to the current instance of the class
- **Distinguishes** between different objects of the same class
- **Required** as first parameter in all instance methods
- **Not** passed explicitly when calling methods

### Why `self` is Needed
```python
# Without self, Python wouldn't know which cookie's color to get
cookie1.color  # ✅ Gets cookie1's color
cookie2.color  # ✅ Gets cookie2's color
# color         # ❌ Which cookie's color?
```

### Self in Action
When you call `cookie1.get_color()`, Python internally does:
```python
Cookie.get_color(cookie1)  # self becomes cookie1
```

## 🏭 Creating Objects

### Syntax
```python
object_name = ClassName(arguments)
```

### Step-by-Step Process
1. **Call the class**: `Cookie("green")`
2. **Python creates**: New object in memory
3. **Runs constructor**: `__init__(self, "green")`
4. **Returns object**: Assigns to variable

### Multiple Instances
```python
cookie1 = Cookie("green")  # First instance
cookie2 = Cookie("blue")   # Second instance (completely separate)

# Each has its own color attribute
print(cookie1.color)  # "green"
print(cookie2.color)  # "blue"

# Changing one doesn't affect the other
cookie1.set_color("yellow")
print(cookie1.color)  # "yellow"
print(cookie2.color)  # "blue" (unchanged)
```

## 🗂️ Application to Data Structures

### Why Classes for Data Structures?
1. **Encapsulation**: Bundle data and operations together
2. **Reusability**: Create multiple instances easily
3. **Organization**: Keep related functionality together
4. **Abstraction**: Hide implementation details

### Linked List Example Structure
```python
class LinkedList:
    def __init__(self):
        # Initialize empty list
        self.head = None
        self.length = 0
    
    def append(self, value):        # O(1)
        # Add to end
        pass
    
    def prepend(self, value):       # O(1)
        # Add to beginning
        pass
    
    def insert(self, index, value): # O(n)
        # Add at specific position
        pass
    
    def remove(self, value):        # O(n)
        # Remove specific value
        pass
    
    def pop(self):                  # O(1)
        # Remove from end
        pass
```

### Benefits for Data Structures
- **State Management**: Each list maintains its own data
- **Method Organization**: All list operations in one place
- **Multiple Lists**: Can create many independent lists
- **Consistent Interface**: Same methods across all instances

---

# Visual Diagrams

## Class vs Object Relationship

```
    BLUEPRINT LEVEL (Class)
    ┌─────────────────────────────────┐
    │         Cookie Class            │
    │  ───────────────────────────── │
    │  📋 Attributes:                 │
    │     • color (string)            │
    │                                 │
    │  🔧 Methods:                    │
    │     • __init__(color)           │
    │     • get_color()               │
    │     • set_color(color)          │
    └─────────────────────────────────┘
                    │
                    │ creates instances
                    ▼
    INSTANCE LEVEL (Objects)
    ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
    │  cookie1    │     │  cookie2    │     │  cookie3    │
    │ ─────────── │     │ ─────────── │     │ ─────────── │
    │ color:"green"│     │ color:"blue"│     │ color:"red" │
    │             │     │             │     │             │
    │ 🔧 Same     │     │ 🔧 Same     │     │ 🔧 Same     │
    │   methods   │     │   methods   │     │   methods   │
    └─────────────┘     └─────────────┘     └─────────────┘
```

## Constructor Flow Diagram

```
    Step 1: Call Constructor
    ┌─────────────────────────┐
    │ cookie1 = Cookie("green")│
    └─────────────┬───────────┘
                  │
                  ▼
    Step 2: Python Creates Object
    ┌─────────────────────────┐
    │   New Cookie Object     │
    │   (empty memory space)  │
    └─────────────┬───────────┘
                  │
                  ▼
    Step 3: Call __init__ Method
    ┌─────────────────────────┐
    │ __init__(self, "green") │
    │                         │
    │ self.color = "green"    │
    └─────────────┬───────────┘
                  │
                  ▼
    Step 4: Return Initialized Object
    ┌─────────────────────────┐
    │     cookie1             │
    │   ┌─────────────────┐   │
    │   │ color: "green"  │   │
    │   │ methods: ready  │   │
    │   └─────────────────┘   │
    └─────────────────────────┘
```

## Self Keyword Explanation

```
    When you call: cookie1.get_color()
    
    What Python does internally:
    ┌─────────────────────────────────────┐
    │ Cookie.get_color(cookie1)           │
    │                    ↑                │
    │                    │                │
    │              This becomes 'self'    │
    └─────────────────────────────────────┘
    
    Inside the method:
    ┌─────────────────────────────────────┐
    │ def get_color(self):                │
    │     return self.color               │
    │            ↑                        │
    │            │                        │
    │      Refers to cookie1              │
    └─────────────────────────────────────┘
```

## Memory Layout of Multiple Objects

```
    Memory Space
    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │  cookie1 (Object 1)          cookie2 (Object 2)        │
    │  ┌─────────────────┐         ┌─────────────────┐       │
    │  │ Memory Address: │         │ Memory Address: │       │
    │  │ 0x1A2B3C4D      │         │ 0x5E6F7G8H      │       │
    │  │                 │         │                 │       │
    │  │ Attributes:     │         │ Attributes:     │       │
    │  │ color = "green" │         │ color = "blue"  │       │
    │  │                 │         │                 │       │
    │  │ Methods:        │         │ Methods:        │       │
    │  │ (shared code)   │ ────────┼─(shared code)   │       │
    │  └─────────────────┘         └─────────────────┘       │
    │                                                         │
    └─────────────────────────────────────────────────────────┘
    
    Note: Methods are shared (same code), but each object has its own attributes
```

## Method Call Flow

```
    When you call: cookie1.set_color("yellow")
    
    ┌─────────────────────────────────────────────────────────┐
    │                    Call Flow                            │
    └─────────────────────────────────────────────────────────┘
                              │
                              ▼
    ┌─────────────────────────────────────────────────────────┐
    │ 1. Python identifies 'cookie1' as the object           │
    └─────────────────┬───────────────────────────────────────┘
                      │
                      ▼
    ┌─────────────────────────────────────────────────────────┐
    │ 2. Finds 'set_color' method in Cookie class            │
    └─────────────────┬───────────────────────────────────────┘
                      │
                      ▼
    ┌─────────────────────────────────────────────────────────┐
    │ 3. Calls: Cookie.set_color(cookie1, "yellow")          │
    │    - self = cookie1                                     │
    │    - color = "yellow"                                   │
    └─────────────────┬───────────────────────────────────────┘
                      │
                      ▼
    ┌─────────────────────────────────────────────────────────┐
    │ 4. Executes: self.color = color                        │
    │    Which means: cookie1.color = "yellow"               │
    └─────────────────┬───────────────────────────────────────┘
                      │
                      ▼
    ┌─────────────────────────────────────────────────────────┐
    │ 5. cookie1's color attribute is now "yellow"           │
    └─────────────────────────────────────────────────────────┘
```

## Object Independence Demonstration

```
    Initial State:
    cookie1 ──→ Cookie Object 1
                ┌─────────────┐
                │ color:"green"│
                └─────────────┘
    
    cookie2 ──→ Cookie Object 2
                ┌─────────────┐
                │ color:"blue" │
                └─────────────┘
    
    After cookie1.set_color("yellow"):
    cookie1 ──→ Cookie Object 1
                ┌──────────────┐
                │ color:"yellow"│  ← Changed
                └──────────────┘
    
    cookie2 ──→ Cookie Object 2
                ┌─────────────┐
                │ color:"blue" │  ← Unchanged
                └─────────────┘
    
    Key Point: Each object maintains its own state independently!
```

## Data Structure Application - Linked List

```
    LinkedList Class Structure
    ┌─────────────────────────────────────────────────────────┐
    │                   LinkedList                            │
    │  ─────────────────────────────────────────────────────  │
    │                                                         │
    │  📋 Attributes:                                         │
    │     • head (pointer to first node)                     │
    │     • tail (pointer to last node)                      │
    │     • length (number of nodes)                         │
    │                                                         │
    │  🔧 Methods:                                            │
    │     • __init__()           [O(1)]                      │
    │     • append(value)        [O(1)]                      │
    │     • prepend(value)       [O(1)]                      │
    │     • insert(index, value) [O(n)]                      │
    │     • remove(value)        [O(n)]                      │
    │     • pop()                [O(1)]                      │
    └─────────────────────────────────────────────────────────┘
                    │
                    │ creates instances
                    ▼
    ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
    │   list1     │     │   list2     │     │   list3     │
    │ ─────────── │     │ ─────────── │     │ ─────────── │
    │ head: Node1 │     │ head: NodeA │     │ head: None  │
    │ tail: Node3 │     │ tail: NodeC │     │ tail: None  │
    │ length: 3   │     │ length: 3   │     │ length: 0   │
    └─────────────┘     └─────────────┘     └─────────────┘
         │                       │                   │
         ▼                       ▼                   ▼
    [1]->[2]->[3]          [A]->[B]->[C]         (empty)
```

---

# Working Code Examples

## Complete Cookie Class Implementation

```python
"""
Classes and Data Structures - Code Examples
===========================================

This section contains all the working code examples from the video transcript
about classes and their application to data structures.
"""

# ============================================================================
# BASIC COOKIE CLASS IMPLEMENTATION
# ============================================================================

class Cookie:
    """
    A simple class demonstrating the fundamental concepts of classes in Python.
    Uses a cookie analogy where each cookie has a color attribute.
    """
    
    def __init__(self, color):
        """
        Constructor method - initializes a new cookie with a specific color.
        
        Args:
            color (str): The color of the cookie
        """
        self.color = color
    
    def get_color(self):
        """
        Getter method - returns the current color of the cookie.
        
        Returns:
            str: The color of the cookie
        """
        return self.color
    
    def set_color(self, color):
        """
        Setter method - changes the color of the cookie.
        
        Args:
            color (str): The new color for the cookie
        """
        self.color = color


# ============================================================================
# DEMONSTRATION OF COOKIE CLASS USAGE
# ============================================================================

def demonstrate_cookie_class():
    """Demonstrates the usage of the Cookie class with examples from the video."""
    
    print("=" * 50)
    print("COOKIE CLASS DEMONSTRATION")
    print("=" * 50)
    
    # Creating two cookie instances
    print("\n1. Creating cookies:")
    cookie1 = Cookie("green")
    cookie2 = Cookie("blue")
    
    print(f"Cookie 1 created with color: {cookie1.get_color()}")
    print(f"Cookie 2 created with color: {cookie2.get_color()}")
    
    # Demonstrating getter methods
    print("\n2. Getting colors:")
    print(f"Cookie 1 is {cookie1.get_color()}")
    print(f"Cookie 2 is {cookie2.get_color()}")
    
    # Demonstrating setter method
    print("\n3. Changing cookie1's color:")
    cookie1.set_color("yellow")
    print(f"Cookie 1 is now {cookie1.get_color()}")
    print(f"Cookie 2 is still {cookie2.get_color()}")
    
    # Demonstrating independence of instances
    print("\n4. Demonstrating instance independence:")
    cookie2.set_color("red")
    print(f"After changing cookie2 to red:")
    print(f"Cookie 1 remains: {cookie1.get_color()}")
    print(f"Cookie 2 is now: {cookie2.get_color()}")


# ============================================================================
# LINKED LIST CLASS TEMPLATE
# ============================================================================

class LinkedList:
    """
    A template for a LinkedList class showing how classes are used
    for data structure implementation.
    
    This is a high-level overview as mentioned in the video transcript.
    Methods are not fully implemented but show the structure.
    """
    
    def __init__(self):
        """Constructor - initializes an empty linked list."""
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        """
        Add an element to the end of the linked list.
        
        Args:
            value: The value to append
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Implementation would go here
        print(f"Appending {value} to the linked list")
        pass
    
    def prepend(self, value):
        """
        Add an element to the beginning of the linked list.
        
        Args:
            value: The value to prepend
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Implementation would go here
        print(f"Prepending {value} to the linked list")
        pass
    
    def insert(self, index, value):
        """
        Insert an element at a specific index.
        
        Args:
            index (int): The index where to insert
            value: The value to insert
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Implementation would go here
        print(f"Inserting {value} at index {index}")
        pass
    
    def remove(self, value):
        """
        Remove the first occurrence of a value from the linked list.
        
        Args:
            value: The value to remove
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Implementation would go here
        print(f"Removing {value} from the linked list")
        pass
    
    def pop(self):
        """
        Remove and return the last element from the linked list.
        
        Returns:
            The value of the removed element
            
        Time Complexity: O(1) if we maintain a tail pointer
        Space Complexity: O(1)
        """
        # Implementation would go here
        print("Popping element from the end of the linked list")
        pass


# ============================================================================
# ADDITIONAL EXAMPLES FOR PRACTICE
# ============================================================================

class Student:
    """Example class for practice - demonstrates class concepts with a Student."""
    
    def __init__(self, name, grade, age):
        """Initialize a student with name, grade, and age."""
        self.name = name
        self.grade = grade
        self.age = age
    
    def get_info(self):
        """Return formatted student information."""
        return f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
    def set_grade(self, new_grade):
        """Update the student's grade."""
        self.grade = new_grade
        print(f"{self.name}'s grade updated to {new_grade}")
    
    def is_passing(self):
        """Check if student is passing (grade >= 60)."""
        return self.grade >= 60


class BankAccount:
    """Advanced example showing validation and error handling."""
    
    def __init__(self, account_number, initial_balance=0):
        """Initialize a bank account."""
        self.account_number = account_number
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return True
        return False
    
    def get_balance(self):
        """Get current balance."""
        return self.balance
    
    def get_statement(self):
        """Get transaction history."""
        return self.transaction_history.copy()


# ============================================================================
# DEMONSTRATION FUNCTIONS
# ============================================================================

def demonstrate_student_class():
    """Demonstrate the Student class functionality."""
    print("\n" + "=" * 50)
    print("STUDENT CLASS DEMONSTRATION")
    print("=" * 50)
    
    # Create students
    student1 = Student("Alice", 85, 20)
    student2 = Student("Bob", 55, 19)
    
    # Display information
    print(f"Student 1: {student1.get_info()}")
    print(f"Student 2: {student2.get_info()}")
    
    # Check passing status
    print(f"Alice is passing: {student1.is_passing()}")
    print(f"Bob is passing: {student2.is_passing()}")
    
    # Update grade
    student2.set_grade(75)
    print(f"Bob is now passing: {student2.is_passing()}")


def demonstrate_bank_account():
    """Demonstrate the BankAccount class functionality."""
    print("\n" + "=" * 50)
    print("BANK ACCOUNT DEMONSTRATION")
    print("=" * 50)
    
    # Create account
    account = BankAccount("12345", 100)
    print(f"Initial balance: ${account.get_balance()}")
    
    # Make transactions
    account.deposit(50)
    print(f"After deposit: ${account.get_balance()}")
    
    account.withdraw(30)
    print(f"After withdrawal: ${account.get_balance()}")
    
    # Show transaction history
    print("Transaction history:")
    for transaction in account.get_statement():
        print(f"  - {transaction}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def run_all_examples():
    """Run all the code examples."""
    # Run the cookie class demonstration
    demonstrate_cookie_class()
    
    # Show linked list structure
    print("\n" + "=" * 50)
    print("LINKED LIST CLASS TEMPLATE")
    print("=" * 50)
    
    # Create a linked list instance
    my_list = LinkedList()
    print("\nLinkedList Class Structure:")
    print("├── Constructor: __init__()")
    print("├── append(value)")
    print("├── prepend(value)")
    print("├── insert(index, value)")
    print("├── remove(value)")
    print("└── pop()")
    
    # Demonstrate method calls (template only)
    print("\nMethod call examples:")
    my_list.append("first")
    my_list.prepend("zero")
    my_list.insert(1, "middle")
    my_list.remove("first")
    my_list.pop()
    
    # Run student class demonstration
    demonstrate_student_class()
    
    # Run bank account demonstration
    demonstrate_bank_account()
    
    print("\n" + "=" * 50)
    print("KEY CONCEPTS SUMMARY")
    print("=" * 50)
    print("✓ Classes are blueprints for creating objects")
    print("✓ Constructor (__init__) initializes new instances")
    print("✓ 'self' refers to the current instance")
    print("✓ Methods are functions that belong to a class")
    print("✓ Each instance maintains its own state")
    print("✓ Classes enable building complex data structures")


# To run the examples, uncomment the line below:
# run_all_examples()
```

## Time & Space Complexity Analysis

### Cookie Class Operations
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| `__init__()` | O(1) | O(1) | Constant time creation |
| `get_color()` | O(1) | O(1) | Direct attribute access |
| `set_color()` | O(1) | O(1) | Direct attribute assignment |

### Memory Usage
- Each cookie instance uses O(1) space
- Creating n cookies uses O(n) total space
- No additional overhead per method call

---

# Practice Exercises

## 🏃‍♂️ Quick Practice Exercises

### Exercise 1: Car Class (5 minutes)
Create a `Car` class with:
- Attributes: make, model, year, is_running
- Methods: start_engine(), stop_engine(), get_info()

**Solution:**
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
    
    def start_engine(self):
        self.is_running = True
        return f"{self.make} {self.model} engine started!"
    
    def stop_engine(self):
        self.is_running = False
        return f"{self.make} {self.model} engine stopped!"
    
    def get_info(self):
        status = "running" if self.is_running else "stopped"
        return f"{self.year} {self.make} {self.model} - {status}"
```

### Exercise 2: Rectangle Class (10 minutes)
Create a `Rectangle` class with:
- Attributes: width, height
- Methods: get_area(), get_perimeter(), is_square()

**Solution:**
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height
```

### Exercise 3: Library Book Class (15 minutes)
Create a `Book` class with:
- Attributes: title, author, pages, is_checked_out
- Methods: check_out(), return_book(), get_info()

**Solution:**
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_checked_out = False
    
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"'{self.title}' has been checked out."
        return f"'{self.title}' is already checked out."
    
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f"'{self.title}' has been returned."
        return f"'{self.title}' was not checked out."
    
    def get_info(self):
        status = "checked out" if self.is_checked_out else "available"
        return f"'{self.title}' by {self.author} ({self.pages} pages) - {status}"
```

## 🎓 Advanced Exercises

### Exercise 4: Temperature Class
Create a class that handles temperature conversions between Celsius, Fahrenheit, and Kelvin.

### Exercise 5: Shopping Cart Class
Create a shopping cart that can add items, remove items, calculate total, and apply discounts.

### Exercise 6: Simple Stack Class
Implement a basic stack data structure using a class with push, pop, peek, and is_empty methods.

---

# Advanced Topics

## 🔧 Special Methods (Magic Methods)

### String Representation
```python
class Cookie:
    def __init__(self, color):
        self.color = color
    
    def __str__(self):
        """Human-readable string representation."""
        return f"Cookie(color={self.color})"
    
    def __repr__(self):
        """Developer-friendly representation."""
        return f"Cookie('{self.color}')"
```

### Comparison Methods
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __eq__(self, other):
        """Equal comparison."""
        return self.grade == other.grade
    
    def __lt__(self, other):
        """Less than comparison."""
        return self.grade < other.grade
```

## 🏛️ Class vs Instance Variables

```python
class Cookie:
    # Class variable (shared by all instances)
    bakery_name = "Sweet Treats Bakery"
    
    def __init__(self, color):
        # Instance variable (unique to each instance)
        self.color = color
    
    @classmethod
    def get_bakery_name(cls):
        return cls.bakery_name
```

## 🔒 Encapsulation and Privacy

### Private Attributes (Convention)
```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance      # Protected (convention)
        self.__pin = "1234"         # Private (name mangling)
    
    def _validate_pin(self, pin):   # Protected method
        return pin == self.__pin
    
    def get_balance(self, pin):
        if self._validate_pin(pin):
            return self._balance
        return "Invalid PIN"
```

## 🎯 Properties and Decorators

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Getter for radius."""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter for radius with validation."""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        """Calculated property."""
        return 3.14159 * self._radius ** 2
```

---

# Troubleshooting Guide

## 🐛 Common Mistakes and Solutions

### ❌ Forgetting `self`
```python
# Wrong
def get_color():
    return color        # NameError: name 'color' is not defined

# Correct
def get_color(self):
    return self.color   # Works!
```

### ❌ Wrong Class Naming
```python
# Wrong
class cookie:           # Should be PascalCase
class Cookie_Class:     # Avoid underscores

# Correct
class Cookie:           # PascalCase
class StudentRecord:    # Multiple words together
```

### ❌ Calling Methods Incorrectly
```python
# Wrong
Cookie.get_color()      # TypeError: missing 1 required positional argument

# Correct
cookie1 = Cookie("red")
cookie1.get_color()     # Works!
```

### ❌ Modifying Class Variables
```python
# Potential issue
class Counter:
    count = 0  # Class variable
    
    def increment(self):
        self.count += 1  # Creates instance variable, doesn't modify class variable

# Better approach
class Counter:
    count = 0
    
    def increment(self):
        Counter.count += 1  # Modifies class variable
```

## 🔍 Debugging Tips

### Print Debug Information
```python
def debug_object(self):
    print(f"Object type: {type(self)}")
    print(f"Attributes: {self.__dict__}")
    print(f"Methods: {[method for method in dir(self) if not method.startswith('_')]}")
```

### Check Attribute Existence
```python
def safe_get_attribute(self, attr_name):
    if hasattr(self, attr_name):
        return getattr(self, attr_name)
    return f"Attribute '{attr_name}' not found"
```

### Validate Input
```python
def set_grade(self, grade):
    if not isinstance(grade, (int, float)):
        raise TypeError("Grade must be a number")
    if not 0 <= grade <= 100:
        raise ValueError("Grade must be between 0 and 100")
    self.grade = grade
```

## 🆘 Error Messages and Solutions

### AttributeError
**Error**: `'Cookie' object has no attribute 'colour'`
**Solution**: Check spelling of attribute names

### TypeError
**Error**: `get_color() missing 1 required positional argument: 'self'`
**Solution**: Call method on an instance, not the class

### NameError
**Error**: `name 'self' is not defined`
**Solution**: Include `self` as first parameter in method definition

### IndentationError
**Error**: `expected an indented block`
**Solution**: Ensure proper indentation in class methods

---

## 🎓 Key Takeaways

### Essential Concepts
1. **Classes are blueprints** for creating custom data types
2. **Constructor (`__init__`)** initializes new objects
3. **`self` keyword** refers to the current instance
4. **Methods are functions** that belong to a class
5. **Each instance is independent** with its own attributes

### Best Practices
- Use **PascalCase** for class names (e.g., `Cookie`, `LinkedList`)
- Always include **`self`** as first parameter in methods
- Write **clear docstrings** for classes and methods
- Keep **related functionality** together in the same class
- **Validate input** in setter methods
- Use **properties** for calculated values

### Memory Tips
- **Cookie cutter analogy**: Class = cutter, Object = cookie
- **`self` = "this specific instance"**
- **Constructor = initialization**
- **Methods = actions objects can perform**

### Next Steps
- Understand how classes enable complex data structures
- Learn about inheritance and polymorphism
- Practice implementing various data structures using classes
- Study how built-in Python types use similar concepts

---

## 📖 Glossary

- **Class**: Template/blueprint for creating objects
- **Object/Instance**: Actual item created from a class
- **Constructor**: Method that initializes new objects (`__init__`)
- **Method**: Function that belongs to a class
- **Attribute**: Variable that stores data in an object
- **self**: Keyword referring to the current instance
- **Instantiation**: Process of creating an object from a class
- **Encapsulation**: Bundling data and methods together in a class

---

*This complete study guide covers everything you need to know about classes as the foundation for data structures. Master these concepts before moving on to implementing specific data structures like linked lists, stacks, and queues.*

*Last updated: July 16, 2025*
