Link: 

Solution: The problem contains 3 different parts: 

Part 1: Find the middle of linked list - use fast, slow pointer
Part 2: Reverse second half of linked list
Part 3: Merge 2 lists together

Part 1: 

```python
fast, slow = head, head

while fast and fast.next:
  fast = fast.next.next
  slow = slow.next
```

Part 2: 

```python
curr = slow.next
slow.next = None
prev = None
while curr:
  temp = curr.next
  curr.next = prev
  prev = curr
  curr = temp
```

Part 3: 

```python
# pointer to second list is prev

```

