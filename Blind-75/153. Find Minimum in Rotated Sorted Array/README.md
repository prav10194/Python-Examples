Problem Statement: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Level: Medium

<b>Solution: The base condition would be when nums[l] < nums[r] - then return the left most. 
<br>                              
For the other cases, find middle and compare it with nums[l], if greater than that then minimum lies on the right else goes to left. 
</b>

