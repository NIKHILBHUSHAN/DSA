class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """words=s.split(" ")
        if len(pattern)!=len(words):
            return False
        for i in range(len(pattern)):
            for j in range(i):
                if pattern[i]==pattern[j] and words[i]!=words[j]:
                    return False
                if words[i]==words[j] and pattern[i]!=pattern[j]:
                    return False
        return True

        """ 
        words=s.split(" ")
        p2s={}
        s2p={}
        if len(pattern)!=len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] in p2s and p2s[pattern[i]]!=words[i]:
                return False
            if words[i] in s2p and s2p[words[i]]!=pattern[i]:
                return False
            p2s[pattern[i]]=words[i]
            s2p[words[i]]=pattern[i]
        return True
        