Link: https://leetcode.com/problems/linked-list-cycle/

<b>Solution: </b>

You need to run 2 pointers - slow, fast

```python
slow, fast = head, head

while fast and fast.next:
  fast = fast.next.next
  slow = slow.next
  if fast == slow:
    return True
return False
```
