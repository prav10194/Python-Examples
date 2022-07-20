Problem Link: https://leetcode.com/problems/search-a-2d-matrix/

<b>Solution: First do a binary search on the rows of matrix to find which row would have the value. Then using that information run a binary search on the 1D array to check if target is there in that row or not. 
</b>
<br><br>
Time Complexity: O(log m * log n)<br>
Space Complexity: O(1)
