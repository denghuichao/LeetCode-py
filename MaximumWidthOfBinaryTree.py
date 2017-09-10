# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = []
        max_width = 0
        if root:
            queue.append(root)

        while len(queue) > 0:
            size = len(queue)
            left = -1
            right = -1
            for i in range(size):
                node = queue.pop(0)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    left = i if left == -1 else left
                    right = i
                else:
                    queue.append(None)
                    queue.append(None)
            if left == -1:
                break

            max_width = max(max_width, right - left + 1)

        return max_width

    def widthOfBinaryTree_faster(self, root):
        queue = [(root, 0, 0)]
        cur_depth, left_pos, res = 0, 0, 0
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth + 1, pos * 2))
                queue.append((node.right, depth + 1, pos * 2 + 1))
                if depth != cur_depth:
                    left_pos = pos
                    cur_depth = depth
                res = max(res, pos - left_pos + 1)
        return res


root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right = TreeNode(2)
root.right.right = TreeNode(2)
s = Solution()
print s.widthOfBinaryTree_faster(root)