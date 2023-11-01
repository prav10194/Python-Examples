<b>Level: </b>Hard

<b>Category: </b>Two Pointers

<b>Solution: </b>
The formula for calculating how much water can be stored at an index is 
<br/><br/>
<b><i>min(max(values at left of index), max(values at right of index)) - height[index]</b></i>
<br/><br/>
First, we initialize our pointers as well as 2 variables for max left and max right. And res stores the final amount of water. 

```python
  l, r = 0, len(height) - 1
  lmax, rmax = height[l], height[r]
  res = 0
```

Our main logic will work based on our formula above (a bit modified). While will run unless left becomes greater than right. 

```python
 while l < r:
```

If left max < right max, we updated our left pointer by 1. Then based on the formula we calculate how much water can it store (only if it > 0 else we skip). And then we update our lmax to new value. 

```python
 if lmax < rmax:
    l += 1
    if lmax > height[l]:
        res += min(lmax, rmax) - height[l]
    lmax = max(lmax, height[l])                
```

Similar condition if rmax > lmax. 

```python
if rmax < lmax:
  r -= 1
  if rmax > height[r]:
      res += min(lmax, rmax) - height[r]
  rmax = max(rmax, height[r])
```
