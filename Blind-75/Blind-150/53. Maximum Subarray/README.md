Link: https://leetcode.com/problems/maximum-subarray/

<b>Solution: </b><br/>We start with iterating over the nums array. We check if curSum < 0, if yes then we reset it to zero. <br/>Then we add the current num in curSum and compare it to maxSum. 

```python
        maxSum = nums[0]
        curSum = 0
        
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSum = max(maxSum, curSum)
        return maxSum
```
