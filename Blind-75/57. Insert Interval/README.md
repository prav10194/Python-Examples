Problem Link: https://leetcode.com/problems/insert-interval/

Level: Medium

Category: Intervals

<b>Solution: The slots are sorted in ascending order based on start date. There can be three conditions for the newInterval: 
<br>if endTime < current interval startTime: <i>append in result and return all the other intervals as it is.</i>
<br>elif startTime > current interval endTime: <i>append in result.</i>
<br>else overlap: <i>update newInterval with correct startTime and endTime.</i>
  
</b>
