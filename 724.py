from typing import List, Annotated, Optional

class Solution:
    def pivotIndex(self, nums: List[int]):
        for i in range(len(nums)):
            if sum(nums[i+1:]) == sum(nums[:i:]):
                return i 
            
        return -1