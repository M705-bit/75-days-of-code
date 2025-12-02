class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        N = len(gain)
        heights = [0]*(N+1)
        highest_point = 0
        for i in range(N):

            heights[i+1]=gain[i]+heights[i]
        
        return max(heights)
