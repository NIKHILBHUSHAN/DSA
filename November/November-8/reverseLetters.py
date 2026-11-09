class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """chars=list(s)
        letters=[]
        for ch in s:
            asc2=ord(ch)
            if 65<=asc2<=90 or 97<=asc2<=122:
                letters.append(ch)
        left=0
        right=len(letters)-1
        while left<right:
            letters[left],letters[right]=letters[right],letters[left]
            left+=1
            right-=1
        j=0
        for i in range(len(chars)):
            asc2=ord(chars[i])
            if 65<=asc2<=90 or 97<=asc2<=122:
                chars[i]=letters[j]
                j+=1
        return "".join(chars)"""

        chars=list(s)
        left=0
        right=len(chars)-1
        while left<right:
            if chars[left].isalpha() and chars[right].isalpha():
                chars[left],chars[right]=chars[right],chars[left]
                left+=1
                right-=1
            elif chars[left].isalpha() and not chars[right].isalpha():
                right-=1
            else:
                left+=1
        return "".join(chars)

        