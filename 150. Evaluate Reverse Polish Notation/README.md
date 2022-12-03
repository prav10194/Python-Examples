Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Similar question: https://leetcode.com/problems/baseball-game/

<b>Solution: </b>We can use stack for solving this - 

```python
numbers = []

for token in tokens:
  if token == "+" # or "-" or "*" or "/":
    # perform mathematical operation and store result in numbers
  else:
    numbers.append(int(token))

return numbers[-1]
```
