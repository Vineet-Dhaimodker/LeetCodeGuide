class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            s=list(str(x))
            if s==s[::-1]:
                return True
            else:
                return False