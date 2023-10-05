<b>Level: </b>Medium

<b>Solution: </b>
<br/>We need to create a new hashmap that would contain the reference of new nodes with their values.

```python
new_ll = { None: None }

curr = head

while curr:
    new_ll[curr] = Node(curr.val)
    curr = curr.next
```

<br/>Next we will set the pointers for next and random for our new linked list. Return the hashmap. 

```python
curr = head

while curr:
    new_ll[curr].next = new_ll[curr.next]
    new_ll[curr].random = new_ll[curr.random]
    curr = curr.next

return new_ll[head]
```
