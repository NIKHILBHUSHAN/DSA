class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """end=-1
        for i in range(len(word)):
            if word[i]==ch:
                end=i
                break
        if end==-1:
            return word
        prefix=[]
        for i in range(end+1):
            prefix.append(word[i])
        result=""
        for i in range(len(prefix)-1,-1,-1):
            result+=prefix[i]
        for i in range(end+1,len(word)):
            result+=word[i]
        return result"""

        result=""
        end=-1
        for i in range(len(word)):
            if word[i]==ch:
                end=i
                break
        if end==-1:
            return word
        for i in range(end,-1,-1):
            result+=word[i]
        for i in range(end+1,len(word)):
            result+=word[i]
        return result
        
        