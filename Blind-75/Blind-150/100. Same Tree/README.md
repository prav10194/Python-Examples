Link - https://leetcode.com/problems/same-tree/

<b>Solution: </b>Iteratively check for each value in both the trees. <br/><br/>* If both nodes are None then it means the end and return True. <br/>* If one of the nodes are None, then return False. <br/>* If value is not equal, then return False. <br/>* Call the iterative function for both the trees. 
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
