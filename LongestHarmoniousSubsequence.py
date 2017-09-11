#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/9/11'

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_counts = {}
        ans = 0
        for n in nums:
            n_counts[n] = n_counts.get(n, 0) + 1

        for k in n_counts.keys():
            if n_counts.has_key(k + 1):
                ans = max(ans, n_counts[k] + n_counts[k + 1])

        return ans

s = Solution()
print(s.findLHS([1,3,2,2,5,2,3,7]))
