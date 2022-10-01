class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closingMap = {')': '(', ']': '[', '}': '{'}
        for p in s:
            if p in closingMap:
                if (stack and stack[-1]) == closingMap[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return True if not stack else False
