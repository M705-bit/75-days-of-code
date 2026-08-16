class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        end = len(nums) -1
        j = 0
        vez = 0 
        qtd_zeros = 0
        while vez>= (end+1)-qtd_zeros:
            if nums[vez] == 0:
                start = vez
                for i in range(start, end):
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                vez = 0 
                qtd_zeros+=1
            else:
                vez+=1 
        
            
       
