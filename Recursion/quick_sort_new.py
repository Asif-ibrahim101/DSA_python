import random

def partition(arr, start, end):
    pivot_inx = random.randint(start, end)
    arr[pivot_inx], arr[end] = arr[end], arr[pivot_inx]
    pivot = arr[end]
     
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def Quick_sort(arr, start=None, end=None):
    if not arr:
        return arr
    
    if start is None:
        start = 0
    if end is None:
        end = len(arr) -1
        
    
    #main logic
    if start < end:
        pivot_idx = partition(arr, start, end)
        Quick_sort(arr, start, pivot_idx - 1)
        Quick_sort(arr, pivot_idx + 1, end)
    
    return arr


data = [1, 7, 4, 1, 10, 9, -2]
print(f"Sorted array: {Quick_sort(data)}")