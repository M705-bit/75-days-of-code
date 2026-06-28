class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vogais = ['a','e','i','o', 'u']
       
        queue = []
        str = list(s)
        
        for i in range(len(str)):
            if str[i] in vogais:
                #alguma letra tem que entrar aqui, se esta eh a primeira a ultima tem que entrar 
                
                queue.append(str[i])
        for i in range(len(str)):
            if str[i] in vogais:
                #alguma letra tem que entrar aqui, se esta eh a primeira a ultima tem que entrar 
                #agr recebe a ultima queue[-1]
                str[i]= queue.pop()

        #como eu faco isso em um for 
                
        #palavra = ''.join(x[0] for x in queue)
        palavra= ''.join(str)
        return palavra
        
    
s = Solution()

print(s.reverseVowels("anaconda"))

def reverse2(s:str) ->str:
    s=list(s)
    vogais = "aeiou"
    esq, dir = 0, len(s)-1
    while esq < dir:
        #confere se a esqquerda esta em vogal, no moneto em que achar, vai tentar achar a direita no vogal
        #os dois vao se encontrar no mesmo espaco tempo
        #troque os de lugar e continue o loop
        while s[esq] not in vogais:
            esq+=1
        #strq[esq] in vowals
        while s[dir] not in vogais:
            dir-=1
        #achou
        s[esq], s[dir] = s[dir], s[esq]
    
    palavra = ''.join(s)
    return palavra 

print(reverse2("anaconda"))