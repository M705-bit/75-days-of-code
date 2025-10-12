def solution (A):
    #0 <= P < Q < len(A), is caleed 
    # a média da parte é a soma de todos os elementos de P - Q dividido pelo tamanho da parte.
    # (0,1)

    #a soma tem que ser a menor possível 
    # n is a integer array within the range 2 - ...
    min_sum = A[0] + A[1]
    k = len(A)
    index = 0
    #percoirre a array
    for i in range(0, k-1):
        current_sum = 0 
        for j in range(0, 2):
            current_sum+= A[i+j]
        if current_sum < min_sum:
            min_sum = current_sum 
            index = i
    return index   
        

print(solution([4,2,2,5,1,5,8]))
print(solution(list(range(2,100000))))
