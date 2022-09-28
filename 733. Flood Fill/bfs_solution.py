class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        ROWS, COLS = len(image), len(image[0])
        oldColor = image[sr][sc]
        image[sr][sc] = color
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            
            while q:
                row, col = q.popleft()
                
                for x, y in directions:
                    if (row + x) in range(ROWS) and (col + y) in range(COLS) and image[row + x][col + y] == oldColor:
                        image[row + x][col + y] = color
                        q.append((row + x, col + y))
                
        bfs(sr, sc)
        return image
