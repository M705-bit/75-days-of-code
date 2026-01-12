#---Solução 1---
'''
def solution(nums):
    triplets = []
    for i in range(len(nums)-1, -1, -1):
        if len(triplets) < 3:
            print(f"Quem está na avaliação: {nums[i]}")

            if i == 0 and nums[i] == min(nums[i], triplets[i-1], triplets[i-2] ):
                triplets.append(nums[i])
                print(f"Quem entrou: {nums[i]}")
                return True
            else:
                if nums[i] > nums[i-1]:
                    if nums[i] != min(nums) and len(triplets) < 2:
                        triplets.append(nums[i])
                        print(f"Quem entrou: {nums[i]}")
                elif len(triplets)  == 2:
                    triplets.append(nums[i])
                    print(f"Quem entrou: {nums[i]}")
        else:
            return True
    
    return Falseprint(solution([1,2,3,4,5])) # Expected output: True
print(solution([5,4,3,2,1])) # Expected output: False
print(solution([2,1,5,0,4,6])) # Expected output: True  """

'''

#---Solução 2---
'''
def solution(nums):
        triplets = []
        for i in range(len(nums)-1, -1, -1):
            if len(triplets) < 3:
                if triplets and len(triplets) < 2:
                    #print(f"Quem está na avaliação: {nums[i]}")
                    if nums[i] < triplets[-1] and nums[i] != min(nums):
                        #print(f"Quem entrou: {nums[i]}")
                        triplets.append(nums[i])
                else:
                    #print(f"Quem entrou: {nums[i]}")
                    triplets.append(nums[i])
        return len(triplets) == 3  
'''
#---Solução 3---
'''
def increasingTriplet(nums):
        third = float('-inf')   # candidato ao 3º elemento
        stack = []

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < third:
                return True

            while stack and nums[i] > stack[-1]:
                third = stack.pop()

            stack.append(nums[i])
            print(stack, third)

        return False    

print(increasingTriplet([1,2,1,3]))# Expected output: True
print(increasingTriplet([1,2,3,4,5])) # Expected output: True
print(increasingTriplet([5,4,3,2,1])) # Expected output: False
print(increasingTriplet([2,1,5,0,4,6])) # Expected output: True 
'''
#'--Solução 4---
'''
from typing import List
from typing import Optional

class Solution:
    def increasingTriplet(self, nums: List[int]) -> List[int]:
        if len(nums) < 3:
            return []
        
        first = float('inf') # meior numero de tds
        second = float('inf') # maior numero de tds
        #[4,5,2147483647,1,2]
        for num in nums:
            if num <= first: # 4 entra como first, 1 entra como first, 0 entra como first 
                first = num
            elif num <= second: # 5 entra como second, 4 entra como second,
                second = num
            else: 
                return [first, second, num] #2, 5 
        return []
'''
#Solução Final:
from typing import List
from typing import Optional
from math import inf

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)< 3:
            return False

        primeiro = float(inf)
        segundo = float(inf)
        
        for num in nums:
            if num <=primeiro:
                primeiro = num
            elif num <=segundo:
                segundo = num
            else:
                return True
        return False