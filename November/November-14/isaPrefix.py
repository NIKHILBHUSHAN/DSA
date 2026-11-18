class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
       """combined=""
       for word in words:
        combined+=word
        if len(combined)>len(s):
            return False
        if combined==s[:len(combined)]:
            if len(combined)==len(s):
                return True
       return False"""
       i=0
       for word in words:
        for ch in word:
            if i>=len(s) or ch!=s[i]:
                return False
            i+=1
        if i==len(s):
            return True
       return False
        