sparkle
You've been using functions like print(), len(), and range(). Now it's time to create your own. Functions let you write code once and use it many times. They make your code organized, readable, and easier to test.


The Quick Version
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
greet("Bob")    # Hello, Bob!
def defines a function. The code inside runs when you call the function.

sparkle
Basic Function Structure
def function_name():
    # Code goes here
    print("This is a function")

# Call the function
function_name()



Key parts:

def keyword starts the definition

Function name (follows same rules as variables)

Parentheses () (may contain parameters)

Colon : ends the definition line

Indented body (the code that runs)

sparkle
Functions Without Parameters
The simplest functions take no input:

def say_hello():
    print("Hello, world!")

def print_separator():
    print("-" * 40)

# Use them
say_hello()        # Hello, world!
print_separator()  # ----------------------------------------
sparkle
Functions With Parameters
Most functions need input to be useful:

def greet(name):
    print(f"Hello, {name}!")

def square(number):
    print(number ** 2)

greet("Alice")  # Hello, Alice!
square(5)       # 25


Parameters are variables that receive values when the function is called.

sparkle
Multiple Parameters
def greet_formally(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

def add(a, b):
    print(a + b)

greet_formally("Alice", "Smith")  # Hello, Alice Smith!
add(3, 5)                         # 8


Parameters are separated by commas.

sparkle
Question: What does this print?

def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Go!")

countdown(3)
sparkle
Answer:

3 
2
1
Go!
The function receives n=3, then counts down. The parameter n is local to the function changing it doesn't affect anything outside.

sparkle
Function Naming Conventions
Python uses snake_case for function names:


# Good
def calculate_total():
    pass

def send_welcome_email():
    pass

def get_user_by_id():
    pass

# Not Pythonic
def CalculateTotal():    # This is class naming style
def calculateTotal():    # This is JavaScript style
Use verbs that describe what the function does: get_, set_, calculate_, send_, process_, validate_.

sparkle
Docstrings - Documenting Functions

Add documentation with a docstring:

def calculate_area(width, height):
    """
    Calculate the area of a rectangle.

    Args:
        width: The width of the rectangle
        height: The height of the rectangle

    Returns:
        The area (width * height)
    """
    return width * height


Docstrings appear when you use help(calculate_area) and in IDE tooltips.

sparkle
Functions Are Objects
In Python, functions are objects you can assign them to variables:

def shout(text):
    return text.upper()

# Assign function to variable (no parentheses)
yell = shout

# Call through the new name
print(yell("hello"))  # HELLO

# Pass functions to other functions
def apply_twice(func, value):
    return func(func(value))

print(apply_twice(shout, "hi"))  # HI (already uppercase)
This becomes useful with sorting, filtering, and callbacks.

sparkle
Quick Practice
tick
2 correct
cross
1 incorrect
chevron
Q1.
What's wrong with this function definition?

def greet(name)
    print(f"Hello, {name}!")
Missing return statement
tick
Missing colon after the parameter list
name should be in quotes
Should use function instead of def
Q2.
Which is the most Pythonic function name for a function that validates an email address?

ValidateEmail
validateEmail
tick
validate_email
VALIDATE_EMAIL
Q3.
What happens when you write my_func without parentheses?

def my_func():
    print("Running!")

result = my_func
The function runs and result gets None
result becomes a reference to the function object
tick
Error - functions must be called with parentheses
result becomes the string "my_func"
sparkle
Where You'll Use This in Django
Django is built around functions (and classes). Views are functions:

# views.py
def home(request):
    """Display the home page."""
    return render(request, 'home.html')

def user_profile(request, user_id):
    """Display a user's profile."""
    user = get_object_or_404(User, id=user_id)
    return render(request, 'profile.html', {'user': user})

def api_status(request):
    """Return API health status as JSON."""
    return JsonResponse({'status': 'healthy'})


Helper functions keep your code DRY (Don't Repeat Yourself):

# utils.py
def format_currency(amount):
    """Format a number as currency."""
    return f"${amount:,.2f}"

def send_notification(user, message):
    """Send a notification to a user."""
    Notification.objects.create(user=user, message=message)
    # Could also send email, push notification, etc.

# views.py
def checkout(request):
    total = calculate_total(request.user.cart)
    send_notification(request.user, f"Order placed: {format_currency(total)}")
    ...
Quick Recap
def function_name(): defines a function

Parameters go inside the parentheses

Don't forget the colon : after the definition

Use snake_case for function names

Docstrings document what functions do

Functions are objects - you can assign and pass them