class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """if len(s)!=len(t):
            return False
        used=[False]*len(t)
        for i in range(len(s)):
            found=False
            for j in range(len(t)):
                if s[i]==t[j] and not used[j]:
                    found=True
                    used[j]=True
                    break
            if not found:
                return False
        return True
        
        """
        freq={}
        
        for char in s:
            if char not in freq:
                freq[char]=1
            else:
                freq[char]+=1
        for char in t:
            if char in freq:
                freq[char]-=1
            else:
                return False
             
        for value in freq.values():
            if value!=0:
                return False
        return True
        