class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(s)+1):
            curr = int(s[i-1])
            prev = int(s[i-2])
            if curr != 0:  # valid single number
                dp[i] += dp[i-1]
            if prev != 0 and prev * 10 + curr <= 26:  # valid double number
                dp[i] += dp[i-2]
        return dp[len(s)]
