Level: Medium

Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

<b>Solution: Sliding window problem, create 2 pointers l and r and use set to check if character exists. Create maxLength for storing the amximum length. <br>If doesn't exists, place it in the set and calculate length. If exists, set the variables back to next position and find max of maxLength and tempLength. Return will have max of maxLength and (r - l). </b>
