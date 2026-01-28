from typing import List, Optional 

#class Solution:
class Solution():
    def uniqueOccurrences(self, arr: List[int]) -> bool:
            d = {}
            
            for a in arr:
                if a in d:
                    d[a]+=1
                else:
                    d.setdefault(a, 1)
            #como eu sei se o numero de ocorrências é o mesmo 
            #como eu imprimo os valores
            
            ocorrencias = list(d.values())


            return True if len(set(ocorrencias)) == len(ocorrencias) else False 
        

