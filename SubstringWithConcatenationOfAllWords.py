"""
    You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of
    substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

    For example, given:
    s: "barfoothefoobarman"
    words: ["foo", "bar"]

    You should return the indices: [0,9].
    (order does not matter).
"""
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        dict_w = dict((w, words.count(w)) for w in set(words))
        wlen, sum_len, res = len(words[0]), len(words[0]) * len(words), []
        left = right = count = 0
        while right < len(s) - wlen:
            w = s[right: right + wlen]
            if w in dict_w:
                dict_w[w] = dict_w[w] - 1
                right += wlen
                if dict_w[w] >= 0:
                    count += 1
                if count == len(words):
                    count = 0
                    res.append(left)
                    left += 1
                    right = left
                    dict_w = dict((w, words.count(w)) for w in set(words))
            else :
                right += 1
                left  = right
        return res

s = Solution()
print(s.findSubstring("barfoofoobarthefoobarman", ["foo", "bar", "the"]))
