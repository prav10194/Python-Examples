Problem Link: https://leetcode.com/problems/unique-paths/

Level: Medium

Category: 2-D Dynamic Programming


<b>Solution: Using DP, if we visualize how the array would look like this - 


<br><br> So we can start with the bottom row as we see they are all 1s. Then move upwards to create other rows where each cell would have value from the right cell + bottom cell
<br><br>Create the topmost row and return row[0] as the answer. 



