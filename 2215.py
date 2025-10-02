class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        x, y = set(nums1), set(nums2)
        answer = list([x for x in range(2)])
        answer[0] = list(x-y)
        answer[1] = list(y-x)
        return answer
