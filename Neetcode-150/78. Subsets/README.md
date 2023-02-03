Link: https://leetcode.com/problems/subsets/

<b>Solution: </b> Simple logic for backtracking, either we can add an element or we can chose not to add an element. 
Once we reach the index  == len(nums), we can append our tempSubset into our results and return. 

```python
  
  result = []
  tempSubset = []

  def backtrack(index):
      if index == len(nums):
          result.append(tempSubset.copy())
          return
      
      # path 1 - adding element
      tempSubset.append(nums[index])
      backtrack(index + 1)
      
      
      # path 2 - not adding an element
      tempSubset.pop()
      backtrack(index + 1)

  backtrack(0)
  return result

```
