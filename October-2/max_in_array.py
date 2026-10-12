array=[15,12,9,98,55]
max=array[0]
for i in range(1,len(array)):
    if array[i]>max:
        max=array[i]
print(max)