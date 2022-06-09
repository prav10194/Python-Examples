class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        
        path = path.replace('//','/')
        
        for dir in path.split('/'):
            if dir:
                if dir == '..':
                    if stack:
                        stack.pop() 
                else:
                    if dir != '.':
                        stack.append(dir)
        
        return '/' + '/'.join(stack)
