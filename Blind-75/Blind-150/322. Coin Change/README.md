Link: https://leetcode.com/problems/coin-change/

<b>Solution: </b>

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            
            min_cost = float('inf')

            for coin in coins:
                res = dfs(rem - coin)
                if res != -1:
                    min_cost = min(min_cost, res + 1)
            
            if min_cost != float('inf'):
                return min_cost
            else:
                return -1
        return dfs(amount)
```
