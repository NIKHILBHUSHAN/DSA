class Solution:
    def rearrangeCharacters(self,s,target):
        '''
        arr=list(s)
        count=0
        while True:
            temp=[]
            possible=True
            for ch in target:
                found=False
                for i in range(len(arr)):
                    if arr[i]==ch:
                        arr[i]=""
                        found=True
                        break
                if not found:
                    possible=False
                    break
            if not possible:
                return count
            count+=1
        '''
        freq1={}
        freq2={}
        for ch in s:
            if ch not in freq1:
                freq1[ch]=1
            else:
                freq1[ch]+=1
        for ch in target:
            if ch not in freq2:
                freq2[ch]=1
            else:
                freq2[ch]+=1
        ans=len(s)
        for ch in freq2:
            if ch not in freq1:
                return 0
            count=freq1[ch]//freq2[ch]
            if count<ans:
                ans=count
        return ans