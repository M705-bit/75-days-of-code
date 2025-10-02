class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maior_num = max(candies)
        result = list(map(lambda x: (x + extraCandies) >= maior_num, candies))
        return result
