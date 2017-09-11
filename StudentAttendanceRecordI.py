import re
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern = re.compile(r'.*LLL.*')
        return s.upper().count('A') <= 1 and not pattern.match(s)

s = Solution()
print (s.checkRecord("PPALLLP"))
