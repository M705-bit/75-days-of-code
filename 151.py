class Solution:
    def reverseWords(self, s: str) -> str:
    
        string = list(s)
        flag = 0
        array = []
        for char in range(len(string)-1, -1,-1):
                
                if string[char] != " " and flag == 0:
                    flag = 1
                    ultima = char
                    
                if string[char] != " " and (string[char-1]== " " or char == 0) and flag == 1:
                        array.append(''.join(string[char:ultima+1]))
                        #print(f"adicionando: {''.join(string[char:ultima+1])} character count: {char} ultima: {ultima}")
                        flag = 0
                        
        return ' '.join(array)
        

#testes
sol = Solution()
print(sol.reverseWords("the sky is blue"))  # Output: "blue is sky the"
print(sol.reverseWords("  hello world  "))  # Output: "world hello"
print(sol.reverseWords("a good   example"))  # Output: "example good a"