class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """word=strs[0]
        for i in range(len(strs),0,-1):
            prefix=word[:i]
            iscommon=True
            for j in range(1,len(strs)):
                if len(strs[j])<i:
                    iscommon=False
                    break
                for k in range(i):
                    if prefix[k]!=strs[j][k]:
                        iscommon=False
                        break
                if not iscommon:
                    break
            if iscommon:
                return prefix
        return ""
        """
        
        largestprefix=""
        index=0
        while index<len(strs[0]):
            word=strs[0]
            ch=word[index]
            ispresent=True
            for j in range(1,len(strs)):
                if index>=len(strs[j]) or ch!=strs[j][index]:
                    ispresent=False
                    break
            if not ispresent:
                 break
            largestprefix+=ch
            index+=1
        return largestprefix


                
        