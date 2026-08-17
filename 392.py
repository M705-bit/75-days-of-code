class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j, i = 0, 0
        while j < len(s):
            if  i > len(t)-1 and j<=len(s):
                return False 
                
            if t[i] == s[j]:
                j+=1
            i+=1
            

        return True 
            
        
