class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        d = deque(flowerbed)
        d.appendleft(0)
        d.append(0)
        count_n = 0
        for i in range(1, len(d)-1):

                if (d[i-1] + d[i] + d[i+1]) == 0 :
                    d[i] = 1
                    count_n+=1
           
        #print(f'O count eh {count_n} e a array eh {d}')
        return True if count_n >= n else False
