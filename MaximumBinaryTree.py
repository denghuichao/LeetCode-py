from functools import reduce


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        m = max(nums)
        index = nums.index(m)
        root = TreeNode(m)
        root.left = self.constructMaximumBinaryTree(nums[:index:])
        root.right = self.constructMaximumBinaryTree(nums[index + 1::])
        return root


s = Solution()
root = s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
print(root)
