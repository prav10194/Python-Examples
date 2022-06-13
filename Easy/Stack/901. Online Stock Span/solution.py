class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if self.stack and self.stack[-1][1] <= price:
            span = 1
            while self.stack and self.stack[-1][1] <= price:
                index, oldPrice = self.stack.pop()
                span += index
            self.stack.append([span, price])
        else:
            self.stack.append([1, price])
        return self.stack[-1][0]
            
            
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
