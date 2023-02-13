<b>Link: </b>https://leetcode.com/problems/walls-and-gates/

<b>Solution: </b>We will apply BFS to solve this problem. <br/>Step 1 - would be to append all the gates in the deque on which we will run our BFS algorithm. <br/>Step 2 - Calculate the distance and update the rooms matrix for all the cells that are != -1. 

<b>Code: </b>

```python
ROWS, COLS = len(rooms), len(rooms[0])
visited = set()

q = collections.deque()

for row in range(ROWS):
    for col in range(COLS):
        if rooms[row][col] == 0:
            q.append((row, col))
            visited.add((row, col))

dist = 0
while q: 
    for i in range(len(q)):
        x, y = q.popleft()
        rooms[x][y] = dist

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for dx, dy in directions: 
            row = x + dx
            col = y + dy
            if row not in range(ROWS) or col not in range(COLS) or rooms[row][col] == -1 or (row, col) in visited:
                continue
            visited.add((row, col))
            q.append((row, col))
    dist += 1
```

<b>Algorithm analysis: </b></br> Space Complexity - </br>Run Complexity - 
