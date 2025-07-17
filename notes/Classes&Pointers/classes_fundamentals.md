# Classes & Data Structures - Study Notes

## 📚 Table of Contents
1. [What are Classes?](#what-are-classes)
2. [Cookie Cutter Analogy](#cookie-cutter-analogy)
3. [Class Components](#class-components)
4. [Constructor Method](#constructor-method)
5. [Instance Methods](#instance-methods)
6. [The `self` Keyword](#the-self-keyword)
7. [Creating Objects](#creating-objects)
8. [Application to Data Structures](#application-to-data-structures)
9. [Code Examples](#code-examples)

---

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

---

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

### Visual Representation
```
    Cookie Class (Blueprint)
    ┌─────────────────────┐
    │  🍪 Cookie Class    │
    │  ────────────────   │
    │  • color attribute  │
    │  • get_color()      │
    │  • set_color()      │
    └─────────────────────┘
              │
              ▼ (creates instances)
    ┌─────────────┐    ┌─────────────┐
    │ cookie1     │    │ cookie2     │
    │ color:green │    │ color:blue  │
    └─────────────┘    └─────────────┘
```

---

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

---

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

---

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

---

## 🎯 The `self` Keyword

### What is `self`?
- **Reference** to the current instance of the class
- **Distinguishes** between different objects of the same class
- **Required** as first parameter in all instance methods
- **Not** passed explicitly when calling methods

### Visual Understanding
```python
cookie1 = Cookie("green")  # self refers to cookie1
cookie2 = Cookie("blue")   # self refers to cookie2

cookie1.get_color()  # self = cookie1, returns "green"
cookie2.get_color()  # self = cookie2, returns "blue"
```

### Why `self` is Needed
```python
# Without self, Python wouldn't know which cookie's color to get
cookie1.color  # ✅ Gets cookie1's color
cookie2.color  # ✅ Gets cookie2's color
# color         # ❌ Which cookie's color?
```

---

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

---

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
    
    def append(self, value):
        # Add to end
        pass
    
    def prepend(self, value):
        # Add to beginning
        pass
    
    def insert(self, index, value):
        # Add at specific position
        pass
    
    def remove(self, value):
        # Remove specific value
        pass
    
    def pop(self):
        # Remove from end
        pass
```

### Benefits for Data Structures
- **State Management**: Each list maintains its own data
- **Method Organization**: All list operations in one place
- **Multiple Lists**: Can create many independent lists
- **Consistent Interface**: Same methods across all instances

---

## 💻 Code Examples

### Complete Cookie Class
```python
class Cookie:
    def __init__(self, color):
        """Constructor - creates a new cookie with specified color"""
        self.color = color
    
    def get_color(self):
        """Getter method - returns the cookie's color"""
        return self.color
    
    def set_color(self, color):
        """Setter method - changes the cookie's color"""
        self.color = color

# Creating and using cookies
cookie1 = Cookie("green")
cookie2 = Cookie("blue")

# Testing getter methods
print(f"Cookie 1 is {cookie1.get_color()}")  # Cookie 1 is green
print(f"Cookie 2 is {cookie2.get_color()}")  # Cookie 2 is blue

# Testing setter method
cookie1.set_color("yellow")
print(f"Cookie 1 is now {cookie1.get_color()}")  # Cookie 1 is now yellow
print(f"Cookie 2 is still {cookie2.get_color()}")  # Cookie 2 is still blue
```

### Time & Space Complexity

#### Cookie Class Operations
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| `__init__()` | O(1) | O(1) | Constant time creation |
| `get_color()` | O(1) | O(1) | Direct attribute access |
| `set_color()` | O(1) | O(1) | Direct attribute assignment |

#### Memory Usage
- Each cookie instance uses O(1) space
- Creating n cookies uses O(n) total space
- No additional overhead per method call

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

### Next Steps
- Understand how classes enable complex data structures
- Learn about inheritance and polymorphism
- Practice implementing various data structures using classes
- Study how built-in Python types use similar concepts

---

## 📝 Practice Exercises

### Exercise 1: Student Class
Create a `Student` class with:
- Attributes: name, grade, age
- Methods: get_info(), set_grade(), is_passing() (grade >= 60)

### Exercise 2: Bank Account Class
Create a `BankAccount` class with:
- Attributes: account_number, balance, owner
- Methods: deposit(), withdraw(), get_balance(), transfer()

### Exercise 3: Book Class
Create a `Book` class with:
- Attributes: title, author, pages, is_read
- Methods: mark_as_read(), get_info(), __str__()

---

*These notes cover the fundamental concepts of classes as building blocks for data structures. Master these concepts before moving on to implementing specific data structures like linked lists, stacks, and queues.*
