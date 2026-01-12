
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      
        #prefixo = len(nums)*[0]
        #sufixo = prefixo.copy()
        print("entrei")
        prefixo = []
        sufixo = len(nums)*[0]
        array = []
        for i in range(len(nums)):
            if prefixo:
                prefixo.append(prefixo[-1]*nums[i-1])
                sufixo[len(nums)-i-1] = (sufixo[len(nums)-i]*nums[len(nums)-i])
            else:
                prefixo.append(1)
                sufixo[len(nums)-i-1] = 1
        
       
        for i in range(len(nums)):
            array.append(prefixo[i]*sufixo[i])  
        return array