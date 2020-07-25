def mergesort(arr,n):
    if n == 1:
        return(arr)
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    mergesort(left,mid)
    mergesort(right,n-mid)
    i = 0
    j = 0
    k = 0
    while i < mid and j < n-mid:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j +=1
        k += 1
    while i < mid:
        arr[k] = left[i]
        k += 1
        i += 1
    while j < n-mid:
        arr[k] = right[j]
        k += 1
        j += 1
    return(arr)

