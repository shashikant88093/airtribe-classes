
# sparkle
# Adding attributes after creating an object works, but it's fragile. What if you forget to set one? What if different parts of your code set them differently? The __init__ method solves this by guaranteeing that every object starts with the right data


# The Quick Version
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

user = User("Alice", "alice@example.com")
print(user.name)   # Alice
print(user.email)  # alice@example.com
# __init__ runs automatically when you create an object.

# sparkle
# The init Method
# __init__ (short for "initialize") is a special method that runs when an object is created:

class User:
    def __init__(self):
        print("A new user was created!")

user = User()  # Prints: A new user was created!


# The double underscores indicate it's a special Python method (called "dunder" methods).

# sparkle
# The self Parameter
# Every method in a class receives self as its first parameter:

class User:
    def __init__(self):
        print(self)  # The object being created

user = User()  # Prints: <__main__.User object at 0x...>

# self refers to the specific instance being created or used. Python passes it automatically you don't include it when calling.

# sparkle
# Setting Instance Attributes
# Use self to attach attributes to the object:

class User:
    def __init__(self, name, email):
        self.name = name    # Attach 'name' to this instance
        self.email = email  # Attach 'email' to this instance

user = User("Alice", "alice@example.com")
print(user.name)   # Alice
print(user.email)  # alice@example.com
# Now every User object is guaranteed to have name and email.

# sparkle
# Passing Arguments to init
# Arguments go in the parentheses when creating an object:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(10, 5)  # width=10, height=5
print(rect.width)   # 10
print(rect.height)  # 5
# sparkle
# Pause and Think
# Question: What does this print?

class Counter:
    def __init__(self, start=0):
        self.value = start

c1 = Counter()
c2 = Counter(10)

print(c1.value, c2.value)
# sparkle
# Answer:

# 0 10 
# c1 uses the default value (start=0), so c1.value is 0. c2 passes 10, so c2.value is 10. Default parameters work in __init__ just like regular functions.

# sparkle
# Required vs Optional Attributes
# Use default values for optional attributes:

class User:
    def __init__(self, name, email, role="user"):
        self.name = name
        self.email = email
        self.role = role

# Required: name, email. Optional: role
user1 = User("Alice", "alice@example.com")
user2 = User("Bob", "bob@example.com", "admin")

print(user1.role)  # user (default)
print(user2.role)  # admin
# sparkle
# Instance Attributes vs Class Attributes
# Instance attributes: Belong to a specific object (set in __init__ with self.)

# Class attributes: Shared by all instances (defined in the class body)

class User:
    # Class attribute — shared by all instances
    species = "human"

    def __init__(self, name):
        # Instance attribute — unique to each instance
        self.name = name

user1 = User("Alice")
user2 = User("Bob")

# Instance attributes are unique
print(user1.name)  # Alice
print(user2.name)  # Bob

# Class attributes are shared
print(user1.species)  # human
print(user2.species)  # human
print(User.species)   # human


# sparkle
# When to Use Each
# Instance attributes (most common):

# Data that varies between objects

# User name, email, age

# Order total, items, date

# Class attributes (less common):

# Constants shared by all instances

# Default values

# Counters for all instances

class User:
    # Class attribute — count all users
    total_users = 0

    def __init__(self, name):
        self.name = name          # Instance attribute
        User.total_users += 1     # Update class attribute

user1 = User("Alice")
user2 = User("Bob")
print(User.total_users)  # 2
# sparkle
# Computing Attributes
# You can compute values in __init__:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height  # Computed

rect = Rectangle(10, 5)
print(rect.area)  # 50
# Note: This area is computed once at creation. If width changes later, area won't update automatically. (We'll see better approaches with methods and properties.)

# sparkle
# Quick Practice
# tick
# 1 correct
# cross
# 2 incorrect
# chevron
# Q1.
# What does self refer to inside a method?

# tick
# The class itself
# The specific instance the method was called on
# The parent class
# The __init__ method
# Q2.
# What happens if you create a User without passing the required arguments?

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

user = User()  # ???
# tick
# User is created with empty name and email
# User is created with None values
# TypeError - missing required arguments
# User is created normally
# Q3.
# What is the difference between self.name = name and name = name in a Python class?

# No difference
# tick
# self.name attaches to the instance; name is just a local variable
# name = name is more efficient
# self.name causes an error
# Where You'll Use This in Django
# Django models use __init__ behind the scenes, but you'll override it for custom initialization:

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call parent's __init__
        # Custom initialization
        self._word_count = None  # Cached value

# More commonly, you'll work with model instances:
article = Article(
    title="Hello World",
    slug="hello-world",
    content="This is my article..."
)


# Forms use __init__ for customization:


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email


# Custom managers and mixins:

class TimestampMixin:
    """Add created_at tracking to any class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = timezone.now()
sparkle
# Ask AI guide
# Explain Django models
# Customize forms with __init__
# Use custom managers
# Add mixins to classes

# Continue