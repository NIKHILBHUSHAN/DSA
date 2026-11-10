class Solution:
    def reverseWords(self, s: str) -> str:
        """words=[]
        reverse=""
        left=0
        right=0
        while right<len(s):
            if s[right]==" ":
                right+=1
            left=right
            while right<len(s) and s[right]!=" ":
                right+=1
            word=""
            for i in range(right-1,left-1,-1):
                word+=s[i]
            words.append(word)
        for i in range(len(words)):
            if i!=0:
                reverse+=" "
            reverse+=words[i]
        return reverse"""
        result=""
        left=0
        right=0
        while right<len(s):
            if s[right]==" ":
                result+=" "
                right+=1
                continue
            left=right
            while right<len(s) and s[right]!=" ":
                right+=1
            for i in range(right-1,left-1,-1):
                result+=s[i]
        return result

        

        
        