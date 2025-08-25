from collections import Counter

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        freq = Counter(nums)
        count = 0

        for num in list(freq.keys()):
            complement = k - num
            if complement in freq:
                if num == complement:
                    pairs = freq[num] // 2
                else:
                    pairs = min(freq[num], freq[complement])
                count += pairs
                freq[num] -= pairs
                freq[complement] -= pairs

        return count
