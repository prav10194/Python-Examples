Link - https://leetcode.com/problems/valid-parentheses/

<b>Solution: Hashmap to store the closing bracket. <br/>
Run conditions to check if it's an opening bracket - store it in list. <br/>
If closing bracket, check condition - if last element in list is dictionary value of element then continue, else return False. <br/>
After return stack==[].   </b>
