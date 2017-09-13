"""
    Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

    For example,
    S = "ADOBECODEBANC"
    T = "ABC"
    Minimum window is "BANC".

    Note:
    If there is no such window in S that covers all characters in T, return the empty string "".
    If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c_dict = dict((letter, t.count(letter)) for letter in set(t))
        left = right = count = 0
        min_len = min_left = 10e9

        for right in range(len(s)):
            rc = s[right]
            if rc in c_dict:
                c_dict[rc] = c_dict[rc] - 1
                if c_dict[rc] >= 0:
                    count += 1
            while count == len(t):
                if right - left + 1 < min_len:
                    min_left = left
                    min_len = right - left + 1
                lc = s[left]
                if lc in c_dict:
                    c_dict[lc] = c_dict[lc] + 1
                    if c_dict[lc] > 0:
                        count -= 1
                left += 1
        return '' if min_len == 10e9 else s[min_left : min_left + min_len]

s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))