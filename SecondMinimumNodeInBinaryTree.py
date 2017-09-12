#Definition for a binary tree node.
import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this
        tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value
        among its two sub-nodes.

        Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in
        the whole tree.
        If no such second minimum value exists, output -1 instead.

        :type root: TreeNode
        :rtype: int
        """
        ans = [float('inf')]
        def traversal(node):
            if not node:
                return
            if root.val < node.val < ans[0]:
                ans[0] = node.val
            traversal(node.left)
            traversal(node.right)

        traversal(root)
        return -1 if ans[0] == sys.maxsize else ans[0]




