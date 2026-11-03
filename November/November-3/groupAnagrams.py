class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """groupanagrams=[]
        found=[False]*len(strs)
        for i in range(len(strs)):
            if not found[i]:
                anagrams=[strs[i]]
                found[i]=True
                word=strs[i]
                freq={}
                for char in word:
                    if char not in freq:
                        freq[char]=1
                    else:
                        freq[char]+=1
                for j in range(i+1,len(strs)):
                    if not found[j] and len(strs[i])==len(strs[j]):
                        isanagram=True
                        cfreq=freq.copy()
                        for char in strs[j]:
                            if char not in cfreq:
                                break
                            else:
                                cfreq[char]-=1
                        for value in cfreq.values():
                            if value!=0:
                                isanagram=False
                                break
                        if isanagram:
                            found[j]=True
                            anagrams.append(strs[j])
                groupanagrams.append(anagrams)
        return groupanagrams"""
        groups={}
        for word in strs:
            freq=[0]*26
            for char in word:
                index=ord(char)-97
                freq[index]+=1
            key=tuple(freq)
            if key not in groups:
                groups[key]=[word]
            else:
                groups[key].append(word)
        return list(groups.values())

        