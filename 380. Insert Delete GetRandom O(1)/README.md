## Problem Statement

Implement the functions of the class such that each function (insert, remove, getRandom) works in average O(1) time complexity.

The runtime complexity of the <b>set.add(), set.remove() function is O(1)</b> because Python's set data structure is implemented as a hash table and you can expect lookup, insert, and delete operations to have constant runtime complexity.

#### Data Structure

![image](https://user-images.githubusercontent.com/8276139/196842026-474f9aa0-85dc-400a-9760-ccbcff737201.png)


We have to use Hashmap + List to create the RandomizedSet

```python
class RandomizedSet:
  def __init__(self):
    # Dictionary key = item, value = index of the item in list
    self.dict = {}
    self.list = []
```

#### Insertion

Check if item in self.dict, if not insert it into dictionary with value = length of list (not length - 1 as we have to append as the next in list)
Append it in list

```python
  def insert(self, item):
    if item in self.dict:
      return False
    self.dict[item] = len(self.list)
    self.list.append(item)
    return True
```

#### Deletion

```python
def delete(self, item):
  if item not in self.dict:
    return False
  index = self.dict[item]

  self.dict[self.list[-1]], self.dict[item] = self.dict[item], self.dict[self.list[-1]]
  
  self.list[-1], self.list[index] = self.list[index], self.list[-1]
  
  del self[item]
  self.list.pop()
  return True
```

#### Random

```python
def getrandom(self):
  return random.choice(self.list)
```
