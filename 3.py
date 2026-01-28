class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        if len(s) ==0 or None:
            return 0
        arr = []
        lista = []
        maior_tam = 1
        for i in range(len(s)):
            if s[i] in arr:
                maior_tam=max(len(arr), maior_tam)
                if maior_tam == len(arr): lista = arr
                arr = []
            
            arr.append(s[i])
        return maior_tam
        #return len(s)

sol = Solution()
print(sol.lengthOfLongestSubstring(""))
print(sol.lengthOfLongestSubstring("1"))