<b>Level: </b>Easy

<b>Category: </b>Sliding Window

<b>Space Complexity: </b>O(1)
<b>Time Complexity: </b>O(n)

<b>Solution: </b>Simple problem where we need to maintain a sliding window to track the lowest and maximum stock prices. 
<br/>Our sliding window starts by maintaining left and right as 0 and 1 respectively. We also maintain 2 extra variables - finalProfit and tempProfit (this will be for the loop). 

```python
finalProfit = 0
tempProfit = 0

l, r = 0, 1
```

Our main logic will calculate tempProfit of current left and right values and update finalProfit if needed. 

```python
while r <= len(prices) - 1:
  tempProfit = prices[r] - prices[l]
  if tempProfit > finalProfit:
      finalProfit = tempProfit
```

Now to move our pointers, we will check if value at left < value at right, in that case only the right pointer is updated. If the value at left > value at right, then we set left = right and increase right by 1. 

```python
if prices[l] < prices[r]:
    r += 1
else:
    l = r
    r += 1
```

Complete code

```python
def maxProfit(self, prices: List[int]) -> int:

        finalProfit = 0
        tempProfit = 0

        l, r = 0, 1

        while r <= len(prices) - 1:
            tempProfit = prices[r] - prices[l]

            if tempProfit > finalProfit:
                finalProfit = tempProfit
            
            if prices[l] < prices[r]:
                r += 1
            else:
                l = r
                r += 1
        
        return finalProfit
```
