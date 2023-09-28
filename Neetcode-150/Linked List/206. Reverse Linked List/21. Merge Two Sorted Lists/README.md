<b>Level:</b> Easy

<b>Solution:</b>
<br/>We need to create a new linked list that will contain the merged nodes.

<br/>First we will go through both the linked lists and if val of a node is less than the value of other node, then the first node will be set to new linked list. Vice-versa if second node has a lesser value.

<br/>We have 2 edge cases - where if one of the linked list is empty, all of the values from the second LL is set to merged LL. 


```python
merged_list = ListNode()
head = merged_list

while list1 and list2:
    if list1.val <= list2.val:
        head.next = list1
        list1 = list1.next
    else:
        head.next = list2
        list2 = list2.next
    head = head.next

if not list1:
    while list2:
        head.next = list2
        list2 = list2.next

if not list2:
    while list1:
        head.next = list1
        list1 = list1.next

return merged_list.next
```
