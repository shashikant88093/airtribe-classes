# https://leetcode.com/problems/asteroid-collision/description/


ast = [5,10,5]

# algo. 
#  + + no collision
#  + -  collision
#  - + no collision
#  - - no collision
stack =[]
def asteriod_collision(arr):
    for num in arr:
        if num >0:
            stack.append(num)
        else:
            while stack and stack[-1] >0 and stack[-1]<abs(num):
                stack.pop()
            if not stack or stack[-1]<0:
                stack.append(num)
            elif stack[-1] == abs(num):
                stack.pop()
            

    return stack





asteriod_collision(ast)
