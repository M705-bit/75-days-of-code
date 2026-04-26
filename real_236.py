# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       
        #como encontrar o ancestor mais proximo de dois numeros:
     
        def dfs(root, target, path):
            if not root:
                return False 
            path.append(root)
            if root.val == target:
                return True
              #testa se alguem deu certo em achar o caminho, 
            if dfs(root.left, target, path) or dfs(root.right, target, path):
                return True
            path.pop()
            return False
        
        path_Q = []
        path_P = []

        dfs(root,q.val, path_Q)
        dfs(root,p.val, path_P)
        #ver o que ha de comum nos dois caminhos
        
        #percorre as duas arrays e quando encontrar um elemento que se repete aponta 
        
        ultimo_elemento_repetido = None
        vistos = [node.val for node in path_Q]
        vistosP = [node.val for node in path_P]
        
        for node in path_P:
            if node.val in vistos:
                ultimo_elemento_repetido = node
             
        return ultimo_elemento_repetido
