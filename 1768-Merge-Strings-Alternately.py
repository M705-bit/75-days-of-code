class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        j =0
        k =0
        string = []
        while (j < len(word1) or k < len(word2)):
            if j < len(word1):
                string.append(word1[j])
                #string = string + word1[j]
                j+=1
            else:
                pass
            if k < len(word2):
                string.append(word2[k])
                #string = string + word2[k]
                k+=1
        return ''.join(string)
