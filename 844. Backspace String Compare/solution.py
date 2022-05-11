class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(inputString: str) -> str:
            ans = []
            for c in inputString:
                if c!='#':
                    ans.append(c)
                else:
                    ans.pop()
            return "".join(ans)
        return build(s) == build(t)
