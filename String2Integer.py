class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        start = 0;
        while start < len(str) and str[start] == ' ':
            start+=1
        if start == len(str):
            return 0;

        res, sign, start = 0,  1 if str[start] == '-' else -1, start + 1 if str[start] in '-+' else start
        while start < len(str) and str[start] in '0123456789':
            if res < -214748364 or res == -214748364 and str[start] == '9':
                res = -2147483648
                break
            res = res * 10 - int(str[start])
            start += 1
        return sign * res if res > -2147483648 or res == -2147483648 and sign == 1 else 2147483647

s = Solution()
print s.myAtoi(" b11228552307")