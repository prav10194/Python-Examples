<b>Level: </b>Medium

<b>Category: </b>Sliding Window

<b>Space Complexity: </b>
<b>Time Complexity: </b>

<b>Solution: </b>To solve this problem, we would have to come up with the logic for a "valid" window. 
<br/>We are given <b><i>k</b></i> which is the max we can go for substitution. 

The equation for a valid window would be: 

<b><i>windowSize - maxFrequency <= k</b></i>

<b>Example of a valid window: </b>Let's assume our windowSize is 4 (AABC), and our k = 2. Now our frequency count would look something like - 

```json
{
  "A": 2,
  "B": 1,
  "C": 1
}
```

So this window is valid ( 4 - 2 <= 2 ) and hence we can substitute B and C with A. 

<b>Example of an invalid window: </b>Let's assume our windowSize is 5 (AABCD), and our k = 2. Now our frequency count would look something like -


```json
{
  "A": 2,
  "B": 1,
  "C": 1,
  "D": 1
}
```

Now based on the equation, the window is invalid ( 5 - 2 !<= 2 ). 
<br/><br/><b>What do we do if a window is invalid?</b> In this case, we will decrease the value of s[left] by 1 and increment left pointer by 1. 

<br/><b>Code: </b>We can maintain a dictionary to keep track of our character count in the current window. Let's call it "count". 
<br/>Also, let's create a left and right pointer, and result for keeping track of max length. 

```python
l, r = 0, 0
result = 0
count = defaultdict(int)
```

Main code logic (based on equation above)

```python
while r <= len(s) - 1:
    count[s[r]] += 1
    while r - l + 1 - max(count.values()) > k:
        count[s[l]] -= 1
        l += 1
    result = max(result, r - l + 1)
    r += 1

return result
```


