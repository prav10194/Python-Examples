Link - https://leetcode.com/problems/max-area-of-island/

Category: DFS

<b>Solution: </b>Since it's a dfs problem, we will create a dfs function - check for these following conditions: 
1. (r,c) not in visited
2. r in range(ROWS) and c in range(COLS)
3. grid[r][c] == 1


```python
  visited.add((r, c))
  return (1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r + 1, c))
```

Call dfs function and check for max area
  
```python
  for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 1 and (r, c) not in visited:
          area = max(area, dfs(r, c))
```


