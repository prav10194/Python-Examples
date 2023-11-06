<b>Level: </b>Hard

<b>Category: </b>Sliding Window & Monotonically decreasing queue

<b>Space Complexity: </b>
<br/><b>Time Complexity: </b>

<b>Solution: </b>This is a problem that involves a "monotonically decreasing queue".
<br/><b>Why this? </b>Brute force solution of checking max in each window would be O(n-k)*O(k) = n-k iterations and O(k) for finding max. 
<br/>With a monotonic queue, we can support efficient insertion, deletion, and retrieval of elements in a specific order, typically in increasing or decreasing order. 
<br/>We will start with creating a double-ended queue. On each element we encounter in our iteration, we will be focussing on 3 major operations: 
<br/><b>1. Appending an element to queue</b>
<br/><b>2. Removing an element from queue from left</b>
<br/><b>3. Appending an element to the final result list</b>

```python
dq = collections.deque()
res = []
l, r = 0, 0 # left and right pointers to keep track of the window
```
<br/><b>1. Appending an element to the queue: </b>If the last value inserted in the queue < the current value in the list, we will append it to the queue at the right. This also includes removing all the previous values which are less than the current value. 
<br/><i>Note: We are keeping track of indexes and not the actual values in the queue.</i>

```python
while dq and nums[dq[-1]] < nums[r]:
  dq.pop()
dq.append(r)
```

<br/><b>2. Removing an element from the queue from left: </b>If the left pointer is more than the left most value in the queue (since we are storing indices), we pop the value of left leftmost element in the queue. 

```python
 if l > dq[0]:
    dq.popleft()
```

<br/><b>3. Appending an element to the final result list: </b>If the current window becomes equal to k, we move the left most value of queue in our final result array (and increment the left most pointer)

```python
 if (r + 1) >= k:
    res.append(nums[dq[0]])
    l += 1
```

<b>Complete code: </b>

```python
dq = collections.deque()
res = []
l, r = 0, 0

while r <= len(nums) - 1:

    # append the new value
    while dq and nums[dq[-1]] < nums[r]:
        dq.pop()
    dq.append(r)

    # remove left value from window
    if l > dq[0]:
        dq.popleft()
    
    if (r + 1) >= k:
        res.append(nums[dq[0]])
        l += 1
    r += 1
return res
```


