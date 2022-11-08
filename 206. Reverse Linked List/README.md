Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Solution: start with 2 pointers: **prev and curr** Initilaize them as **None and head** respectively. 

Now start with swapping the pointers for curr and prev and then move forward

<img width="812" alt="image" src="https://user-images.githubusercontent.com/8276139/200450191-31c520c7-6e42-4d2a-8fce-3c1928adb154.png">


```python

while curr:
  temp = curr.next
  curr.next = prev
  prev = curr
  curr = temp
return prev


```

