Link - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Level - Medium

<b>Solution: p and q are Nodes of the Tree. So if the value matches (or if p.val < root.val and q.val > root.val or vice-versa), return Root. Else iterate recursively to either left or right depending on the values being less than root or more than root. </b>
