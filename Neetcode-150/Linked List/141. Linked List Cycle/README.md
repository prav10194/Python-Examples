<b>Level: </b>Easy

<b>Solution: </b>There are 2 ways to detect cycles in Linked List. 
<br/><br/>1. Using a set. Keep a track of all the nodes that have been traversed. If found a node already there in set, return False. Else return true. 

```python
        nodes = set()
        curr = head

        while curr:
            if curr in nodes:
                return True
            nodes.add(curr)
            curr = curr.next
        return False 
```


<br/><br/>2. Using fast, slow pointers. 

```python
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```
