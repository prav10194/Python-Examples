## Unrolled Linked List

An unrolled linked list is a combination of arrays + traditional linked list. By using arrays, we can decrease the overhead of our linkedlist (which was 50% before - because each node had 1 data value and 1 next pointer). 
<br/>
2 advantages - 
* It has a small memory overhead (a benefit of an array) 
* efficient insertion and deletion operations (benefits of a linked list).

The unrolled linked list has two pointers: head and tail. Head points to the first node, and tail refers to the last node.

#### Defining the structure of our node

```python
class Node:
  def __init__(self):
    self.length = 0
    self.array = []
    self.next = None
```

#### Defining the structure of our unrolled linked list
```python
class UnrolledLinkedList:
  def __init__(self, capacity):
    self.capacity = capacity #maximum capacity of an array in node
    self.head = None
    self.tail = None
```

#### Insertion

3 cases - 

* If ULL is empty, create a new node and insert it in head. Also Tail = Head
* If current node capacity is not full, insert it into teh current node. 
* If current node capacity is full, create a new node and fill half of the elements from current node to new node.

```python
  def insert(self, value):
    # unrolled linked is empty
    if self.head == None: 
      self.head = Node()
      
      # add the value
      self.head.array.append(value) 
      self.head.length += 1
      self.tail = self.head

    # current node's capacity is not full
    elif self.tail.length + 1 <= self.capacity: 
      
      # add the given value
      self.tail.array.append(value) 
      self.tail.length += 1 

    # current node's capacity is full
    else: 
      # create a new node
      new_node = Node() 
      
      # move final half of elements from the current node to the new node
      half_length = self.tail.length//2
      new_node.array.extend(self.tail.array[half_length:])

      # add the given value to the new node
      new_node.array.append(value) 

      # set the length of the new node's array
      new_node.length = len(new_node.array)
      
      # update the length of the current node's array
      self.tail.length = half_length 
      
      # make current node next pointer refer to the new node
      self.tail.next = new_node 
      
      # update the tail
      self.tail = new_node 
```

#### Deletion

For deleting, we have to start from head and go through all the nodes to find the value. 
* Once we find it, we will delete it from the array and decrease the length
* Move elements from next node to current node if current node capacity is less than 50%. Fill it till half the capacity. 
* If next node length is less than 50%, then we can merge it to our current one and delete the next node.


```python
  def delete(self, value):
    # find the given value and delete it 
    temp = self.head
    
    while temp:
      for i in range(0, temp.length):
        if temp.array[i] == value:

          # remove the given value from the array
          temp.array.pop(i) 
          temp.array.append(None)
          
          # decrease the length
          temp.length -= 1 

          # if the current node's length is less than 50% then move elements from next node's array to the current one. Only until it is filled to half the capacity. 
          while temp.length < (self.capacity//2) and temp.next:
            temp.array[temp.length] = temp.next.array.pop(0) 
            temp.length +=1
            temp.next.length -= 1
          
          # if the next node's length is less than 50%  then merge the two halves
          if temp.next and temp.next.length < (self.capacity//2) : 
            temp.array[temp.length:temp.length+temp.next.length] = temp.next.array[:temp.next.length]
            temp.length += temp.next.length
            deleted_node = temp.next
            temp.next = temp.next.next
            del deleted_node
          return 
      temp = temp.next
    
    raise ValueError(f'Value {value} does not exist in the list')
```
