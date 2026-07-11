# Functions That Belong to Objects
# Objects have data (attributes). But real objects also do things. A User can log in. An Order can calculate its total. A Rectangle can compute its area. Methods are functions defined inside a class that give objects behavior.

# The Quick Version
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}"

user = User("Alice")
print(user.greet())  # Hello, I'm Alice
# Methods are functions that have access to self the object's data.


# Defining Methods
# Methods are just functions inside a class:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(10, 5)
print(rect.area())       # 50
print(rect.perimeter())  # 30
# Every method takes self as its first parameter.



# Methods Access Instance Data
# self gives methods access to the object's attributes:

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # 150

account.withdraw(30)
print(account.get_balance())  # 120




class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def is_square(self):
        return self.width == self.height

    def describe(self):
        shape = "square" if self.is_square() else "rectangle"
        return f"A {shape} with area {self.area()}"

rect = Rectangle(5, 5)
print(rect.describe())  # A square with area 25



# Pause and Think
# Question: What does this print?

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self

    def get(self):
        return self.value

c = Counter()
c.increment().increment().increment()
print(c.get())




# The repr Method
# For developer-friendly representation:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(name='{self.name}', email='{self.email}')"

user = User("Alice", "alice@example.com")
print(repr(user))  # User(name='Alice', email='alice@example.com')
# __repr__ is used in the debugger and when you inspect objects in the REPL.

