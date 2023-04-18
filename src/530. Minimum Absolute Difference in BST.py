# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = float("inf")
        self.pre = None

    def traversal(self, node) -> None:
        if not node:
            return
        self.traversal(node.left)
        if self.pre:
            self.result = min(node.val - self.pre.val, self.result)
        self.pre = node
        self.traversal(node.right)

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.traversal(root)
        return self.result


if __name__ == "__main__":
    sol = Solution()
