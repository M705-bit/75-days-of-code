class Solution:
    def decodeString(self, s: str) -> str:
        string = list(s)
        stack_de_num = []
        stack_de_idx = []
        i = 0

        while i < len(string):
            if string[i].isdigit():
                num = []
                while i < len(string) and string[i].isdigit():
                    num.append(string[i])
                    i += 1
                stack_de_num.append(int(''.join(num)))
            elif string[i] == '[':
                stack_de_idx.append(i)
                i += 1
            elif string[i] == ']':
                start = stack_de_idx.pop()
                repeat_str = string[start+1:i]
                repeat_count = stack_de_num.pop()
                string = string[:start - len(str(repeat_count))] + repeat_str * repeat_count + string[i+1:]
                i = start - len(str(repeat_count)) + len(repeat_str) * repeat_count
            else:
                i += 1

        return ''.join(string)
