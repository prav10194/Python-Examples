Medium

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:

Input: n = 1, k = 1
Output: [[1]]

 

Constraints:

    1 <= n <= 20
    1 <= k <= n


<b>Solution: We will use backtrack alogorithm to solve this. 
  The base condition would be when length of our local combincation == k. Store a copy in results array. 
  <br>
  We will run a for loop from start to n where start will move by 1 in every recusrive call to avoid adding the same element again. We will append element at position i, backtrack and then pop. 
</b>
  
