from typing import List, Annotated, Optional

class Solution:
    def compress(self, chars: List[str]) -> int:
        stack = []
        count = 1
        
        for i in range(1, len(chars)+1):        
            if i < len(chars) and chars[i] == chars[i-1]: 
                count+=1  #incrementa a contagem  
            else: #se eles forem diferentes adiciona o anterior na pilha
                stack.append(chars[i-1])
                if count > 1: # tem contagem? 
                    stack.append(count)
                    
                count = 1    
        chars = ''.join(str(item) for item in stack)

        return len(stack)

solution = Solution()
print(solution.compress(["a","a","b","b","c","c","c"]))  # Output: 6, chars = ["a","2","b","2","c","3"]
