Link: https://leetcode.com/problems/number-of-islands/

<b>Solution: </b>We can use DFS to solve the problem (also can be solved using BFS). 
* The logic for the algorithm is simple where we run a DFS algorithm on all our nodes. 
* We check in all 4 directions from our current node.   


```python
  ROWS, COLS = len(grid), len(grid[0])
  visited = set()
  islands = 0

  def dfs(row, col):
      
      # check for all conditions for which we don't add the node to visited and do a return
      if row not in range(ROWS) or col not in range(COLS) or grid[row][col] != "1" or (row, col) in visited:
          return 
      
      # add current node in visited
      visited.add((row, col))
      
      # define 4 directions
      directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
      for dx, dy in directions:
          # call dfs with all 4 directions
          dfs(row + dx, col + dy)

  for m in range(ROWS):
      for n in range(COLS):
          if grid[m][n] == "1" and (m, n) not in visited:
              islands += 1
              dfs(m, n)

  return islands
```
