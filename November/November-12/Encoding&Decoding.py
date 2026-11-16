def encode(strs:list[str]):
    encoded=""
    for word in strs:
        encoded+=str(len(word))+"#"+word
    return encoded
def decode(s):
    decoded=[]
    i=0
    while i<len(s):
        length=""
        while s[i]!="#":
            length+=s[i]
            i+=1
        count=int(length)
        i+=1
        word=""
        for j in range(count):
            word+=s[i+j]
        i+=count
        decoded.append(word)
    return decoded


strs=["hello","world"]
encoded=encode(strs)
decoded=decode(encoded)

print("Original:",strs)
print("Encoded:",encoded)
print("Decoded:",decoded)
