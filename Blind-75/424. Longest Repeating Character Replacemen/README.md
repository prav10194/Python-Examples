Problem Link: https://leetcode.com/problems/longest-repeating-character-replacement/

Level: Medium

Category: Sliding window

<b>Solution: A hashmap has to be created that will store the word count of each letter. 
<br><br>We would have to look for (length of substring) - max frequency word should be greated than k. <br>Iterate and find left and right till this condition is satisfied, when it is not compute result by finding length of the remaining substring. <br>Compare it with max value of result. 
</b>
