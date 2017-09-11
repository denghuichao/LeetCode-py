#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/9/11'


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ziped = [a == b for (a, b) in zip(nums, sorted(nums))]
        return 0 if all(ziped) else len(ziped) - ziped[::-1].index(False) - ziped.index(False)
