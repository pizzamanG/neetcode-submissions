class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {'(': ')', '[': ']', '{': '}'}
        for ch in s:
            if ch in mappings:
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if ch != mappings[top]:
                    return False
        return len(stack) == 0



        