Problem Link: https://leetcode.com/problems/unique-paths/

Level: Medium

Category: 2-D Dynamic Programming


<b>Solution: Using DP, if we visualize how the array would look like this - 
<img width="662" alt="image" src="https://user-images.githubusercontent.com/8276139/178165266-45519eaa-309c-4111-a75c-b657bdea77a8.png">


<br><br> So we can start with the bottom row as we see they are all 1s. Then move upwards to create other rows where each cell would have value from the right cell + bottom cell
<br><br>Create the topmost row and return row[0] as the answer. 



