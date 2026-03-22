from typing import List, Optional

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      
        minimo = 0
        maximo = 0
        i = 0
        intervals.sort(key=lambda x: x[0])
        array = []
        for i in range(len(intervals)):
                if not array:                        
                        array.append(intervals[i])
                        continue
                if (intervals[i][0]>array[-1][1] or intervals[i][1] < array[-1][0]):
                        #acrescenta ele a array tmb
                        array.append(intervals[i])
                else:
                        minimo = min(array[-1][0], intervals[i][0])
                        maximo = max(array[-1][1], intervals[i][1])
                        array[-1] = [minimo, maximo]
        return array
 
            
    