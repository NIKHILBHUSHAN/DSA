class Solution:
    def strStr(self,haystack:str,needle:str)->int:
        """
        for i in range(len(haystack)-len(needle)+1):
            j=0
            while j<len(needle) and haystack[i+j]==needle[j]:
                j+=1
            if j==len(needle):
                return i
        return -1
        """
        n=len(haystack)
        m=len(needle)
        if m==0:
            return 0
        if m>n:
            return -1
        for i in range(n-m+1):
            j=0
            while j<m and haystack[i+j]==needle[j]:
                j+=1
            if j==m:
                return i
        return -1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """if len(needle)>len(haystack):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            j=0
            ismatch=True
            while j<len(needle):
                if  needle[j]!=haystack[i+j]:
                    ismatch=False
                    break
                j+=1
            if ismatch:
                return i
                break
        return -1 """
        if not needle:
            return 0
        lps=[0]*len(needle)
        length=0
        i=1
        while i<len(needle):
            if needle[i]==needle[length]:
                length+=1
                lps[i]=length
                i+=1
            elif length>0:
                length=lps[length-1]
            else:
                lps[i]=0
                i+=1
        i=0
        j=0
        while i<len(haystack):
            if haystack[i]==needle[j]:
                i+=1
                j+=1
                if j==len(needle):
                    return i-j
            elif j>0:
                j=lps[j-1]
            else:
                i+=1
        return -1   