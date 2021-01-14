def stanton_measure(arr):
    counter_1=0
    counter_2=0
    for i in range(0,len(arr)):
        if arr[i]==1:
            counter_1+=1

    for i in range(0,len(arr)):
        if arr[i]==counter_1:
            counter_2+=1


    return counter_2



print("Fixed Tests")
print(stanton_measure([1, 4, 3, 2, 1, 2, 3, 2]), 3);