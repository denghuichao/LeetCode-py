#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/9/11'

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p:
            return []

        res = []
        c_count = [0 for i in range(256)]
        for c in p:
            c_count[ord(c)] += 1

        left, right, count = 0, 0, len(p)
        while right < len(s):
            if c_count[ord(s[right])] > 0:
                count -= 1
            c_count[ord(s[right])] -= 1
            right += 1

            if count == 0:
                res.append(left)

            if right - left == len(p):
                if c_count[ord(s[left])] >= 0 :
                    count += 1
                c_count[ord(s[left])] += 1
                left += 1

        return res

s = Solution()
print(s.findAnagrams("cbaebabacd", 'abc'))
