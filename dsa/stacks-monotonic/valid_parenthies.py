# https://leetcode.com/problems/valid-parentheses/description/

stack = []
mapping = {
    "{":"}",
    "(":")",
    "[":"]"
}
def validParenthis(string):
    
    for char in range(len(string)):
        if char in mapping.values():
            stack.append(char)
        else:
            if not stack or stack.pop() != mapping[char]:
                return False
            
    return len(stack) == 0


