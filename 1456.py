class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        N = len(s)
        vogais = ['a','e','i','o','u']
        count = max_vowels = l = r =0
     
        while r < N:
            if s[r] in vogais:
                    count+=1
            if r - l + 1 > k:
                if s[l] in vogais:
                    count-=1
                l +=1

            max_vowels = max(max_vowels, count)
            r+=1
        return max_vowels
