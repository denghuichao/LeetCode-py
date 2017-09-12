#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/9/12'
class Solution(object):
    def isBadVersion(version):
        pass

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        min_version, max_version = 1, n
        first_bad = n
        while min_version <= max_version:
            mid_version = min_version + (max_version - min_version) / 2
            if self.isBadVersion(mid_version):
                first_bad = min(first_bad, mid_version)
                max_version = mid_version - 1
            else:
                min_version = mid_version + 1
        return first_bad
