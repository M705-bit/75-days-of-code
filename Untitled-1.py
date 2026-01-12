
from ast import List

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
    
solution = increasingTriplet
list = [2,1,5,0,4,6]
res = solution(list)
