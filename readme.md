# Programming = Giving instructions to a computer to perform specific tasks. It involves writing code in various programming languages to create software applications, websites, and other digital solutions. Programming requires logical thinking, problem-solving skills, and an understanding of algorithms and data structures.

# Software Development Life Cycle (SDLC) = A process used by software developers to design, develop, test, and deploy software applications. The SDLC consists of several phases, including planning, analysis, design, implementation, testing, deployment, and maintenance. Each phase has specific deliverables and activities that ensure the software meets the desired requirements and quality standards.

## Python -> Translation -> Machine Language

## is python compiled or interpreted?
Python is an interpreted language. This means that Python code is executed line by line by the Python interpreter, rather than being compiled into machine code before execution.

# In Programming Languages, We have
# 1. Statement 
# 2. Expression
# 3. Data Types

## Statements
A statement is a line of code that performs a specific action. It is an instruction that the Python interpreter can execute. For example:
```python
print("Hello, World!")
```
This line is a statement that prints the text "Hello, World!" to the console.

## Expressions
An expression is a combination of values, variables, and operators that can be evaluated to produce a new value. Expressions can be as simple as a single value or more complex, involving multiple operations. For example:
```python
x = 5
y = 10
z = x + y
```
In this case, `x + y` is an expression that evaluates to `15`, which is then assigned to the variable `z`.

## Statements
A statement is a line of code that performs a specific action. It is an instruction that the Python interpreter can execute. For example:
```python
print("Hello, World!")
```
This line is a statement that prints the text "Hello, World!" to the console.

## Data Types
Data types define the kind of data that can be stored and manipulated in a programming language. In Python, common data types include:
### Primitives:
- Integers (`int`): Whole numbers 32 bits, e.g., `5`, `-3`, `42` Range: -2,147,483,648 to 2,147,483,647
- Floating-point numbers (`float`): Decimal numbers 32 bits, e.g., `3.14`, `-0.001`, `2.0`
- Characters (`char`): Single characters 16 bits, e.g., `'a'`, `'1'`, `'#'`
- Short integers (`short`): Smaller range of whole numbers 16 bits, e.g., `-32768` to `32767`
- Long integers (`long`): Larger range of whole numbers 32 bits, e.g., `-9,223,372,036,854,775,808` to `9,223,372,036,854,775,807`
- Numbers (`number`): Represents numeric values, including integers and floating-point numbers 64 bits 
- Floats (`float`): Represents decimal numbers 32 bits, e.g., `3.14`, `-0.001`, `2.0`
- Doubles (`double`): Represents decimal numbers 64 bits, e.g., `3.14`, `-0.001`, `2.0`
- Booleans (`bool`): Represents `True` or `False`

## Non-Primitives:

- Strings (`str`): Sequences of characters 8 bits, e.g., `"Hello"`, `'Python'`
- Lists (`list`): Ordered collections of items, e.g., `[1, 2, 3]`, `['apple', 'banana']`
- Tuples (`tuple`): Immutable ordered collections of items, e.g., `(1, 2, 3)`, `('a', 'b', 'c')`
- Dictionaries (`dict`): Unordered collections of key-value pairs, e.g., `{'name': 'Alice', 'age': 30}`, `{'fruit': 'apple', 'color': 'red'}`
- Sets (`set`): Unordered collections of unique items, e.g., `{1, 2, 3}`, `{'apple', 'banana', 'cherry'}`   
- NoneType (`None`): Represents the absence of a value, e.g., `None`
- Complex numbers (`complex`): Numbers with a real and imaginary part, e.g., `3 + 4j`, `2 - 5j`
- Bytes (`bytes`): Immutable sequences of bytes, e.g., `b'hello'`, `b'\x00\x01\x02'`
- Bytearrays (`bytearray`): Mutable sequences of bytes, e.g., `bytearray(b'hello')`, `bytearray(b'\x00\x01\x02')`
- Memoryview (`memoryview`): A view object that allows access to the memory of another object without copying it, e.g., `memoryview(b'hello')`, `memoryview(bytearray(b'\x00\x01\x02'))`
- Range (`range`): Represents a sequence of numbers, e.g., `range(5)` produces `0, 1, 2, 3, 4`
- Frozen sets (`frozenset`): Immutable unordered collections of unique items, e.g., `frozenset([1, 2, 3])`, `frozenset({'apple', 'banana', 'cherry'})`
- NoneType (`None`): Represents the absence of a value, e.g., `None`    

## one byte = 8 bits || 1 bit = 0 or 1 | 1 bit = [0, 1]
## 1 byte can (stores number) | -128 to 127 (signed) or 0 to 255 (unsigned)