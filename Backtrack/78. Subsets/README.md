Medium

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.

<b>Solution: For each element in nums, either we can add it in the subset or we don't - making the total number of subsets to be 2^n. 
The backtracking algorithm (takes in position of element) would be run twice with element appended and the other when element is not there. 
When index reaches length of array, append the temp subset into result. </b>
