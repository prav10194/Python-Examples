Problem link: https://leetcode.com/problems/find-median-from-data-stream/

Level: Hard

Category: Heap

Company: 

<b>Solution: We will use 2 heaps to solve the issue. One heap will be to store the smaller numbers, another to store the larger numbers.<br>
Python only lets us create min-heaps. So for max heap, save each element as -1 * val<br>
We will check for 2 conditions - first will be to check if on adding a number to max heap (which is done by default) the max in max heap should be less than min in min heap. If not, move the element. <br>
The second condition will be if difference in size of the heaps shouldn't be more than 1 - if not, move elements. 
<br><br>
For median, there will be 3 conditions - if size is unequal, the extra element will be the median. If size is equal, sum of max in max heap and min in min heap + divided by 2
