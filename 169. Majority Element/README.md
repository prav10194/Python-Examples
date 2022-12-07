Link - https://leetcode.com/problems/majority-element/

Category - Array

<b>Solution: </b>

Logic: When we iterate over the array we will maintain 2 values - one will be for the count and the other for majValue. The algorithm will work in such a way that if count == 0 (which it will be in the start), maxValue = current value. <br/>Also we will have another condition which will check if majValue == current value, if yes increment the count by 1 else decrement it by 1. The algorithm will always at the end of loop will return the majority elemnt as the count will never be zero in that case and majValue will never be reset.  

```python
  mValue = 0
  count = 0

  for num in nums: 
      if count == 0:
          mValue = num
      if num == mValue: 
          count += 1
      else:
          count -= 1
  return mValue
```
