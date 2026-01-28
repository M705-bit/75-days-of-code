from typing import List

class Solution():
    def longestSubarray(self,nums: List[int]) -> int:
    
        flag = 0
        start=0
        longest_subarray=0
        window_lenght=0
        stack=[]
        for i in range(len(nums)):
            if nums[i]==0:
                if stack:
                    start=stack[-1]+1
                stack.append(i)  
                     
            longest_subarray=max(longest_subarray,i-start+1)
        
        return  longest_subarray-1
    
#print(longestSubarray(list((0,1,1,1,0,1,1,0,1))))
#yo mustr delete one element
#print(longestSubarray(list((1,1,1))))
#print(longestSubarray(list((1,1,0,1))))
print(longestSubarray(list((1,1,0,0,1,1,1,0,1))))
