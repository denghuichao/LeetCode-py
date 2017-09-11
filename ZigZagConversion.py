class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lines = [[] for i in range(numRows)]
        period = 1 if numRows == 1 else numRows * 2 - 2
        for i in range(len(s)):
            r = i % period
            if r < numRows:
                lines[r].append(s[i])
            else:
                lines[numRows - 2 - (r - numRows)].append(s[i])
        return ''.join(''.join(line) for line in lines)

s = Solution()
print(s.convert("PAYPALISHIRING", 2))
