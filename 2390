class Solution:
    def removeStars(self, s: str) -> str:
       string  = list(s)
       stack = []
       for s in range(len(string)):
            if string[s] == '*': 
               stack.pop() 
            else: 
                stack.append(string[s])
       if len(stack) == 0:
            return ''
       return ''.join(stack)
