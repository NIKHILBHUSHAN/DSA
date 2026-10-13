class Solution:
    def countFreq(self, arr):
        #code here
        freq={}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        nums=[]
        for num in freq:
            nums.append([num,freq[num]])
        return nums