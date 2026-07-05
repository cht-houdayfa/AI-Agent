# Hello World Program in Python
def hello_world():
    """
    This function returns the string 'Hello, World!' when called.
    
    Example Usage: 
        `print(hello_world())` would print `'Hello, World!'` to the console.
    """
    return "Hello, World!"
```

```python
# Calculator Application in Python
def add(x, y):
    """
    This function takes two numbers as arguments and returns their sum when called.
    
    Example Usage: 
        `print(add(5,3))` would print `8` to the console.
    """
    return x + y

def subtract(x, y):
    """
    This function takes two numbers as arguments and returns the difference of the first from the second when called.
    
    Example Usage: 
        `print(subtract(5,3))` would print `2` to the console.
    """
    return x - y

def multiply(x, y):
    """
    This function takes two numbers as arguments and returns their product when called.
    
    Example Usage: 
        `print(multiply(5,3))` would print `15` to the console.
    """
    return x * y

def divide(x, y):
    """
    This function takes two numbers as arguments and returns their division result when called. It checks if the divisor is not zero before performing division. If it's zero, it returns a message indicating that division by zero is not allowed.
    
    Example Usage: 
        `print(divide(6,3))` would print `2` to the console.
        `print(divide(5,0))` would print `"لا يمكن المزده على صفر"` to the console.
    """
    if y != 0:
        return x / y
    else:
        return "لا يمكن المزده على صفر"