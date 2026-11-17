class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """if len(s)!=len(t):
            return False
        for i in range(len(s)):
            for j in range(i):
                if s[i]==s[j] and t[i]!=t[j]:
                    return False
                if t[i]==t[j] and s[i]!=s[j]:
                    return False
        return True
        """
        s2t={}
        t2s={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]]!=t[i]:
                return False
            if t[i] in t2s and t2s[t[i]]!=s[i]:
                return False
            s2t[s[i]]=t[i]
            t2s[t[i]]=s[i]
        return True
            

    