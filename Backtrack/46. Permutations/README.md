<b>Level: </b>Medium

<b>Category: </b>Backtrack

<b>Space Complexity: </b>
<br/><b>Time Complexity: </b>

<b>Solution: </b><i>Note: This is a slightly different approach than the one in solution.py</i>
<br/><br/>Every backtracking problem follows the same pattern. We need to figure out these things: 

<b>1. Find out what will be the parameter on which the backtrack will run (and break): </b>For permutations, we will pass the temp list that stores the current permutation as the parameter. 

```python
def bt(tempPermutation):
 # main logic here
```

<b>2. The condition when we will exit the backtrack and append the result - also known as break condition: </b>When the length of the current permutation equals the length of our nums array,  we will append the temp permutation into our main result and return. 

```python
if len(tempPermutation) == len(nums):
  permutations.append(tempPermutation.copy())
  return
```

<b>3. All the possible scenarios when we call the backtrack function: </b>Since each permutation should contain each element from our input array, we will iterate over the nums array and append it in our temp permutation if the element has not been in it yet. We call bt() just once with our updated temp combination. 

```python
for num in nums:
  if num not in tempPermutation:
      tempPermutation.append(num)
      bt(tempPermutation)
      tempPermutation.pop()
```

<b>4. The initial parameter passed to start the backtrack: </b>We will start with an empty list initially. 

```python
bt([])
```

<br/><b>Complete code: </b>

```python
permutations = []
def bt(tempPermutation):
    if len(tempPermutation) == len(nums):
        permutations.append(tempPermutation.copy())
        return
    
    for num in nums:
        if num not in tempPermutation:
            tempPermutation.append(num)
            bt(tempPermutation)
            tempPermutation.pop()

bt([])
return permutations
```
