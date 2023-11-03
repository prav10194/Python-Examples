<b>Level: </b>Medium

<b>Category: </b>Sliding Window

<b>Space Complexity: </b>O(n) - worst case would be when the complete string would be unique and is there in set. 
<b>Time Complexity: </b>O(2n)

<b>Solution: </b>This sliding window problem also involves using a set() to check for uniqueness in the substring. 
<br/>
Covering the edge cases

```python
if len(s) == 0: return 0
if len(s) == 1: return 1
```

Setting up the pointers and set. 

```python
unique = set()
tempLength = maxLength = 0
left, right = 0, 0
```

The logic would work in this way: if we don't have a unique value (value not there in set), then we add the value in set and update the right pointer along with tempLength. 
<br/>
Else, we update maxLength, clear the set and update the left and right pointers. <b><i>Also, we have covered another edge case at the end where we check if tempLength > maxLength, then we return tempLength. Example for this case would be "au" where it never goes in else condition to update maxLength. </b></i>

```python
while right <= len(s) - 1:
    if s[right] not in unique:
        unique.add(s[right])
        tempLength = right - left + 1
        right += 1
    else:
        if tempLength > maxLength:
            maxLength = tempLength
        unique.clear()
        left += 1
        right = left
if tempLength > maxLength:
    return tempLength
else:
    return maxLength
```

Complete code is as follows:

```python
unique = set()
tempLength = maxLength = 0
left, right = 0, 0

if len(s) == 0: return 0
if len(s) == 1: return 1

while right <= len(s) - 1:
    if s[right] not in unique:
        unique.add(s[right])
        tempLength = right - left + 1
        right += 1
    else:
        if tempLength > maxLength:
            maxLength = tempLength
        unique.clear()
        left += 1
        right = left
if tempLength > maxLength:
    return tempLength
else:
    return maxLength
```
