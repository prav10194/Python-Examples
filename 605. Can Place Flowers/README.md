Link - https://leetcode.com/problems/can-place-flowers/

Category - Array

<b>Solution - Check for 3 consective zeroes. Add a 0 on left and right to cover the edge cases. Easy way in Python would be to: 

```python
  flowerbed = [0] + flowerbed + [0]
  
  # or
  
  flowerbed.insert(0, 0)
  flowerbed.insert(len(flowerbed), 0)
  
```
</b>
