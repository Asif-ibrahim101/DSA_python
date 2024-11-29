# sort the array using merge sort

def mergeSort(arr):
    #Base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    Left_arr = arr[:mid]
    right_arr = arr[mid:]

    #Recussively sorting the array
    Left = mergeSort(Left_arr)
    right = mergeSort(right_arr)

    return merge_arrays(Left, right)

def merge_arrays(Left, right):
    sorted_array = []
    i = 0
    j = 0

    while i < len(Left) and j < len(right):
        if Left[i] <= right[j]:
            sorted_array.append(Left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1


    #Appending the remainning arrays
    sorted_array.extend(Left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

array = [12, 1, 50, 23, 2, 0, 45]
print(mergeSort(array))
