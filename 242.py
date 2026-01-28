class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        dic = {}
        for a in s:
            if a not in d:
                d.setdefault(a,1)
            else:
                d[a]+=1

        for a in t:
            if a not in dic:
                dic.setdefault(a,1)
            else:
                dic[a]+=1
            
        return True if dic == d else False

sol= Solution()
print(sol.isAnagram("rat", "car"))