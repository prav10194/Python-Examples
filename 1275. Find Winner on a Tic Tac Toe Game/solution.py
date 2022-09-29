class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, cols = [0]*n, [0]*n
        d1, d2 = 0, 0
        player = 1
        
        for r, c in moves:
            rows[r] += player
            cols[c] += player
            
            if r == c:
                d1 += player
            if (r + c) == n - 1:
                d2 += player
            if abs(rows[r]) == n  or abs(cols[c]) == n or abs(d1) == n or abs(d2) == n:
                if player == 1:
                    return 'A'
                else:
                    return 'B'
            player *= -1
            
        if len(moves) == n*n:
            return 'Draw'
        else:
            return 'Pending'
            
        
