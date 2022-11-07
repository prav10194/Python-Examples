Link: https://leetcode.com/problems/linked-list-cycle/description/

<b>Solution: </b> Run 2 pointers, fast and slow. While fast and fast.next - increment fast twice while slow is incremented once. Check if they are same, if yes then return True as cycle exists. Return False after while loop ends. 
