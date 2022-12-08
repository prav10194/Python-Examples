Link: https://leetcode.com/problems/permutation-in-string/

<b>Solution: </b>The best way to solve this problem would be to compare the hashmaps of s1 and the window of size len(s1) for s2. If they match, return true else move forward with the window (maintain 2 pointers for the window). 

```python
class Solution:

    def checkPermutation(self, freqStr1, str2):
        freqStr2 = Counter(str2)
        return freqStr1 == freqStr2

    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        freqStr1 = Counter(s1)

        while r <= len(s2) - 1:
            if self.checkPermutation(freqStr1, s2[l:r + 1]):
                return True
            l += 1
            r += 1
        return False
```
