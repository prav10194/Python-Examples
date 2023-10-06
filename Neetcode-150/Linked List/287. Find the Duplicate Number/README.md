<b>Level: </b>Medium/Hard

<b>Solution: </b>
<br/><br/>This is a classic Floyd's problem of detecting the entrance of the cycle. According to the algorithm, 
<br/>The distance of the node entrance of a cycle from start = Distance of the entrance from where fast and slow pointers first met. Based on this we can solve this problem. 
<br/><br/><b>Proof: </b>

![image](https://github.com/prav10194/Python-Examples/assets/8276139/96554e43-656f-4391-a279-7c5ef424498d)

Now we know the slow pointer is moving twice as slow as fast. So,

2 (slow) = fast

Total distance covered by slow pointer (at the point of intersection), <b>Y + X - Z</b>

Total distance covered by fast pointer (at the point of intersection), <b>Y + X + (X - Z)</b> (because the fast pointer will cover the cycle once before intersecting)

Now based on the initial equation, 

2 (Y + X - Z) = Y + X + (X - Z)

2Y + 2X - 2Z = Y + 2X - Z

Y - Z = 0

Y = Z

<b>Python code: </b>

```python

f, s = nums[0], nums[0]

while True:
    s = nums[s]
    f = nums[nums[f]]
    if s == f:
        break

s = nums[0]

while s != f:
    s = nums[s]
    f = nums[f]

return s
```
