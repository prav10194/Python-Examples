<b>Level: </b>Medium

<b>Category: </b>Sliding Window

<b>Space Complexity: </b>2 * O(l1) = O(l1), where l1 is the length of string 1 and l2 is the length of string 2. 
<br/><b>Time Complexity: </b>O(l1) + [O(l2 - l1) * O(l2)],  the first one is for the counter for string 1, the second is for the while loop and the third one is for the counter for string 2.

<b>Solution: </b>
<br/>A very basic solution to this problem involves creating a frequency counter of string 1 and a substring of string 2 with length = length of string 1. Compare both of them and return True if it matches. 
<br/>Solutioning it in Python is a little easier as we can use Counter(). 

```python
    def checkPermutation(self, freqStr1, str2):
        freqStr2 = Counter(str2) # create frequency counter of the sliding window
        return freqStr1 == freqStr2
    
    def checkInclusion(self, str1: str, str2: str) -> bool:
        l, r = 0, len(str1) - 1
        freqStr1 = Counter(str1) # creating frequency counter of string 1 outside the while as it remains unchanged

        while r <= len(str2) - 1:
            if self.checkPermutation(freqStr1, str2[l:r + 1]): # sending the sliding window to our function. To call a python function in same class we use self. 
                return True
            else:
                l += 1
                r += 1
        return False
```

