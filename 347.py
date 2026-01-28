from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        lista = []
        for n in nums:
            if n not in d:
                d.setdefault(n,1)
            else:
                d[n]+=1
        lista = sorted(list(d.items()), key= lambda item : item[1], reverse=True)
        
        return list(map(lambda item: item[0], lista[:k]))



            