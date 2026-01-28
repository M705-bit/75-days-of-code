class Solution():
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        palavra = ""
        for i,str1 in enumerate(strs):
            palavra="".join(sorted(str1)) #ordena a palavra atual 
            if palavra in d:
                d[palavra].append(str1)
            else:
                d[palavra]=[str1]
        return list(d.values())
        #return list(map(lambda item: item[1],d))
