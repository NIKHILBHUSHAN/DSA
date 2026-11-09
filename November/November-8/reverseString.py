class Solution:
    def reverseWords(self, s: str) -> str:
        """words=[]
        reverse=""
        left=0
        right=0
        while right<len(s):
            if s[right]==" ":
                right+=1
                continue
            left=right
            while right<len(s) and s[right]!=" ":
                right+=1
            word=""
            for i in range(left,right):
                word+=s[i]
            words.append(word)
        for i in range(len(words)-1,-1,-1):
            reverse+=words[i]
            if i!=0:
                reverse+=" "
        return reverse"""
        result=""
        right=len(s)-1
        while right>=0:
            if s[right]==" ":
                right-=1
                continue
            end=right
            while right>=0 and s[right]!=" ":
                right-=1
            start=right+1
            if result!="":
                result+=" "
            for i in range(start,end+1):
                result+=s[i]
        return result
            








        