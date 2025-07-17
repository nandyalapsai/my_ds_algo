"""
Classes and Data Structures - Code Examples
===========================================

This file contains all the working code examples from the video transcript
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
    
    def display_structure(self):
        """Display the structure and methods of the LinkedList class."""
        print("\nLinkedList Class Structure:")
        print("├── Constructor: __init__()")
        print("├── append(value)")
        print("├── prepend(value)")
        print("├── insert(index, value)")
        print("├── remove(value)")
        print("└── pop()")


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


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Run the cookie class demonstration
    demonstrate_cookie_class()
    
    # Show linked list structure
    print("\n" + "=" * 50)
    print("LINKED LIST CLASS TEMPLATE")
    print("=" * 50)
    
    # Create a linked list instance
    my_list = LinkedList()
    my_list.display_structure()
    
    # Demonstrate method calls (template only)
    print("\nMethod call examples:")
    my_list.append("first")
    my_list.prepend("zero")
    my_list.insert(1, "middle")
    my_list.remove("first")
    my_list.pop()
    
    # Run student class demonstration
    demonstrate_student_class()
    
    print("\n" + "=" * 50)
    print("KEY CONCEPTS SUMMARY")
    print("=" * 50)
    print("✓ Classes are blueprints for creating objects")
    print("✓ Constructor (__init__) initializes new instances")
    print("✓ 'self' refers to the current instance")
    print("✓ Methods are functions that belong to a class")
    print("✓ Each instance maintains its own state")
    print("✓ Classes enable building complex data structures")
