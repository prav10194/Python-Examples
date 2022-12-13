Link: https://leetcode.com/problems/jump-game/

<b>Solution: </b><br/>The idea of this is to solve by greedy. <br/>We will start from second last index in array and check can we reach our goal (initially set to len(nums) - 1). <br/>To check we will add current index + value at index. If it is >= goal, then we set the goal to current index.

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for index in range(len(nums) - 2, -1, -1):
            jump = nums[index]
            
            if (index + jump) >= goal:
                goal = index
        
        return (goal == 0)
        
```
