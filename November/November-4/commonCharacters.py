class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        freq={}
        for ch in words[0]:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1
        for word in words[1:]:
            current={}
            for ch in word:
                if ch not in current:
                    current[ch]=1
                else:
                    current[ch]+=1
            for ch in freq:
                if ch in current:
                    freq[ch]=min(freq[ch],current[ch])
                else:
                    freq[ch]=0
        result=[]
        for ch in freq:
            for i in range(freq[ch]):
                result.append(ch)
        return result

        