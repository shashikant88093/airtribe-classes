# https://leetcode.com/problems/valid-parentheses/description/


def validParenthis(s):
    mapping= {
    "(":")",
    "{":"}",
    "[":"]"
}

    stack = []
    
    for chr in s:
        if chr in mapping:
            # Push opening brackets onto the stack
            stack.append(chr)
        else:
            # For closing brackets: check if stack has an opening bracket to match
            if not stack:
                return False
            
            # Access the top element of STACK (not string 's')
            topEle = stack[-1]
            print(topEle,"topEle")
            print(stack,"sstack")
            if chr == mapping[topEle]:
                stack.pop()
            else:
                return False

    return len(stack) == 0


# print(validParenthis("({[)"))   # Output: False
# print(validParenthis("()[]{}")) # Output: True
    

print(validParenthis("()[]{}"))






