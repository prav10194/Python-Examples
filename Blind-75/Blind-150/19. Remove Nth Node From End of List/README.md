Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

<b>Solution: </b>Since we have to do it in one pass - create 2 pointers fast and slow. Move fast by n indexes initially. <br/><br/>Now while fast.next - move the slow pointer. Where the slow pointer is after the while ends, remove the next node.
