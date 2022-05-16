class Solution:
    def isValid(self, s: str) -> bool:
        string_stack = []
        paranthesis_dict = {")": "(", "}": "{", "]": "["}
        
        for c in s: 
            if c == "(" or c == "{" or c == "[":
                string_stack.append(c)
            else:
                if paranthesis_dict.get(c) in string_stack:
                    string_stack.pop()
        return string_stack == []
