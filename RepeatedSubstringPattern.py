import re
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for k in range(1, len(s) / 2 + 1):
            s_array = [s[i: i + k] for i in range(0, len(s), k)]
            if 1 < len(s_array) == s_array.count(s_array[0]) :
                return True

        return False

s = Solution()
print (s.repeatedSubstringPattern('abcabcabcabc'))
