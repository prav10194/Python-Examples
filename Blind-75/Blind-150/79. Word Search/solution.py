class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLUMNS = len(board), len(board[0])
        visited = set() # (r, c)
        
        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLUMNS 
                or (r, c) in path or word[i] != board[r][c]): 
                return False
            
            visited.add((r, c))
            res = (backtrack(r + 1, c, i + 1) or 
                  backtrack(r, c + 1, i + 1) or 
                  backtrack(r - 1, c, i + 1) or 
                  backtrack(r, c - 1, i + 1))
            visited.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLUMNS):
                if backtrack(r, c, 0):
                    return True
        return False
        
            
