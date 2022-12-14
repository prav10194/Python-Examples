Link: https://leetcode.com/problems/daily-temperatures/

<b>Solution: </b>This is a stack problem. Create a stack which would take [index, temperature]. <br/>Iterate over the temperature array, 
* while not stack - insert [index, temp]
* while stack and stack[-1][-1] < current temp:
    i, t = stack.pop()
    res[index] = (index - i)

```python
stack = []
res = [0]*len(temperatures)

for index in range(len(temperatures)):
    while stack and stack[-1][1] < temperatures[index]:
        i, t = stack.pop()
        res[i] = (index - i)
    stack.append([index, temperatures[index]])
return res
```
