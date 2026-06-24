# Python if / else examples

# Basic if statement
number = 10

if number > 0:
    print("Positive number")

# if / else: either one block runs
number = -5

if number >= 0:
    print("Zero or positive")
else:
    print("Negative number")

# if / elif / else: multiple conditions
score = 75

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"

print(f"Score {score} gives grade {grade}")

# Condition can be any expression that is True or False
name = "Alex"

if name == "Alex":
    print("Hello Alex")
else:
    print("Hello stranger")

# You can also use boolean variables directly
is_raining = False

if is_raining:
    print("Take an umbrella")
else:
    print("No umbrella needed")

# Nested if: one if inside another
age = 20

if age >= 18:
    print("Adult")
    if age >= 21:
        print("Can drink alcohol in some countries")
    else:
        print("Cannot drink alcohol in some countries")
else:
    print("Not an adult")

# Example with input (commented out for easier learning)
# user_age = int(input("Enter your age: "))
# if user_age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")

# Using break inside a loop
# break stops the entire loop immediately.
for i in range(1, 6):
    print(f"Checking {i}")
    if i == 3:
        print("Found 3, stopping loop")
        break

print("For loop ended")

# Using break inside a while loop
# break also stops a while loop immediately.
count = 1
while count <= 5:
    print(f"Checking {count}")
    if count == 3:
        print("Found 3 in while loop, stopping")
        break
    count += 1

print("While loop ended")

# Using continue inside a loop
# continue skips the rest of the current loop iteration,
# but the loop itself keeps going.
for i in range(1, 6):
    if i == 3:
        print("Skipping 3")
        continue
    print(f"Processing {i}")

print("Loop completed")
