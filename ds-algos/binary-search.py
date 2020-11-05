def binarySearch(arr, left, right, val):
    if (left <= right):
        mid = (left + right) // 2

        if (arr[mid] == val):
            return mid
        elif (val < arr[mid]):
            return binarySearch(arr, left, mid - 1, val)
        else:
            return binarySearch(arr, mid + 1, right, val)
    
    else:
        return -1

print(binarySearch([1,2,3,4,5,6,7,8,9,10], 0, 9, -12))
