class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0;
        sign =  -1 if x >= 0 else 1
        x = -x if x > 0 else x
        for c in str(x)[1::][::-1]:
            if res < -214748364 or res == -214748364 and c == '9':
                return 0
            res = res * 10 - int(c)

        return res * sign if res > -2147483648\
            else res * sign if sign == 1\
            else 0

s = Solution()
print s.reverse(2147480007)