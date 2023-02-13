<b>Link: </b>https://leetcode.com/problems/rotting-oranges/

<b>Solution: </b>We will apply BFS for this paticular problem. <br/>Count all the fresh oranges in the grid, that we will check for in case we miss any at the end, we will return -1 <br/>Append the rotten ones in the queue. <br/>After that we run the standard BFS code on our grid. 

<b> Code: </b>
```python
    time, fresh = 0, 0
    ROWS, COLS = len(grid), len(grid[0])
    q = collections.deque()
    
    # count all the fresh oranges and append the rotten ones in the queue. 
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append((r, c))
    
    while q and fresh > 0:
        x = len(q)
        for i in range(x):
            x, y = q.popleft()
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

            for dx, dy in directions:
                row, col = x + dx, y + dy
                if row not in range(ROWS) or col not in range(COLS) or grid[row][col] != 1:
                    continue
                grid[row][col] = 2
                fresh -= 1
                q.append((row, col))
        time += 1
    return time if fresh == 0 else -1
```

<b>Runtime: </b>Space Complexity: O(n^2) - Since in worst case we can have the whole grid full of rotten oranges and that will be the length of the queue. <br/>Runtime Complexity: O(n^2) - Since in  initial part of code, we are going through each and every cell to count the fresh and append the rotten. 
