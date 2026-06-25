sparkle
Basic parameters work, but real code needs more flexibility. What if some values are optional? What if you want to be explicit about which argument is which? Python's parameter system handles all of this.


The Quick Version
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                    # Hello, Alice!
greet("Bob", "Hi")               # Hi, Bob!
greet(greeting="Hey", name="Charlie")  # Hey, Charlie!
Parameters can have defaults, and arguments can be passed by name.
Parameters can have defaults, and arguments can be passed by name.

sparkle
Parameters vs Arguments
Quick terminology:

Parameters: Variables in the function definition

Arguments: Values passed when calling the function


def add(a, b):      # a and b are parameters
    return a + b

result = add(3, 5)  # 3 and 5 are arguments
sparkle
Positional Arguments
Arguments matched by position:



def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")

describe_pet("dog", "Rex")    # I have a dog named Rex
describe_pet("Rex", "dog")    # I have a Rex named dog (wrong!)


Order matters with positional arguments.

sparkle
Keyword Arguments
Arguments matched by name:


def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")

describe_pet(animal="dog", name="Rex")  # I have a dog named Rex
describe_pet(name="Rex", animal="dog")  # I have a dog named Rex (same!)
Keyword arguments can be in any order.



sparkle
Mixing Positional and Keyword
You can use both, but positional must come first:


def create_user(username, email, role="user"):
    print(f"Creating {role}: {username} ({email})")

# All valid
create_user("alice", "alice@example.com")
create_user("bob", "bob@example.com", "admin")
create_user("charlie", email="charlie@example.com")
create_user("diana", "diana@example.com", role="moderator")

# Invalid — positional after keyword
# create_user(username="eve", "eve@example.com")  # SyntaxError
sparkle
Default Parameter Values
Make parameters optional with defaults:

def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

greet("Alice")                           # Hello, Alice!
greet("Bob", "Hi")                      # Hi, Bob!
greet("Charlie", "Hey", "?")            # Hey, Charlie?
greet("Diana", punctuation="...")       # Hello, Diana...
Parameters with defaults must come after parameters without defaults.

sparkle
Question: What does this print?



def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(2, 3))
print(power(exponent=3, base=2))
sparkle
Answer:

9
8 
8
power(3): Uses default exponent=2, so 3² = 9

power(2, 3): Positional arguments, 2³ = 8

power(exponent=3, base=2): Keyword arguments (order doesn't matter), 2³ = 8

sparkle
The Mutable Default Gotcha
Never use a mutable object as a default value:

# DON'T DO THIS
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("a"))  # ["a"]
print(add_item("b"))  # ["a", "b"] — Wait, what?!
The default list is created once and shared between calls.

The fix:

def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("a"))  # ["a"]
print(add_item("b"))  # ["b"] — Correct!
Use None as the default and create a new list inside the function.



sparkle
Required vs Optional Parameters
Design functions with required parameters first, optional last:

def send_email(to, subject, body, cc=None, bcc=None, priority="normal"):
    """
    Send an email.

    Required: to, subject, body
    Optional: cc, bcc, priority
    """
    print(f"Sending to {to}: {subject}")
    if cc:
        print(f"  CC: {cc}")
    if bcc:
        print(f"  BCC: {bcc}")
    print(f"  Priority: {priority}")

# Minimal call
send_email("bob@example.com", "Hello", "Message body")

# With options
send_email(
    "bob@example.com",
    "Urgent",
    "Please respond",
    priority="high"
)
sparkle
Quick Practice
tick
1 correct
cross
2 incorrect
chevron
Q1.
What's wrong with this function?

def greet(greeting="Hello", name):
    print(f"{greeting}, {name}!")
tick
Nothing, it works fine
Parameters with defaults must come after required parameters
Can't use f-strings in functions
Missing return statement
Q2.
You want to call this function with animal="cat" but use the default name. How do you call it?

def describe_pet(animal="dog", name="Buddy"):
    print(f"A {animal} named {name}")
describe_pet("cat")
describe_pet(animal="cat")
tick
describe_pet("cat", name="Buddy")
Both A and B work
Q3.
Why should you avoid mutable default arguments like def func(items=[]):?

It causes a syntax error
tick
The default is shared across all calls, leading to unexpected behavior
Lists can't be used as parameters
It makes the function slower
sparkle
Where You'll Use This in Django
Django functions use parameters extensively:

# View with URL parameters
def article_detail(request, article_id, slug=None):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article.html', {'article': article})

# Model methods with defaults
class Order(models.Model):
    def calculate_total(self, include_tax=True, include_shipping=True):
        total = self.subtotal
        if include_tax:
            total += self.tax
        if include_shipping:
            total += self.shipping
        return total

# Utility functions
def send_welcome_email(user, template="welcome", delay_minutes=0):
    """Send welcome email to new user."""
    if delay_minutes:
        schedule_email(user, template, delay_minutes)
    else:
        send_email_now(user, template)

# Form processing with optional fields
def process_registration(
    username,
    email,
    password,
    first_name=None,
    last_name=None,
    newsletter=False
):
    user = User.objects.create_user(username, email, password)
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    user.save()

    if newsletter:
        subscribe_to_newsletter(email)

    return user
sparkle
Quick Recap
Positional arguments: Matched by order

Keyword arguments: Matched by name, can be in any order

Default values: Make parameters optional (param=default)

Required parameters must come before optional ones

Never use mutable defaults ([], {}). Use None instead.

Keyword arguments after positional: func(pos1, pos2, key=val)

