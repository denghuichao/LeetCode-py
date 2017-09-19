#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/9/11'

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums1, nums2 = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i] + 1:
                nums1[i] = nums1[i + 1]
                nums2[i + 1] = nums2[i]

        return nums1 == sorted(nums1) or nums2 == sorted(nums2)

s = Solution()
print(s.checkPossibility([1, 2, 4, 1,3]))
