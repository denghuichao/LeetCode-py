class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s_array = [s[i: i + k] for i in range(0, len(s), k)]
        return ''.join([s_array[i][::-1] if i % 2 == 0 else s_array[i] for i in range(len(s_array))])

s = Solution()
print s.reverseStr('abcdefg', 2)
