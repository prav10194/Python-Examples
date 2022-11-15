Link: https://leetcode.com/problems/valid-anagram/

Level: Easy

Category: Array and Hashing

<b>Solution: </b>Create 2 hashmaps and insert elements. Compare them in the end. 
<br/>
Complexity - Time: O(n)
<br/>
Space: O(n)

Another solution - 
```python
return sorted(s) == sorted(t)
```
<br/>
Complexity - Time: O(nlogn)
<br/>
Space: O(1)

