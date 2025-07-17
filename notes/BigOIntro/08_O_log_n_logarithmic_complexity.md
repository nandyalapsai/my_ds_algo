# 08. O(log n) - Logarithmic Time Complexity

## 📚 Overview
O(log n) represents logarithmic time complexity, one of the most efficient time complexities for search algorithms. It's characterized by cutting the problem size in half with each operation.

## 🎯 Key Concept: Binary Search Demonstration

### The Setup
- **Data Structure**: Sorted list with elements [1, 2, 3, 4, 5, 6, 7, 8]
- **Goal**: Find the number 1
- **Requirement**: Data MUST be sorted for this approach to work

### Step-by-Step Process

```
Initial List: [1, 2, 3, 4, 5, 6, 7, 8]
                    ↑
               Middle point

Step 1: Cut in half
Left Half:  [1, 2, 3, 4]
Right Half: [5, 6, 7, 8]
Decision: Target (1) is NOT in right half → Remove right half

Step 2: Cut remaining half
Remaining: [1, 2, 3, 4]
Left Half:  [1, 2]
Right Half: [3, 4]
Decision: Target (1) is NOT in right half → Remove right half

Step 3: Cut remaining half
Remaining: [1, 2]
Left Half:  [1]
Right Half: [2]
Decision: Found target (1) in left half!
```

### Visual Representation

```
┌─────────────────────────────────────┐
│  Original: [1,2,3,4,5,6,7,8]        │ 8 items
└─────────────────────────────────────┘
                   │
                   ▼ (divide by 2)
┌─────────────────┐
│  [1,2,3,4]      │                     4 items
└─────────────────┘
        │
        ▼ (divide by 2)
┌───────┐
│ [1,2] │                               2 items
└───────┘
    │
    ▼ (divide by 2)
┌───┐
│[1]│                                   1 item (FOUND!)
└───┘
```

## 🧮 Mathematical Foundation

### Logarithm Relationship
- **Exponential form**: 2³ = 8
- **Logarithmic form**: log₂(8) = 3

This means: "2 to what power equals 8?" Answer: 3

### Real-World Power of Logarithms

| List Size | Linear Search (O(n)) | Binary Search (O(log n)) |
|-----------|---------------------|---------------------------|
| 8 items   | Up to 8 operations  | 3 operations             |
| 1,000     | Up to 1,000 ops     | ~10 operations           |
| 1,000,000 | Up to 1M ops        | ~20 operations           |
| 1 billion | Up to 1B ops        | 31 operations            |

### Calculation Example
For 1,073,741,824 (over 1 billion):
- log₂(1,073,741,824) = 31
- This means cutting the list in half 31 times gets you to 1 item

## 📊 Complexity Comparison Graph

```
Performance Chart (Operations vs Input Size)

Operations
    ↑
1000│                                    ●  O(n²)
    │                               ●
 800│                          ●
    │                     ●
 600│                ●
    │           ●
 400│      ●
    │ ●
 200│●                          ●────────●  O(n)
    │                      ●
 100│               ●
    │          ●
  50│     ●
    │●
   0└●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●──────────→ Input Size (n)
    0  100  200  300  400  500  600  700  800
    
    ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●  O(log n) - Nearly flat!
    ●  O(1) - Completely flat
```

## 🔍 Binary Search Algorithm

### Pseudocode
```
ALGORITHM BinarySearch(array, target):
    left = 0
    right = length(array) - 1
    
    WHILE left ≤ right:
        middle = (left + right) / 2
        
        IF array[middle] = target:
            RETURN middle
        ELSE IF array[middle] < target:
            left = middle + 1
        ELSE:
            right = middle - 1
    
    RETURN -1  // Not found
```

### Time Complexity Analysis
- **Best Case**: O(1) - Target is at the middle
- **Average Case**: O(log n) - Target found after log n divisions
- **Worst Case**: O(log n) - Target at beginning/end or not present

### Space Complexity
- **Iterative**: O(1) - Only using a few variables
- **Recursive**: O(log n) - Due to call stack depth

## 🏆 Efficiency Rankings

From most to least efficient:

1. **O(1)** - Constant Time ⭐⭐⭐⭐⭐
2. **O(log n)** - Logarithmic Time ⭐⭐⭐⭐
3. **O(n)** - Linear Time ⭐⭐⭐
4. **O(n log n)** - Linearithmic Time ⭐⭐
5. **O(n²)** - Quadratic Time ⭐

## 🔄 O(n log n) - Linearithmic Complexity

### Usage in Sorting Algorithms
- **Merge Sort**: O(n log n) in all cases
- **Quick Sort**: O(n log n) average case
- **Heap Sort**: O(n log n) in all cases

### Why O(n log n) for Optimal Sorting?
- Most efficient possible for comparison-based sorting of general data
- Some specialized sorting algorithms for numbers can be faster
- For sorting strings and mixed data types, O(n log n) is optimal

### Sorting Complexity Comparison
```
Sorting Algorithm    | Best Case | Average Case | Worst Case
--------------------|-----------|--------------|------------
Bubble Sort         | O(n)      | O(n²)        | O(n²)
Selection Sort      | O(n²)     | O(n²)        | O(n²)
Insertion Sort      | O(n)      | O(n²)        | O(n²)
Merge Sort          | O(n log n)| O(n log n)   | O(n log n)
Quick Sort          | O(n log n)| O(n log n)   | O(n²)
Heap Sort           | O(n log n)| O(n log n)   | O(n log n)
```

## 🎯 Real-World Applications

### Where O(log n) Appears:
1. **Binary Search Trees** - Search, insert, delete operations
2. **Database Indexing** - B-trees and B+ trees
3. **File Systems** - Directory lookups
4. **Network Routing** - IP address lookups
5. **Game Development** - Spatial partitioning (Quadtrees, Octrees)

### Requirements for O(log n):
- Data must be **sorted** or **organized** in a specific structure
- Must be able to **eliminate half** the search space each step
- **Random access** to data elements (like arrays)

## 📝 Key Takeaways

1. **O(log n) is extremely efficient** for large datasets
2. **Requires sorted data** for binary search
3. **Scales beautifully** - billion items → 31 operations
4. **Foundation for many advanced algorithms** and data structures
5. **O(n log n) is optimal** for general-purpose sorting
6. **Trade-off**: Efficiency for preprocessing (sorting) requirement

## 🔗 Next Topics Preview
- Binary Search Trees (BST)
- Balanced Trees (AVL, Red-Black)
- Heap Data Structure
- Advanced Sorting Algorithms

---
*"The power of logarithmic complexity lies in its ability to handle massive datasets with remarkably few operations."*
