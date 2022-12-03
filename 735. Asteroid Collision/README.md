Link: https://leetcode.com/problems/asteroid-collision/description/

<b>Solution: </b>This is a stack question. Positive value of asteroid means it is going in direction right and negative value means it is going in direction left. 

Logic: Check for current value in asteroids and see if it's negative, non-zero and also the top of stack is positive. If yes, find the difference. 
* If difference > 0, we don't need to change anything else in stack so set asteroid = 0. 
* If difference < 0, that means we need to pop the top of stack and continue with the while loop. 
* If equal, set asteroid = 0 and pop the top value.  

```python
def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []

    for asteroid in asteroids:
        while stack and asteroid < 0 and stack[-1] > 0:
            diff = asteroid + stack[-1]
            if diff > 0:
                asteroid = 0
            elif diff < 0:
                stack.pop()
            else: 
                asteroid = 0
                stack.pop()
        if asteroid:
            stack.append(asteroid)
    return stack
```
