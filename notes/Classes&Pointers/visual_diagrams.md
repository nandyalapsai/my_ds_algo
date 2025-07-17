# Visual Diagrams for Classes & Data Structures

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

## Class vs Built-in Types Comparison

```
    Built-in Types              Custom Classes
    ┌─────────────────┐        ┌─────────────────┐
    │      int        │        │     Cookie      │
    │ ─────────────── │        │ ─────────────── │
    │ x = 5           │   VS   │ c = Cookie("red")│
    │                 │        │                 │
    │ Methods:        │        │ Methods:        │
    │ • __add__()     │        │ • __init__()    │
    │ • __str__()     │        │ • get_color()   │
    │ • __mul__()     │        │ • set_color()   │
    │ • etc.          │        │ • etc.          │
    └─────────────────┘        └─────────────────┘
           │                           │
           ▼                           ▼
    ┌─────────────────┐        ┌─────────────────┐
    │ Predefined by   │        │ Defined by YOU  │
    │ Python language │        │ Custom behavior │
    └─────────────────┘        └─────────────────┘
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

## Time Complexity Comparison

```
    Cookie Class Operations:
    ┌─────────────────┬─────────────┬─────────────────┐
    │ Operation       │ Time        │ Space           │
    ├─────────────────┼─────────────┼─────────────────┤
    │ Create object   │ O(1)        │ O(1)            │
    │ Get attribute   │ O(1)        │ O(1)            │
    │ Set attribute   │ O(1)        │ O(1)            │
    │ Call method     │ O(1)*       │ O(1)            │
    └─────────────────┴─────────────┴─────────────────┘
    * Depends on method implementation
    
    Future Data Structure Operations:
    ┌─────────────────┬─────────────┬─────────────────┐
    │ LinkedList Op   │ Time        │ Space           │
    ├─────────────────┼─────────────┼─────────────────┤
    │ append()        │ O(1)        │ O(1)            │
    │ prepend()       │ O(1)        │ O(1)            │
    │ insert(index)   │ O(n)        │ O(1)            │
    │ remove(value)   │ O(n)        │ O(1)            │
    │ search(value)   │ O(n)        │ O(1)            │
    └─────────────────┴─────────────┴─────────────────┘
```
