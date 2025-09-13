

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        i = 0
        n = len(chars)
        write = 0

        while i < n: 
            ch = chars[i]
            j = i
            while j < n and chars[j] == ch:
                j += 1
                count = j - i
            
            chars[write] = ch
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
            i = j

        return write
        
