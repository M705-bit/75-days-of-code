from typing import List, Optional 


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]):
        aux = count = sum = 0
        maximumHeight = sorted(maximumHeight, reverse= True)
        #print(maximumHeight)
        sum=maximumHeight[0]
        for i in range(1,len(maximumHeight)):
            maximumHeight[i]=min(maximumHeight[i], maximumHeight[i-1]-1)
            if maximumHeight[i]==0:
                  return -1
            sum+=maximumHeight[i]
        return sum


sol = Solution()
print(sol.maximumTotalSum(list((2,3,4,3))))
print(sol.maximumTotalSum(list((5,3,3,6,5,2,1))))
