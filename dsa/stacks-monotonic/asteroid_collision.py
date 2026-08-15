# https://leetcode.com/problems/asteroid-collision/description/



# algo. 
#  + + no collision
#  + -  collision
#  - + no collision
#  - - no collision
def asteriod_collision(list):
    stack =[]
    
    for char in list:
        # print(char)
        if (char >0):
            stack.append(char)
        else:
            if not stack:
                return False
            top=stack[-1]
            if top <= abs(char):
                stack.pop()


    return stack



# ast = [5,10,-5]
# ast = [8,-8]
ast = [3,5,-6,2,-1,4]

asteriod_collision(ast)

# print(stack)

