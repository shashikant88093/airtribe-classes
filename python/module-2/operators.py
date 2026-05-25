
# The and Operator
# and returns True only if both conditions are True:

has_ticket = True
has_id = True
if has_ticket and has_id:
    print("Welcome!")  # This prints
# Truth table:

True and True    # True
True and False   # False
False and True   # False
False and False  # False



# The or Operator
# or returns True if at least one condition is True:

is_member = False
has_coupon = True

if is_member or has_coupon:
    print("You get a discount!")  # This prints
# Truth table:

True or True    # True
True or False   # True
False or True   # True
False or False  # False



# The not Operator
# not flips a boolean:

not True   # False
not False  # True
# Useful for inverting conditions:

is_banned = False

# These are equivalent:
if not is_banned:
    print("Welcome!")

if is_banned == False:
    print("Welcome!")


# Order of Operations

# Python evaluates in this order:

# not (first)

# and

# or (last)

# Without parentheses
True or False and False
# Python reads: True or (False and False)
# Result: True or False → True

# With parentheses - different result
(True or False) and False
# Result: True and False → False