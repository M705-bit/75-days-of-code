class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        max_area = 0
        m =  len(height)-1
        while l<m:
            altura=min(height[l], height[m])  
            base = m-l
            max_area=max(max_area,(base*altura))
            if height[l] > height[m]:
                m-=1
            else:
                l+=1
        return max_area
