# Classes & Data Structures - Quick Reference

## 🚀 Quick Syntax Reference

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

### String Representation
```python
def __str__(self):
    return f"Cookie(color={self.color})"
```

## 🐛 Common Mistakes to Avoid

### ❌ Forgetting `self`
```python
def get_color():        # Missing self
    return color        # Won't work!
```

### ✅ Correct Version
```python
def get_color(self):    # Include self
    return self.color   # Works!
```

### ❌ Wrong Class Naming
```python
class cookie:           # Should be PascalCase
class Cookie_Class:     # Avoid underscores
```

### ✅ Correct Naming
```python
class Cookie:           # PascalCase
class StudentRecord:    # Multiple words together
```

### ❌ Calling Methods Incorrectly
```python
Cookie.get_color()      # Missing instance
```

### ✅ Correct Method Call
```python
cookie1.get_color()     # Call on instance
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

## 🎯 Memory Tips

### Remember the Cookie Analogy
- **Cookie cutter** = Class (blueprint)
- **Cookie** = Object (actual thing)
- **Cookie color** = Attribute (property)
- **Eating cookie** = Method (action)

### Remember `self`
Think: "**SELF** refers to the specific object **ITSELF**"

### Constructor Remember
`__init__` = "**Initialize** the object"

## 🔧 Testing Your Classes

### Basic Test Template
```python
def test_class():
    # Create object
    obj = ClassName("test_value")
    
    # Test getter
    assert obj.get_attribute() == "test_value"
    
    # Test setter
    obj.set_attribute("new_value")
    assert obj.get_attribute() == "new_value"
    
    print("All tests passed!")
```

## 📚 Next Steps

1. **Master Basic Classes**
   - Practice with different class examples
   - Understand `self` thoroughly
   - Get comfortable with constructors

2. **Learn Advanced Features**
   - Special methods (`__str__`, `__len__`, etc.)
   - Property decorators
   - Class vs instance variables

3. **Apply to Data Structures**
   - Implement LinkedList class
   - Create Stack and Queue classes
   - Build Tree structures

4. **Study Design Patterns**
   - Learn common class patterns
   - Understand inheritance
   - Explore composition

## 🏃‍♂️ Quick Practice Exercises

### 5-Minute Exercise
Create a `Car` class with:
- Attributes: make, model, year
- Methods: start_engine(), stop_engine(), get_info()

### 10-Minute Exercise
Create a `BankAccount` class with:
- Attributes: account_number, balance, owner
- Methods: deposit(), withdraw(), get_balance()
- Validation: prevent negative balance

### 15-Minute Exercise
Create a `Playlist` class with:
- Attributes: name, songs (list)
- Methods: add_song(), remove_song(), play_all(), shuffle()

## 🆘 Debugging Tips

### Check These First
1. Did you include `self` in method definitions?
2. Are you calling methods on an instance, not the class?
3. Did you initialize attributes in `__init__`?
4. Are you using correct indentation?

### Print Debug Information
```python
def debug_object(self):
    print(f"Object type: {type(self)}")
    print(f"Attributes: {self.__dict__}")
```

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

*Keep this reference handy while learning data structures!*
