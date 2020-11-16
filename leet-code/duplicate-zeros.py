def duplicateZeros(self, arr: List[int]) -> None:
    length = len(arr)
    i = 0
    while i < length:
        if arr[i] == 0:
            arr.insert(i, 0)
            i += 1
            
        i += 1
           
    arr[:] = arr[:length]