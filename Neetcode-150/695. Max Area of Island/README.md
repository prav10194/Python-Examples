Link: https://leetcode.com/problems/max-area-of-island/

<b>Solution: </b>Similar to the number of islands - we will apply DFS. <br/>Looking at the code - we can see the change is in the backtracking step where we add 1 to the result of all the dfs calls in all directions. 

```python
  ROWS = len(grid)
  COLS = len(grid[0])
  area = 0
  visited = set()

  def dfs(r, c):
      if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1 and (r, c) not in visited:
          visited.add((r, c))
          return (1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1))
      else:
          return 0


  for r in range(ROWS):
      for c in range(COLS):
          if (r, c) not in visited and grid[r][c] == 1:
              area = max(area, dfs(r,c))

  return area
```
