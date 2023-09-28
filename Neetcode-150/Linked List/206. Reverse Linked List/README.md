<b>Level:</b> Easy

<b>Solution: </b> 
<br/>One of the basic problems of Linked List. Create 2 new pointers: prev -> None, curr -> head

<br/>Start a loop and continue till curr != None. Create a new local pointer for reference for next loop iteration,  nxt -> curr.next. At the very end of loop set curr = nxt
<br/>Set curr.next = prev and prev = curr. 

<br/>Return prev

```python3

prev, curr = None, head

while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

return prev

```
