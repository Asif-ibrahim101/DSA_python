def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    
    (arr[i + 1], arr[end]) = (arr[end], arr[i + 1])
    return i + 1

def Quick_Sort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        Quick_Sort(arr, start, pi - 1)
        Quick_Sort(arr, pi + 1, end)

array = [1, 7, 4, 1, 10, 9, -2]
Quick_Sort(array, 0, len(array) - 1)
print(array)  # [-2, 1, 1, 4, 7, 9, 10]