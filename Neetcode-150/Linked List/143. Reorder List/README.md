<b>Level:</b> Medium

<b>Solution:</b>
<br/>This problem involves 3 steps - 
1. find middle of LL - using slow, fast
2. reverse LL
3. merge 2 LL together

```python
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle of LL - using slow, fast
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse LL
        curr = slow.next
        prev = None
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # merge 2 LL together
        first = head
        second = prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
```
