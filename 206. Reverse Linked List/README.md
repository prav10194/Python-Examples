Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Solution: start with 2 pointers: **prev and curr** Initilaize them as **None and head** respectively. 

Now start with swapping the pointers for curr and prev and then move forward

<img width="775" alt="image" src="https://user-images.githubusercontent.com/8276139/200451030-b22bf844-976a-448d-bb29-dcece537fede.png">


```python

while curr:
  temp = curr.next
  curr.next = prev
  prev = curr
  curr = temp
return prev


```

