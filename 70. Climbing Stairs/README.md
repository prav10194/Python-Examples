Link: https://leetcode.com/problems/climbing-stairs/description/

<b>Solution: </b>If we look at the pattern, 

In case there is 1 step: total ways = 1 way (0->1)<br/>
In case there are 2 steps: total ways = 2 ways (0->2, 0->1->1)<br/>
In case there are 3 ways: total ways = 3 ways (0->2->1, 0->1->1->1, 0->1->2)<br/>
In case there are 4 ways: total ways = 5 ways (0->1->1->1->1, 0->2->2, 0->1->2->1, 0->1->1->2, 0->2->1->1)<br/>

So pattern is totalSteps (n) = totalSteps (n - 1) + totalSteps (n - 2)<br/>

So it's a fibonacci sequence. <br/>

```python
def climbStairs(self, n: int) -> int:
    a,b = 0, 1
    count = 0
    for index in range(n): 
        count = a + b
        a = b
        b = count
    return count
```
