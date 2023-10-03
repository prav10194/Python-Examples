## Starter code

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

sixth = ListNode(6, next = None)
fifth = ListNode(5, next = sixth)
fourth = ListNode(4, next = fifth)
third = ListNode(3, next = fourth)
second = ListNode(2, next = third)
first = ListNode(1, next = second)

curr = first

while curr:
    print(curr.val)
    curr = curr.next
    
```
