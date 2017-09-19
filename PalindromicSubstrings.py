#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/9/13'
class Solution(object):
    def countSubstrings(self, s):
        """
        1 2 1
        :type s: str
        :rtype: int
        """
        n, res= len(s), 0
        dp = [[False for i in range(n)] for j in range(n)]
        for i in [n - 1 - k for k in range(n)]:
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1])
                if dp[i][j]:res += 1
        return res

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp =  [[False for i in range(n)] for j in range(n)]
        start, end = 0, 0

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1])
                if dp[i][j] and j - i > end - start:
                    start, end = i, j
        return s[start:end+1]

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [1 for i in range(n)]
        for i in range(n - 1, -1, -1):
            pre = dp[i]
            for j in range(i + 1, n):
                temp = dp[j]
                dp[j] = (2 if j - i == 1 else 2 + pre) if s[i] == s[j] \
                        else max(dp[j - 1], dp[j])
                pre = temp

        return dp[n-1]



s = Solution()
print(s.countSubstrings('abc'))
print(s.longestPalindrome('"fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"'))
print(s.longestPalindromeSubseq('bbbab'))
