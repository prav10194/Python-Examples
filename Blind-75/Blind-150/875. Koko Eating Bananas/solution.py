class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 0, max(piles)
        speed = right
        
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        
        while left <= right:
            m = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            if hours <= h:
                speed = min(speed, m)
                right = m - 1
            else:
                left = m + 1
        return speed
        
