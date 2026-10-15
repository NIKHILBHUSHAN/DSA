arr=[1,2,3,4,5,6,7,8]   
start = 0
k=3
while start < len(arr):
    left=start
    right = min(left+k-1,len(arr)-1)
    while left<right:
        temp=arr[left]
        arr[left]=arr[right]
        arr[right]=temp
        left+=1
        right-=1
    start+=k
print(arr)