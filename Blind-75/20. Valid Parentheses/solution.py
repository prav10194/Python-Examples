class Solution:
    def isValid(self, s: str) -> bool:
        string_stack = []
        paranthesis = {')': '(', ']': '[', '}': '{'}     
        
        for c in s:
            if c in paranthesis.values():
                string_stack.append(c)
            else:
                if not string_stack or string_stack[-1] != paranthesis.get(c):
                    return False
                else:
                    string_stack.pop()
        return string_stack == []
