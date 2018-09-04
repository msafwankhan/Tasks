array = [4, 8, 3, 2, 6, 1,0,9]

array.append(7)

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

for i in range(len(array)):
    if array[i]<7 and array[i+1]>7:
        array[i]=7


print(array)

print("maximum of the array is:", max(array))
print('minimum of the array is:', min(array))
print("Number of elements in the array is:",len(array))