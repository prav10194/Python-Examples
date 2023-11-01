<b>Level: </b>Medium

<b>Category: </b>Two Pointers

<b>Solution: </b>
<br/>We can have 2 pointers, left and right. And a variable called area will keep track of updated area. 

```python
left = 0
right = len(height) - 1
area = min(height[left], height[right]) * (right - left)
```
<br/>We can calculate the area by finding the minimum height at left and right and the distance between the 2 indexes. 
<br/>We can update left and right based on which is shorter. 

```python
while left < right:
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
    
    tempArea = min(height[left], height[right]) * (right - left)
  
    if tempArea > area:
        area = tempArea
```

