Link: https://leetcode.com/problems/matchsticks-to-square/

Level: Medium

<b>Solution: Use backtracking with the decision tree as shown below: 
  
  <img width="883" alt="image" src="https://user-images.githubusercontent.com/8276139/174522622-daa01f56-b5b3-4c36-9835-286f661d94d4.png">
  
  Base condition: When index reaches the length of matchsticks array.
  <br>
  <br>
  Run a loop for each side - left, right, top and bottom
  <br>
  <br>
  Add the length of current index from the <i><u>sorted array</u></i> into the sides array if the length doesn't exceed the maxLength of a square side. 
  <br>
   <br>
  Call the backtrack with index + 1
  <br>
  <br> 
  Cleanup condition: Subtrack the length of current index from the sides array
  
  
