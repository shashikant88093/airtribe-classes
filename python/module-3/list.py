
# Nested Dictionaries
# Dictionaries can contain other dictionaries:

users = {
    "alice": {
        "email": "alice@example.com",
        "age": 30
    },
    "bob": {
        "email": "bob@example.com",
        "age": 25
    }
}

# Access nested values
users["alice"]["email"]  # "alice@example.com"

# Safe nested access
users.get("charlie", {}).get("email", "N/A")  # "N/A"



# Creating Lists
# Lists use square brackets []:

# List of strings
colors = ["red", "green", "blue"]

# List of numbers
prices = [10.99, 24.50, 5.00]

# Mixed types (allowed, but usually not a good idea)
mixed = ["hello", 42, True]

# Empty list
empty = []



# Accessing Items
# Lists are zero-indexed, the first item is at position 0:

fruits = ["apple", "banana", "cherry"]

fruits[0]   # "apple" (first item)
fruits[1]   # "banana" (second item)
fruits[2]   # "cherry" (third item)
fruits[-1]  # "cherry" (last item)
fruits[-2]  # "banana" (second from last)
# Negative indices count from the end. This is useful when you want the last item without knowing the list's length.

# Modifying Lists
# Lists are mutable, you can change them after creation:

fruits = ["apple", "banana", "cherry"]

# Change an item
fruits[0] = "apricot"
print(fruits)  # ["apricot", "banana", "cherry"]

# Add to the end
fruits.append("date")
print(fruits)  # ["apricot", "banana", "cherry", "date"]

# Insert at a specific position
fruits.insert(1, "blueberry")
print(fruits)  # ["apricot", "blueberry", "banana", "cherry", "date"]



# Removing Items
# Several ways to remove items:

fruits = ["apple", "banana", "cherry", "banana"]

# Remove by value (first occurrence only)
fruits.remove("banana")
print(fruits)  # ["apple", "cherry", "banana"]

# Remove by index
del fruits[0]
print(fruits)  # ["cherry", "banana"]

# Remove and return the last item
last = fruits.pop()
print(last)    # "banana"
print(fruits)  # ["cherry"]

# Remove and return item at specific index
fruits = ["apple", "banana", "cherry"]
item = fruits.pop(1)
print(item)    # "banana"


# List Length and Membership
fruits = ["apple", "banana", "cherry"]

# Length
len(fruits)  # 3

# Check if item exists
"banana" in fruits      # True
"mango" in fruits       # False
"mango" not in fruits   # True
# The in operator is very useful for checking membership before performing operations.

# Slicing Lists
# Get a portion of a list:

letters = ["a", "b", "c", "d", "e"]

letters[1:4]    # ["b", "c", "d"] (index 1 to 3)
letters[:3]     # ["a", "b", "c"] (start to index 2)
letters[2:]     # ["c", "d", "e"] (index 2 to end)
letters[::2]    # ["a", "c", "e"] (every 2nd item)
letters[::-1]   # ["e", "d", "c", "b", "a"] (reversed)
# The pattern is list[start:stop:step]. The stop index is excluded.





# Common List Operations
numbers = [3, 1, 4, 1, 5, 9]

# Sort (modifies the original list)
numbers.sort()
print(numbers)  # [1, 1, 3, 4, 5, 9]

# Reverse
numbers.reverse()
print(numbers)  # [9, 5, 4, 3, 1, 1]

# Get a sorted copy (original unchanged)
original = [3, 1, 4]
sorted_copy = sorted(original)
print(original)     # [3, 1, 4]
print(sorted_copy)  # [1, 3, 4]

# Count occurrences
numbers = [1, 2, 2, 3, 2]
numbers.count(2)  # 3

# Find index
numbers.index(3)  # 3 (position of first occurrence)



# Combining Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenate
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# Extend (modifies list1)
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]