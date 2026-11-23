class Solution:
    def closeStrings(self,word1,word2):
        '''
        if len(word1)!=len(word2):
            return False
        freq1={}
        freq2={}
        for ch in word1:
            if ch not in freq1:
                freq1[ch]=1
            else:
                freq1[ch]+=1
        for ch in word2:
            if ch not in freq2:
                freq2[ch]=1
            else:
                freq2[ch]+=1
        if len(freq1)!=len(freq2):
            return False
        for ch in freq1:
            if ch not in freq2:
                return False
        values1=[]
        values2=[]
        for ch in freq1:
            values1.append(freq1[ch])
        for ch in freq2:
            values2.append(freq2[ch])
        i=1
        while i<len(values1):
            key=values1[i]
            j=i-1
            while j>=0 and values1[j]>key:
                values1[j+1]=values1[j]
                j-=1
            values1[j+1]=key
            i+=1
        i=1
        while i<len(values2):
            key=values2[i]
            j=i-1
            while j>=0 and values2[j]>key:
                values2[j+1]=values2[j]
                j-=1
            values2[j+1]=key
            i+=1
        return values1==values2
        '''
        if len(word1)!=len(word2):
            return False
        freq1={}
        freq2={}
        for ch in word1:
            if ch not in freq1:
                freq1[ch]=1
            else:
                freq1[ch]+=1
        for ch in word2:
            if ch not in freq2:
                freq2[ch]=1
            else:
                freq2[ch]+=1
        if set(freq1)!=set(freq2):
            return False
        count1={}
        count2={}
        for ch in freq1:
            if freq1[ch] not in count1:
                count1[freq1[ch]]=1
            else:
                count1[freq1[ch]]+=1
        for ch in freq2:
            if freq2[ch] not in count2:
                count2[freq2[ch]]=1
            else:
                count2[freq2[ch]]+=1
        return count1==count2