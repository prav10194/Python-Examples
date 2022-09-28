class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        ROWS, COLS = len(image), len(image[0])
        oldColor = image[sr][sc]
        if oldColor == color: return image
        def dfs(r, c):
            if image[r][c] == oldColor: 
                image[r][c] = color
                if r > 0: dfs(r - 1, c)
                if r < ROWS - 1: dfs(r + 1, c)
                if c > 0: dfs(r, c - 1)
                if c < COLS - 1: dfs(r, c + 1)
                
        dfs(sr, sc)
        return image
