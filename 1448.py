# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        branch = []
        i = 0 
        good_nodes = 0
        def dfs(root, branch):
            if not root or root.val is None:
                return 
            max_val = max(branch) if branch else float('-inf')
            if root.val >= max_val:
                yield 1
            else:                
                yield 0
            branch.append(root.val)
            yield from dfs(root.left, branch)
            yield from dfs(root.right, branch)

            #aqui chegamos em uma folha, fim do branch 
            branch.pop()  # ← sempre faz backtracking
                
            
        return sum(dfs(root, []))
        
            