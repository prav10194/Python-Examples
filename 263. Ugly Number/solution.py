class Solution:
    def isUgly(self, n: int) -> bool:
        prime_nums = [2,3,5]
        
        while n > 1: 
            temp = n
            for x in prime_nums: 
                if n % x == 0:
                    n = n / x
            if n == temp:
                return False
        return True
