Problem link: https://leetcode.com/problems/merge-intervals/

Level: Medium

Category: Intervals

<b>Solution: Sort the intervals based on the start date. After that run through the intervals and compare the first and second interval to see if they overlap, if yes merge the first interval with second. Append to result in case there is no overlap. <br>Can be done in-place too. </b>
