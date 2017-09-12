class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c_hash, count = set(), 0
        for c in s:
            if c in c_hash:
                count += 1
                c_hash.remove(c)
            else:
                c_hash.add(c)

        return count * 2 + 1 if  c_hash else count * 2