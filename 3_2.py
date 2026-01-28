from math import inf

def lengthOfLongestSubstring(s: str) -> int:
    start = 0
    seen ={}
    arr=[]
    window_lenght=0
    max_tam=0
    for end, char in enumerate(s):
        if char in seen and seen[char] >=start:
            start=seen[char]+1

        seen[char]=end

        window_lenght= end-start+1
        arr.append(((start, end)))
        #arr.append(window_lenght)
        max_tam= max(window_lenght, max_tam)
    return max_tam, arr

     


#print(lengthOfLongestSubstring("1"))
#print(lengthOfLongestSubstring("au"))
#print(lengthOfLongestSubstring("aab"))
#print(lengthOfLongestSubstring("abcabcbb")) 
print(lengthOfLongestSubstring("pwwkew"))
#print(lengthOfLongestSubstring("dvdf"))


