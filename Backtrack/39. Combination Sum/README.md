<b>Link: </b>https://leetcode.com/problems/combination-sum/

<b>Level: </b>Medium

<b>Category: </b>Backtrack

<b>Solution: </b>Recognizing the pattern for backtracking. In this case it would look something like this - 

<img width="961" alt="image" src="https://user-images.githubusercontent.com/8276139/210379944-59a8e0c3-7ba0-4f86-b689-74cc410d92e5.png">

So we can either add an element and keep the index as it is without incrementing (as we can have repeated values) or we can not add it and move to the next element. 

<b>The recursive function will keep track of the index as well as the tempSum. </b>

The break condition would be when 
* tempSum == target: append the current copy of temp subset in results and return
* if tempSum > target or index == len(candidates): just return

```python
results = []

tempSubset = []

def bt(index, tempSum):

    if tempSum == target:
        results.append(tempSubset.copy())
        return

    if index == len(candidates) or tempSum > target:
        return

    tempSubset.append(candidates[index])
    bt(index, tempSum + candidates[index])

    tempSubset.pop()
    bt(index + 1, tempSum)

bt(0, 0)
return results
```
