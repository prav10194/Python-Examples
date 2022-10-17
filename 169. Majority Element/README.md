Link - https://leetcode.com/problems/majority-element/

Category - Array

<b>Solution: Keep a counter and increment and save the value if counter == 0. Also check the counter and increment if saved value equal to current value and vice-versa. 

```python
  for num in nums:
      if counter == 0:
          mValue = num
      counter += 1 if mValue == num else -1
```
</b>
