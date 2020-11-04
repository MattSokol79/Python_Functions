# Day 3 - Functions
## Objectives:
- What are functions and why are they useful
- How to create a function
- Industry function best practices

**What are functions and why we use them:**
- DRY: Dont, Repeat, Yourself

**Functions**
```python
# Creating a greetings function

# Syntax def name_of_function():
# Each function has a block of code to execute to ideally run one task
# Note: We can assign variables to functions e.g. a = add(5, 7) and a = 12 forever more

def greeting(name):
    print(f"Welcome on board {name}, hope you'll enjoy the ride")
# If we execute this program now it would display nothing as we have not called this function

# Syntax to call a function:
greeting('Matt')
```
### Create simple functions
```python
# Creating a function that adds 2 arguments to eachother
def add(num1, num2):
    print(num1 + num2)

add(1, 2)

# Creating a function that subtracts 2 arguments from eachother
def subtract(arg1, arg2):
    print(arg1 - arg2)

subtract(72, 50)
```
### Task
```python
# Create a function to *
# Create a function to /
# Create a function to %
# Create a function to **

def multiply(arg1, arg2):
    return arg1 * arg2

def divide(arg1, arg2):
    return arg1 / arg2

def percent(arg1, arg2):
    # To get percentage of arg1 in arg2
    percent = (arg1 / arg2) * 100
    return percent

def power(arg1, arg2):
    # Where arg1 is the number and arg2 is the power
    return arg1**arg2

def modulus(arg1, arg2):
    return arg1 % arg2

# Can also use return() instead of print() which returns the answer of the function

print(multiply(5, 10))
print(divide(33, 11))
print(percent(27, 932))
print(power(3, 3))
print(modulus(19,2))
```

### Best Practices
- Best practice is to have a small block
of code in any function that does 1 job.
- Pseudocode where required to explain
what the code is doing, usually 1 line.
- HINTs: create hints in simple bullet 
points or pointers
- Comments regarding your function results
at the end are also acceptable. This means
you dont necessarily need huge amounts
of pseudocoding