class Solution(object):
    """
    Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of
    which the sum ≥ s. If there isn't one, return 0 instead.

    For example, given the array [2,3,1,2,4,3] and s = 7,
    the subarray [4,3] has the minimal length under the problem constraint.
    """
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        min_len = 0
        left, cur_sum = 0, 0
        for right in range(len(nums)):
            cur_sum += nums[right]
            if cur_sum >= s:
                while cur_sum >= s:
                    min_len = right - left + 1 if min_len == 0 or min_len > right - left + 1\
                        else min_len
                    cur_sum -= nums[left]
                    left += 1
        return min_len

s = Solution()
print(s.minSubArrayLen(1, [2,3,1,2,4,3]))
