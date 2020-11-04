# Creating a greetings function

# Syntax def name_of_function():
# Each function has a block of code to execute to ideally run one task
# Note: We can assign variables to functions e.g. a = add(5, 7) and a = 12 forever more

def greeting(name):
    print(f"Welcome on board {name}, hope you'll enjoy the ride")
# If we execute this program now it would display nothing as we have not called this function

# Syntax to call a function:
greeting('Matt')

# Creating a function that adds 2 arguments to eachother
def add(num1, num2):
    print(num1 + num2)

add(1, 2)

# Creating a function that subtracts 2 arguments from eachother
def subtract(arg1, arg2):
    print(arg1 - arg2)

subtract(72, 50)


# Task
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

# Can also use return() instead of print() which returns the answer as a value to be used

print(multiply(5, 10))
print(divide(33, 11))
print(percent(27, 932))
print(power(3, 3))