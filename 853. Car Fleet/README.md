Link: https://leetcode.com/problems/car-fleet/description/

<b>Solution: </b>We have 2 arrays - position and speed. Step 1 would be to merge both the arrays and sort in descending based on position. 

```python
# position = [10,8,0,5,3], speed = [2,4,1,1,3]
# after sorting
posSpeed = [[10, 2], [8, 4], [5, 1], [3, 3], [0, 1]]
```

Logic: Calculate time of each pair, if time > stack[-1], append into result stack else do nothing. At the end, just return length of stack for the number of pairs. 
