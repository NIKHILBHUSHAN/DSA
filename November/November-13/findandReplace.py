class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        """result=[]
        for word in words:
            if len(word)!=len(pattern):
                continue
            valid=True
            for i in range(len(pattern)):
                for j in range(i):
                    if pattern[i]==pattern[j] and word[i]!=word[j]:
                        valid=False
                        break
                    if word[i]==word[j] and pattern[i]!=pattern[j]:
                        valid=False
                        break
            if valid:
                result.append(word)
        return result
        """
        result=[]
        for word in words:
            p2w={}
            w2p={}
            valid=True
            if len(pattern)!=len(word):
                continue
            for i in range(len(pattern)):
                if pattern[i] in p2w and p2w[pattern[i]]!=word[i]:
                    valid=False
                    break
                if word[i] in w2p and w2p[word[i]]!=pattern[i]:
                    valid=False
                    break
                p2w[pattern[i]]=word[i]
                w2p[word[i]]=pattern[i]
            if valid:
                result.append(word)
        return result
        