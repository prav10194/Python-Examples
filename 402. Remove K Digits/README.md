Link: https://leetcode.com/problems/remove-k-digits/description/

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # monotonic increasing stack
        stack = []
        
        for digit in num:
            while stack and digit < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k:
            stack.pop()
            k -= 1

        res = '0' + ''.join(stack)

        return str(int(res))

```
