class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # posição para escrever
        read = 0   # posição para ler
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # conta repetições
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # escreve o caractere
            chars[write] = char
            write += 1
            
            # escreve o número se count > 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        
        return write
