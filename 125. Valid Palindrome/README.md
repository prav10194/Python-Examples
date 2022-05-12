A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.



Solution: 

Create 2 pointers: Left and Right. Read one character from both sides - if they don't match return false. 

Space Complexity: O(1) ?? 

Time Complexity: O(n) ??

