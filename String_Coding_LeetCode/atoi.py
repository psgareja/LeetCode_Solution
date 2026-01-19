def Wordstoint(self, s: int) -> str:
        s.lstrip()
        if not s:
            return 0
        
        sing = 1
        i=0
        if s[0]=='+':
            i+=1
        elif s[0]=='-':
            sing=-1
            i-=1
        
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
        
        result *=sing

        INT_MIN = -2**31
        INT_MAX = 2**31 -1
        if result < INT_MIN:
            return INT_MIN
        if result >INT_MAX:
            return INT_MAX
        
        return result
        
        