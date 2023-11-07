 <b>Link: </b>https://leetcode.com/problems/subsets/
<br/><br/><b>Level: </b>Medium
<br/><br/><b>Category: </b>Backtrack
<br/><br/>
<b>Solution: </b><br/>For each element in nums, either we can add it in the subset or we don't - making the total number of subsets to be 2^n. 

<img width="500" alt="image" src="https://user-images.githubusercontent.com/8276139/210325416-32b08512-1232-411c-802e-14d79255e654.png">

<br/>For most of the backtracking problems, we need to figure out these things: 

<b>1. Find out what will be the parameter on which the backtrack will run (and break): </b> In this case, we would pass current index as a parameter. 

```python
def backtrack(index):
  # rest of the code here
```

<br/><b>2. The condition when we will exit the backtrack and append the result - also known as break condition: </b>In this problem it be when the current index == length of the array, as that would mean we don't have any elements to add (or to not add). 

```python
if index == len(nums):
 subsets.append(tempSubset.copy())
 return
```


<br/><b>3. All the possible scenarios when we call the backtrack function: </b>In our case we have 2 possible conditions on which we will backtrack<br/>a) if element is added and b) if nothing is added. The index is incremented by 1 on each recursive call. 

```python
tempSubset.append(nums[index])
backtrack(index + 1)

tempSubset.pop()
backtrack(index + 1)
```

<br/><b>4. Initial parameter passed to start the backtrack: </b>We will pass index = 0 to start from the left most element in the array.

```python
backtrack(0)
```

<br/><br/><b>Complete code: </b>

```python
subsets = []
tempSubset = []

def backtrack(index):
  if index == len(nums):
      subsets.append(tempSubset.copy())
      return
  
  tempSubset.append(nums[index])
  backtrack(index + 1)

  tempSubset.pop()
  backtrack(index + 1)

backtrack(0)

return subsets
```

