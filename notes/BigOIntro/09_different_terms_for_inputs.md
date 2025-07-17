# 09 - Different Terms for Inputs (Big O Gotcha)

## 📋 Overview
A common interview gotcha question where functions with multiple parameters require different Big O analysis than single-parameter functions.

## 🎯 Key Concept
**Rule**: When a function has multiple input parameters, you **cannot** combine them into a single variable in Big O notation.

---

## 🔍 Single Parameter vs Multiple Parameters

### Single Parameter Function
```javascript
function example(n) {
    // First loop
    for (let i = 0; i < n; i++) {
        console.log(i);
    }
    
    // Second loop  
    for (let j = 0; j < n; j++) {
        console.log(j);
    }
}
```

**Analysis:**
- First loop: O(n)
- Second loop: O(n)
- Combined: O(n + n) = O(2n)
- **After dropping constants**: O(n)

### Multiple Parameters Function
```javascript
function example(a, b) {
    // First loop runs 'a' times
    for (let i = 0; i < a; i++) {
        console.log(i);
    }
    
    // Second loop runs 'b' times
    for (let j = 0; j < b; j++) {
        console.log(j);
    }
}
```

**Analysis:**
- First loop: O(a)
- Second loop: O(b)
- Combined: O(a + b)
- **Cannot simplify further** ❌

---

## 🚫 Common Mistake

### ❌ WRONG Approach
```
"Oh, it's just two loops, so it's O(n + n) = O(2n) = O(n)"
```

### ✅ CORRECT Approach
```
"First loop is O(a), second loop is O(b), total is O(a + b)"
```

**Why the mistake happens:**
- Students assume a = n and b = n
- But a and b are **independent variables**
- They could have completely different values

---

## 📊 Visual Representation

```
Single Parameter (n):
┌─────────────┐    ┌─────────────┐
│   Loop 1    │ +  │   Loop 2    │  = O(2n) → O(n)
│   O(n)      │    │   O(n)      │
└─────────────┘    └─────────────┘

Multiple Parameters (a, b):
┌─────────────┐    ┌─────────────┐
│   Loop 1    │ +  │   Loop 2    │  = O(a + b)
│   O(a)      │    │   O(b)      │
└─────────────┘    └─────────────┘
                   ↑
            Cannot simplify further!
```

---

## 🔄 Nested Loops with Different Terms

### Code Example
```javascript
function nestedExample(a, b) {
    for (let i = 0; i < a; i++) {
        for (let j = 0; j < b; j++) {
            console.log(i, j);
        }
    }
}
```

**Analysis:**
- Outer loop runs `a` times
- Inner loop runs `b` times for each iteration of outer loop
- Total operations: a × b
- **Time Complexity: O(a × b)**

---

## 🌍 Real-World Examples

### Example 1: Processing Two Arrays
```javascript
function processArrays(arrayA, arrayB) {
    // Process first array
    for (let item of arrayA) {
        process(item);           // O(a) where a = arrayA.length
    }
    
    // Process second array
    for (let item of arrayB) {
        process(item);           // O(b) where b = arrayB.length
    }
}
// Time Complexity: O(a + b)
```

### Example 2: Matrix Operations
```javascript
function printMatrix(rows, cols) {
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            console.log(`Cell [${i}][${j}]`);
        }
    }
}
// Time Complexity: O(rows × cols)
```

### Example 3: Search in Multiple Databases
```javascript
function searchMultipleDBs(users, products) {
    // Search users database
    for (let user of users) {
        if (user.id === targetId) return user;    // O(u)
    }
    
    // Search products database  
    for (let product of products) {
        if (product.id === targetId) return product;  // O(p)
    }
}
// Time Complexity: O(u + p)
```

---

## 📈 Complexity Comparison Table

| Scenario | Single Parameter | Multiple Parameters |
|----------|------------------|-------------------|
| Sequential Loops | O(n + n) = O(n) | O(a + b) |
| Nested Loops | O(n²) | O(a × b) |
| Three Loops | O(n + n + n) = O(n) | O(a + b + c) |
| Triple Nested | O(n³) | O(a × b × c) |

---

## 🎯 Interview Tips

### Questions to Ask Yourself:
1. **How many input parameters does the function have?**
2. **Are the parameters independent or related?**
3. **Can I assume they're the same size?**

### Red Flags in Interview:
- Function signature: `func(array1, array2)` 
- Two separate data structures
- Different loop bounds using different variables

### Safe Assumptions:
- **Never assume** different parameters are equal
- **Always express** complexity in terms of actual parameters
- **Ask interviewer** if parameters are related

---

## 🧠 Memory Aid

**"Different Doors, Different Keys"**
- Each parameter is like a different door
- Each needs its own key (variable) in Big O
- Can't use one key for multiple doors

---

## 💡 Practice Problems

### Problem 1
```javascript
function mystery(x, y, z) {
    for (let i = 0; i < x; i++) {
        console.log(i);
    }
    
    for (let j = 0; j < y; j++) {
        for (let k = 0; k < z; k++) {
            console.log(j, k);
        }
    }
}
```
**Answer**: O(x + y × z)

### Problem 2
```javascript
function process(arr1, arr2) {
    arr1.forEach(item1 => {
        arr2.forEach(item2 => {
            if (item1 === item2) {
                console.log("Match found");
            }
        });
    });
}
```
**Answer**: O(n × m) where n = arr1.length, m = arr2.length

---

## 🔗 Related Concepts
- [Drop Constants Rule](04_drop_constants_rule.md)
- [Time Complexity Analysis](02_time_space_complexity_analysis.md)
- [O(n²) Quadratic Complexity](05_O_n_squared_quadratic_complexity.md)

---

## ✅ Key Takeaways

1. **Multiple parameters = Multiple variables in Big O**
2. **Cannot combine different input terms**
3. **Sequential operations: O(a + b)**
4. **Nested operations: O(a × b)**
5. **Always be explicit about parameter relationships**

---

*Remember: In interviews, when you see multiple parameters, resist the urge to simplify to O(n). Keep them separate!*
