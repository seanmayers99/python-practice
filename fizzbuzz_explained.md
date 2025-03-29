# 🔁 FizzBuzz Explained – Python Coding Challenge

This markdown document walks through the FizzBuzz challenge in Python, explaining the logic, code, and reasoning behind the approach.

---

## ✅ Problem Statement

Print the numbers from 1 to 100:
- For multiples of 3, print `"Fizz"`
- For multiples of 5, print `"Buzz"`
- For numbers divisible by both 3 and 5, print `"FizzBuzz"`

---

## 🧠 Python Code with Comments

```python
def fizzbuzz():
    """
    Prints numbers from 1 to 100 with:
    - 'Fizz' for multiples of 3
    - 'Buzz' for multiples of 5
    - 'FizzBuzz' for multiples of both
    """
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Run the function
fizzbuzz()
