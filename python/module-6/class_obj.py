# Class blueprint

class lollines:
    pass

lollines_1 = lollines()
print(lollines_1)
print(type(lollines_1))


# Defining a Class
class User:
    pass
# That's it , the simplest possible class. The pass statement is a placeholder.

# Naming convention: classes use PascalCase (capitalize each word, no underscores).

# class ShoppingCart:   # Good
# class shopping_cart:  # Not conventional for classes

# Creating Objects (Instances)
class User:
    pass

# Create instances
user1 = User()
user2 = User()

# Each is a separate object
print(user1)  # <__main__.User object at 0x...>
print(user2)  # <__main__.User object at 0x...> (different address)

print(user1 == user2)  # False — different objects
# Every call to User() creates a new, independent object.


# Adding Data to Objects
# You can attach data to objects using dot notation:

class User:
    pass

user = User()
user.name = "Alice"
user.email = "alice@example.com"
user.age = 30

print(user.name)   # Alice
print(user.email)  # alice@example.com
# These attached values are called attributes.



# Each Instance Has Its Own Data
class User:
    pass

user1 = User()
user1.name = "Alice"

user2 = User()
user2.name = "Bob"

print(user1.name)  # Alice
print(user2.name)  # Bob


# Changing one object doesn't affect others.

# Changing one object doesn't affect others.

# Pause and Think
# Question: What does this print?

class Counter:
    pass

c1 = Counter()
c2 = Counter()

c1.value = 10
c2.value = 20
c1.value = c1.value + 5

print(c1.value, c2.value)

    
# Class vs Instance
# Class: The blueprint/templat/e (e.g., User)

# Instance: A specific object created from the class (e.g., user1)

class Car:
    wheels = 4  # Class attribute — shared by all instances

car1 = Car()
car2 = Car()

print(car1.wheels)  # 4
print(car2.wheels)  # 4

# Class attributes are shared
Car.wheels = 6
print(car1.wheels)  # 6
print(car2.wheels)  # 6


# We'll cover the difference between class attributes and instance attributes more in the next topic.