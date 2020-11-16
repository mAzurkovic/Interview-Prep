def insertAt(arr, value, index):
    length = len(arr)
    arr.append(arr[-1])
    
    for i in range(index+1, length):
        arr[length - i] = arr[length - i - 1]
    
    arr[index] = value

    return arr


print(insertAt([1,2,3,4,5], 4, 2))
l = [1,2,3,4,5]
l.insert(3, 6)
print(l)