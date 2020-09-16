# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0

        def recurse(root):
            if root:
                if root.val >= L and root.val <= R:
                    self.ans += root.val
                recurse(root.left)
                recurse(root.right)

        recurse(root)
        return self.ans


root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right = TreeNode(15)
root.right.right = TreeNode(18)

print(Solution().rangeSumBST(root, 7, 15))
