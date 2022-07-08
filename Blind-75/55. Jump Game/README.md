Problem Link: https://leetcode.com/problems/jump-game/

Difficulty: Medium

Category: Greedy

<b>Solution: <br><br>Define goal to be the last index. Now start from the back, if current index + value of index >= goal, change goal to current index. <br>Return True ig goal == 0. </b>
