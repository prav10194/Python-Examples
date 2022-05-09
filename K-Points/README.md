README: https://github.com/Seanforfun/Algorithm-and-Leetcode/blob/master/leetcode/973.%20K%20Closest%20Points%20to%20Origin.md

Solution: 

```python
points = [[1,-2], [2,0], [1,1], [0,2], [2,2]]

points.sort(key = lambda K: K[0]*K[0] + K[1]*K[1])
```
