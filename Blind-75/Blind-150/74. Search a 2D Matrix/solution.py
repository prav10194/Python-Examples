class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS - 1
        
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        else:
            row = (top + bot) // 2
            left, right = 0, len(matrix[row])
            
            while left <= right:
                middle = (left + right) // 2
                if target < matrix[row][middle]:
                    right = middle - 1
                elif target > matrix[row][middle]:
                    left = middle + 1
                else:
                    return True
        
