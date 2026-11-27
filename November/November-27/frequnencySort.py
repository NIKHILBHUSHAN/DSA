class Solution:
    def frequencySort(self,s):
        '''
        freq={}
        for ch in s:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1
        chars=[]
        for ch in freq:
            chars.append(ch)
        for i in range(len(chars)):
            best=i
            for j in range(i+1,len(chars)):
                if freq[chars[j]]>freq[chars[best]]:
                    best=j
            chars[i],chars[best]=chars[best],chars[i]
        res=""
        for ch in chars:
            for i in range(freq[ch]):
                res+=ch
        return res
        '''
        freq={}
        for ch in s:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1
        buckets=[[] for i in range(len(s)+1)]
        for ch in freq:
            buckets[freq[ch]].append(ch)
        res=""
        for i in range(len(s),0,-1):
            for ch in buckets[i]:
                for j in range(i):
                    res+=ch
        return res