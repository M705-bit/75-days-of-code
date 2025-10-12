def solution2(A):
      N = len(A)
      starts = [ i - A[i] for i in range(N) ]
      ends = [ i + A[i] for i in range(N) ]
      starts.sort()
      ends.sort()
      pairs = 0
      j = 0   
      #vamos testar quantos starts iniciam antes dos ends
      # e o que isso nos dá intersecções
      for i in range(N):
          while j < N and starts[j] <= ends[i]:
              j += 1

        # pesne que temos 3 conjuntos, A , B , C e quereos ver quais conjuntos intersectam com A, lgo precismaos deconbtar um do j , que é o proprio A
        #depois precisamos descontar os conjuntos que ja foram contados, que são os i
          pairs += j - i - 1
              #cada start que inicia antes de um end é uma intersecção
          

      return pairs

print(solution2(list((0, 1, 2, 3, 2, 1, 0))))
