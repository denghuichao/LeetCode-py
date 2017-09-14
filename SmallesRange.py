from heapq import *
class Solution(object):
    def smallestRange(self, nums):
        """
        You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number
        from each of the k lists.

        We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.
        List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
        List 2: [0, 9, 12, 20], 20 is in range [20,24].
        List 3: [5, 18, 22, 30], 22 is in range [20,24].
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        ptr = [0 for i in range(0, len(nums))]
        minrange = min_val = max_val = 10e9
        start, end = -10e9, 10e9
        while True:
            temp_array = [nums[i][ptr[i]] for i in range(len(ptr))]
            min_val, max_val = min(temp_array), max(temp_array)
            min_index = temp_array.index(min_val)
            if max_val - min_val < minrange:
                minrange = max_val - min_val
                start, end = min_val, max_val
            ptr[min_index] += 1
            if ptr[min_index] == len(nums[min_index]):
                break

        return start, end

    def smallestRange_priority(self, nums):
        # i stores the current index of the jth list
        ptr = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapify(ptr)

        ans = -10e9, 10e9
        # end keeps the max num of the candinate range
        end = max(row[0] for row in nums)
        while ptr:
            start, i, j = heappop(ptr)
            if end - start < ans[1] - ans[0]:
                ans = start, end
            if j + 1 == len(nums[i]):
                break
            end = max(end, nums[i][j+1])
            heappush(ptr, (nums[i][j+1], i, j + 1))

        return ans

s = Solution()
print(s.smallestRange_priority([[4, 10, 15, 24,26], [0, 9, 12, 20], [5, 18, 22, 30]]))
