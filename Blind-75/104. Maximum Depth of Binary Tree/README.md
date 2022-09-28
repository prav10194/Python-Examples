Link - https://leetcode.com/problems/maximum-depth-of-binary-tree/

Level - Easy

<b>Solution: Recursively iterate to calculate the length of both left and right trees. Then find the max and increase it by one to find the actual length. </b>

```python

lh = self.calculateDepth(self.left)
rh = self.calculateDepth(self.right)
return max(lh + rh) + 1

```
