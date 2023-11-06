<b>Level: </b>Hard

<b>Category: </b>Sliding Window

<b>Space Complexity: </b>
<b>Time Complexity: </b>

<b>Solution: </b>
The logic for this problem mostly involves updating the pointers and optimizing. Let's look at the logic for updating the left and right pointers first. 
<br/>
<br/>
<b>Updating left and right pointers: </b>We will check the frequency count of "t" and "s" (just the windowSize) and return True if we are able to find all the keys from t in s (and also the frequency of a key in t should be <= frequency of the same key in s).

```python
freqStr1[s[r]] += 1 # to optimize we generate the frequency on fly vs. using Counter as it will give TLE for a few test cases
if self.checkSubstring(freqStr1, freqStr2):
    # rest of the code here
```

```python
def checkSubstring(self, freqStr1, freqStr2):
        for key in freqStr2:
            if freqStr1[key] < freqStr2[key]:
                return False
        return True
```

If returned False, we move the window by 1 on right and keep the left as it is. 

```python
if self.checkSubstring(freqStr1, freqStr2):
  # rest of the code here
else:
  r += 1
```
If True, means the current window is valid (might not be optimum). In this case, we check for len(minString) and update if the current window is smaller. We update only left pointer in this case by moving it by 1 but before doing that we update the frequency counter to remove the frequency of s[l] as we will update left pointer and also update s[r] as while loop by default increment s[r] in frequency and since we didn't update index of r, this will be repeated again in next while iteration.

```python
if self.checkSubstring(freqStr1, freqStr2):
  if len(s[l:r + 1]) < len(minString):
      minString = s[l:r + 1]
  freqStr1[s[l]] -= 1
  freqStr1[s[r]] -= 1
  l += 1
```

<i>Note: For else condition when we update right pointer, we won't decrement the frequency of s[r] as the window is moving in a positive direction. Only when we update left pointer we do this as window doesn't have s[l] anymore. </i>

<b>Complete code</b>

```python
def checkSubstring(self, freqStr1, freqStr2):
    for key in freqStr2:
        if freqStr1[key] < freqStr2[key]:
            return False
    return True
        
def minWindow(self, s: str, t: str) -> str:
    l, r = 0, 0
    minString = ""
    freqStr2 = Counter(t)
    freqStr1 = defaultdict(int)
    if len(t) > len(s):
        return ""

    while r <= len(s) - 1:
        # print(str(freqStr1))
        freqStr1[s[r]] += 1
        if self.checkSubstring(freqStr1, freqStr2):
            if not minString:
                minString = s[l:r + 1]
            if len(s[l:r + 1]) < len(minString):
                minString = s[l:r + 1]
            freqStr1[s[l]] -= 1
            freqStr1[s[r]] -= 1
            l += 1
        else:
            r += 1
        
    return minString
```
