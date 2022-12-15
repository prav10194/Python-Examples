Link: https://leetcode.com/problems/find-the-duplicate-number/

<b>Solution: </b> Refer - https://leetcode.com/problems/find-the-duplicate-number/solutions/127594/find-the-duplicate-number/?orderBy=most_votes

The solution is using Floyd's Algorithm. <br/>Phase 1 is finding the intersection point by moving tortoise by one step and hare by 2 steps. Once we find the intersection, we keep the value of hare as it is and reset tortoise to nums[0].<br/>Phase 2 would be find where they intersect again, and then return the intersection. 

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise, hare = nums[0], nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
            
        tortoise = nums[0]

        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
            
        return hare     
            
```
