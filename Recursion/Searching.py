# def CheckSorted(array, size, index=0):
#     # Base case: if we've reached end of array or only one element left
#     if index == size - 1:
#         return True
#
#     # Check if current element is greater than next element
#     if array[index] > array[index + 1]:
#         return False
#
#     # Recursive call with next index
#     return CheckSorted(array, size, index + 1)
#
#
# array = [2, 4, 5, 6, 7, 8, 10]
# size = len(array)
#
# ans = CheckSorted(array, size)
# print(ans)

# lenear search with recurssion
arr = [3, 5, 1, 2, 6]
length = len(arr)


def LinearSearch(arr, size, x, index=0):
    # print(arr, size)
    #base case
    if index >= size:
        return False

    if arr[index] == x:
        return index

    #Reccursive relation
    Search = LinearSearch(arr, size, x, index + 1)
    return Search

print(LinearSearch(arr, length, 5))
