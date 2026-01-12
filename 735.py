from typing import List, Annotated, Optional

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:  # colisão só ocorre se o da pilha for positivo e o atual negativo
                if stack[-1] < -a:   # topo menor → explode
                    stack.pop()  # remove o asteroide menor
                    continue # o else sempre adiciona o asteroide atual só não adiciona no caso de ambos serem iguais
                elif stack[-1] == -a:  # iguais → ambos somem
                    stack.pop()
                break #sai do while e não adiciona o asteroide atual
            else:
                stack.append(a) #pega o asteroide atual e coloca na pilha
                
        return stack

solucao = Solution()
print(solucao.asteroidCollision([5,10,-5]))
