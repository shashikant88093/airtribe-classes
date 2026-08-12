# Use Last In First Out (LIFO).

## Algorithm
1. Initialize an empty stack.
2. If the current character is an opening bracket, push it onto the stack.
3. If it is a closing bracket:
   - If the stack is empty, return false.
   - Compare it with the top of the stack.
   - If they match, pop the stack.
   - Otherwise, return false.
4. After processing all characters, return true only if the stack is empty.


## Complexity Analysis
- Time Complexity: O(n), where n is the length of the input string. Each character is processed once.
- Space Complexity: O(n), in the worst case, all opening brackets are pushed onto the stack.


### Pseudocode
```
function isValidParentheses(s):
    stack = empty stack
    for char in s:
        if char is an opening bracket:
            stack.push(char)
        else if char is a closing bracket:
            if stack is empty:
                return false
            top = stack.peek()
            if top and char match:
                stack.pop()
            else:
                return false
    return stack is empty
```