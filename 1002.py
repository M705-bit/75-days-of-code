from typing import List

""" class Solution(): """
def longestOnes(nums: List[int], k: int) -> int:
        #fazer uma lista de substrings, em ordem decrescente, do maior tamanho de 1s consecutiuvos para o menor
        #veja qual a distância entre elas e veja se dá pra adicioanr os ks
        
        start=0
        window_lenght = 0
        max_lenght = 0
        arr=[]
        k_zeros=0
        for i in range(len(nums)):
            
            if nums[i] == 0:
                
                k_zeros+=1
                     
                while k_zeros > k:
                    if nums[start]== 0:
                         k_zeros-=1
                    start+=1
                    
            
            window_lenght=i-start+1   
            max_lenght=max(window_lenght, max_lenght)
            
        return max_lenght
        
#sol = Solution()
print(longestOnes(list((1,1,1,0,0,0,1,1,1,1,0)), 2))
print(longestOnes(list(([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1])),3))