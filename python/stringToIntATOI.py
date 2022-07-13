

class Solution:
    def myAtoi(self, s: str) -> int:
        s.strip()
        if len(s) == 0:
            return 0
        
        for i in range(0, len(s), 1):
            if s[i].isdigit() or s[i] == '-':
                st = st + s[i]
            if s[i].isalpha() or s[i] == '.':
                if st.isdigit():
                    return st
                else:
                    return 0
                
        if int(st) > 2147483647:
            st = 2147483647
        if int(st) < -2147483647:
            st = -2147483648
        
        return st
