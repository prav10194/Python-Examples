Link: https://leetcode.com/problems/next-greater-element-i

Level - Easy

Category: Array/Stack

<b>Solution: </b>
Create a hashmap of nums1 with value as key, index as the value. 

Need to maintain a stack that will keep the values of nums2 array - 
* add value to stack if current value in nums2 is less than the top value in stack
* Pop value otherwise
    * While popping - get index of the popped value from hashmap and insert the current value at that index in res array
 
