Link - https://leetcode.com/problems/count-good-nodes-in-binary-tree/

<b>Solution: </b>Definition of good node - Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.<br/>We need to build a recursive solution to count the total number of good nodes.<br/><br/><b>Logic: </b><br/>* In the recusrive function we pass node as well as current max value. Store result in a variable. <br/>* Increment everytime the current node value >= max value.<br/>* Update the max value. 

```python
def goodNodes(self, root: TreeNode) -> int:
  
    def dfs(n, maxVal):

        if not n:
            return 0

        res = 1 if n.val >= maxVal else 0
        maxVal = max(n.val, maxVal)

        res += dfs(n.left, maxVal)
        res += dfs(n.right, maxVal)

        return res

    return dfs(root, root.val)
```
