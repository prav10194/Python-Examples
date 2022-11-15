Link: https://leetcode.com/problems/group-anagrams/description/

<b>Solution: </b>

```python
hm = defaultdict(list)
  for s in strs:
    hm[str(sorted(s))].append(s)
        
  return hm.values()
```
