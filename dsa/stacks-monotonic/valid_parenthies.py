# https://leetcode.com/problems/valid-parentheses/description/


def validParenthis(s):

    mapping={
        "(":")",
        "{":"}",
        "[":"]"
    }

    stack = []

    for chr in s:
        #  for opening
        if chr in mapping:
            stack.append(chr)
            # for closing
        else:
            if not stack:
                return False
            top_value = stack[-1]
            if chr == mapping[top_value]:
                stack.pop()
            else:
                return False
        
    return len(stack) == 0
    


print(validParenthis("({[)"))   # Output: False
print(validParenthis("()[]{}")) # Output: True
    

# print(validParenthis("()[]{}"))






