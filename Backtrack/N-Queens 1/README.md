51. N-Queens
Hard

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]]

 

Constraints:

    1 <= n <= 9

<b>Solution: This is a backtrack problem. We will be backtracking on row number as there can be only one Queen in one row. 
Create three sets for column, positive diagonal (r+c will be same) and negative diagonal (r-c will be same). 
For each row, don't add into the set if either of c, r+c or r-c is not unique. Add if unique, and backtrack to next row. In case of duplicate, remove the last added value and repeat the process.</b>
