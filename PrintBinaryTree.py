# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        h = self.height(root)
        w = pow(2, h) - 1
        res = [['' for _ in range(w)] for __ in range(h)]
        self.print_helper(res, 0, 0, w - 1, root)
        return res

    def print_helper(self, lists, d, start, end, root):
        if root:
            mid = (start + end ) >> 1
            lists[d][mid] = str(root.val)
            if root.left:
                self.print_helper(lists, d + 1, start, mid - 1, root.left)
            if root.right:
                self.print_helper(lists, d + 1, mid + 1, end, root.right)

    def height(self, root):
        return 0 if not root else 1 + max(self.height(root.left), self.height(root.right))

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.right = TreeNode(5)
s = Solution()
print(s.printTree(root))