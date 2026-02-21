class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if pairs[i] != top:
                    return False
        if stack:
            return False
        else:
            return True
        
