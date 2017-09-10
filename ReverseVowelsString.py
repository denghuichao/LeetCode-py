class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_pos = [i for i in range(len(s)) if s[i] in 'aeiouAEIOU']
        i, j = 0, len(vowels_pos) - 1
        res = [a for a in s]
        while i < j:
            res[vowels_pos[i]], res[vowels_pos[j]] = res[vowels_pos[j]], res[vowels_pos[i]]
            i, j = i + 1, j - 1

        return ''.join(res)


s = Solution()
print s.reverseVowels('leetcode')

