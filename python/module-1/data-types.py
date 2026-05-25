# Python has four basic types:

name = "Alex"       # str (string) - text
age = 25            # int (integer) - whole number
price = 19.99       # float - decimal number
is_active = True    # bool (boolean) - True or False
# Plus a special one:

middle_name = None # NoneType - "no value" 


# Common String Operations

# Strings come with useful built-in methods:

name = "  Alex Smith  "
name.lower()       # "  alex smith  "
name.upper()       # "  ALEX SMITH  "
name.strip()       # "Alex Smith" (removes whitespace)
name.replace("Smith", "Jones")  # "  Alex Jones  "
email = "user@example.com"
email.startswith("user")  # True
email.endswith(".com")    # True
"@" in email              # True


# Checking Types

# Use type() to see what type something is:

print(type("hello"))   # <class 'str'>
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type(True))      # <class 'bool'>
print(type(None))      # <class 'NoneType'>
# Useful for debugging when something isn't behaving as expected.

# Checking Specific Types
# Sometimes you need to check if a value is a specific type:

age = 25
name = "Alex"
isinstance(age, int)     # True
isinstance(age, str)     # False
isinstance(name, str)    # True

# Check multiple types at once
isinstance(age, (int, float))  # True, age is one of these types


# Converting Between Types

# Sometimes you need to convert:

# String to integer
age_str = "25"
age_num = int(age_str)  # Now it's the number 25

# Integer to string
count = 10
count_str = str(count)  # Now it's "10"

# String to float
price_str = "19.99"
price_num = float(price_str)  # Now it's 19.99
# Why This Matters
# User input is almost always a string:

user_input = "25"  # From a form

# This would crash: 😢
# next_year = user_input + 1  # Can't add string and number

# Convert first:
age = int(user_input)
next_year = age + 1  # Works: 26



# Important: input() Always Returns a String
# Even if the user types a number:

age = input("Enter your age: ")
print(type(age))  # <class 'str'>
# If the user types 25, age is "25" (string), not 25 (number).

# To do math, convert it:

age = int(input("Enter your age: "))
# This is a common source of bugs. Keep it in mind.

# String Formatting
# Let's say you want to display: "Hello, Dhaval! Your balance is $100.50"

# The Clunky Way
name = "Dhaval"
balance = 100.50
message = "Hello, " + name + "! Your balance is $" + str(balance)
# This works but it's messy and easy to get wrong.

# The Modern Way: f-strings
# Put f before the quote, then use {variable} to embed values:

name = "Dhaval"
balance = 100.50
message = f"Hello, {name}! Your balance is ${balance}"
print(message)
# Hello, Dhaval! Your balance is $100.50


# f-string Superpowers
# Do Math Inside
price = 19.99
quantity = 3
print(f"Total: ${price * quantity}")
# Total: $59.97
# Call Methods
name = "alex"
print(f"Hello, {name.upper()}!")
# Hello, ALEX!
# Format Numbers
# Two decimal places
price = 19.5
print(f"${price:.2f}")  # $19.50

# Add commas for thousands
population = 7900000000
print(f"{population:,}")  # 7,900,000,000

# Percentages
rate = 0.756
print(f"{rate:.1%}")  # 75.6%


# Question:

# What does this print?

print("Hello", "World", sep="-", end="!\n")
# Think about it...

# Answer:

# Hello-World!


# Multiline Strings
# Use triple quotes for text that spans lines:

email = """
Hi Dhaval,

Your order has shipped!

Thanks,
The Team
"""


# Shorthand Operators
# When you're updating a variable based on its current value, Python offers shortcuts:

count = 10

# These are the same:
count = count + 1
count += 1

# Works with other operators too:
count -= 5   # Same as count = count - 5
count *= 2   # Same as count = count * 2
count /= 4   # Same as count = count / 4




# A Handy Trick: Multiple Assignment


# Python lets you do this:

# Assign same value to multiple variables
x = y = z = 0

# Assign different values in one line
name, age, city = "Alex", 25, "Mumbai"

# Swap values without a temp variable
a = 1
b = 2
a, b = b, a
print(a, b)  # 2 1