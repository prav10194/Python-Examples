1. Two Sum

<b>Solution: Create a hashmap to store (key, value) where <i>key = current number in array</i> and <i>value is current index</i>. <br>Before adding, check if target - num exists in hashmap.keys(). If yes, return with the current index and hashmap value.</b> 

Space Complexity: O(n)
Time Complexity: O(n)

167. Two Sum II - Input Array Is Sorted

<b> Solution: Keep two pointers, left and right. </b>

Space Complexity: O(1)
Time Complexity: O(n)
  
15. 3Sum

<b>Solution: Follow the approach for 2Sum II, sort the elements - O(n*logn). <br>Iterate over each element, keep two pointers left and right and find sum of all three.<br>If sum < 0, increase left pointer else if > 0 increase right pointer. If == 0, add it to set.</br> 

Space Complexity: O(n)
Time Complexity: O(n*logn)  
