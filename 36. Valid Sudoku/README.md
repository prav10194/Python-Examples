Link: https://leetcode.com/problems/valid-sudoku/

Category: Array

<b>Solution: 

Create 3 set hashmaps - one for row, col and for the 9 boxes (r//3, c//3)
  
```python
# Don't do this - sets are updated together
# rowCheck = colCheck = boxCheck = defaultdict(set)
rowCheck = defaultdict(set)
colCheck = defaultdict(set)
boxCheck = defaultdict(set)
```

Iterate through each cell and check if value is there in any of these sets, if yes - return False as it is not a valid sudoku

```python
# if value is not '.'
if board[r][c] in rowCheck[r] or board[r][c] in colCheck[c] or board[r][c] in boxCheck[(r//3, c//3)]:
    return False
```
else just add the value in the sets. Return True if all values are iterated. 

</b>
