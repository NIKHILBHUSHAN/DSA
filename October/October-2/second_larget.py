array=[15,12,9,98,55]
largest=array[0]
second_largest=None
for i in range(1,len(array)):
    if array[i]>largest:
        second_largest=largest
        largest=array[i]
    elif array[i]<largest:
        if second_largest is None or array[i]>second_largest:
            second_largest=array[i]
print(second_largest)