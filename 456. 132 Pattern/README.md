Link: https://leetcode.com/problems/132-pattern/description/

<b>Solution: </b>This is a stack monotonic question. We will define a stack that will have a pair of [num, minLeft]

```python
stack = []
curMin = nums[0]
```

Now we loop over the nums starting from index 1. 
* While current value is greater than or equal to stack top, pop the top value.  
* If current value is greater than the minLeft of top, return True as we have found our 132 sequence. 
* Return False, if all elemnts have been vsisted. 

```python
for num in nums[1:]: 
    while stack and num >= stack[-1][0]:
        stack.pop()
    if stack and num > stack[-1][-1]:
        return True
    stack.append([num, curMin])
    curMin = min(curMin, num)
return False
```

