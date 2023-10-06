<b>Level: </b>Medium

<b>Solution: </b>
<br/>1. Create a new linked list. Maintain a carry and sum. 

```python
        carry = 0
        sum_ll = ListNode()
        curr = sum_ll
```

<br/>2. There will be 4 scenarios that we would be considering - 
<br/>  a. If both l1 and l2 are not empty. 

```python
        while l1 and l2:
            temp = ListNode()

            s = l1.val + l2.val + carry

            if s >= 10:
                carry = s // 10
                s = s % 10
                temp.val = s
            else:
                temp.val = s
                carry = 0
            l1 = l1.next
            l2 = l2.next
            curr.next = temp
            curr = temp
```

<br/>  b. If l1 is empty.

```python
        if not l1:
            while l2:
                temp = ListNode()

                s = l2.val + carry

                if s >= 10:
                    carry = s // 10
                    s = s % 10
                    temp.val = s
                else:
                    temp.val = s
                    carry = 0

                l2 = l2.next
                curr.next = temp
                curr = temp
```

<br/>  c. If l2 is empty. 

```python
        if not l2:
            while l1:
                temp = ListNode()

                s = l1.val + carry

                if s >= 10:
                    carry = s // 10
                    s = s % 10
                    temp.val = s
                else:
                    temp.val = s
                    carry = 0
                
                l1 = l1.next
                curr.next = temp
                curr = temp
```

<br/>  d. If carry is not empty. 

```python
        if carry:
            temp = ListNode(carry)
            curr.next = temp
```
