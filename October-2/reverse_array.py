array=[1,2,3,4,5]
left=0
right=len(array)-1
while left<right:
    temp=array[left]
    array[left]=array[right]
    array[right]=temp
    left+=1
    right-=1
print(array)