class Solution:
    def toLowerCase(self, s: str) -> str:
        lower=""
        for char in s:
            asc2=ord(chr)
            if asc2>=65 and asc2<=90:
                lower+=chr(asc2+32)
            else:
                lower+=char
        return lower

class Solution:
    def toLowerCase(self, s: str) -> str:
        lower=[]
        for char in s:
            asc=ord(char)
            if 65<=asc<=90:
                lower.append(chr(asc+32))
            else:
                lower.append(char)
        return "".join(lower)
        
        