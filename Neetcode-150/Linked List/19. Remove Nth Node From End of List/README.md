<b>Level:</b> Medium

<b>Solution:</b>
<br/>Step 1 - Create 2 pointers: left and right. Move the right pointer - until n becomes zero. Create a dummy value to store head in its next. Will be used in step 4. 
<br/>Step 2 - In next iteration, move left pointer and right pointer until right reaches till end.
<br/>Step 3 - The left pointer will be one node before whoch needs to be deleted. Set the next pointer of left to left.next.next. 
<br/>Step 4 - Return dummy.next

<b>Python Code:</b>
```python
        dummy = ListNode(0, next = head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next
```
