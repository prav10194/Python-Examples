Link: https://leetcode.com/problems/min-stack/

Level: Medium

<b>Solution: </b>We will start with creating 2 arrays - one for storing the actual values and one for storing the minimum value at the point

For push - 

```python

stack.append(val)

if val < minStack[-1]:
  minStack.append(val)
else:
  minStack.append(minStack[-1])

```

For pop - 

```python
stack.pop()
minStack.pop()
```

For top - 

```python
return stack[-1]
```

To get the minimum - 

```python
return minStack[-1]
```
