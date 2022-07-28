Problem link: https://leetcode.com/problems/meeting-rooms/

Level: Easy

Category: Intervals

<b>Solution: The meeting rooms must be sorted based on start times. Keep a tracker for storing the first meeting end time. Iterate through the list, return false if start time < tracker. If not, update tracker with new end time. Return true in the end. </b>
