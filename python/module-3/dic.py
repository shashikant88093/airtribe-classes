
# Common Operations
user = {"name": "Alice", "age": 30}

# Get all keys
list(user.keys())  # ["name", "age"]

# Get all values
list(user.values())  # ["Alice", 30]

# Get key-value pairs as tuples
list(user.items())  # [("name", "Alice"), ("age", 30)]

# Number of keys
len(user)  # 2

# Merge dictionaries
defaults = {"role": "user", "active": True}
user.update(defaults)
# user is now {"name": "Alice", "age": 30, "role": "user", "active": True}

# Python 3.9+ merge syntax
merged = user | defaults  # Creates new dict



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