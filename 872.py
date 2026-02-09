# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution():
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
                if not root:
                    return 
                yield from dfs(root.left)
                yield from dfs(root.right)
                if not root.left and not root.right:
                    yield root.val
        set1 = list((dfs(root1)))
        set2 = list((dfs(root2)))
        return True if set2==set1 else False
