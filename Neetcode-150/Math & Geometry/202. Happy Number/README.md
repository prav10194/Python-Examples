<b>Level:</b> Easy

<b>Solution #1:</b> 
<br/>We need to create a set and store each calculated value (sum of each digit squared). 
<br/> If we find the value = 1, return True. 
<br/>If we find calculated value already in set, return False

```python3
 def squaredSum(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output

def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.squaredSum(n)
            if n == 1:
                return True
        return False
```
