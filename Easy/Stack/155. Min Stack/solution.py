class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        if self.minstack:
            if val < self.minstack[-1]:
                self.minstack.append(val)
            else:
                self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
