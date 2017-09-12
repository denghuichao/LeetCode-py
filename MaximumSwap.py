#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/9/12'

class Solution(object):
    def maximumSwap(self, num):
        """
        Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
        Return the maximum valued number you could get.

        Example 1:
        Input: 2736
        Output: 7236
        Explanation: Swap the number 2 and the number 7.
        Example 2:
        Input: 9973
        Output: 9973
        Explanation: No swap.
        :type num: int
        :rtype: int
        """
        A = list(str(num))
        res = A[:]
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                A[j], A[i] = A[i], A[j]
                if A > res:res = A
                A[j], A[i] = A[i], A[j]

        return int(''.join(A))

    def maximumSwap_ON(self, num):
        A = list(map(int, str(num)))
        last = {x : i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, i) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int(''.join(map(str, A)))

        return num

s = Solution()
print(s.maximumSwap_ON(2736))

