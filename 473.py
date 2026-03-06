from typing import List, Annotated, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum.append(node.val)
            count = 0
            
            # verifica todos os prefixos possíveis
            s = 0
            for i in range(len(current_sum)-1, -1, -1):
                s += current_sum[i]
                if s == targetSum:
                    count += 1
            
            # recursão nos filhos
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            # backtracking
            current_sum.pop()
            return count
        
        return dfs(root, [])


tree=TreeNode(5)
#por que apareceu o erro 'NoneType' object has no attribute 'val'
tree.left = TreeNode(4)
tree.right = TreeNode(8)
tree.left.left = TreeNode(11)
tree.left.left.left = TreeNode(7)
tree.left.left.right = TreeNode(2)
tree.right.left = TreeNode(13)
tree.right.right = TreeNode(4)
tree.right.right.left = TreeNode(5)
tree.right.right.right = TreeNode(1)

solution = Solution()
#vou tentar printar em lista como foram as rotas para eu conseguir entender o que está acontecendo
print(solution.pathSum(tree, 22))

