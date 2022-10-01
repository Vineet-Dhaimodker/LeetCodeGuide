class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        start = 0
        maxL = 0
        for i, ch in enumerate(s):
            if ch not in curr:
                curr.add(ch)
            else:
                maxL = len(curr) if maxL < len(curr) else maxL
                while s[start] != ch:
                    curr.remove(s[start])
                    start += 1
                start += 1
        maxL = len(curr) if maxL < len(curr) else maxL
        return maxL