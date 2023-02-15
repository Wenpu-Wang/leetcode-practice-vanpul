class TreeNode:
    def __init__(self, value=0):
        self.val = value
        self.left = None
        self.right = None


if __name__ == "__main__":
    node = TreeNode()
    node.left = TreeNode(1)
    print("node:", node.val)
    print("node.left:", node.left.val)