
# 🔁 Deep Dive: Reversing a String Using a Backward Loop in Python

This document explains the logic behind reversing a string manually in Python using a loop that moves backwards through the string. It includes a step-by-step breakdown and annotated code.

---

## 🔍 Problem Statement

Write a function that takes a string as input and returns the reversed string.  
**Do not use slicing (`[::-1]`) or built-in `reversed()` functions.**

---

## ✅ Python Code with Comments

```python
def reverse_string(word):
    reversed_str = ""  # Start with an empty string to build the result

    for i in range(len(word) - 1, -1, -1):  # Loop backwards from the last index to 0
        reversed_str += word[i]  # Add the character at the current index to the result

    return reversed_str  # Return the reversed string
```

---

## 🧠 How the Loop Works

We use Python's `range()` function:

```python
range(start, stop_before, step)
```

- `start = len(word) - 1`: Start at the **last index**
- `stop_before = -1`: Stop **before** -1 (so we include index 0)
- `step = -1`: Move **one step backwards**

---

## 🧪 Example: Reverse the String `"Sean"`

String and its indices:
```
'S' → index 0  
'e' → index 1  
'a' → index 2  
'n' → index 3
```

Our loop:
```python
for i in range(3, -1, -1)
```

The values of `i` will be:
```
3 → 2 → 1 → 0
```

Characters accessed:
```
'n' → 'a' → 'e' → 'S'
```

Result: `'naeS'`

---

## 🧠 Key Takeaways

- Strings are **immutable** — we build a new one
- We loop **backward** using `range(start, stop, step)`
- Understanding this logic is great for interviews and shows comfort with indexing

---
