Problem link: https://leetcode.com/problems/non-overlapping-intervals/

Level: Medium

Category: Intervals

<b>Solution: <br><br>Sort the intervals based on startTime. 
<br>Compare the startTime on next interval with previous and increment the counter in case they overalp. 
<br>Update the endTime with the minimum of the current endTime vs. previous end time to know which one ends sooner. We remove the one which ends later. 
