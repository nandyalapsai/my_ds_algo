# O(n²) - Quadratic Time Complexity

## 📚 Overview
O(n²) represents **quadratic time complexity**, where the number of operations grows proportionally to the square of the input size. This occurs when we have **nested loops** where both loops depend on the input size.

---

## 🔍 Key Concept: Nested Loops

### What Creates O(n²)?
- **One loop inside another loop** (nested loops)
- Both loops iterate through the same input size `n`
- Total operations = n × n = n²

### Code Example from Video:
```javascript
function printPairs(n) {
    for (let i = 0; i < n; i++) {        // Outer loop: n iterations
        for (let j = 0; j < n; j++) {    // Inner loop: n iterations for each i
            console.log(i, j);
        }
    }
}

printPairs(10);  // Prints pairs from (0,0) to (9,9) = 100 total outputs
```

### Execution Breakdown:
- **Input**: n = 10
- **Output**: 100 pairs (0,0), (0,1), ..., (9,9)
- **Total operations**: 10 × 10 = 100 = n²

---

## 📊 Time Complexity Analysis

### Growth Pattern:
| Input Size (n) | Operations (n²) | Growth Factor |
|----------------|-----------------|---------------|
| 1              | 1               | -             |
| 2              | 4               | 4x            |
| 5              | 25              | 6.25x         |
| 10             | 100             | 4x            |
| 100            | 10,000          | 100x          |
| 1,000          | 1,000,000       | 100x          |

### Visual Representation:
```
Operations vs Input Size

     |
10k  |         ●  O(n²)
     |       ╱
     |     ╱
 1k  |   ╱
     | ╱
100  |╱
     |    ● O(n)
  10 |  ╱
     |╱
   1 |●────●────●────●────●
     +─────────────────────
     1   10   20   30   40  (Input Size)
```

---

## 🎯 Real-World Examples

### 1. **Comparing All Pairs**
```javascript
// Find all pairs of students for group projects
function findAllPairs(students) {
    const pairs = [];
    for (let i = 0; i < students.length; i++) {
        for (let j = i + 1; j < students.length; j++) {
            pairs.push([students[i], students[j]]);
        }
    }
    return pairs;
}
// Time Complexity: O(n²)
```

### 2. **Bubble Sort Algorithm**
```javascript
function bubbleSort(arr) {
    for (let i = 0; i < arr.length; i++) {           // Outer loop
        for (let j = 0; j < arr.length - i - 1; j++) { // Inner loop
            if (arr[j] > arr[j + 1]) {
                // Swap elements
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
            }
        }
    }
    return arr;
}
// Time Complexity: O(n²)
```

### 3. **Matrix Operations**
```javascript
// Multiply two n×n matrices
function matrixMultiply(A, B) {
    const result = [];
    for (let i = 0; i < A.length; i++) {
        result[i] = [];
        for (let j = 0; j < B[0].length; j++) {
            result[i][j] = 0;
            for (let k = 0; k < A[0].length; k++) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    return result;
}
// Time Complexity: O(n³) - even worse!
```

---

## 📈 Comparison with Other Complexities

### Efficiency Ranking (Best to Worst):
```
O(1)     Constant   ■
O(log n) Logarithmic ■■
O(n)     Linear      ■■■■■
O(n²)    Quadratic   ■■■■■■■■■■■■■■■■■■■■■■■■■
O(2ⁿ)    Exponential ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
```

### Performance Impact:
- **O(n)**: If n doubles, operations double
- **O(n²)**: If n doubles, operations quadruple!

---

## ⚠️ When to Avoid O(n²)

### Problems with Quadratic Complexity:
1. **Scalability Issues**: Becomes extremely slow with large datasets
2. **Resource Intensive**: Uses excessive CPU time and memory
3. **User Experience**: Causes noticeable delays in applications

### Example Impact:
- **1,000 items**: 1 million operations
- **10,000 items**: 100 million operations
- **100,000 items**: 10 billion operations! ⚡

---

## 🔧 Optimization Strategies

### 1. **Use Better Algorithms**
```javascript
// Instead of O(n²) search:
function findInArray(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            if (arr[i] + arr[j] === target) return true;
        }
    }
}

// Use O(n) with hash map:
function findInArrayOptimized(arr, target) {
    const seen = new Set();
    for (let num of arr) {
        if (seen.has(target - num)) return true;
        seen.add(num);
    }
    return false;
}
```

### 2. **Break Early When Possible**
```javascript
function findDuplicate(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[i] === arr[j]) {
                return arr[i];  // Exit early!
            }
        }
    }
    return null;
}
```

---

## 🧠 Key Takeaways

### ✅ Remember:
- **Nested loops** typically create O(n²) complexity
- Performance degrades **rapidly** as input size increases
- Always consider **alternative algorithms** for large datasets
- O(n²) is **much less efficient** than O(n)

### 🚨 Red Flags:
- Two nested loops iterating over the same data
- Comparing every element with every other element
- Algorithms that don't scale well

### 💡 Best Practices:
- Profile your code with large inputs
- Look for opportunities to use hash maps, sorting, or other techniques
- Consider if the nested loop is truly necessary
- Sometimes O(n log n) sorting + O(n) processing beats O(n²)

---

## 📝 Practice Problems

1. **Identify the time complexity** of algorithms with nested loops
2. **Optimize bubble sort** using early termination
3. **Find alternatives** to brute force O(n²) solutions
4. **Implement two-pointer technique** to reduce O(n²) to O(n)

---

*Next Topic: [Drop Non-Dominant Terms](06_drop_non_dominant_terms.md)*
*Previous Topic: [Drop Constants Rule](04_drop_constants_rule.md)*
