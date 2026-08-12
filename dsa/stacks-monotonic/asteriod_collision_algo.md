## Asteriod Collision Algorithm
- ## Problem Statement
  - Given an array of integers representing asteroids in a row, each asteroid moves at the same speed. The absolute value of each integer represents the size of the asteroid, and the sign indicates its direction (positive for right, negative for left). When two asteroids collide, the smaller one explodes. If they are the same size, both explode. Asteroids moving in the same direction will never collide. The task is to determine the state of the asteroids after all collisions.
- ## Algorithm
  1 . Initialize an empty stack to keep track of the surviving asteroids.
  2 . Iterate through each asteroid in the input array:
     - If the asteroid is moving to the right (positive), push it onto the stack.
     - If the asteroid is moving to the left (negative), check for potential collisions:
     - While the stack is not empty and the top of the stack is a right-moving asteroid (positive):
     - Compare the sizes of the top asteroid and the current left-moving asteroid.
     - If the top asteroid is smaller, pop it from the stack (it explodes).
     - If the top asteroid is larger, the current left-moving asteroid explodes (do not push it onto the stack).
     - If they are the same size, pop the top asteroid from the stack (both explode) and break out of the loop.
     - If the stack is empty or the top of the stack is a left-moving asteroid (negative), push the current left-moving asteroid onto the stack (it survives).
  3 . After processing all asteroids, the stack will contain the surviving asteroids in the order they appear. Return the stack as the final state of the asteroids.
- ## Complexity Analysis
  - Time Complexity: O(n), where n is the number of asteroids. Each asteroid is processed at most twice (once when it is pushed onto the stack and once when it is popped).
  - Space Complexity: O(n), in the worst case, all asteroids are moving in the same direction and are pushed onto the stack.
- ## Pseudocode
```
function asteroidCollision(asteroids):
    stack = empty stack
    for asteroid in asteroids:
        if asteroid > 0:
            stack.push(asteroid)
        else:
            while stack is not empty and stack.peek() > 0:
                top = stack.peek()
                if abs(top) < abs(asteroid):
                    stack.pop()  # Top asteroid explodes
                elif abs(top) == abs(asteroid):
                    stack.pop()  # Both explode
                    break
                else:
                    break  # Current asteroid explodes
            else:
                stack.push(asteroid)  # Current asteroid survives
    return stack as list
```
