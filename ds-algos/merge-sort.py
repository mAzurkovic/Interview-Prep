def merge(arr, left, mid, right):
    L = arr[left:mid]
    R = arr[mid:right+1]

    L.append(float('inf'))
    R.append(float('inf'))

    i = j = 0
    for k in range(left, right+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

def mergeHelper(arr, left, right):
    if (left > right):
        return
    mid = (left + right) // 2
    mergeHelper(arr, left, mid)
    mergeHelper(arr, mid + 1, right)
    merge(arr, left, mid, right)

def ms(arr):
    mergeHelper(arr, 0, len(arr) - 1)

def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

a = [5,2,4,5,2,1,3,9]
mergeSort(a)
print(a)