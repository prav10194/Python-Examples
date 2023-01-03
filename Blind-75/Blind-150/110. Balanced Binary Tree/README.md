Link - https://leetcode.com/problems/balanced-binary-tree/

<b>Solution: </b>We need a recursive function. 

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            
            if not root: 
                return [0, True]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1
            return [1 + max(left[0], right[0]), balanced]
        
        return dfs(root)[1]
```
