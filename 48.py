class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matriz = [[] for matriz in matrix]
        count = 0
        contagem = 0
        #lista = [x for i in range(len(matrix))]
        while (contagem<(len(matrix)*len(matrix))):
            for i in range(len(matrix)-1,-1,-1):
            
                matriz[count].append(matrix[i][count])
            contagem+=len(matrix)
            count+=1
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]=matriz[i][j]
