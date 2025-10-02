def swap(x, y):
    return y, x

def contar_frequencias(palavra):
    frequencias = {}
    for letra in palavra:
        if letra in frequencias:
            frequencias[letra] += 1
        else:
            frequencias[letra] = 1
    return frequencias

class Solution:
    def closeStrings(self, word1: str, word2: str) -> str | bool:
        #1º passo: verificar se as strings são de tamanhos iguais
        if len(word1) != len(word2):
            return False
        #2 verificar se as strings tem o mesmo conjunto de caracteres 
        if set(word1) != set(word2):
            return False
      
        #3º passo: verificar se as strings têm a mesma frequência de caracteres
        if sorted(contar_frequencias(word1).values()) != sorted(contar_frequencias(word2).values()):    
            return False
        return True
