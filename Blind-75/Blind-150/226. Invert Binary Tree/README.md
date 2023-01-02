Link - https://leetcode.com/problems/invert-binary-tree/

<b>Solution: </b>Intutive solution. Recursive call to the main function, each time swapping the left and right pointers. Return None if there is no node. 

```python
 def invertTree(self, root):
    
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)
    
    return root
```
