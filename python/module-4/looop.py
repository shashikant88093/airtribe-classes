# sparkle
# You've learned how to store multiple items in lists, tuples, and dictionaries. Now you need to process them. Send an email to each user in a list. Calculate the total of all items in a cart. Check every entry in a database result. That's what loops are for.



# The Quick Version
users = ["alice", "bob", "charlie"]

for user in users:
    print(f"Hello, {user}!")

# Output:
# Hello, alice!
# Hello, bob!
# Hello, charlie!
# The for loop runs once for each item in the collection.

# sparkle
# Basic For Loop
colors = ["red", "green", "blue"]

for color in colors:
    print(color)
# How it works:

# First iteration: color = "red", print it

# Second iteration: color = "green", print it

# Third iteration: color = "blue", print it

# No more items, loop ends

# The variable name (color) is your choice, use something meaningful.

# sparkle
# Looping Over Different Types
# 1. Lists
prices = [10.99, 24.50, 5.00]
total = 0

for price in prices:
    total += price

print(total)  # 40.49
# 2. Strings
word = "Python"

for char in word:
    print(char)
# P, y, t, h, o, n (each on its own line)
# 3. Dictionaries
user = {"name": "Alice", "age": 30, "role": "admin"}

# Loop over keys (default)
for key in user:
    print(key)  # name, age, role

# Loop over values
for value in user.values():
    print(value)  # Alice, 30, admin

# Loop over both
for key, value in user.items():
    print(f"{key}: {value}")
# sparkle
# The range() Function
# Need to loop a specific number of times? Use range():

# 0 to 4 (5 times)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# 1 to 5
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# 0, 2, 4, 6, 8 (step of 2)
for i in range(0, 10, 2):
    print(i)

# Countdown: 5, 4, 3, 2, 1
for i in range(5, 0, -1):
    print(i)
range(start, stop, step) # - stop is excluded, just like slicing.

# sparkle
# Question: What does this print?

total = 0
for i in range(1, 4):
    total += i
print(total)
# sparkle
# Answer: 6

range(1, 4) # gives 1, 2, 3 (stop is excluded).

# First iteration: total = 0 + 1 = 1

# Second iteration: total = 1 + 2 = 3

# Third iteration: total = 3 + 3 = 6

# sparkle
# Getting the Index with enumerate()
# Sometimes you need both the item and its position:

fruits = ["apple", "banana", "cherry"]

# Without enumerate (works but clunky)
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (cleaner)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Start from a different number
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")
# 1: apple, 2: banana, 3: cherry
enumerate() # is the Pythonic way to get both index and value.

# sparkle
# Looping Over Multiple Lists with zip()
# Process two lists together:

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Output:
# Alice: 85
# Bob: 92
# Charlie: 78
zip() #pairs up items by position. It stops when the shortest list ends.

# sparkle
# Nested Loops
# Loops inside loops:

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")
# The inner loop runs completely for each iteration of the outer loop.

# sparkle
# Building New Lists
# A common pattern, process items and collect results:

numbers = [1, 2, 3, 4, 5]
squares = []

for n in numbers:
    squares.append(n ** 2)

print(squares)  # [1, 4, 9, 16, 25]
