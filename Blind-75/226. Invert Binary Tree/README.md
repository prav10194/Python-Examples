Link - https://leetcode.com/problems/invert-binary-tree/

Level - Easy

<b>Solution: Invert the nodes by passing the reference of left in right and right in left. Call the function recurvisely. </b>

```python
root.left,  root.right = root.right, root.left

self.invertTree(root.left)
self.invertTree(root.right)

return root
```
