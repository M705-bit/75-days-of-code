# Definition for a binary tree node.
from typing import List, Optional
from collections import deque 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #tu recebeu um root
        if not root:
            return 0
        queue = deque([root])
        depth = 1
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return (depth-1)

# criando os nós
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(None)
root.right.left = TreeNode(None)
root.right.right = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
res= solution.maxDepth(root)
print(res)
