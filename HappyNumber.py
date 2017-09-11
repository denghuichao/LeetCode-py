class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        meet = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in meet:
                return False
            meet.add(n)

        return True

s = Solution()
print (s.isHappy(20))
