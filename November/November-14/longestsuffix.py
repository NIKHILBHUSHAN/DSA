def longestsuffix(strs:list[str])->str:
    suffix=""
    index=len(strs[0])-1
    while index>=0:
        word=strs[0]
        ch=word[index]
        isPresent=True
        for i in range(1,len(strs)):
            if index>=len(strs[i]) or ch!=strs[i][index]:
                isPresent=False
                break
        if not isPresent:
            break
        suffix+=ch
        index-=1
    result=""
    for i in range(len(suffix)-1,-1,-1):
        result+=suffix[i]
    return result
def longestsuffix(strs:list[str])->str:
    if not strs:
        return ""
    index=1
    min_length=len(strs[0])
    for word in strs:
        if len(word)<min_length:
            min_length=len(word)
    while index<=min_length:
        ch=strs[0][-index]
        for i in range(1,len(strs)):
            if strs[i][-index]!=ch:
                return strs[0][len(strs[0])-index+1:]
        index+=1
    return strs[0][len(strs[0])-min_length:]


strs=["running","jogging","walking"]
print(longestsuffix(strs))
