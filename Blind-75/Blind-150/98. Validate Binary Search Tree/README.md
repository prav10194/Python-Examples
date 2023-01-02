Link - https://leetcode.com/problems/validate-binary-search-tree/

<b>Solution: </b>We create a recursive function that takes in the current node and lowest possible value and highest possible value. <br/>We check for if current node value should be between left and right. If not, then return False. We call the recursive function twice. 

```python
def isValidBST(self, root: Optional[TreeNode]) -> bool:

    def isValid(n, left, right):
        if not n:
            return True

        if not (n.val > left and n.val < right):
            return False

        return (isValid(n.left, left, n.val) and isValid(n.right, n.val, right))

    return isValid(root, float('-inf'), float('inf'))
```

