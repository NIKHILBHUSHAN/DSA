class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """if len(magazine)<len(ransomNote):
            return False
        found=[False]*len(magazine)
        for i in range(len(ransomNote)):
            matched=False
            for j in range(len(magazine)):
                if not found[j] and ransomNote[i]==magazine[j]:
                        found[j]=True
                        matched=True
                        break     
            if not matched:
                    return False
        return True
                    """

        freq={}
        for ch in magazine:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1
        for ch in ransomNote:
            if ch not in freq or freq[ch]==0:
                return False
            freq[ch]-=1
        return True

        