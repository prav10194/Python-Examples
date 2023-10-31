<b>Level:</b> Hard

<b>Category:</b> Two Pointers

<b>Solution:</b><br/> This problem is similar to solving 2 Sum (if the array is sorted). What we will first do is sort the complete array. Since we can have more than one solution, we will maintain a set. 

```python3
  nums = sorted(nums, reverse = False)
  res = set()
```
<br/>
After that loop through the complete list. Take the current element, and the rest of the remaining array becomes a 2 Sum problem. 

<i><b>Things to note:</b> The inner loop has to run until l < r (and not l <= r)
<br/>
Also left pointer needs to be updated even if tempSum == 0 for more solutions. </i>


```python3
  for index, num in enumerate(nums):
      l, r = index + 1, len(nums) - 1
  
      while l < r:
          temp = num + nums[l] + nums[r]
  
          if temp == 0:
              res.add((num, nums[l], nums[r]))
              l = l + 1
          else:
              if temp < 0:
                  l = l + 1
              else:
                  r = r - 1
  
  return res
```
