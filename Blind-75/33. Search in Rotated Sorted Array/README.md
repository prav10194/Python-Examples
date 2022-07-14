Problem link - https://leetcode.com/problems/search-in-rotated-sorted-array/

Level - Medium

Category - Binary Search

<b> Solution: Divide problem by searching in either left sorted array (if nums[left] <= nums[middle]) or right sorted array. 
<br><br>For left sorted array, if target > nums[middle] or < nums[left], target index will be on right else it will be in left array
<br><br>Similar for right sorted array, if target < nums[middle] or > nums[right], target index will be on left else right. 
<br><br>Base condition will be target == nums[middle]
  </b>
                                                                                                    
