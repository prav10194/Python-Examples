Link - https://leetcode.com/problems/subsets/

<b>Solution: </b><br/>For each element in nums, either we can add it in the subset or we don't - making the total number of subsets to be 2^n. 

<img width="917" alt="image" src="https://user-images.githubusercontent.com/8276139/210325416-32b08512-1232-411c-802e-14d79255e654.png">

<br/>The backtracking algorithm (takes in position of element) would be run twice with element appended and the other when element is not there. 
When index reaches length of array, append the temp subset into result.
